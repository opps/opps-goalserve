# coding:utf-8

import base64
import json

from datetime import timedelta
from django.utils import timezone as datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.files import File
from django.utils.text import slugify
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.conf import settings
from tempfile import NamedTemporaryFile

from opps.images.models import Image
from .countries import COUNTRIES

User = get_user_model()

TZ_DELTA = timedelta(hours=getattr(settings, "TZ_DELTA", 2))

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

PLAYER_POSITION = {
    'goalkeeper': _("Goal Keeper"),
    'midfielder': _("Mid Fielder"),
    'attacker': _("Attacker"),
}


class GoalServeModel(models.Model):

    g_id = models.CharField(
        _("Goalserve ID"), max_length=255, null=True, unique=True)
    g_static_id = models.CharField(_("Goalserve  Static ID"), max_length=255,
                                   null=True, unique=True)
    g_fix_id = models.CharField(_("Goalserve Fixture ID"), max_length=255,
                                null=True)
    g_player_id = models.CharField(_("Goalserve Player ID"), max_length=255,
                                   null=True)
    g_event_id = models.CharField(_("Goalserve Event ID"), max_length=255,
                                  null=True)
    g_bet_id = models.CharField(
        _("Goalserve Bet ID"), max_length=255, null=True)

    g_driver_id = models.CharField(
        _("Goalserve Driver ID"), max_length=255, null=True, unique=True)
    g_team_id = models.CharField(
        _("Goalserve Team ID"), max_length=255, null=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    extra = models.TextField(_('extra data'), null=True, blank=True)

    @property
    def extra_data(self):
        try:
            return json.loads(self.extra)
        except:
            return {}

    def set_extra(self, **kwargs):
        if self.extra:
            extra = self.extra_data
            extra.update(kwargs)
            self.extra = json.dumps(extra)
        else:
            self.extra = json.dumps(kwargs)

    def get_extra(self, key):
        return self.extra_data.get(key)

    class Meta:
        abstract = True


class Base64Imaged(models.Model):
    image_base = models.TextField(_("Image"), blank=True, null=True)
    image_file = models.ForeignKey('images.Image', null=True, blank=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=_(u'Image File'))

    @property
    def image(self):
        return self.image_base and base64.decodestring(self.image_base)

    @image.setter
    def image(self, data):  # lint:ok
        self.image_base = base64.encodestring(data)

    @property
    def image_url(self):
        if not self.image_file:
            return 'http://placehold.it/50x50/'
        return self.image_file.archive.url

    @property
    def http_image_url(self):
        if not self.image_file:
            return 'http://placehold.it/50x50/'
        return "http://{img.site.domain}{img.archive.url}".format(
            img=self.image_file
        )

    def create_image(self):
        if not self.image_base:
            return

        f = NamedTemporaryFile()
        f.file.write(self.image_base.decode('base64'))
        f.file.flush()
        archive = File(f)
        image = Image.objects.create(
            site=Site.objects.get(pk=settings.SITE_ID),
            title=self.name,
            slug=slugify(self.name),
            archive=archive,
            user=User.objects.all()[0],
            tags=u"goalserve,sport,{}".format(self.name)
        )
        return image

    def set_image_file(self, update=False):
        if update or not self.image_file:
            self.image_file = self.create_image()
            self.save()

    class Meta:
        abstract = True


class Country(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, unique=True,
                            choices=COUNTRIES)

    display_name = models.CharField(
        _("Display name"), max_length=255, null=True, blank=True)

    def get_name(self):
        return self.display_name or self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Category(GoalServeModel):

    name = models.CharField(_("Name"), max_length=255, null=True, blank=True)
    country = models.ForeignKey("goalserve.Country", verbose_name=_("Country"),
                                on_delete=models.SET_NULL, null=True)

    display_name = models.CharField(
        _("Display name"), max_length=255, null=True, blank=True)

    def get_name(self):
        return self.display_name or self.name

    def __unicode__(self):
        return self.display_name or self.name or unicode(_('No name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Stadium(GoalServeModel, Base64Imaged):

    name = models.CharField(_("Stadium name"), max_length=255, null=True,
                            blank=True)

    display_name = models.CharField(_("Display name"), max_length=255,
                                    null=True, blank=True)

    def get_name(self):
        return self.display_name or self.name

    country = models.ForeignKey("goalserve.Country",
                                verbose_name=_("Country"),
                                on_delete=models.SET_NULL, null=True)

    surface = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')


class Team(GoalServeModel, Base64Imaged):

    name = models.CharField(_(u"Team name"), max_length=255, null=True,
                            blank=True)

    display_name = models.CharField(_(u"Display name"), max_length=255,
                                    null=True, blank=True)

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

    founded = models.CharField(_(u"Founded"), null=True,
                               max_length=255, blank=True)

    coach = models.CharField(_(u"Coach"), null=True, max_length=255,
                             blank=True)

    abbr = models.CharField(_(u'Abbreviation'), null=True, blank=True,
                            max_length=255)

    def get_name(self):
        return self.display_name or self.name

    def __unicode__(self):
        return self.display_name or self.name or unicode(_('No name'))

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')


class Player(GoalServeModel, Base64Imaged):

    name = models.CharField(_("Player name"), max_length=255, null=True,
                            blank=True)

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
    number = models.CharField(_("Number"), max_length=255, null=True,
                              blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.name or u'', self.team)

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

    def get_position(self):
        return PLAYER_POSITION.get(
            self.position.lower() if self.position else '',
            self.position
        )


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
    stadium_name = models.CharField(_("Stadium name"), max_length=255,
                                    null=True, blank=True)

    localteam_goals = models.IntegerField(_("Local result"), default=0)

    visitorteam_goals = models.IntegerField(_("Visitor result"), default=0)

    week_number = models.IntegerField(_('Week number'), null=True, blank=True)
    group_name = models.CharField(_("Grupo"), max_length=255,
                                  null=True, blank=True)

    @property
    def round_number(self):
        return self.week_number

    @property
    def teams(self):
        return [self.localteam, self.visitorteam]

    @property
    def fmatch_time(self):
        try:
            match_time = self.match_time - TZ_DELTA
            return match_time.strftime("%d/%m/%Y %H:%M")
        except:
            return ''

    @property
    def fstatus(self):
        return self.status

    @property
    def group(self):
        """
        set priority to group_name and if is empty should find group
        through MatchStandings
        """
        try:
            if self.group_name:
                return self.group_name
            return MatchStandings.objects.get(
                category=self.category, team=self.localteam).group
        except:
            return None

    @property
    def name(self):
        try:
            return u"""{self.localteam} x {self.visitorteam}
            - {self.fmatch_time} - {self.fstatus}""".format(self=self)
        except:
            return self.pk

    @property
    def title(self):
        try:
            return (u"{self.category} - {self.localteam} x "
                    u"{self.visitorteam}".format(self=self))
        except:
            return self.pk

    def __unicode__(self):
        return u"{0} x {1}".format(self.localteam, self.visitorteam)

    def local_lineup(self):
        return self.matchlineup_set.filter(team=self.localteam)

    def visitor_lineup(self):
        return self.matchlineup_set.filter(team=self.visitorteam)

    def get_transmission_events(self):
        t = self.transmission_set.filter(
            transmissionevent__isnull=False
        )
        if not t:
            return {}

        t = t[0]

        return [
            {
                "id_message": e.id_message,
                "event": e.event,
                "minute": e.minute,
                "team": e.team.id if e.team else '',
                "player": e.player.id if e.player else '',
                "player_in": e.player_in.id if e.player_in else '',
                "player_out": e.player_out.id if e.player_out else '',
                "f1team": e.f1team.id if e.f1team else '',
                "driver": e.driver.id if e.driver else '',
                "acao": e.acao,
                "half": e.half,
                "text": e.text
            }
            for e in t.transmissionevent_set.all()
        ]

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

    order = models.IntegerField(_("Order"), default=0)

    def get_position(self):
        return PLAYER_POSITION.get(
            self.player_position.lower() if self.player_position else '',
            self.player_position
        )

    def __unicode__(self):
        return u"{} - {} - {}".format(self.match, self.player.name,
                                      self.team.name)

    class Meta:
        verbose_name = _('Match Lineup')
        verbose_name_plural = _('Match Lineups')
        ordering = ('order',)


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
        return u"{} - off:{} in:{}".format(self.match, self.player_off,
                                           self.player_in)

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
                               null=True, blank=True,
                               on_delete=models.SET_NULL)
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
    season = models.CharField(verbose_name=_("Season"),
                              max_length=255, null=True, blank=True)
    round = models.CharField(verbose_name=_("Round"),
                             max_length=255, null=True, blank=True)
    team = models.ForeignKey("goalserve.Team", verbose_name=_("Team"),
                             on_delete=models.SET_NULL, null=True)
    position = models.CharField(verbose_name=_("Position"),
                                max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    recent_form = models.CharField(verbose_name=_("Recent results"),
                                   max_length=255, null=True, blank=True)
    total_gd = models.CharField(verbose_name=_("Goals Difference"),
                                max_length=255, null=True, blank=True)
    total_p = models.CharField(verbose_name=_("Points"),
                               max_length=255, null=True, blank=True)

    overall_gp = models.CharField(verbose_name=_("Matches"),
                                  max_length=255, null=True, blank=True)

    overall_gs = models.CharField(verbose_name=_("Goals Scored"),
                                  max_length=255, null=True, blank=True)
    overall_ga = models.CharField(verbose_name=_("Goals Against"),
                                  max_length=255, null=True, blank=True)

    overall_w = models.CharField(verbose_name=_("Wins"),
                                 max_length=255, null=True, blank=True)
    overall_l = models.CharField(verbose_name=_("Loses"),
                                 max_length=255, null=True, blank=True)

    description = models.CharField(verbose_name=_("Description"),
                                   max_length=255, null=True, blank=True)
    group = models.CharField(verbose_name=_("Group"),
                             max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"{self.category} - {self.team} = {self.position}".format(
            self=self)

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
    display_name = models.CharField(_("Display name"), max_length=255,
                                    null=True, blank=True)

    def get_name(self):
        return self.display_name or self.name

    class Meta:
        verbose_name = _('F1 Tournament')
        verbose_name_plural = _('F1 Tournaments')

    def __unicode__(self):
        return self.name


class F1Track(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    display_name = models.CharField(_("Display name"), max_length=255,
                                    null=True, blank=True)

    country = models.CharField(_("Country"), max_length=255,
                               null=True, blank=True)

    locality = models.CharField(_("Locality"), max_length=255,
                                null=True, blank=True)

    link = models.CharField(_("Link"), max_length=255,
                            null=True, blank=True)

    flag = models.ForeignKey('images.Image', null=True, blank=True,
                             on_delete=models.SET_NULL,
                             verbose_name=_(u"Flag"),
                             related_name='f1track_flag')

    track_map = models.ForeignKey('images.Image', null=True, blank=True,
                                  on_delete=models.SET_NULL,
                                  verbose_name=_(u"Mapa do circuito"),
                                  related_name='f1track_map')

    def __unicode__(self):
        return u"{o.name} - {o.country} - {o.locality}".format(o=self)

    def get_name(self):
        return self.display_name or self.name

    class Meta:
        verbose_name = _(u'F1 Track')
        verbose_name_plural = _(u'F1 Tracks')


class F1Race(GoalServeModel, Base64Imaged):
    tournament = models.ForeignKey("goalserve.F1Tournament",
                                   verbose_name=_("Category"),
                                   on_delete=models.SET_NULL, null=True)
    race_type = models.CharField(_("Race Type"), max_length=255,
                                 choices=RACE_TYPES, default="race")
    status = models.CharField(_("Status"), max_length=255, null=True,
                              blank=True)
    circuit = models.ForeignKey('goalserve.F1Track',
                                verbose_name=_("Track"),
                                on_delete=models.SET_NULL,
                                null=True, blank=True)
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

    def __unicode__(self):
        return u"{self.race_type} - {self.tournament}".format(self=self)

    @property
    def lap_length(self):
        """
        Lap is served in miles
        """
        if self.distance:
            try:
                return round(float(self.distance) / 100 * 1.6, 3)
            except:
                return self.distance
        return 0

    @property
    def results(self):
        return self.f1results_set.all()

    @property
    def results_html(self):
        html = ['<ul>']
        [html.append(
            "<li>{r.pos} - {r.driver.name} - {r.team.name}</li>".format(
                r=result
            )) for result in self.results]
        html += ['</ul>']

        return "".join(html)


class F1Team(GoalServeModel, Base64Imaged):
    name = models.CharField(_("Name"), max_length=255)
    post = models.IntegerField(_("Post"), null=True, blank=True)
    points = models.IntegerField(_("Points"), null=True, blank=True)
    display_name = models.CharField(_('Display name'), blank=True, null=True,
                                    max_length=255)
    country = models.CharField(_('Country'), null=True, blank=True,
                               max_length=255)
    tires = models.CharField(_(u'Tires'), null=True, blank=True,
                             max_length=255)
    website = models.URLField(_(u'Site'), null=True, blank=True)
    engine = models.CharField(_(u'Engine'), null=True, blank=True,
                              max_length=255)
    titles = models.CharField(_(u'Titles'), null=True, blank=True,
                              max_length=255)
    launch_date = models.IntegerField(_(u'Launch date'), blank=True,
                                      null=True)

    def get_name(self):
        return self.display_name or self.name

    class Meta:
        verbose_name = _('F1 Team')
        verbose_name_plural = _('F1 Teams')

    def __unicode__(self):
        return self.name


class Driver(GoalServeModel, Base64Imaged):
    name = models.CharField(_("Name"), max_length=255)
    team = models.ForeignKey("goalserve.F1Team", null=True, blank=True,
                             on_delete=models.SET_NULL)
    post = models.IntegerField(_("Post"), null=True, blank=True)
    points = models.IntegerField(_("Points"), null=True, blank=True)

    helmet = models.ForeignKey('images.Image', null=True, blank=True,
                               related_name='driver_helmet')
    display_name = models.CharField(_('Display name '), blank=True, null=True,
                                    max_length=255)

    country = models.CharField(_('Country'), null=True, blank=True,
                               max_length=255)
    short_name = models.CharField(_("Short name"), blank=True, null=True,
                                  max_length=255)
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    birth_city = models.CharField(_("Birth City"), blank=True, null=True,
                                  max_length=255)
    titles = models.CharField(_("Titles"), blank=True, null=True,
                              max_length=255)
    past_teams = models.CharField(_("Past Teams"), blank=True, null=True,
                                  max_length=255)
    first_race = models.CharField(_("First Race"), blank=True, null=True,
                                  max_length=255)

    def get_name(self):
        return self.display_name or self.name

    @property
    def helmet_url(self):
        if not self.helmet:
            return "http://placehold.it/32x32/"
        return self.helmet.archive.url

    class Meta:
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')

    def __unicode__(self):
        return self.name


class F1Results(GoalServeModel):
    race = models.ForeignKey("goalserve.F1Race", verbose_name=_("Race"))
    pos = models.IntegerField(_("Position"), null=True, blank=True)
    driver = models.ForeignKey("goalserve.Driver", verbose_name=_("Driver"))
    team = models.ForeignKey("goalserve.F1Team")
    time = models.CharField(_("Time"), max_length=255, null=True, blank=True)
    pitstops = models.IntegerField(null=True, blank=True)
    is_retired = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('F1 Result')
        verbose_name_plural = _('F1 Results')

    def __unicode__(self):
        return "{self.race} - {self.driver} - {self.pos}".format(self=self)


class F1Commentary(GoalServeModel):
    race = models.ForeignKey("goalserve.F1Race", verbose_name=_("Race"))
    period = models.CharField(_("Period"), max_length=255, null=True)
    comment = models.TextField(_("Comment"), blank=True)

    class Meta:
        verbose_name = _('F1 Commentary')
        verbose_name_plural = _('F1 Commentaries')

    def __unicode__(self):
        return self.comment


class RaceDriverPosition(models.Model):
    TABLE = (
        ("1", _(u"Start")),
        ("2", _(u"Real time")),
        ("3", _(u"Final"))
    )
    race = models.ForeignKey(F1Race)
    table = models.CharField(max_length=255, choices=TABLE)
    driver = models.ForeignKey(Driver)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ('position',)
        verbose_name = _(u'Race driver position')
        verbose_name_plural = _(u'Race driver positions')

    def __unicode__(self):
        return u"{s.race} {s.driver.name} {s.table} {s.position}".format(
            s=self)
