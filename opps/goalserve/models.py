# coding:utf-8

import base64
from django.utils import timezone as datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .countries import COUNTRIES

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


COUNTRIES_NAMES = [(country, country.title()) for country in COUNTRIES]


class GoalServeModel(models.Model):

    g_id = models.CharField(_("Goalserve ID"), max_length=255, null=True, unique=True)
    g_static_id = models.CharField(_("Goalserve  Static ID"), max_length=255,
                                   null=True, unique=True)
    g_fix_id = models.CharField(_("Goalserve Fixture ID"), max_length=255,
                                null=True)
    g_player_id = models.CharField(_("Goalserve Player ID"), max_length=255,
                                   null=True)
    g_event_id = models.CharField(_("Goalserve Event ID"), max_length=255,
                                  null=True)
    g_bet_id = models.CharField(_("Goalserve Bet ID"), max_length=255,
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    class Meta:
        abstract = True


class Base64Imaged(models.Model):
    image_base = models.TextField(_("Image"), blank=True, null=True)

    @property
    def image(self):
        return self.image_base and base64.decodestring(self.image_base)

    @image.setter
    def image(self, data):  # lint:ok
        self.image_base = base64.encodestring(data)

    @property
    def image_url(self):
        return 'http://placehold.it/50x50/'

    class Meta:
        abstract = True


class Country(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, unique=True,
                            choices=COUNTRIES_NAMES)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Category(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, null=True, blank=True)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"),
                                on_delete=models.SET_NULL, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Stadium(GoalServeModel, Base64Imaged):

    name = models.CharField(_("Stadium name"), max_length=255, null=True, blank=True)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"),
                                on_delete=models.SET_NULL, null=True)
    surface = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')


class Team(GoalServeModel, Base64Imaged):

    name = models.CharField(_("Team name"), max_length=255, null=True, blank=True)
    full_name = models.CharField(_("Team full name"), max_length=255,
                                 null=True, blank=True)
    country = models.ForeignKey("goalserve.Country",
                                verbose_name=_("Country"),
                                null=True, blank=True,
                                on_delete=models.SET_NULL)
    stadium = models.ForeignKey("goalserve.Stadium",
                                verbose_name=_("Stadium"),
                                null=True, blank=True,
                                on_delete=models.SET_NULL)
    founded = models.CharField(_("Founded"), null=True,
                                 max_length=255, blank=True)
    coach = models.CharField(_("Coach"), null=True, max_length=255, blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.name, self.country)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')



class Player(GoalServeModel, Base64Imaged):

    name = models.CharField(_("Player name"), max_length=255, null=True, blank=True)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             null=True, blank=True,
                             on_delete=models.SET_NULL)

    birthdate = models.DateField(_("Birth date"), null=True, blank=True)
    age = models.IntegerField(_("Age"), null=True, blank=True)

    nationality = models.CharField(_("Nationality"), max_length=255,
                                   null=True, blank=True)
    birthplace = models.CharField(_("Birth place"), max_length=255,
                                  null=True, blank=True)
    position = models.CharField(_("Position"), max_length=255,
                                null=True, blank=True)
    weight = models.CharField(_("Weight"), max_length=255,
                              null=True, blank=True)
    height = models.CharField(_("Height"), max_length=255,
                              null=True, blank=True)
    number = models.CharField(_("Number"), max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.name, self.team)

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')


