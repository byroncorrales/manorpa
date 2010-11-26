# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Municipio.historia'
        db.delete_column('municipios_municipio', 'historia')

        # Deleting field 'Municipio.ubicacion'
        db.delete_column('municipios_municipio', 'ubicacion')

        # Adding field 'Municipio.pontencialidades'
        db.add_column('municipios_municipio', 'pontencialidades', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Municipio.gobierno'
        db.add_column('municipios_municipio', 'gobierno', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Municipio.enlaces'
        db.add_column('municipios_municipio', 'enlaces', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Municipio.historia'
        db.add_column('municipios_municipio', 'historia', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Municipio.ubicacion'
        db.add_column('municipios_municipio', 'ubicacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Municipio.pontencialidades'
        db.delete_column('municipios_municipio', 'pontencialidades')

        # Deleting field 'Municipio.gobierno'
        db.delete_column('municipios_municipio', 'gobierno')

        # Deleting field 'Municipio.enlaces'
        db.delete_column('municipios_municipio', 'enlaces')


    models = {
        'documentos.categoriadocumento': {
            'Meta': {'object_name': 'CategoriaDocumento'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'documentos.subcategoriadocumento': {
            'Meta': {'ordering': "['categoria']", 'object_name': 'SubCategoriaDocumento'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.CategoriaDocumento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '25', 'db_index': 'True'})
        },
        'municipios.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'caracterizacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'documentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.SubCategoriaDocumento']"}),
            'enlaces': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gobierno': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'pontencialidades': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'})
        }
    }

    complete_apps = ['municipios']
