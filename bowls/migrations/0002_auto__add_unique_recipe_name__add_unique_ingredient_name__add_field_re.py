# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Recipe', fields ['name']
        db.create_unique(u'bowls_recipe', ['name'])

        # Adding unique constraint on 'Ingredient', fields ['name']
        db.create_unique(u'bowls_ingredient', ['name'])

        # Adding field 'Recipe_Ingredient.sequence'
        db.add_column(u'bowls_recipe_ingredient', 'sequence',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Ingredient', fields ['name']
        db.delete_unique(u'bowls_ingredient', ['name'])

        # Removing unique constraint on 'Recipe', fields ['name']
        db.delete_unique(u'bowls_recipe', ['name'])

        # Deleting field 'Recipe_Ingredient.sequence'
        db.delete_column(u'bowls_recipe_ingredient', 'sequence')


    models = {
        u'bowls.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'bowls.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cuisine': ('django.db.models.fields.CharField', [], {'default': "'AMERICAN'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bowls.Ingredient']", 'through': u"orm['bowls.Recipe_Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'preparation': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'VEGGIE'", 'max_length': '10'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'bowls.recipe_ingredient': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'Recipe_Ingredient'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Ingredient']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Recipe']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['bowls']