# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OwnedItem'
        db.create_table('items_owneditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['items.Item'])),
        ))
        db.send_create_signal('items', ['OwnedItem'])

        # Deleting field 'BorrowedItem.item'
        db.delete_column('items_borroweditem', 'item_id')

        # Adding field 'BorrowedItem.owned_item'
        db.add_column('items_borroweditem', 'owned_item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='owned_item', to=orm['items.OwnedItem']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'OwnedItem'
        db.delete_table('items_owneditem')

        # Adding field 'BorrowedItem.item'
        db.add_column('items_borroweditem', 'item',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='item', to=orm['items.Item']),
                      keep_default=False)

        # Deleting field 'BorrowedItem.owned_item'
        db.delete_column('items_borroweditem', 'owned_item_id')


    models = {
        'items.borroweditem': {
            'Meta': {'object_name': 'BorrowedItem'},
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Person']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owned_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_item'", 'to': "orm['items.OwnedItem']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['profiles.Person']"})
        },
        'items.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'meta_tags': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'items.owneditem': {
            'Meta': {'object_name': 'OwnedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['items.Item']"})
        },
        'profiles.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['items']