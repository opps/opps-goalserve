# -*- coding: utf-8 -*-

from opps.goalserve.models import Team, Player, F1Team, Driver

# tastypie
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.exceptions import Unauthorized


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
