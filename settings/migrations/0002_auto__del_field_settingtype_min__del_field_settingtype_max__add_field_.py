# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SettingType.min'
        db.delete_column('settings_settingtype', 'min')

        # Deleting field 'SettingType.max'
        db.delete_column('settings_settingtype', 'max')

        # Adding field 'SettingType.setting_max'
        db.add_column('settings_settingtype', 'setting_max',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'SettingType.setting_min'
        db.add_column('settings_settingtype', 'setting_min',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'SettingType.value_max'
        db.add_column('settings_settingtype', 'value_max',
                      self.gf('django.db.models.fields.IntegerField')(default=15),
                      keep_default=False)

        # Adding field 'SettingType.value_min'
        db.add_column('settings_settingtype', 'value_min',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SettingType.min'
        raise RuntimeError("Cannot reverse this migration. 'SettingType.min' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SettingType.max'
        raise RuntimeError("Cannot reverse this migration. 'SettingType.max' and its values cannot be restored.")
        # Deleting field 'SettingType.setting_max'
        db.delete_column('settings_settingtype', 'setting_max')

        # Deleting field 'SettingType.setting_min'
        db.delete_column('settings_settingtype', 'setting_min')

        # Deleting field 'SettingType.value_max'
        db.delete_column('settings_settingtype', 'value_max')

        # Deleting field 'SettingType.value_min'
        db.delete_column('settings_settingtype', 'value_min')


    models = {
        'apps.app': {
            'Meta': {'object_name': 'App'},
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
        'settings.setting': {
            'Meta': {'object_name': 'Setting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'setting_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['settings.SettingType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'settings.settingtype': {
            'Meta': {'object_name': 'SettingType'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apps.App']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'setting_max': ('django.db.models.fields.IntegerField', [], {}),
            'setting_min': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'value_max': ('django.db.models.fields.IntegerField', [], {}),
            'value_min': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['settings']