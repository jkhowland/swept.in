# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'App.api_key'
        db.add_column('apps_app', 'api_key',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apikeytoken.ApiKey'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'App.api_key'
        db.delete_column('apps_app', 'api_key_id')


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
        }
    }

    complete_apps = ['apps']