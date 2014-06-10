# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q

from opps.db import Db
from opps.views.generic.json_views import JSONResponse, JSONPResponse, JSONView

from .models import Match, Category, Driver, F1Team
from .models import MatchLineUp, Player, Team
from .tasks import get_matches
from .utils import data_match, serialize, get_tournament_standings
from .forms import LineupAddForm, LineupEditForm

from celery.result import AsyncResult
from dateutil.tz import tzutc
import time
import logging

UTC = tzutc()


logger = logging.getLogger()


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class SuccessURLMixin(object):
    def get_success_url(self):
        return self.request.path + "?status=success"


def set_to_manual(match):
    try:
        # put match in manual mode
        # celery tasks will ignore lineup updates
        match.set_extra(manual_mode=True)
        match.save()
    except Exception as e:
        logger.warning(
            "Error putting in manual mode {m.id} - {msg}".format(
                m=match,
                msg=str(e)
            )
        )


class PostMixin(object):
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        response = request.REQUEST.get('response', '')

        if response.lower() == "jsonp":
            if form.is_valid():
                self.form_valid(form)
                data = form.cleaned_data
                data['lineup_id'] = self.lineup.id
                data['player_id'] = self.player.id
                data['team_id'] = self.team.id
                data['match_id'] = self.match.id
                data['order'] = self.lineup.order
                data['error'] = False
                return JSONPResponse(data)
            else:
                errors = form.errors
                errors['error'] = True
                return JSONPResponse(errors)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class LineupAddView(CSRFExemptMixin, LoginRequiredMixin, SuccessURLMixin, PostMixin, FormView):
    template_name = 'goalserve/lineupform.html'
    form_class = LineupAddForm


    def get_initial(self):
        initial = {}
        for field in self.form_class.base_fields.keys():
            if field in self.request.GET:
                initial[field] = self.request.GET.get(field)
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        match = Match.objects.get(pk=data.get('match_id'))
        set_to_manual(match)
        team = Team.objects.get(pk=data.get('team_id'))
        player = Player.objects.create(
            name=data.get('player_name'),
            number=data.get('player_number') or None,
            position=data.get('player_position') or None,
            team=team
        )

        self.player = player
        self.team = team
        self.match = match

        self.lineup = MatchLineUp.objects.create(
            team=team,
            player=player,
            player_position=player.position,
            player_number=player.number,
            match=match,
            player_status=data.get('player_status'),
            team_status=data.get('team_status'),
            order=data.get('order') or 0
        )

        return super(LineupAddView, self).form_valid(form)


class LineupEditView(CSRFExemptMixin, LoginRequiredMixin, SuccessURLMixin, PostMixin, FormView):
    template_name = 'goalserve/lineupform.html'
    form_class = LineupEditForm

    def get_initial(self):
        initial = {}
        for field in self.form_class.base_fields.keys():
            if field in self.request.GET:
                initial[field] = self.request.GET.get(field)
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        lineup = MatchLineUp.objects.get(
            pk=data.get('lineup_id'))

        set_to_manual(lineup.match)

        lineup.player.name = data.get('player_name', lineup.player.name)
        lineup.player.position = data.get('player_position') or None
        lineup.player.number = data.get('player_number') or None
        lineup.player.save()

        lineup.player_position = data.get('player_position') or None
        lineup.player_number = data.get('player_number') or None
        lineup.player_status = data.get('player_status')
        lineup.order = data.get('order', lineup.order) or 0
        lineup.save()

        self.lineup = lineup
        self.player = lineup.player
        self.team = lineup.team
        self.match = lineup.match

        return super(LineupEditView, self).form_valid(form)


@login_required
def lineup_delete(request):
    match_id = request.REQUEST.get('match_id')
    lineup_id = request.REQUEST.get('lineup_id')
    response = request.REQUEST.get('response', '')

    if not match_id or not lineup_id:
        return HttpResponse("ERROR: Provide match_id and lineup_id")

    qs = MatchLineUp.objects.filter(
        match__id=int(match_id),
        pk=int(lineup_id)
    )

    if not qs.count():
        return HttpResponse("ERROR: No object found to delete")

    error = False

    try:
        qs.delete()
        set_to_manual(Match.objects.get(pk=int(match_id)))
    except:
        error = True

    if response.lower() == "jsonp":
        data = {"lineup_id": lineup_id, "match_id": match_id}
        if error:
            data["error"] = True
        else:
            data["error"] = False

        return JSONPResponse(data)
    else:
        return HttpResponse("SUCCESS" if not error else "ERROR")


