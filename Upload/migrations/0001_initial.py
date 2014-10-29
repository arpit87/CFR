# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacts'
        db.create_table(u'Upload_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cfrid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('phone1', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('phone2', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('phone3', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('email1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'Upload', ['Contacts'])

        # Adding model 'SMS'
        db.create_table(u'Upload_sms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cfrid', self.gf('django.db.models.fields.IntegerField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Upload', ['SMS'])

        # Adding model 'CallLog'
        db.create_table(u'Upload_calllog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cfrid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Upload', ['CallLog'])


    def backwards(self, orm):
        # Deleting model 'Contacts'
        db.delete_table(u'Upload_contacts')

        # Deleting model 'SMS'
        db.delete_table(u'Upload_sms')

        # Deleting model 'CallLog'
        db.delete_table(u'Upload_calllog')


    models = {
        u'Upload.calllog': {
            'Meta': {'object_name': 'CallLog'},
            'cfrid': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'Upload.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'cfrid': ('django.db.models.fields.IntegerField', [], {}),
            'email1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'email3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'phone1': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'phone2': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'phone3': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'Upload.sms': {
            'Meta': {'object_name': 'SMS'},
            'cfrid': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Upload']