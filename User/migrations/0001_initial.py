# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserDetails'
        db.create_table(u'User_userdetails', (
            ('cfrid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('date_joined', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'User', ['UserDetails'])


    def backwards(self, orm):
        # Deleting model 'UserDetails'
        db.delete_table(u'User_userdetails')


    models = {
        u'User.userdetails': {
            'Meta': {'object_name': 'UserDetails'},
            'cfrid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['User']