# coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from opps.core.models import Publishable


class GoalServeModel(models.Model):

    g_id = models.CharField(_("Goalserve ID"), max_length=255, null=True)
    g_static_id = models.CharField(_("Goalserve  Static ID"), max_length=255,
                                   null=True)
    g_fix_id = models.CharField(_("Goalserve Fixture ID"), max_length=255,
                                null=True)
    g_player_id = models.CharField(_("Goalserve Player ID"), max_length=255,
                                   null=True)
    g_event_id = models.CharField(_("Goalserve Event ID"), max_length=255,
                                  null=True)

    class Meta:
        abstract = True


class Country(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, required=True)


class Category(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, required=True)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"))


class Team(GoalServeModel):

    name = models.CharField(_("Team name"), max_length=255)


class Player(GoalServeModel):

    name = models.CharField(_("Team name"), max_length=255)


class Match(Publishable, GoalServeModel):

    status = models.CharField(_("Status"), max_length=255, null=True)

    transmission_date = models.DateTimeField(_("Transmission time"))
    create_live_blog = models.BooleanField(_("Create live blog"), default=True)

    category = models.ForeignKey("goalserve.Category",
                                 verbose_name=_("Category"))

    localteam = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))
    visitorteam = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))
    ht_result = models.CharField(_("HT Result"), max_length=255, null=True)


class MatchEvent(GoalServeModel):

    EVENT_TYPES = (
        ("goal", _("Goal")),
        ("yellowcard", _("Yellow Card")),
        ("redcard", _("Red Card")),
    )

    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))

    event_type = models.CharField(_("Event type"), max_length=255,
                                  choices=EVENT_TYPES)

    minute = models.PositiveIntegerField(_("Minute"), null=True)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))
    player = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    result = models.CharField(_("Result"), max_length=255, null=True)