class Match(GoalServeModel):

    status = models.CharField(_("Status"), max_length=255,
                              null=True, blank=True)

    category = models.ForeignKey("goalserve.Category",
                                 verbose_name=_("Category"),
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)

    match_time = models.DateTimeField(_("Match time"), null=True, blank=True)

    localteam = models.ForeignKey("goalserve.Team", verbose_name=_("Local"),
                                  on_delete=models.SET_NULL, null=True,
                                  related_name='match_localteam')
    visitorteam = models.ForeignKey("goalserve.Team",
                                    verbose_name=_("Visitor"),
                                    related_name='match_visitorteam',
                                    null=True,
                                    on_delete=models.SET_NULL)
    ht_result = models.CharField(_("HT Result"), max_length=255,
                                 null=True, blank=True)
    stadium = models.ForeignKey("goalserve.Stadium", verbose_name=_("Stadium"),
                                null=True, blank=True,
                                on_delete=models.SET_NULL)
    attendance_name = models.CharField(_("Attendance name"), max_length=255,
                                       null=True, blank=True)
    time_name = models.CharField(_("Time name"), max_length=255,
                                 null=True, blank=True)
    referee_name = models.CharField(_("Referee name"), max_length=255,
                                    null=True, blank=True)

    localteam_goals = models.IntegerField(_("Local result"), default=0)
    visitorteam_goals = models.IntegerField(_("Visitor result"), default=0)

    @property
    def fmatch_time(self):
        try:
            return self.match_time.strftime("%d/%m/%Y %H:%M")
        except:
            return ''

    @property
    def fstatus(self):
        return self.status

    @property
    def name(self):
        try:
            return u"""{self.localteam.name} x {self.visitorteam.name}
            - {self.fmatch_time} - {self.fstatus}""".format(self=self)
        except:
            return self.pk

    @property
    def title(self):
        try:
            return u"""{self.category.name} - {self.localteam.name} x {self.visitorteam.name}"""\
                   .format(self=self)
        except:
            return self.pk

    def __unicode__(self):
        return u"({}) - {} x {}".format(self.g_static_id, self.localteam, self.visitorteam)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')


class MatchStats(models.Model):

    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)

    shots = models.IntegerField(_("Shots"), null=True, blank=True)
    shots_on_goal = models.IntegerField(_("Shots on goal"), null=True,
                                        blank=True)
    fouls = models.IntegerField(_("Fouls"), null=True, blank=True)
    corners = models.IntegerField(_("Corners"), null=True, blank=True)
    offsides = models.IntegerField(_("Offsides"), null=True, blank=True)
    possesiontime = models.CharField(_("Possesion time"), null=True,
                                        blank=True, max_length=255)
    saves = models.IntegerField(_("Saves"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)


    @property
    def yellowcards(self):
        return self.match.matchevent_set.filter(
            team=self.team,
            event_type='yellowcard'
        ).count()

    @property
    def redcards(self):
        return self.match.matchevent_set.filter(
            team=self.team,
            event_type='redcard'
        ).count()

    @property
    def goals(self):
        return self.match.matchevent_set.filter(
            team=self.team,
            event_type='goal'
        ).count()

    def __unicode__(self):
        return u"{} - {}".format(self.match, self.team)

    class Meta:
        verbose_name = _('Match Stats')
        verbose_name_plural = _('Match Stats')


class MatchLineUp(models.Model):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)

    player_status = models.CharField(_("Player Status"), max_length=255,
                                     choices=PLAYER_STATUS, default="player")
    player = models.ForeignKey("goalserve.Player", verbose_name=_("Player"))
    player_number = models.IntegerField(_("Player number"), null=True,
                                        blank=True)
    player_position = models.CharField(_("Player position"), max_length=255,
                                         blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)


    def __unicode__(self):
        return u"{} - {} - {}".format(self.match, self.player.name, self.team.name)

    class Meta:
        verbose_name = _('Match Lineup')
        verbose_name_plural = _('Match Lineups')



class MatchSubstitutions(models.Model):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    player_off = models.ForeignKey("goalserve.Player",
                                   verbose_name=_("Player Off"),
                                   related_name='matchsubstitutions_off',
                                   null=True, blank=True)
    player_in = models.ForeignKey("goalserve.Player",
                                  verbose_name=_("Player In"),
                                  related_name='matchsubstitutions_in',
                                  null=True, blank=True)
    minute = models.IntegerField(_("Minute"), null=True, blank=True)

    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS, null=True, blank=True)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    def __unicode__(self):
        return u"{} - off:{} in:{}".format(self.match, self.player_off, self.player_in)

    class Meta:
        verbose_name = _('Match Substitution')
        verbose_name_plural = _('Match Substitutions')



