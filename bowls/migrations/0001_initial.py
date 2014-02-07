# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'bowls_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bowls', ['Ingredient'])

        # Adding model 'Recipe'
        db.create_table(u'bowls_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cuisine', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('preparation', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'bowls', ['Recipe'])

        # Adding model 'Recipe_Ingredient'
        db.create_table(u'bowls_recipe_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bowls.Recipe'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bowls.Ingredient'])),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'bowls', ['Recipe_Ingredient'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'bowls_ingredient')

        # Deleting model 'Recipe'
        db.delete_table(u'bowls_recipe')

        # Deleting model 'Recipe_Ingredient'
        db.delete_table(u'bowls_recipe_ingredient')


    models = {
        u'bowls.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bowls.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cuisine': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bowls.Ingredient']", 'through': u"orm['bowls.Recipe_Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preparation': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'bowls.recipe_ingredient': {
            'Meta': {'object_name': 'Recipe_Ingredient'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Ingredient']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Recipe']"})
        }
    }

    complete_apps = ['bowls']