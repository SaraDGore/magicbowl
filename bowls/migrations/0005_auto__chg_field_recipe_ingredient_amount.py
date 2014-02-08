# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe_Ingredient.amount'
        db.alter_column(u'bowls_recipe_ingredient', 'amount', self.gf('django.db.models.fields.CharField')(max_length=25))

    def backwards(self, orm):

        # Changing field 'Recipe_Ingredient.amount'
        db.alter_column(u'bowls_recipe_ingredient', 'amount', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'bowls.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'bowls.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'bowls.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bowls.Cuisine']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bowls.Ingredient']", 'through': u"orm['bowls.Recipe_Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'preparation': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'VEGGIE'", 'max_length': '10'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'bowls.recipe_ingredient': {
            'Meta': {'ordering': "['sequence']", 'object_name': 'Recipe_Ingredient'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Ingredient']"}),
            'listable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Recipe']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['bowls']