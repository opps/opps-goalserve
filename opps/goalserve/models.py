# coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from opps.core.models import Publishable


# ==============================================================================
# Soccer
# ==============================================================================

TEAM_STATUS = (
    ('localteam', _('Local')),
    ('visitorteam', _('Visitor'))
)


PLAYER_STATUS = (
    ('substitute', _('Substitute')),
    ('player', _('Player'))
)


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


class Stadium(GoalServeModel):

    name = models.CharField(_("Stadium name"), max_length=255)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"))


class Team(GoalServeModel):

    name = models.CharField(_("Team name"), max_length=255)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"))
    stadium = models.ForeignKey("goalserve.Stadium", verbose_name=_("Stadium"))


class Player(GoalServeModel):

    name = models.CharField(_("Team name"), max_length=255)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             null=True)


class Match(GoalServeModel):

    status = models.CharField(_("Status"), max_length=255, null=True)

    category = models.ForeignKey("goalserve.Category",
                                 verbose_name=_("Category"))

    match_time = models.DateTimeField(_("Match time"))

    localteam = models.ForeignKey("goalserve.Team", verbose_name=_("Local"))
    visitorteam = models.ForeignKey("goalserve.Team", verbose_name=_("Visitor"))
    ht_result = models.CharField(_("HT Result"), max_length=255, null=True)
    stadium = models.ForeignKey("goalserve.Stadium", verbose_name=_("Stadium"))

    attendance_name = models.CharField(_("Attendance name"), max_length=255,
                                       null=True)
    time_name = models.CharField(_("Time name"), max_length=255,
                                       null=True)
    referee_name = models.CharField(_("Referee name"), max_length=255,
                                       null=True)


class MatchStats(models.Model):

    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)

    shots = models.IntegerField(_("Shots"), null=True)
    shots_on_goal = models.IntegerField(_("Shots on goal"), null=True)
    fouls = models.IntegerField(_("Fouls"), null=True)
    corners = models.IntegerField(_("Corners"), null=True)
    offsides = models.IntegerField(_("Offsides"), null=True)
    possesiontime = models.IntegerField(_("Possesion time"), null=True)
    saves = models.IntegerField(_("Saves"), null=True)

    @property
    def yellowcards(self):
        return self.match.match_event_set.filter(
            team=self.team,
            event_type='yellowcard'
        ).count()

    @property
    def redcards(self):
        return self.match.match_event_set.filter(
            team=self.team,
            event_type='redcard'
        ).count()

    @property
    def goals(self):
        return self.match.match_event_set.filter(
            team=self.team,
            event_type='goal'
        ).count()


class MatchLineUp(models.Model):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))

    player_status = models.CharField(_("Player Status"), max_length=255,
                                     choices=PLAYER_STATUS, default="player")
    player = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    player_number = models.IntegerField(_("Player number"), null=True)
    player_position = models.CharField(_("Player position"), max_length=255)


class MatchSubstitutions(models.Model):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    player_off = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    player_in = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    minute = models.IntegerField(_("Minute"), null=True)


class MatchCommentary(GoalServeModel):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    important = models.BooleanField(_("Important"), default=False)
    is_goal = models.BooleanField(_("Is Goal"), default=False)
    minute = models.IntegerField(_("Minute"), null=True)
    comment = models.TextField(_("Comment"), blank=True)


class MatchEvent(GoalServeModel):

    EVENT_TYPES = (
        ("goal", _("Goal")),
        ("yellowcard", _("Yellow Card")),
        ("redcard", _("Red Card")),
    )

    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))

    event_type = models.CharField(_("Event type"), max_length=255,
                                  choices=EVENT_TYPES)

    own_goal = models.BooleanField(_("Own Goal"), default=False)
    penalty = models.BooleanField(_("Penalty"), default=False)

    minute = models.IntegerField(_("Minute"), null=True)
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"))
    player = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    result = models.CharField(_("Result"), max_length=255, null=True)


class Transmission(Publishable):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    transmission_date = models.DateTimeField(_("Transmission time"))
    create_live_blog = models.BooleanField(_("Create live blog"), default=True)
    live_blog = models.ForeignKey("liveblogging.Event")


class MatchResult(Publishable):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    localteam_result = models.IntegerField(_("Local result"), default=0)
    visitorteam_result = models.IntegerField(_("Visitor result"), default=0)

    @property
    def localteam(self):
        return self.match.localteam

    @property
    def visitorteam(self):
        return self.match.visitorteam


# ==============================================================================
#  F1
# ==============================================================================


RACE_TYPES = (
    ("race", _("Race")),
    ("qualification", _("Qualification")),
    ("last_practice", _("Last Practice")),
    ("second_practice", _("Second Practice")),
    ("first_practice", _("First Practice")),
)


class F1Tournament(GoalServeModel):
    name = models.CharField(_("Name"), max_length=255)


class F1Race(GoalServeModel):
    tournament = models.ForeignKey("goalserve.F1Tournament",
                                 verbose_name=_("Category"))
    race_type = models.CharField(_("Race Type"), max_length=255,
                                 choices=RACE_TYPES, default="race")
    status = models.CharField(_("Status"), max_length=255, null=True)
    track = models.CharField(_("Track"), max_length=255, null=True)
    distance = models.CharField(_("Distance"), max_length=255, null=True)
    total_laps = models.CharField(_("Total laps"), max_length=255, null=True)
    laps_running = models.CharField(_("Total laps"), max_length=255, null=True)
    race_time = models.DateTimeField(_("Race time"), null=True)


class F1Team(GoalServeModel):
    name = models.CharField(_("Name"), max_length=255)
    post = models.IntegerField(_("Post"))
    points = models.IntegerField(_("Points"))


class Driver(GoalServeModel):
    name = models.CharField(_("Name"), max_length=255)
    team = models.ForeignKey("goalserve.F1Team")
    post = models.IntegerField(_("Post"))
    points = models.IntegerField(_("Points"))


class F1Results():
    race = models.ForeignKey("goalserve.F1Race", verbose_name=_("Race"))
    pos = models.IntegerField(_("Position"))
    driver = models.ForeignKey("goalserve.Driver", _("Driver"))
    team = models.ForeignKey("goalserve.F1Team")
    time = models.CharField(_("Time"), max_length=255)
    pitstops = models.IntegerField(null=True)
    is_retired = models.BooleanField(default=False)
