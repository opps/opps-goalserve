#coding: utf-8

import urllib
import datetime
from .xml2dict import parse
from .countries import COUNTRIES
from .commentaries import COMMENTARIES
from .models import Country, Category, Match, Team, Stadium, Player, MatchLineUp

DOMAIN = 'http://www.goalserve.com'

"""
Formula 1:

/getfeed/{gid}/f1/drivers
/getfeed/{gid}/f1/f1-results
/getfeed/{gid}/f1/f1-shedule
/getfeed/{gid}/f1/live
/getfeed/{gid}/f1/teams
"""

URLS = {
    'matches': ['/getfeed/{gid}/soccernew/{country}',
               '/getfeed/{gid}/soccernew/{country}_shedule'],
    'standings': '/getfeed/{gid}/standings/{country}.xml',
    'comments': '/getfeed/{gid}/commentaries/{xml}',
    'team': '/getfeed/{gid}/soccerstats/team/{team_id}',
    'player': '/getfeed/{gid}/soccerstats/player/{player_id}'
}


class Crawler(object):
    def __init__(self, gid):
        self.gid = gid

    def load_countries(self):
        for country in COUNTRIES:
            # print
            Country.objects.get_or_create(
                name=country
            )

    def get(self, url):
        print "getting", url
        try:
            return parse(
                urllib.urlopen(
                    DOMAIN + url
                ).read()
            )
        except Exception as e:
            print  e.message
            return None

    def parse_date(self, date, time=None, format=None):
        print "parsing date", date, format
        if not date:
            return


        dt = '{date} {time}'.format(date=date, time=time) if time else date
        parsed = datetime.datetime.strptime(
            dt,
            format or '%d.%m.%Y %H:%M'
        )
        print parsed
        return parsed

    def get_country_by_name(self, name):
        print "getting country by", name
        _country, created = Country.objects.get_or_create(name=name)
        return _country

    def get_stadium(self, data, country=None):
        print "getting stadium"
        _stadium, created = Stadium.objects.get_or_create(
            country=country or self.get_country_by_name(data['country']),
            name=data['venue_name'],
            g_id=data['venue_id']
        )

        try:
            _stadium.surface = data.get('venue_surface')
            _stadium.capacity = data.get('venue_capacity')
            _stadium.image_base = data.get('venue_image')
            _stadium.save()
        except Exception as e:
            print  e.message

        return _stadium

    def get_team(self, team):
        print "getting team"
        # OrderedDict([(u'@name', u'Santos'), (u'@goals', u'?'), (u'@id', u'7560')]))
        _team, created = Team.objects.get_or_create(
            name=team['@name'],
            g_id=team['@id']
        )

        # http://www.goalserve.com/getfeed/c93ce5a5b570433b8a7d96b3c53f119d/soccerstats/team/9260
        data = self.get(
            URLS.get('team').format(gid=self.gid, team_id=team['@id'])
        )

        try:
            team = data['teams']['team']
            _team.full_name = team.get('fullname')
            _team.country = self.get_country_by_name(team.get('country'))
            _team.stadium = self.get_stadium(team, _team.country)
            _team.founded = team.get('founded')
            _team.coach = team.get('coach', {}).get('@name')
            _team.image_base = team.get('image')
            _team.save()
        except Exception as e:
            print  e.message

        if not team.get('@is_national'):  # dont overrride player for worldcup team
            for player in data['teams']['team']['squad']['player']:
                self.get_player(player, _team)

        return _team

    def get_player(self, player, team):
        print "getting player"
        _player, created = Player.objects.get_or_create(
                name=player['@name'],
                team=team,
                g_id=player['@id'],
                g_player_id=player['@id'],
        )

        _player.number = player.get('@number', _player.number)

        # http://www.goalserve.com/getfeed/c93ce5a5b570433b8a7d96b3c53f119d/soccerstats/player/193
        data = self.get(
            URLS.get('player').format(gid=self.gid, player_id=player['@id'])
        )

        if not data:
            return

        try:
            player = data['players']['player']
            _player.birthdate=self.parse_date(player.get('birthdate'), format='%m/%d/%Y')
            _player.age=player.get('age')
            _player.nationality=player.get('nationality')
            _player.birthplace=player.get('birthplace')
            _player.position=player.get('position')
            _player.weight=player.get('weight')
            _player.height=player.get('height')
            _player.image_base=player.get('image')
            _player.save()
        except Exception as e:
            print  e.message

        print _player
        return _player

    def get_commentaries(self, _match, country_name=None):
        print "getting commentaries"
        xmls = COMMENTARIES.get(country_name or _match.category.country.name, [])
        for xml in xmls:
            data = self.get(
                URLS.get('comments').format(gid=self.gid, xml=xml)
            )

            try:
                matches = data['commentaries']['tournament']['match']
            except KeyError:
                continue

            for match in matches:
                if match.get('@static_id') != _match.g_static_id:
                    continue

                try:
                    _match.status = match.get('@status')
                    _match.match_time=self.parse_date(
                                   match.get('@formatted_date'),
                                   match.get('@time')
                    )

                    try:
                        stadium_name, stadium_city, stadium_country = \
                            match['matchinfo']['stadium']['@name'].split(',')
                        _match.stadium, created = Stadium.objects.get_or_create(
                            name=stadium_name.strip(),
                            country=self.get_country_by_name(stadium_country.strip().lower())
                        )
                    except:
                        pass


                    _match.save()
                except Exception as e:
                    print  e.message

                else:
                    self.get_match_lineup(_match, match['teams'])


    def get_match_lineup(self, _match, teams):
        print "getting linepup"
        for team_status in ['localteam', 'visitorteam']:
            team = teams[team_status]
            _team = getattr(_match, team_status, None)
            for player in team['player']:

                try:
                    _player =  Player.objects.get(g_id=player['@id'])
                except:
                    _player = self.get_player(player, _team)

                _lineup = MatchLineUp.objects.get_or_create(
                    match=_match,
                    player=_player,
                    team=_team,
                    team_status=team_status,
                    player_number=_player.number,
                    player_position=player.get('@pos', _player.position)
                )

                print  _lineup


    def get_matches(self, countries=COUNTRIES, g_static_id=None):
        print "getting matches"
        for country in countries:
            _country, created = Country.objects.get_or_create(
                name=country
            )

            for xml_url in URLS.get('matches'):
                url = xml_url.format(
                    gid=self.gid, country=country
                )

                data = self.get(url)

                for category in data['scores']['category']:
                    _category, created = Category.objects.get_or_create(
                        name=category['@name'],
                        g_id=category['@id'],
                        country=_country
                    )

                    print "category", _category.name, created

                    # import ipdb; ipdb.set_trace()
                    for match in category['matches']['match']:

                        # TODO: catch this bug
                        if isinstance(match, (unicode, str)):
                            continue

                        if not match.get('@static_id'):
                            print  "Match not ready"
                            continue

                        _match, created = Match.objects.get_or_create(
                            category=_category,
                            g_static_id=match['@static_id'],
                        )

                        if g_static_id and str(g_static_id) != _match.g_static_id:
                            print "skipping", g_static_id, _match.g_static_id
                            continue

                        print "getting", _match.g_static_id

                        try:
                            _match.status=match.get('@status')
                            _match.match_time=self.parse_date(
                                           match.get('@formatted_date'),
                                           match.get('@time')
                            )
                            _match.localteam=self.get_team(match.get('localteam'))
                            _match.visitorteam=self.get_team(match.get('visitorteam'))
                            _match.ht_result=match.get('ht', {}).get('@score')
                            _match.g_id=match.get('@id')
                            _match.g_fix_id=match.get('@fix_id')
                            _match.save()
                        except Exception as e:
                            print  e.message
                        else:
                            print  _match.pk

                        if _match.g_static_id:
                            self.get_commentaries(_match, country)
