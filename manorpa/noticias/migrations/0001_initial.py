# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CategoriaNoticia'
        db.create_table('noticias_categorianoticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40, db_index=True)),
        ))
        db.send_create_signal('noticias', ['CategoriaNoticia'])

        # Adding model 'Noticia'
        db.create_table('noticias_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.CategoriaNoticia'])),
            ('imagen', self.gf('manorpa.noticias.thumbs.ImageWithThumbsField')(max_length=100)),
            ('contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('noticias', ['Noticia'])


    def backwards(self, orm):
        
        # Deleting model 'CategoriaNoticia'
        db.delete_table('noticias_categorianoticia')

        # Deleting model 'Noticia'
        db.delete_table('noticias_noticia')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('manorpa.multimedia.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'noticias.categorianoticia': {
            'Meta': {'object_name': 'CategoriaNoticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        },
        'noticias.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.CategoriaNoticia']"}),
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('manorpa.noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['noticias']
