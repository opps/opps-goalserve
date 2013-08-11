# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column(u'goalserve_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Player.name'
        db.alter_column(u'goalserve_player', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Team.name'
        db.alter_column(u'goalserve_team', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Stadium.name'
        db.alter_column(u'goalserve_stadium', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Category.name'
        db.alter_column(u'goalserve_category', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Player.name'
        db.alter_column(u'goalserve_player', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Team.name'
        db.alter_column(u'goalserve_team', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Stadium.name'
        db.alter_column(u'goalserve_stadium', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

    models = {
        u'goalserve.category': {
            'Meta': {'object_name': 'Category'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.country': {
            'Meta': {'object_name': 'Country'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.driver': {
            'Meta': {'object_name': 'Driver'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1race': {
            'Meta': {'object_name': 'F1Race'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laps_running': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'race_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'race_type': ('django.db.models.fields.CharField', [], {'default': "'race'", 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_laps': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Tournament']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1results': {
            'Meta': {'object_name': 'F1Results'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Driver']"}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_retired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pitstops': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pos': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1team': {
            'Meta': {'object_name': 'F1Team'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1tournament': {
            'Meta': {'object_name': 'F1Tournament'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.match': {
            'Meta': {'object_name': 'Match'},
            'attendance_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'visitorteam_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'goalserve.matchcommentary': {
            'Meta': {'object_name': 'MatchCommentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['goalserve']