@login_required
def lineup_list(request, match_id):
    match = Match.objects.get(id=int(match_id))
    lineups = match.matchlineup_set.order_by(
        'team', 'player__name', 'player_status'
    )
    context = {
        "lineups": lineups,
        "match": match
    }
    return render_to_response('goalserve/lineuplist.html', context)


class JSONStandingsF1View(JSONView):
    def get_context_data(self, **kwargs):
        # agrregate tournaments
        return {}


class JSONStandingsDriversView(JSONView):
    def get_context_data(self, **kwargs):
        data = {
            'drivers': [
                {"name": driver.get_name(),
                 "post": driver.post,
                 "helmet": driver.helmet_url,
                 "country": driver.country,
                 "team": driver.team.get_name() if driver.team else "",
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
                {"name": team.get_name(),
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
        return get_tournament_standings(**kwargs)


class JSONCategoryView(JSONView):
    def get_context_data(self, **kwargs):
        start = int(self.request.REQUEST.get('start', 0))
        end = int(self.request.REQUEST.get('end', 200))
        filters = dict(country__isnull=False)
        request_filters = self.request.GET.dict()

        if 'start' in request_filters:
            del request_filters['start']
        if 'end' in request_filters:
            del request_filters['end']

        filters.update(request_filters)
        categories = Category.objects.filter(
            **filters)

        return {

           "objects:": [
               {
                  "id": category.id,
                  "name": category.name,
                  "display_name": category.display_name,
                  "country": category.country.name,
                  "goalserve_id": category.g_id
               }
                for category in categories[start: end]
           ],
           "meta": {
               "start": start,
               "end": end,
               "total": categories.count(),
               "filters": filters
           }
       }


class JSONMatchView(JSONView):
    def get_context_data(self, **kwargs):
        start = int(self.request.REQUEST.get('start', 0))
        end = int(self.request.REQUEST.get('end', 100))
        filters = dict(visitorteam__isnull=False, localteam__isnull=False,
                       category__isnull=False)
        request_filters = self.request.GET.dict()

        team_name = self.request.REQUEST.get('team_name')
        team_id = self.request.REQUEST.get('team_id')

        if 'start' in request_filters:
            del request_filters['start']
        if 'end' in request_filters:
            del request_filters['end']
        if 'team_name' in request_filters:
            del request_filters['team_name']
        if 'team_id' in request_filters:
            del request_filters['team_id']

        filters.update(request_filters)
        matches = Match.objects.filter(
            **filters)

        if team_name:
            matches = matches.filter(
                Q(localteam__name__icontains=team_name) |
                Q(visitorteam__name__icontains=team_name)
            )

        if team_id:
            matches = matches.filter(
               Q(localteam__id=team_id) | Q(visitorteam__id=team_id)
            )

        matches = matches.order_by('-match_time')

        return {
           "objects:": [
               {
                  "id": match.id,
                  "name": u"{m.localteam} x {m.visitorteam}".format(
                      m=match),
                  "status": match.status,
                  "category": match.category.name,
                  "category_display_name": match.category.display_name,
                  "match_time": match.match_time.strftime("%Y-%m-%d %H:%M") if match.match_time else '',
                  "localteam_id": match.localteam.id,
                   "localteam_name": match.localteam.name,
                   "localteam_display_name": match.localteam.display_name,
                  "visitorteam_id": match.visitorteam.id,
                   "visitorteam_name": match.visitorteam.name,
                   "visitorteam_display_name": match.visitorteam.display_name,
                   "stadium": match.stadium.name if match.stadium else '',
                   "stadium_display_name": match.stadium.display_name if match.stadium else '',
                   "week_number": match.week_number,
                   "localteam_goals": match.localteam_goals,
                   "visitorteam_goals": match.visitorteam_goals,
                   "localteam_image": match.localteam.image_url,
                   "visitorteam_image": match.visitorteam.image_url,
                   "goalserve_id": match.g_id
               }
                for match in matches[start: end]
           ],
           "meta": {
               "start": start,
               "end": end,
               "total": matches.count(),
               "filters": filters
           }
       }


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
    return HttpResponse(res.status)
