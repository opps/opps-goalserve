# -*- coding: utf-8 -*-

import logging

from opps.goalserve.models import Team, Player, F1Team, Driver, MatchLineUp

# tastypie
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.exceptions import Unauthorized


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

class PlayerResource(ModelResource):
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

        lineup.player_number = bundle.data.get('number', lineup.player_number)
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
