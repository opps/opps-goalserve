
# coding: utf-8
import json
import celery
import datetime
from django.utils import timezone

from opps.db import Db

from .crawler import Crawler
from .no_photo import team_no_photo, player_no_photo
from .actions import  get_match,get_schedule, get_standings, get_fixtures # set_team_image, set_player_image, set_stadium_image,
from .utils import data_match

# TODO: set this model dynamically
# OPPS_GOALSERVE_TRANSMISSION_MODEL = 'x.Transmission'
from portal.transmission.models import Transmission

GID = 'c93ce5a5b570433b8a7d96b3c53f119d'

def log_it(s):
    try:
        open("/tmp/goalserve_task_run.log", "a").write(
            u"{now} - {s}\n".format(now=datetime.datetime.now(), s=s)
        )
    except:
        pass


@celery.task
def get_matches(country_name, match_id=None, cat_id=None):
    crawler = Crawler(GID)
    crawler.get_matches(countries=[country_name], match_id=match_id,
                        get_players=False, cat_id=cat_id)
    log_it('get_matches')


@celery.task.periodic_task(run_every=timezone.timedelta(minutes=10))
def set_images_for_active_transmissions(transmission_id=None):
    if not transmission_id:
        active_transmissions = Transmission.objects.filter(
            published=True,
            event_type__slug="soccer"
        )
    else:
        active_transmissions = Transmission.objects.filter(pk=transmission_id)

    # print active_transmissions

    for transmission in active_transmissions:
            # set_team_image({"pk__in": [t.pk for t in transmission.match.teams]})
            for team in transmission.match.teams:
                if not team.image_file and not team.image_base == team_no_photo:
                    team.set_image_file()

            # set_player_image(
            #     {"pk__in": [p.pk for p in transmission.match.matchlineup_set.all()]}
            # )
            for lineup in transmission.match.matchlineup_set.all():
                player = lineup.player
                if not player.image_file and not player.image_base == player_no_photo:
                    player.set_image_file()

            # if transmission.match.stadium:
            #     set_stadium_image({"pk": transmission.match.stadium.pk})
            if transmission.match.stadium:
                transmission.match.stadium.set_image_file()

    log_it('set_images_for_active_transmissions')


@celery.task.periodic_task(run_every=timezone.timedelta(minutes=15))
def update_feed_for_active_transmissions(transmission_id=None):
    if not transmission_id:
        active_transmissions = Transmission.objects.filter(
            published=True,
            event_type__slug="soccer"
        )
    else:
        active_transmissions = Transmission.objects.filter(pk=transmission_id)

    # print active_transmissions

    for transmission in active_transmissions:
        get_match(country=transmission.match.category.country.name.lower(),
                  match_id=[transmission.match.g_static_id],
                  cat_id=transmission.match.category.g_id if transmission.match.category else None,
                  get_players=True)

        data = json.dumps(data_match(transmission.match.id))
        redis = Db('goalservematch', transmission.match.id)
        redis.publish(data)

    log_it('update_feed_for_active_transmissions')

@celery.task.periodic_task(run_every=timezone.timedelta(hours=24))
def update_schedule():
    get_schedule()
    log_it('update_schedule')


@celery.task.periodic_task(run_every=timezone.timedelta(hours=4))
def update_standings(transmission_id=None):
    if not transmission_id:
        active_transmissions = Transmission.objects.filter(
            published=True,
            event_type__slug="soccer"
        )
    else:
        active_transmissions = Transmission.objects.filter(pk=transmission_id)

    for transmission in active_transmissions:
        get_standings(country=transmission.match.category.country.name.lower())

    log_it('update_standings')


@celery.task.periodic_task(run_every=timezone.timedelta(hours=8))
def update_fixtures(transmission_id=None):
    if not transmission_id:
        active_transmissions = Transmission.objects.filter(
            published=True,
            event_type__slug="soccer"
        )
    else:
        active_transmissions = Transmission.objects.filter(pk=transmission_id)

    for transmission in active_transmissions:
        get_fixtures(country=transmission.match.category.country.name.lower())

    log_it('update_standings')
