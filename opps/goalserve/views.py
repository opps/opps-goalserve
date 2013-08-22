# -*- coding: utf-8 -*-
import datetime
from json import JSONEncoder
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Match, MatchStandings, Category
from .tasks import get_matches

from celery.result import AsyncResult

from dateutil.tz import tzutc

UTC = tzutc()

class dummy_dict(object):
    pass


def get_dict(self, key):
    instance = getattr(self, key, None)
    return getattr(instance, '__dict__', dummy_dict.__dict__)

def serialize_date(dt):
    """
    Serialize a date/time value into an ISO8601 text representation
    adjusted (if needed) to UTC timezone.

    For instance:
    >>> serialize_date(datetime(2012, 4, 10, 22, 38, 20, 604391))
    '2012-04-10T22:38:20.604391Z'
    """
    if hasattr(dt, 'tzinfo'):
        dt = dt.astimezone(UTC).replace(tzinfo=None)
    return dt.isoformat() + 'Z'


def serialize(data, exclude=None):
    exclude = exclude or []

    exclude += ['created_at', 'image_base', 'g_bet_id', 'g_driver_id']

    new_data = {k:v for k, v in data.iteritems()
                if not k.startswith('_') and
                not k in exclude}

    for k, v in new_data.iteritems():
        if isinstance(v, (datetime.datetime, datetime.date)):
            new_data[k] = serialize_date(v)

    return new_data

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json",
                 *args, **kwargs):
        content = simplejson.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    return "text/plain"

def get_players(_players):

# status: "player",
# birthplace: "Monte Azul Paulista",
# number: null,
# g_fix_id: null,
# weight: null,
# age: 28,
# g_event_id: null,
# updated_at: "2013-08-13T09:21:42.354054Z",
# birthdate: "1985-04-04Z",
# g_static_id: null,
# g_id: "37269",
# team_id: 10,
# image: "http://placehold.it/50x50/",
# nationality: "Brazil",
# position: "D",
# height: null,
# g_player_id: "37269",
# id: 1302,
# name: "Rodolfo"

    players = []
    for _player in _players:
        player = serialize(
            _player.player.__dict__,
            exclude=['birthdate', 'birthplace', 'g_static_id', 'g_id', 'height', 'weight',
                     'team_id', 'nationality', 'updated_at', 'age', 'g_event_id']
        )

        player['number'] = _player.player_number or _player.player.number
        # player['status'] = _player.player_status
        # player['position'] = _player.player_position or player['position']
        player['image'] = _player.player.image_url

        if player.get('name'):
            players.append(player)
    return players

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

def get_event(_event):

    try:
        _event.team_name = _event.team.name
        _event.team_image = _event.team.image_url
        _event.player_name = _event.player.name
        _event.player_image = _event.player.image_url
    except:
        pass

    return _event.__dict__


# {"round_standings": {
#         "round": "",
#         "date": "",
#         "teams": [
#             {
#                 "name": "",
#                 "position": "",
#                 "points": "",
#                 "games": ""},
#         ]}}

def get_standings(_category):
    standings = MatchStandings.objects.filter(category=_category).order_by('position')
    if not standings:
        return {}

    rounds = {}

    for stand in standings:
        rounds.setdefault(stand.round, [])

        stand.team_name = stand.team.name
        stand.image = stand.team.image_url

        rounds[stand.round].append(
            serialize(
                stand.__dict__,
                exclude=['g_player_id', 'g_fix_id', 'g_bet_id',
                         'category_id', 'g_event_id', 'country_id', 'g_id',
                         'status', 'overall_w', 'updated_at', 'overall_gs',
                         'g_static_id', 'team_id', 'total_gd', 'recent_form', 'timestamp',
                         'overall_ga', 'overall_l']
            )
        )
        rounds[stand.round] = sorted(rounds[stand.round], key=lambda team: int(team['position']))

    last = max([int(k) for k in rounds.keys()])

    obj = {'round': last, 'teams': rounds[str(last)]}

    return obj



def match(request, match_pk, mode='response'):
    """
    :mode:
       response -  Django response JSON
       json - Dumped JSON object
       python - Pure Python Dictionary
    """
    _match = get_object_or_404(Match, pk=int(match_pk))
    data = serialize(
        _match.__dict__,
        exclude=['time_name', 'attendance_name', 'referee_name', 'ht_result', 'g_player_id',
                 'g_event_id', 'visitorteam_goals', 'localteam_goals', 'localteam_id',
                 'visitorteam_id', 'stadium_id', 'category_id']

    )
    data['result'] = {'localteam': _match.localteam_goals, 'visitorteam': _match.visitorteam_goals}
    data['stadium'] = serialize(get_dict(_match, 'stadium'))
    if data['stadium']:
        # data['stadium']['image'] = _match.stadium.image_url
        data['stadium'] = {"name": data['stadium'].get('name')}
    data['tournament'] = _match.category.name
    data['country'] = _match.category.country.name.title()

    # data['comments'] = [
    #     serialize(
    #         comment.__dict__,
    #         exclude=[
    #             'match_id', 'g_bet_id', 'g_event_id',
    #             'g_static_id', 'g_player_id', 'g_fix_id', 'id'
    #         ]
    #     ) for comment in _match.matchcommentary_set.all()
    # ]

    data['events'] = [
        serialize(
            get_event(event),
            exclude=[
                'match_id', 'g_bet_id',
                'g_static_id', 'g_player_id', 'g_fix_id', 'id', 'g_id', 'own_goal', 'updated_at',
                'penalty', 'result', 'player_id', 'team_id'
            ]
        ) for event in _match.matchevent_set.all()
    ]

    # LOCALTEAM
    data['localteam'] = serialize(
        get_dict(_match, 'localteam'),
        exclude=['g_fix_id', 'country_id', 'g_event_id', 'updated_at', 'g_static_id',
                 'founded', 'full_name', 'stadium_id', 'g_player_id']
    )
    data['localteam']['players'] = get_players(
        _match.localteam.matchlineup_set.filter(match=_match).order_by('player_status', 'player_number')
    )
    # data['localteam']['stats'] = get_team_stats(
    #     _match.matchstats_set.filter(team=_match.localteam)
    # )
    # data['localteam']['substitutions'] = get_team_substitutions(
    #     _match.matchsubstitutions_set.filter(team=_match.localteam)
    # )
    data['localteam']['image'] = _match.localteam.image_url

    # VISITORTEAM
    data['visitorteam'] = serialize(
        get_dict(_match, 'visitorteam'),
        exclude=['g_fix_id', 'country_id', 'g_event_id', 'updated_at', 'g_static_id',
                 'founded', 'full_name', 'stadium_id', 'g_player_id']
    )
    data['visitorteam']['players'] = get_players(
        _match.visitorteam.matchlineup_set.filter(match=_match).order_by('player_status', 'player_number')
    )
    # data['visitorteam']['stats'] = get_team_stats(
    #     _match.matchstats_set.filter(team=_match.visitorteam)
    # )
    # data['visitorteam']['substitutions'] = get_team_substitutions(
    #     _match.matchsubstitutions_set.filter(team=_match.visitorteam)
    # )
    data['visitorteam']['image'] = _match.visitorteam.image_url

    data['round_standings'] = get_standings(_match.category)


    if mode == 'response':
        response = JSONResponse(data, {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
    elif mode == 'json':
        response = simplejson.dumps(data)
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
    qs = Match.objects.filter(category__pk=category_id).order_by('-match_time')
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