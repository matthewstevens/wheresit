# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('items_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_tags', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('items', ['Item'])

        # Adding model 'BorrowedItem'
        db.create_table('items_borroweditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Person'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', to=orm['profiles.Person'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item', to=orm['items.Item'])),
        ))
        db.send_create_signal('items', ['BorrowedItem'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('items_item')

        # Deleting model 'BorrowedItem'
        db.delete_table('items_borroweditem')


    models = {
        'items.borroweditem': {
            'Meta': {'object_name': 'BorrowedItem'},
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Person']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item'", 'to': "orm['items.Item']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['profiles.Person']"})
        },
        'items.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'meta_tags': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'profiles.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['items']