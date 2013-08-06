# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Base64Imaged'
        db.create_table(u'goalserve_base64imaged', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_base', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Base64Imaged'])

        # Adding model 'Country'
        db.create_table(u'goalserve_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'goalserve', ['Country'])

        # Adding model 'Category'
        db.create_table(u'goalserve_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal(u'goalserve', ['Category'])

        # Adding model 'Stadium'
        db.create_table(u'goalserve_stadium', (
            (u'base64imaged_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['goalserve.Base64Imaged'], unique=True, primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL)),
            ('surface', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Stadium'])

        # Adding model 'Team'
        db.create_table(u'goalserve_team', (
            (u'base64imaged_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['goalserve.Base64Imaged'], unique=True, primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Country'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('stadium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Stadium'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('founded', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('coach', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Team'])

        # Adding model 'Player'
        db.create_table(u'goalserve_player', (
            (u'base64imaged_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['goalserve.Base64Imaged'], unique=True, primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Team'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('birthplace', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Player'])

        # Adding model 'Match'
        db.create_table(u'goalserve_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
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
            ('possesiontime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('saves', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
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
        ))
        db.send_create_signal(u'goalserve', ['MatchLineUp'])

        # Adding model 'MatchSubstitutions'
        db.create_table(u'goalserve_matchsubstitutions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('player_off', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matchsubstitutions_off', null=True, to=orm['goalserve.Player'])),
            ('player_in', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matchsubstitutions_in', null=True, to=orm['goalserve.Player'])),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchSubstitutions'])

        # Adding model 'MatchCommentary'
        db.create_table(u'goalserve_matchcommentary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
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
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
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

        # Adding model 'MatchResult'
        db.create_table(u'goalserve_matchresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_insert', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
            ('site_iid', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True, max_length=4, null=True, blank=True)),
            ('site_domain', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('date_available', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, db_index=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.Match'])),
            ('localteam_result', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visitorteam_result', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'goalserve', ['MatchResult'])

        # Adding model 'F1Tournament'
        db.create_table(u'goalserve_f1tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'goalserve', ['F1Tournament'])

        # Adding model 'F1Race'
        db.create_table(u'goalserve_f1race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Tournament'], null=True, on_delete=models.SET_NULL)),
            ('race_type', self.gf('django.db.models.fields.CharField')(default='race', max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('distance', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('total_laps', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('laps_running', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('race_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['F1Race'])

        # Adding model 'F1Team'
        db.create_table(u'goalserve_f1team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post', self.gf('django.db.models.fields.IntegerField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'goalserve', ['F1Team'])

        # Adding model 'Driver'
        db.create_table(u'goalserve_driver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Team'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('post', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['Driver'])

        # Adding model 'F1Commentary'
        db.create_table(u'goalserve_f1commentary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goalserve.F1Race'])),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['F1Commentary'])


    def backwards(self, orm):
        # Deleting model 'Base64Imaged'
        db.delete_table(u'goalserve_base64imaged')

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

        # Deleting model 'MatchResult'
        db.delete_table(u'goalserve_matchresult')

        # Deleting model 'F1Tournament'
        db.delete_table(u'goalserve_f1tournament')

        # Deleting model 'F1Race'
        db.delete_table(u'goalserve_f1race')

        # Deleting model 'F1Team'
        db.delete_table(u'goalserve_f1team')

        # Deleting model 'Driver'
        db.delete_table(u'goalserve_driver')

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
        u'goalserve.base64imaged': {
            'Meta': {'object_name': 'Base64Imaged'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'goalserve.category': {
            'Meta': {'object_name': 'Category'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.country': {
            'Meta': {'object_name': 'Country'},
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'goalserve.driver': {
            'Meta': {'object_name': 'Driver'},
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'goalserve.f1commentary': {
            'Meta': {'object_name': 'F1Commentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"})
        },
        u'goalserve.f1race': {
            'Meta': {'object_name': 'F1Race'},
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laps_running': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'race_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'race_type': ('django.db.models.fields.CharField', [], {'default': "'race'", 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_laps': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Tournament']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.f1team': {
            'Meta': {'object_name': 'F1Team'},
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.IntegerField', [], {})
        },
        u'goalserve.f1tournament': {
            'Meta': {'object_name': 'F1Tournament'},
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.match': {
            'Meta': {'object_name': 'Match'},
            'attendance_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ht_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_localteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"}),
            'match_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'referee_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visitorteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_visitorteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"})
        },
        u'goalserve.matchcommentary': {
            'Meta': {'object_name': 'MatchCommentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'goalserve.matchevent': {
            'Meta': {'object_name': 'MatchEvent'},
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'own_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.matchlineup': {
            'Meta': {'object_name': 'MatchLineUp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']"}),
            'player_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'player_status': ('django.db.models.fields.CharField', [], {'default': "'player'", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.matchresult': {
            'Meta': {'object_name': 'MatchResult'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localteam_result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)}),
            'visitorteam_result': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'goalserve.matchstats': {
            'Meta': {'object_name': 'MatchStats'},
            'corners': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fouls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'offsides': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'possesiontime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.matchsubstitutions': {
            'Meta': {'object_name': 'MatchSubstitutions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_in': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_in'", 'null': 'True', 'to': u"orm['goalserve.Player']"}),
            'player_off': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_off'", 'null': 'True', 'to': u"orm['goalserve.Player']"})
        },
        u'goalserve.player': {
            'Meta': {'object_name': 'Player', '_ormbases': [u'goalserve.Base64Imaged']},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'base64imaged_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['goalserve.Base64Imaged']", 'unique': 'True', 'primary_key': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.stadium': {
            'Meta': {'object_name': 'Stadium', '_ormbases': [u'goalserve.Base64Imaged']},
            u'base64imaged_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['goalserve.Base64Imaged']", 'unique': 'True', 'primary_key': 'True'}),
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surface': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.team': {
            'Meta': {'object_name': 'Team', '_ormbases': [u'goalserve.Base64Imaged']},
            u'base64imaged_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['goalserve.Base64Imaged']", 'unique': 'True', 'primary_key': 'True'}),
            'coach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'founded': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
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
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sources.Source']", 'null': 'True', 'blank': 'True'}),
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
        },
        u'sources.source': {
            'Meta': {'unique_together': "(('site', 'slug'),)", 'object_name': 'Source'},
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        }
    }

    complete_apps = ['goalserve']