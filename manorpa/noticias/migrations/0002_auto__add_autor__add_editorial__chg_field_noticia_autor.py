# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Autor'
        db.create_table('noticias_autor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40, db_index=True)),
            ('imagen', self.gf('manorpa.noticias.thumbs.ImageWithThumbsField')(max_length=100)),
        ))
        db.send_create_signal('noticias', ['Autor'])

        # Adding model 'Editorial'
        db.create_table('noticias_editorial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Autor'])),
            ('contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging_autocomplete.models.TagAutocompleteField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('noticias', ['Editorial'])

        # Renaming column for 'Noticia.autor' to match new field type.
        db.rename_column('noticias_noticia', 'autor', 'autor_id')
        # Changing field 'Noticia.autor'
        db.alter_column('noticias_noticia', 'autor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Autor']))

        # Adding index on 'Noticia', fields ['autor']
        db.create_index('noticias_noticia', ['autor_id'])


    def backwards(self, orm):
        
        # Removing index on 'Noticia', fields ['autor']
        db.delete_index('noticias_noticia', ['autor_id'])

        # Deleting model 'Autor'
        db.delete_table('noticias_autor')

        # Deleting model 'Editorial'
        db.delete_table('noticias_editorial')

        # Renaming column for 'Noticia.autor' to match new field type.
        db.rename_column('noticias_noticia', 'autor_id', 'autor')
        # Changing field 'Noticia.autor'
        db.alter_column('noticias_noticia', 'autor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


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
        'noticias.autor': {
            'Meta': {'object_name': 'Autor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('manorpa.noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        },
        'noticias.categorianoticia': {
            'Meta': {'object_name': 'CategoriaNoticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        },
        'noticias.editorial': {
            'Meta': {'object_name': 'Editorial'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Autor']"}),
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'tags': ('tagging_autocomplete.models.TagAutocompleteField', [], {'max_length': '255', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'noticias.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Autor']"}),
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
