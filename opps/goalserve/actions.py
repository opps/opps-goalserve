# coding: utf-8
from django.conf import settings
from .crawler import Crawler
from .models import Team, Player, Stadium

from .no_photo import team_no_photo, player_no_photo

GID = getattr(settings, 'OPPS_GOALSERVE_GID', '')


def set_team_image(filters=None):
    filters = filters or {}
    elegible = Team.objects.filter(
        image_file__isnull=True, **filters).exclude(image_base=team_no_photo)
    for item in elegible:
        item.set_image_file()


def set_player_image(filters=None):
    filters = filters or {}
    elegible = Player.objects.filter(
        image_file__isnull=True, **filters).exclude(image_base=player_no_photo)
    # print elegible
    for item in elegible:
        item.set_image_file()


def set_stadium_image(filters=None):
    filters = filters or {}
    elegible = Stadium.objects.filter(image_file__isnull=True, **filters)
    for item in elegible:
        item.set_image_file()

def goalserve(method, **kwargs):
    """
    race_id, match_id, feed
    """
    crawler = Crawler(GID)

    if 'countries' in kwargs:
        countries = kwargs['countries']
        if isinstance(countries, (str, unicode)):
            kwargs['countries'] = countries.split(',')

    getattr(crawler, method)(**kwargs)


def get_match(country='brazil', match_id=None, get_players=None, cat_id=None, force_feed=None):
    crawler = Crawler(GID)
    crawler.get_matches(country.split(','),
                        cat_id=cat_id,
                        match_id=match_id,
                        force_feed=force_feed,
                        get_players=get_players)


def get_schedule():
    crawler = Crawler(GID)
    crawler.get_matches(['home', 'd-1', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7'], get_players=False)


def get_standings(**kwargs):
    """country"""
    crawler = Crawler(GID)
    crawler.get_standings(**kwargs)


def get_fixtures(**kwargs):
    """country"""
    crawler = Crawler(GID)
    crawler.get_fixtures(**kwargs)
