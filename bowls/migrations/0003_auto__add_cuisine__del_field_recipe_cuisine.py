# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cuisine'
        db.create_table(u'bowls_cuisine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'bowls', ['Cuisine'])

        # Deleting field 'Recipe.cuisine'
        db.delete_column(u'bowls_recipe', 'cuisine')

        # Adding M2M table for field cuisines on 'Recipe'
        m2m_table_name = db.shorten_name(u'bowls_recipe_cuisines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'bowls.recipe'], null=False)),
            ('cuisine', models.ForeignKey(orm[u'bowls.cuisine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'cuisine_id'])


    def backwards(self, orm):
        # Deleting model 'Cuisine'
        db.delete_table(u'bowls_cuisine')

        # Adding field 'Recipe.cuisine'
        db.add_column(u'bowls_recipe', 'cuisine',
                      self.gf('django.db.models.fields.CharField')(default='AMERICAN', max_length=10),
                      keep_default=False)

        # Removing M2M table for field cuisines on 'Recipe'
        db.delete_table(db.shorten_name(u'bowls_recipe_cuisines'))


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
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Ingredient']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bowls.Recipe']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['bowls']