class MatchCommentary(GoalServeModel):
    match = models.ForeignKey("goalserve.Match", verbose_name=_("Match"))
    important = models.BooleanField(_("Important"), default=False)
    is_goal = models.BooleanField(_("Is Goal"), default=False)
    minute = models.IntegerField(_("Minute"), null=True, blank=True)
    comment = models.TextField(_("Comment"), blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.match, self.comment)

    class Meta:
        verbose_name = _('Match Commentary')
        verbose_name_plural = _('Match Commentaries')


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

    minute = models.IntegerField(_("Minute"), null=True, blank=True)
    team_status = models.CharField(_("Team status"), max_length=255,
                                   choices=TEAM_STATUS)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)
    player = models.ForeignKey("goalserve.Player", verbose_name=_("Player"),
                               null=True, blank=True, on_delete=models.SET_NULL)
    result = models.CharField(_("Result"), max_length=255, null=True,
                              blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.match, self.event_type)

    class Meta:
        verbose_name = _('Match Event')
        verbose_name_plural = _('Match Events')


class MatchStandings(GoalServeModel):
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"),
                                on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("goalserve.Category",
                                 verbose_name=_("Category"),
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    timestamp = models.CharField(max_length=255, null=True, blank=True)
    season = models.CharField(max_length=255, null=True, blank=True)
    round = models.CharField(max_length=255, null=True, blank=True)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    recent_form = models.CharField(max_length=255, null=True, blank=True)
    total_gd = models.CharField(max_length=255, null=True, blank=True)
    total_p = models.CharField(max_length=255, null=True, blank=True)

    overall_gp = models.CharField(max_length=255, null=True, blank=True)

    overall_gs = models.CharField(max_length=255, null=True, blank=True)
    overall_ga = models.CharField(max_length=255, null=True, blank=True)

    overall_w = models.CharField(max_length=255, null=True, blank=True)
    overall_l = models.CharField(max_length=255, null=True, blank=True)

    description = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"{self.category} - {self.team} = {self.position}".format(self=self)

    class Meta:
        verbose_name = _('Match Standing')
        verbose_name_plural = _('Match Standings')




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

    class Meta:
        verbose_name = _('F1 Tournament')
        verbose_name_plural = _('F1 Tournaments')


class F1Race(GoalServeModel):
    tournament = models.ForeignKey("goalserve.F1Tournament",
                                 verbose_name=_("Category"),
                                 on_delete=models.SET_NULL, null=True)
    race_type = models.CharField(_("Race Type"), max_length=255,
                                 choices=RACE_TYPES, default="race")
    status = models.CharField(_("Status"), max_length=255, null=True,
                              blank=True)
    track = models.CharField(_("Track"), max_length=255, null=True, blank=True)
    distance = models.CharField(_("Distance"), max_length=255, null=True,
                                blank=True)
    total_laps = models.CharField(_("Total laps"), max_length=255, null=True,
                                  blank=True)
    laps_running = models.CharField(_("Total laps"), max_length=255, null=True,
                                    blank=True)
    race_time = models.DateTimeField(_("Race time"), null=True, blank=True)

    class Meta:
        verbose_name = _('F1 Race')
        verbose_name_plural = _('F1 Races')


class F1Team(GoalServeModel):
    name = models.CharField(_("Name"), max_length=255)
    post = models.IntegerField(_("Post"))
    points = models.IntegerField(_("Points"))

    class Meta:
        verbose_name = _('F1 Team')
        verbose_name_plural = _('F1 Teams')


class Driver(GoalServeModel):
    name = models.CharField(_("Name"), max_length=255)
    team = models.ForeignKey("goalserve.F1Team", null=True, blank=True,
                             on_delete=models.SET_NULL)
    post = models.IntegerField(_("Post"), null=True, blank=True)
    points = models.IntegerField(_("Points"), null=True, blank=True)

    class Meta:
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')


class F1Results(GoalServeModel):
    race = models.ForeignKey("goalserve.F1Race", verbose_name=_("Race"))
    pos = models.IntegerField(_("Position"))
    driver = models.ForeignKey("goalserve.Driver", verbose_name=_("Driver"))
    team = models.ForeignKey("goalserve.F1Team")
    time = models.CharField(_("Time"), max_length=255, null=True, blank=True)
    pitstops = models.IntegerField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('F1 Result')
        verbose_name_plural = _('F1 Results')



class F1Commentary(GoalServeModel):
    race = models.ForeignKey("goalserve.F1Race", verbose_name=_("Race"))
    period = models.CharField(_("Period"), max_length=255, null=True)
    comment = models.TextField(_("Comment"), blank=True)

    class Meta:
        verbose_name = _('F1 Commentary')
        verbose_name_plural = _('F1 Commentaries')
