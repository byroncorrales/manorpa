# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Boletin'
        db.create_table('boletines_boletin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('imagen', self.gf('manorpa.boletines.thumbs.ImageWithThumbsField')(max_length=100)),
            ('boletin', self.gf('manorpa.boletines.customfilefield.ContentTypeRestrictedFileField')(max_length=100)),
            ('edicion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('boletines', ['Boletin'])


    def backwards(self, orm):
        
        # Deleting model 'Boletin'
        db.delete_table('boletines_boletin')


    models = {
        'boletines.boletin': {
            'Meta': {'object_name': 'Boletin'},
            'boletin': ('manorpa.boletines.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'edicion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('manorpa.boletines.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['boletines']
