# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.answer_type'
        db.delete_column('events_event', 'answer_type')

        # Deleting field 'Event.answer_array'
        db.delete_column('events_event', 'answer_array')

        # Deleting field 'Event.percentage'
        db.delete_column('events_event', 'percentage')

        # Deleting field 'Event.question_description'
        db.delete_column('events_event', 'question_description')

        # Adding field 'Event.task_id'
        db.add_column('events_event', 'task_id',
                      self.gf('django.db.models.fields.CharField')(default='task_id', max_length=200),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column('events_event', 'description',
                      self.gf('django.db.models.fields.TextField')(default='description'),
                      keep_default=False)

        # Adding field 'Event.notes'
        db.add_column('events_event', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='notes'),
                      keep_default=False)

        # Deleting field 'Activity.app'
        db.delete_column('events_activity', 'app_id')

        # Deleting field 'Activity.curriculum_bool'
        db.delete_column('events_activity', 'curriculum_bool')

        # Deleting field 'Activity.subject'
        db.delete_column('events_activity', 'subject')

        # Deleting field 'Activity.activity_group'
        db.delete_column('events_activity', 'activity_group_id')

        # Adding field 'Activity.kit_id'
        db.add_column('events_activity', 'kit_id',
                      self.gf('django.db.models.fields.CharField')(default='kit_id', max_length=200),
                      keep_default=False)

        # Adding field 'Activity.user_json'
        db.add_column('events_activity', 'user_json',
                      self.gf('django.db.models.fields.TextField')(default='user_json'),
                      keep_default=False)

        # Deleting field 'AchievementType.app'
        db.delete_column('events_achievementtype', 'app_id')

        # Deleting field 'AchievementType.curriculum_bool'
        db.delete_column('events_achievementtype', 'curriculum_bool')


    def backwards(self, orm):
        # Adding field 'Event.answer_type'
        db.add_column('events_event', 'answer_type',
                      self.gf('django.db.models.fields.CharField')(default='F', max_length=1),
                      keep_default=False)

        # Adding field 'Event.answer_array'
        db.add_column('events_event', 'answer_array',
                      self.gf('django.db.models.fields.TextField')(default='F'),
                      keep_default=False)

        # Adding field 'Event.percentage'
        db.add_column('events_event', 'percentage',
                      self.gf('django.db.models.fields.DecimalField')(default='.9', max_digits=1, decimal_places=1),
                      keep_default=False)

        # Adding field 'Event.question_description'
        db.add_column('events_event', 'question_description',
                      self.gf('django.db.models.fields.TextField')(default='description'),
                      keep_default=False)

        # Deleting field 'Event.task_id'
        db.delete_column('events_event', 'task_id')

        # Deleting field 'Event.description'
        db.delete_column('events_event', 'description')

        # Deleting field 'Event.notes'
        db.delete_column('events_event', 'notes')

        # Adding field 'Activity.app'
        db.add_column('events_activity', 'app',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='activity', to=orm['apps.App']),
                      keep_default=False)

        # Adding field 'Activity.curriculum_bool'
        db.add_column('events_activity', 'curriculum_bool',
                      self.gf('django.db.models.fields.IntegerField')(default='FALSE'),
                      keep_default=False)

        # Adding field 'Activity.subject'
        db.add_column('events_activity', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='subject', max_length=200),
                      keep_default=False)

        # Adding field 'Activity.activity_group'
        db.add_column('events_activity', 'activity_group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.ActivityGroup'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Activity.kit_id'
        db.delete_column('events_activity', 'kit_id')

        # Deleting field 'Activity.user_json'
        db.delete_column('events_activity', 'user_json')

        # Adding field 'AchievementType.app'
        db.add_column('events_achievementtype', 'app',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='achievement_type', to=orm['apps.App']),
                      keep_default=False)

        # Adding field 'AchievementType.curriculum_bool'
        db.add_column('events_achievementtype', 'curriculum_bool',
                      self.gf('django.db.models.fields.IntegerField')(default='FALSE'),
                      keep_default=False)


    models = {
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
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'events.activity': {
            'Meta': {'object_name': 'Activity'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kit_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subuser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subusers.SubUser']"}),
            'user_json': ('django.db.models.fields.TextField', [], {})
        },
        'events.activitygroup': {
            'Meta': {'object_name': 'ActivityGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subuser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subusers.SubUser']"})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Activity']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'ending_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'starting_time': ('django.db.models.fields.DateTimeField', [], {}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'subusers.subuser': {
            'Meta': {'object_name': 'SubUser'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['events']