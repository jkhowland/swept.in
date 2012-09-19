# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table('events_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subuser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subusers.SubUser'])),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('curriculum_bool', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('events', ['Activity'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Activity'])),
            ('starting_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('ending_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('answer_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('question_description', self.gf('django.db.models.fields.TextField')()),
            ('answer_array', self.gf('django.db.models.fields.TextField')()),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=1, decimal_places=1)),
        ))
        db.send_create_signal('events', ['Event'])

        # Adding model 'AchievementType'
        db.create_table('events_achievementtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.App'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum_bool', self.gf('django.db.models.fields.IntegerField')()),
            ('achievement_min', self.gf('django.db.models.fields.IntegerField')()),
            ('achievement_max', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('events', ['AchievementType'])

        # Adding model 'Achievement'
        db.create_table('events_achievement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subuser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subusers.SubUser'])),
            ('achievement_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.AchievementType'])),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=1, decimal_places=1)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('events', ['Achievement'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table('events_activity')

        # Deleting model 'Event'
        db.delete_table('events_event')

        # Deleting model 'AchievementType'
        db.delete_table('events_achievementtype')

        # Deleting model 'Achievement'
        db.delete_table('events_achievement')


    models = {
        'apikeytoken.apikey': {
            'Meta': {'object_name': 'ApiKey'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'apps.app': {
            'Meta': {'object_name': 'App'},
            'api_key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apikeytoken.ApiKey']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'achievement_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.AchievementType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '1', 'decimal_places': '1'}),
            'subuser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subusers.SubUser']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'events.achievementtype': {
            'Meta': {'object_name': 'AchievementType'},
            'achievement_max': ('django.db.models.fields.IntegerField', [], {}),
            'achievement_min': ('django.db.models.fields.IntegerField', [], {}),
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apps.App']"}),
            'curriculum_bool': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'events.activity': {
            'Meta': {'object_name': 'Activity'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apps.App']"}),
            'curriculum_bool': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subuser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subusers.SubUser']"})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Activity']"}),
            'answer_array': ('django.db.models.fields.TextField', [], {}),
            'answer_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ending_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '1', 'decimal_places': '1'}),
            'question_description': ('django.db.models.fields.TextField', [], {}),
            'starting_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'subusers.subuser': {
            'Meta': {'object_name': 'SubUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['events']