
# coding: utf-8
import json
import celery
import datetime
from django.utils import timezone
from django.conf import settings

from opps.db import Db

from .crawler import Crawler
from .no_photo import team_no_photo, player_no_photo
from .actions import get_match, get_schedule, get_standings, get_fixtures, goalserve

# set_team_image, set_player_image, set_stadium_image,
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


@celery.task.periodic_task(run_every=timezone.timedelta(minutes=5))
def update_feed_for_active_transmissions(transmission_id=None):
    start_date = timezone.now() - datetime.timedelta(hours=4)
    end_date = timezone.now() + datetime.timedelta(hours=4)
    if not transmission_id:
        active_transmissions = Transmission.objects.filter(
            match__match_time__range=(start_date, end_date),
            event_type__slug="soccer",
            published=True
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


@celery.task.periodic_task(run_every=timezone.timedelta(minutes=5))
def update_standings(transmission_id=None):
    start_date = timezone.now() - datetime.timedelta(hours=24)
    end_date = timezone.now() + datetime.timedelta(hours=24)
    if not transmission_id:
        countries = Transmission.objects.filter(
            published=True,
            match__match_time__range=(start_date, end_date),
            event_type__slug="soccer"
        ).values_list('match__category__country__name', flat=True)
    else:
        countries = Transmission.objects.filter(
            pk=transmission_id
        ).values_list('match__category__country__name', flat=True)

    for country in set(countries):
        get_standings(country=country)

    log_it('update_standings')


@celery.task.periodic_task(run_every=timezone.timedelta(minutes=30))
def update_general_standings():
    countries = getattr(settings, 'OPPS_GOALSERVE_STANDINGS_COUNTRIES', ['brazil'])
    for country in countries:
        get_standings(country=country)
    log_it('update_general__standings')


@celery.task.periodic_task(run_every=timezone.timedelta(hours=8))
def update_fixtures(transmission_id=None):
    if not transmission_id:
        countries = Transmission.objects.filter(
            published=True,
            event_type__slug="soccer"
        ).values_list('match__category__country__name', flat=True)

    else:
        countries = Transmission.objects.filter(
            pk=transmission_id
        ).values_list('match__category__country__name', flat=True)

    for country in set(countries):
        get_fixtures(country=country)

    log_it('update_standings')


@celery.task.periodic_task(run_every=timezone.timedelta(hours=1))
def update_f1_drivers():
    goalserve('get_f1_drivers')


@celery.task.periodic_task(run_every=timezone.timedelta(hours=24))
def update_f1_races():
    goalserve('get_races', feed='f1-shedule')

    
@celery.task.periodic_task(run_every=timezone.timedelta(hours=1))
def update_f1_results():
    goalserve('get_races', feed='f1-results')