# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
import opps.goalserve.models

OPPS_ADMIN_FILTERS = getattr(settings, 'OPPS_ADMIN_FILTERS', {})
FILTERS = OPPS_ADMIN_FILTERS.get('opps.goalserve', {})


class GoalServeAdmin(admin.ModelAdmin):
    exclude = ('g_id', 'g_static_id', 'g_fix_id',
               'g_player_id', 'g_event_id', 'g_bet_id',
               'g_driver_id', 'g_team_id')


class PlayerAdmin(GoalServeAdmin):
    search_fields = ['name']
    list_filter = ['position', 'team', 'nationality']
    raw_id_fields = ['team', 'image_file']


class TeamAdmin(GoalServeAdmin):
    search_fields = ['name']
    list_display = ['name', 'display_name', 'full_name', 'abbr']
    list_display_links = list_display
    list_filter = ['country']
    raw_id_fields = ['country', 'stadium', 'image_file']


class MatchAdmin(GoalServeAdmin):
    list_display = ['id', 'name', 'category', 'match_time']
    list_filter = ['category', 'match_time', 'status']
    search_fields = ['localteam__name', 'visitorteam__name', 'category__name']
    #list_filter = ['category', 'match_time', 'week_number']
    raw_id_fields = ['localteam', 'visitorteam', 'category', 'stadium']
    #list_display = ['name', 'id', 'localteam', 'visitorteam', 'g_static_id',
    #                'category']


class RaceDriverPositionAdmin(admin.ModelAdmin):
    search_fields = ['driver__name']
    list_filter = ['race', 'table']
    raw_id_fields = ['driver', 'race']
    list_display = ['race', 'table', 'driver', 'position']


class RaceAdmin(GoalServeAdmin):
    raw_id_fields = ['tournament', 'image_file', 'circuit']
    list_filter = ['tournament']
    opps_filters = FILTERS.get('RaceAdmin', {})

    def save_model(self, request, obj, form, change):
        obj.set_extra(manual_mode=True)
        obj.save()

    def queryset(self, request):
        qs = super(RaceAdmin, self).queryset(request)
        return qs.filter(**self.opps_filters)


class DriverAdmin(GoalServeAdmin):
    raw_id_fields = ['team', 'image_file', 'helmet']
    list_filter = ['team']


class ResultsAdmin(GoalServeAdmin):
    raw_id_fields = ['race', 'driver', 'team']
    list_filter = ['race']


class F1TrackAdmin(admin.ModelAdmin):
    raw_id_fields = ['flag', 'track_map']
    list_filter = ['country']
    search_fields = ['name', 'country', 'locality']


class F1TeamAdmin(admin.ModelAdmin):
    raw_id_fields = ['image_file', ]

# Models with custom admin
admin.site.register(opps.goalserve.models.RaceDriverPosition,
                    RaceDriverPositionAdmin)
admin.site.register(opps.goalserve.models.Player, PlayerAdmin)
admin.site.register(opps.goalserve.models.Team, TeamAdmin)
admin.site.register(opps.goalserve.models.Match, MatchAdmin)
admin.site.register(opps.goalserve.models.Driver, DriverAdmin)
admin.site.register(opps.goalserve.models.F1Race, RaceAdmin)
admin.site.register(opps.goalserve.models.F1Results, ResultsAdmin)
admin.site.register(opps.goalserve.models.F1Track, F1TrackAdmin)
admin.site.register(opps.goalserve.models.F1Team, F1TeamAdmin)

# other models
admin.site.register(opps.goalserve.models.Country)
admin.site.register(opps.goalserve.models.Category)
admin.site.register(opps.goalserve.models.Stadium)
admin.site.register(opps.goalserve.models.MatchStats)
admin.site.register(opps.goalserve.models.MatchLineUp)
admin.site.register(opps.goalserve.models.MatchSubstitutions)
admin.site.register(opps.goalserve.models.MatchCommentary)
admin.site.register(opps.goalserve.models.MatchEvent)
admin.site.register(opps.goalserve.models.F1Tournament)
admin.site.register(opps.goalserve.models.F1Commentary)
admin.site.register(opps.goalserve.models.MatchStandings)
