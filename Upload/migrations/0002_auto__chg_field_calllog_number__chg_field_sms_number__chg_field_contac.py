# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CallLog.number'
        db.alter_column(u'Upload_calllog', 'number', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'SMS.number'
        db.alter_column(u'Upload_sms', 'number', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Contacts.phone2'
        db.alter_column(u'Upload_contacts', 'phone2', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'Contacts.phone3'
        db.alter_column(u'Upload_contacts', 'phone3', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'Contacts.phone1'
        db.alter_column(u'Upload_contacts', 'phone1', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

    def backwards(self, orm):

        # Changing field 'CallLog.number'
        db.alter_column(u'Upload_calllog', 'number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'SMS.number'
        db.alter_column(u'Upload_sms', 'number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Contacts.phone2'
        db.alter_column(u'Upload_contacts', 'phone2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Contacts.phone3'
        db.alter_column(u'Upload_contacts', 'phone3', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Contacts.phone1'
        db.alter_column(u'Upload_contacts', 'phone1', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'Upload.calllog': {
            'Meta': {'object_name': 'CallLog'},
            'cfrid': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
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
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'})
        },
        u'Upload.sms': {
            'Meta': {'object_name': 'SMS'},
            'cfrid': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['Upload']