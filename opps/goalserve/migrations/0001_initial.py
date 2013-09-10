# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'goalserve_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'goalserve', ['Country'])

        # Adding model 'Category'
        db.create_table(u'goalserve_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal(u'goalserve', ['Category'])

        # Adding model 'Stadium'
        db.create_table(u'goalserve_stadium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL)),
            ('surface', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Stadium'])

        # Adding model 'Team'
        db.create_table(u'goalserve_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('stadium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Stadium'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('founded', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('coach', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Team'])

        # Adding model 'Player'
        db.create_table(u'goalserve_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Player'])

        # Adding model 'Match'
        db.create_table(u'goalserve_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Category'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('match_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('localteam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='match_localteam', null=True, on_delete=models.SET_NULL, to=orm['goalserve.Team'])),
            ('visitorteam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='match_visitorteam', null=True, on_delete=models.SET_NULL, to=orm['goalserve.Team'])),
            ('ht_result', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('stadium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Stadium'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('attendance_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('referee_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('localteam_goals', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visitorteam_goals', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('week_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Match'])

        # Adding model 'MatchStats'
        db.create_table(u'goalserve_matchstats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL)),
            ('team_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shots', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shots_on_goal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fouls', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('corners', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('offsides', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('possesiontime', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('saves', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchStats'])

        # Adding model 'MatchLineUp'
        db.create_table(u'goalserve_matchlineup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('team_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL)),
            ('player_status', self.gf('django.db.models.fields.CharField')(default='player', max_length=255)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Player'])),
            ('player_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('player_position', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchLineUp'])

        # Adding model 'MatchSubstitutions'
        db.create_table(u'goalserve_matchsubstitutions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('player_off', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matchsubstitutions_off', null=True, to=orm['goalserve.Player'])),
            ('player_in', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matchsubstitutions_in', null=True, to=orm['goalserve.Player'])),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team_status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchSubstitutions'])

        # Adding model 'MatchCommentary'
        db.create_table(u'goalserve_matchcommentary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('important', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_goal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchCommentary'])

        # Adding model 'MatchEvent'
        db.create_table(u'goalserve_matchevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('own_goal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('penalty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Player'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchEvent'])

        # Adding model 'MatchStandings'
        db.create_table(u'goalserve_matchstandings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Category'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('round', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('recent_form', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('total_gd', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('total_p', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('overall_gp', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('overall_gs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('overall_ga', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('overall_w', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('overall_l', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchStandings'])

        # Adding model 'F1Tournament'
        db.create_table(u'goalserve_f1tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'goalserve', ['F1Tournament'])

        # Adding model 'F1Track'
        db.create_table(u'goalserve_f1track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('flag', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='f1track_flag', null=True, on_delete=models.SET_NULL, to=orm['images.Image'])),
            ('track_map', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='f1track_map', null=True, on_delete=models.SET_NULL, to=orm['images.Image'])),
        ))
        db.send_create_signal(u'goalserve', ['F1Track'])

        # Adding model 'F1Race'
        db.create_table(u'goalserve_f1race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Tournament'], null=True, on_delete=models.SET_NULL)),
            ('race_type', self.gf('django.db.models.fields.CharField')(default='race', max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('circuit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Track'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('distance', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('total_laps', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('laps_running', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('race_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['F1Race'])

        # Adding model 'F1Team'
        db.create_table(u'goalserve_f1team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['F1Team'])

        # Adding model 'Driver'
        db.create_table(u'goalserve_driver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['images.Image'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Team'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('post', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Driver'])

        # Adding model 'F1Results'
        db.create_table(u'goalserve_f1results', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Race'])),
            ('pos', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('driver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Driver'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Team'])),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pitstops', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_retired', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'goalserve', ['F1Results'])

        # Adding model 'F1Commentary'
        db.create_table(u'goalserve_f1commentary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_driver_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('g_team_id', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Race'])),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['F1Commentary'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'goalserve_country')

        # Deleting model 'Category'
        db.delete_table(u'goalserve_category')

        # Deleting model 'Stadium'
        db.delete_table(u'goalserve_stadium')

        # Deleting model 'Team'
        db.delete_table(u'goalserve_team')

        # Deleting model 'Player'
        db.delete_table(u'goalserve_player')

        # Deleting model 'Match'
        db.delete_table(u'goalserve_match')

        # Deleting model 'MatchStats'
        db.delete_table(u'goalserve_matchstats')

        # Deleting model 'MatchLineUp'
        db.delete_table(u'goalserve_matchlineup')

        # Deleting model 'MatchSubstitutions'
        db.delete_table(u'goalserve_matchsubstitutions')

        # Deleting model 'MatchCommentary'
        db.delete_table(u'goalserve_matchcommentary')

        # Deleting model 'MatchEvent'
        db.delete_table(u'goalserve_matchevent')

        # Deleting model 'MatchStandings'
        db.delete_table(u'goalserve_matchstandings')

        # Deleting model 'F1Tournament'
        db.delete_table(u'goalserve_f1tournament')

        # Deleting model 'F1Track'
        db.delete_table(u'goalserve_f1track')

        # Deleting model 'F1Race'
        db.delete_table(u'goalserve_f1race')

        # Deleting model 'F1Team'
        db.delete_table(u'goalserve_f1team')

        # Deleting model 'Driver'
        db.delete_table(u'goalserve_driver')

        # Deleting model 'F1Results'
        db.delete_table(u'goalserve_f1results')

        # Deleting model 'F1Commentary'
        db.delete_table(u'goalserve_f1commentary')


    models = {
        "%s.%s" % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'goalserve.category': {
            'Meta': {'object_name': 'Category'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.country': {
            'Meta': {'object_name': 'Country'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.driver': {
            'Meta': {'object_name': 'Driver'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1commentary': {
            'Meta': {'object_name': 'F1Commentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1race': {
            'Meta': {'object_name': 'F1Race'},
            'circuit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Track']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'laps_running': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'race_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'race_type': ('django.db.models.fields.CharField', [], {'default': "'race'", 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_laps': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Tournament']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1results': {
            'Meta': {'object_name': 'F1Results'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Driver']"}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_retired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pitstops': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1team': {
            'Meta': {'object_name': 'F1Team'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1tournament': {
            'Meta': {'object_name': 'F1Tournament'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1track': {
            'Meta': {'object_name': 'F1Track'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'f1track_flag'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'f1track_map'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"})
        },
        u'goalserve.match': {
            'Meta': {'object_name': 'Match'},
            'attendance_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'ht_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_localteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"}),
            'localteam_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'referee_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'visitorteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_visitorteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"}),
            'visitorteam_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'goalserve.matchcommentary': {
            'Meta': {'object_name': 'MatchCommentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchevent': {
            'Meta': {'object_name': 'MatchEvent'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'own_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchlineup': {
            'Meta': {'object_name': 'MatchLineUp'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']"}),
            'player_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'player_status': ('django.db.models.fields.CharField', [], {'default': "'player'", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchstandings': {
            'Meta': {'object_name': 'MatchStandings'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overall_ga': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_gp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_gs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_l': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_w': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recent_form': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'round': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_gd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_p': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchstats': {
            'Meta': {'object_name': 'MatchStats'},
            'corners': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'fouls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'offsides': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'possesiontime': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchsubstitutions': {
            'Meta': {'object_name': 'MatchSubstitutions'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_in': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_in'", 'null': 'True', 'to': u"orm['goalserve.Player']"}),
            'player_off': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_off'", 'null': 'True', 'to': u"orm['goalserve.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.player': {
            'Meta': {'object_name': 'Player'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'coach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'crop_example': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_x1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_x2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'halign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'smart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'valign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['goalserve']