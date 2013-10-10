## -*- coding: utf-8 -*-

import logging

from opps.contrib.notifications.tasks import notify
from opps.goalserve.models import Team, Player, F1Team, Driver, MatchLineUp, RaceDriverPosition, F1Race, F1Results
from opps.containers.models import Container

# tastypie
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.exceptions import Unauthorized
from tastypie.resources import ALL, ALL_WITH_RELATIONS, convert_post_to_patch



logger = logging.getLogger()


def check_access(user):
    if not (user.is_authenticated() and (user.is_superuser or user.is_staff)):
        raise Unauthorized("Sorry, access denied.")

class GoalserveAuthorization(Authorization):


    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        check_access(bundle.request.user)
        return object_list

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        check_access(bundle.request.user)
        return True

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        check_access(bundle.request.user)
        return object_list

    def create_detail(self, object_list, bundle):
        check_access(bundle.request.user)
        return True

    def update_list(self, object_list, bundle):
        check_access(bundle.request.user)
        return object_list

    def update_detail(self, object_list, bundle):
        check_access(bundle.request.user)
        return True

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class SSEMixin(object):
    def patch_list(self, request, **kwargs):
        response = super(SSEMixin, self).patch_list(request, **kwargs)

        patch = convert_post_to_patch(request)
        data = self.deserialize(patch, patch.body)

        try:
            objects = data.get('objects', [])
            container = Container.objects.get(pk=data.get('container_id'))
            notify.delay(objects, type="json", container=container, user=request.user)
        except Exception as e:
            logger.error("Impossible to create notification {}, {}".format(data, e))

        return response


class RaceDriverPositionResoure(SSEMixin, ModelResource):
    class Meta:
        queryset = RaceDriverPosition.objects.all()
        resource_name = "racedriverposition"
        authorization = GoalserveAuthorization()
        filtering = {
            'race': ALL_WITH_RELATIONS,
            'driver': ALL_WITH_RELATIONS,
            'table': ALL,
        }


    def alter_list_data_to_serialize(self, request, data):
        race_id = request.GET.get('race__id')
        if race_id:
            race = F1Race.objects.get(pk=race_id)
            results =  F1Results.objects.filter(
                race__tournament=race.tournament,
            ).order_by('pos')
            data['qualification'] = [
                {'driver': r.driver.get_name(),
                 'driver_id': r.driver.id,
                 'pos': r.pos,
                 'team': r.team.get_name()}
                for r in results.filter(race__race_type='qualification')
            ]
            data['race'] = [
                {'driver': r.driver.get_name(),
                 'driver_id': r.driver.id,
                 'pos': r.pos,
                 'team': r.team.get_name()}
                for r in results.filter(race__race_type='race')
            ]

        return data

    def dehydrate(self, bundle):
        # import ipdb;ipdb.set_trace()
        bundle.data['race_id'] = bundle.obj.race.id
        bundle.data['driver_id'] = bundle.obj.driver.id
        bundle.data['driver_name'] = bundle.obj.driver.name
        bundle.data['driver_display_name'] = bundle.obj.driver.display_name
        bundle.data['driver_helmet'] = bundle.obj.driver.helmet_url
        bundle.data['driver_country'] = bundle.obj.driver.country

        try:
            bundle.data['team_name'] = bundle.obj.driver.team.name
            bundle.data['team_display_name'] = bundle.obj.driver.team.display_name
        except:
            bundle.data['team_name'] = ''
            bundle.data['team_display_name'] = ''

        return bundle


    def save(self, bundle, **kwargs):
        obj_id = bundle.data.get('id')
        race = F1Race.objects.get(pk=bundle.data.get('race_id'))
        table = bundle.data.get('table')
        driver = Driver.objects.get(pk=bundle.data.get('driver_id'))
        position = bundle.data.get('position', 0)
        if obj_id:
            # existing should update
            obj = RaceDriverPosition.objects.get(pk=obj_id)
            obj.table = table
            obj.position = position
            obj.save()
        else:
            # new should create
            RaceDriverPosition.objects.create(
                race=race,
                table=table,
                driver=driver,
                position=position
            )
        return bundle


class PlayerResource(SSEMixin, ModelResource):
    class Meta:
        queryset = Player.objects.all()
        resource_name = "player"
        authorization = GoalserveAuthorization()  # Authorization
        excludes = ('image_base', 'created_at', 'extra', 'g_bet_id',
                    'g_driver_id', 'g_event_id', 'g_fix_id', 'g_player_id',
                    'g_static_id', 'g_team_id')


    def hydrate(self, bundle):

        lineup_id = bundle.data.get('lineup_id')
        lineup = MatchLineUp.objects.get(id=int(lineup_id))
        player_id = bundle.data.get('id')
        player = Player.objects.get(id=player_id)


        player_dict = {k: v for k, v in player.__dict__.iteritems() if not k.startswith("_")}
        lineup_dict = {k: v for k, v in lineup.__dict__.iteritems() if not k.startswith("_")}


        for k, v in player_dict.iteritems():
            if not k in bundle.data:
                bundle.data[k] = v

        number = bundle.data.get('number')
        if number:
            try:
                lineup.player_number = int(number)
            except:
                logger.warning(
                    "Error coercing number {0} for player {1}".format(
                        number, player_id
                    )
                )

        lineup.player_position = bundle.data.get('position', lineup.player_position)
        lineup.order = bundle.data.get('order', lineup.order)
        lineup.save()

        try:
            # put match in manual mode
            # celery tasks will ignore lineup updates
            match = lineup.match
            match.set_extra(manual_mode=True)
            match.save()
        except Exception as e:
            logger.warning(
                "Error putting in manual mode {m.id} - {msg}".format(
                    m=match,
                    msg=str(e)
                )
            )

        return bundle



# home made api for tasks

def get_team_by_id(_id):
    try:
        return Team.objects.get(pk=int(_id))
    except TypeError:
        pass
    except Team.DoesNotExist:
        pass


def get_player_by_id(_id):
    try:
        return Player.objects.get(pk=int(_id))
    except TypeError:
        pass
    except Player.DoesNotExist:
        pass


def get_f1team_by_id(_id):
    try:
        return F1Team.objects.get(pk=int(_id))
    except TypeError:
        pass
    except F1Team.DoesNotExist:
        pass


def get_driver_by_id(_id):
    try:
        return Driver.objects.get(pk=int(_id))
    except TypeError:
        pass
    except Driver.DoesNotExist:
        pass
