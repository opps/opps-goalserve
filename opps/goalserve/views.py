# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth.decorators import login_required

from opps.db import Db
from opps.views.generic.json_views import JSONResponse, JSONPResponse, JSONView

from .models import Match, Category, Driver, F1Team
from .tasks import get_matches
from .utils import data_match, serialize, get_tournament_standings

from celery.result import AsyncResult
from dateutil.tz import tzutc
import time

UTC = tzutc()


class JSONStandingsF1View(JSONView):
    def get_context_data(self, **kwargs):
        # agrregate tournaments
        return {}

class JSONStandingsDriversView(JSONView):
    def get_context_data(self, **kwargs):
        data = {
            'drivers': [
                {"name": driver.name,
                 "post": driver.post,
                 "team": driver.team.name if driver.team else "",
                 "points": driver.points}
                for driver in sorted(
                    [driver for driver in Driver.objects.filter(post__isnull=False)],
                    key=lambda d:int(d.post or 0)
                )
            ]
        }
        return data

class JSONStandingsTeamsView(JSONView):
    def get_context_data(self, **kwargs):
        data = {
            'teams': [
                {"name": team.name,
                 "post": team.post,
                 "points": team.points}
                for team in sorted(
                    [team for team in F1Team.objects.filter(post__isnull=False)],
                    key=lambda d:int(d.post or 0)
                )
            ]
        }
        return data


class JSONStandingsView(JSONView):
    def get_context_data(self, **kwargs):
        return get_tournament_standings()

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    return "text/plain"

def get_team_stats(_stats):
    if _stats:
        _stats = _stats[0]
        data = serialize(
            _stats.__dict__,
            exclude=['match_id', 'team_status', 'team_id']
        )
        data['yellowcards'] = _stats.yellowcards
        data['redcards'] = _stats.redcards
        data['goals'] = _stats.goals

        return data
    return {}

def get_team_substitutions(_substitutions):
    if not _substitutions:
        return []

    subs = []

    for sub in _substitutions:
        data = serialize(
            sub.__dict__,
            exclude=['match_id', 'team_status', 'team_id']
        )

        try:
            data['player_in'] = sub.player_in.name
            data['player_in_image'] = sub.player_in.image_url
            data['player_off'] = sub.player_off.name
            data['player_off_image'] = sub.player_off.image_url
        except:
            pass

        subs.append(data)

    return subs


def match(request, match_pk, mode='response'):
    """
    :mode:
       response -  Django response JSON
       json - Dumped JSON object
       python - Pure Python Dictionary
    """
    data = data_match(match_pk)

    def _json_response():
        try:
            response = JSONPResponse(data, {}, response_mimetype(request), request.GET['callback'])
        except:
            response = JSONResponse(data, {}, response_mimetype(request))
        return response

    if mode == 'response':
        response = _json_response()
        response['Content-Disposition'] = 'inline; filename=files.json'
    elif mode == 'sse':
        def _sse_queue():
            redis = Db('goalservematch', match_pk)
            pubsub = redis.object().pubsub()
            pubsub.subscribe(redis.key)
            while True:
                for m in pubsub.listen():
                    if m['type'] == 'message':
                        data = m['data'].decode('utf-8')
                        yield u"data: {}\n\n".format(data)
                yield
                time.sleep(0.5)

        response = StreamingHttpResponse(_sse_queue(),
                                         mimetype='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        response['Software'] = 'opps-goalserve'
        response.flush()
    elif mode == 'json':
        response = _json_response()
    elif mode == 'python':
        response = data
    else:
        response = "Please specify the mode argument as python, json or response"

    return response


@login_required
def ajax_categories_by_country_name(request, country_name):
    qs = Category.objects.filter(country__name=country_name)
    if qs:
        items = [u"<option value='{item.pk}'>{item.name}</option>".format(item=item)
                 for item in qs]
        response = u"".join(items)
    else:
        response = u"None"
    return HttpResponse(response)


@login_required
def ajax_match_by_category_id(request, category_id):
    qs = Match.objects.filter(
        category__pk=category_id
    ).exclude(
        status__startswith='F'  # remove FT and Full Time matches
    ).order_by(
        '-match_time'
    )

    if qs:
        items = [u"<option value='{item.pk}'>{item.name}</option>".format(item=item)
                 for item in qs]
        response = u"".join(items)
    else:
        response = u"None"
    return HttpResponse(response)


@login_required
def ajax_get_matches(response, country_name, match_id=None):
    task = get_matches.delay(country_name, match_id)
    return HttpResponse(task.task_id)


@login_required
def get_task_status(request, task_id):
    res = AsyncResult(task_id)
    # import ipdb;ipdb.set_trace()
    return HttpResponse(res.status)