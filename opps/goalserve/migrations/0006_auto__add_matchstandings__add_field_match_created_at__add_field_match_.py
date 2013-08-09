# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MatchStandings'
        db.create_table(u'goalserve_matchstandings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_static_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_fix_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_player_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_event_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('g_bet_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
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
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'goalserve', ['MatchStandings'])

        # Adding field 'Match.created_at'
        db.add_column(u'goalserve_match', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Match.updated_at'
        db.add_column(u'goalserve_match', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchResult.created_at'
        db.add_column(u'goalserve_matchresult', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchResult.updated_at'
        db.add_column(u'goalserve_matchresult', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Commentary.created_at'
        db.add_column(u'goalserve_f1commentary', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Commentary.updated_at'
        db.add_column(u'goalserve_f1commentary', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Stadium.created_at'
        db.add_column(u'goalserve_stadium', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Stadium.updated_at'
        db.add_column(u'goalserve_stadium', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchCommentary.created_at'
        db.add_column(u'goalserve_matchcommentary', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchCommentary.updated_at'
        db.add_column(u'goalserve_matchcommentary', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.created_at'
        db.add_column(u'goalserve_category', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.updated_at'
        db.add_column(u'goalserve_category', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Results.created_at'
        db.add_column(u'goalserve_f1results', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Results.updated_at'
        db.add_column(u'goalserve_f1results', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchEvent.created_at'
        db.add_column(u'goalserve_matchevent', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchEvent.updated_at'
        db.add_column(u'goalserve_matchevent', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchSubstitutions.created_at'
        db.add_column(u'goalserve_matchsubstitutions', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchSubstitutions.updated_at'
        db.add_column(u'goalserve_matchsubstitutions', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Driver.created_at'
        db.add_column(u'goalserve_driver', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Driver.updated_at'
        db.add_column(u'goalserve_driver', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchStats.created_at'
        db.add_column(u'goalserve_matchstats', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchStats.updated_at'
        db.add_column(u'goalserve_matchstats', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.created_at'
        db.add_column(u'goalserve_country', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.updated_at'
        db.add_column(u'goalserve_country', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Team.created_at'
        db.add_column(u'goalserve_f1team', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Team.updated_at'
        db.add_column(u'goalserve_f1team', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.created_at'
        db.add_column(u'goalserve_player', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.updated_at'
        db.add_column(u'goalserve_player', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Race.created_at'
        db.add_column(u'goalserve_f1race', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Race.updated_at'
        db.add_column(u'goalserve_f1race', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.created_at'
        db.add_column(u'goalserve_team', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Team.updated_at'
        db.add_column(u'goalserve_team', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchLineUp.created_at'
        db.add_column(u'goalserve_matchlineup', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'MatchLineUp.updated_at'
        db.add_column(u'goalserve_matchlineup', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Tournament.created_at'
        db.add_column(u'goalserve_f1tournament', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'F1Tournament.updated_at'
        db.add_column(u'goalserve_f1tournament', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'MatchStandings'
        db.delete_table(u'goalserve_matchstandings')

        # Deleting field 'Match.created_at'
        db.delete_column(u'goalserve_match', 'created_at')

        # Deleting field 'Match.updated_at'
        db.delete_column(u'goalserve_match', 'updated_at')

        # Deleting field 'MatchResult.created_at'
        db.delete_column(u'goalserve_matchresult', 'created_at')

        # Deleting field 'MatchResult.updated_at'
        db.delete_column(u'goalserve_matchresult', 'updated_at')

        # Deleting field 'F1Commentary.created_at'
        db.delete_column(u'goalserve_f1commentary', 'created_at')

        # Deleting field 'F1Commentary.updated_at'
        db.delete_column(u'goalserve_f1commentary', 'updated_at')

        # Deleting field 'Stadium.created_at'
        db.delete_column(u'goalserve_stadium', 'created_at')

        # Deleting field 'Stadium.updated_at'
        db.delete_column(u'goalserve_stadium', 'updated_at')

        # Deleting field 'MatchCommentary.created_at'
        db.delete_column(u'goalserve_matchcommentary', 'created_at')

        # Deleting field 'MatchCommentary.updated_at'
        db.delete_column(u'goalserve_matchcommentary', 'updated_at')

        # Deleting field 'Category.created_at'
        db.delete_column(u'goalserve_category', 'created_at')

        # Deleting field 'Category.updated_at'
        db.delete_column(u'goalserve_category', 'updated_at')

        # Deleting field 'F1Results.created_at'
        db.delete_column(u'goalserve_f1results', 'created_at')

        # Deleting field 'F1Results.updated_at'
        db.delete_column(u'goalserve_f1results', 'updated_at')

        # Deleting field 'MatchEvent.created_at'
        db.delete_column(u'goalserve_matchevent', 'created_at')

        # Deleting field 'MatchEvent.updated_at'
        db.delete_column(u'goalserve_matchevent', 'updated_at')

        # Deleting field 'MatchSubstitutions.created_at'
        db.delete_column(u'goalserve_matchsubstitutions', 'created_at')

        # Deleting field 'MatchSubstitutions.updated_at'
        db.delete_column(u'goalserve_matchsubstitutions', 'updated_at')

        # Deleting field 'Driver.created_at'
        db.delete_column(u'goalserve_driver', 'created_at')

        # Deleting field 'Driver.updated_at'
        db.delete_column(u'goalserve_driver', 'updated_at')

        # Deleting field 'MatchStats.created_at'
        db.delete_column(u'goalserve_matchstats', 'created_at')

        # Deleting field 'MatchStats.updated_at'
        db.delete_column(u'goalserve_matchstats', 'updated_at')

        # Deleting field 'Country.created_at'
        db.delete_column(u'goalserve_country', 'created_at')

        # Deleting field 'Country.updated_at'
        db.delete_column(u'goalserve_country', 'updated_at')

        # Deleting field 'F1Team.created_at'
        db.delete_column(u'goalserve_f1team', 'created_at')

        # Deleting field 'F1Team.updated_at'
        db.delete_column(u'goalserve_f1team', 'updated_at')

        # Deleting field 'Player.created_at'
        db.delete_column(u'goalserve_player', 'created_at')

        # Deleting field 'Player.updated_at'
        db.delete_column(u'goalserve_player', 'updated_at')

        # Deleting field 'F1Race.created_at'
        db.delete_column(u'goalserve_f1race', 'created_at')

        # Deleting field 'F1Race.updated_at'
        db.delete_column(u'goalserve_f1race', 'updated_at')

        # Deleting field 'Team.created_at'
        db.delete_column(u'goalserve_team', 'created_at')

        # Deleting field 'Team.updated_at'
        db.delete_column(u'goalserve_team', 'updated_at')

        # Deleting field 'MatchLineUp.created_at'
        db.delete_column(u'goalserve_matchlineup', 'created_at')

        # Deleting field 'MatchLineUp.updated_at'
        db.delete_column(u'goalserve_matchlineup', 'updated_at')

        # Deleting field 'F1Tournament.created_at'
        db.delete_column(u'goalserve_f1tournament', 'created_at')

        # Deleting field 'F1Tournament.updated_at'
        db.delete_column(u'goalserve_f1tournament', 'updated_at')


    models = {
        u'accounts.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
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
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.country': {
            'Meta': {'object_name': 'Country'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'visitorteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_visitorteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"})
        },
        u'goalserve.matchcommentary': {
            'Meta': {'object_name': 'MatchCommentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
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
        u'goalserve.matchresult': {
            'Meta': {'object_name': 'MatchResult'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.CustomUser']"}),
            'visitorteam_result': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.CustomUser']"}),
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.CustomUser']"})
        }
    }

    complete_apps = ['goalserve']