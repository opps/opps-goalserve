# -*- coding: utf-8 -*-
import datetime
from json import JSONEncoder
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import get_object_or_404

from .models import Match, MatchStandings

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

    exclude += ['created_at', 'image_base']

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
    players = []
    for _player in _players:
        player = serialize(_player.player.__dict__)

        player['number'] = _player.player_number
        player['status'] = _player.player_status
        player['position'] = _player.player_position or player['position']
        player['image'] = _player.player.image_url

        players.append(player)
    return players

def get_team_stats(_stats):
    if _stats:
        _stats = _stats[0]
        data = serialize(
            _stats.__dict__,
            exclude=['match_id', 'team_status', 'team_id', 'id']
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
            exclude=['match_id', 'team_status', 'team_id', 'id']
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
                exclude=['id', 'g_player_id', 'g_fix_id', 'g_bet_id',
                         'category_id', 'g_event_id', 'country_id', 'g_id']
            )
        )
    return rounds



def match(request, match_pk):
    _match = get_object_or_404(Match, pk=int(match_pk))
    data = serialize(
        _match.__dict__,
        exclude=['time_name', 'attendance_name', 'referee_name', 'ht_result']

    )
    data['result'] = {'localteam': _match.localteam_goals, 'visitorteam': _match.visitorteam_goals}
    data['stadium'] = serialize(get_dict(_match, 'stadium'))
    if data['stadium']:
        data['stadium']['image'] = _match.stadium.image_url
    data['tournament'] = _match.category.name
    data['country'] = _match.category.country.name.title()

    data['comments'] = [
        serialize(
            comment.__dict__,
            exclude=[
                'match_id', 'g_bet_id', 'g_event_id',
                'g_static_id', 'g_player_id', 'g_fix_id', 'id'
            ]
        ) for comment in _match.matchcommentary_set.all()
    ]

    data['events'] = [
        serialize(
            get_event(event),
            exclude=[
                'match_id', 'g_bet_id',
                'g_static_id', 'g_player_id', 'g_fix_id', 'id', 'g_id'
            ]
        ) for event in _match.matchevent_set.all()
    ]

    # LOCALTEAM
    data['localteam'] = serialize(get_dict(_match, 'localteam'))
    data['localteam']['players'] = get_players(
        _match.localteam.matchlineup_set.filter(match=_match).order_by('player_status', 'player_number')
    )
    data['localteam']['stats'] = get_team_stats(
        _match.matchstats_set.filter(team=_match.localteam)
    )
    data['localteam']['substitutions'] = get_team_substitutions(
        _match.matchsubstitutions_set.filter(team=_match.localteam)
    )
    data['localteam']['image'] = _match.localteam.image_url

    # VISITORTEAM
    data['visitorteam'] = serialize(get_dict(_match, 'visitorteam'))
    data['visitorteam']['players'] = get_players(
        _match.visitorteam.matchlineup_set.filter(match=_match).order_by('player_status', 'player_number')
    )
    data['visitorteam']['stats'] = get_team_stats(
        _match.matchstats_set.filter(team=_match.visitorteam)
    )
    data['visitorteam']['substitutions'] = get_team_substitutions(
        _match.matchsubstitutions_set.filter(team=_match.visitorteam)
    )
    data['visitorteam']['image'] = _match.visitorteam.image_url



    data['round_standings'] = get_standings(_match.category)

    response = JSONResponse(data, {}, response_mimetype(request))
    response['Content-Disposition'] = 'inline; filename=files.json'
    return response
