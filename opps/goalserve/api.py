# -*- coding: utf-8 -*-

from .models import Team, Player, F1Team, Driver

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