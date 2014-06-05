# -*- coding: utf-8 -*-

import datetime
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from dateutil.tz import tzutc

from .models import Match, MatchStandings, Category

UTC = tzutc()


def data_match(match_pk):
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

    '''
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
    '''

    data['events'] = _match.get_transmission_events()

    # LOCALTEAM
    data['localteam'] = serialize(
        get_dict(_match, 'localteam'),

        exclude=['g_fix_id', 'country_id', 'g_event_id', 'updated_at', 'g_static_id',
                 'founded', 'full_name', 'stadium_id', 'g_player_id']
    )
    data['localteam']['players'] = get_players(
        _match.localteam.matchlineup_set.filter(match=_match).order_by('player_status', 'order')
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
        _match.visitorteam.matchlineup_set.filter(match=_match).order_by('player_status', 'order')
    )
    # data['visitorteam']['stats'] = get_team_stats(
    #     _match.matchstats_set.filter(team=_match.visitorteam)
    # )
    # data['visitorteam']['substitutions'] = get_team_substitutions(
    #     _match.matchsubstitutions_set.filter(team=_match.visitorteam)
    # )
    data['visitorteam']['image'] = _match.visitorteam.image_url

    data['round_standings'] = get_standings(_match.category)

    return data


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


def get_dict(self, key):
    instance = getattr(self, key, None)
    return getattr(instance, '__dict__', dummy_dict.__dict__)


class dummy_dict(object):
    pass


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

def get_players(_players):

    players = []
    for _player in _players:
        player = serialize(
            _player.player.__dict__,
            exclude=['birthdate', 'birthplace', 'g_static_id', 'g_id', 'height', 'weight',
                     'team_id', 'nationality', 'updated_at', 'age', 'g_event_id']
        )

        player['number'] = _player.player_number or _player.player.number
        player['status'] = _player.player_status
        player['order'] = _player.order
        # player['position'] = _player.player_position or player['position']
        player['image'] = _player.player.image_url

        if player.get('name'):
            players.append(player)
    return players


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


def get_event(_event):

    try:
        _event.team_name = _event.team.name
        _event.team_image = _event.team.image_url
        _event.player_name = _event.player.name
        _event.player_image = _event.player.image_url
    except:
        pass

    return _event.__dict__


def get_tournament_standings(**kwargs):
    data = {'tournaments': []}

    def filter_kwargs_by_key(key):
        try:
            return {k[len(key):]:v for k,v in kwargs.items() if k.startswith(key)}
        except Exception, e:
            return {}

    category_kwargs =  filter_kwargs_by_key('category__')
    categories = Category.objects.filter(country__name__in=[
        'brazil', 'intl', 'international', 'southamerica', 'worldcup',
    ], **category_kwargs)

    for category in categories:
        category_name = category.name if category.name else unicode(_('No name'))
        item = {
            'title': category_name,
            'id': category.id,
            'slug': slugify(category_name),
            'display_name': category.display_name
        }

        #standings = MatchStandings.objects.filter(
        #    category=category).order_by('position')
        match_kwargs =  filter_kwargs_by_key('match__')
        standings = MatchStandings.objects.select_related(
            'team', 'team__image_file', 'team__image_file__archive').filter(
                category=category, **match_kwargs).order_by('position')

        if not standings:
            continue

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
                             'status', 'updated_at', 'timestamp',]
                )
            )

            rounds[stand.round] = sorted(
                rounds[stand.round], key=lambda team: int(team['position'])
            )


        last = max([int(k) for k in rounds.keys()])

        # obj = {'round': last, 'teams': rounds[str(last)]}

        # teams
        item['teams'] = rounds[str(last)]

        data['tournaments'].append(item)

    return data





