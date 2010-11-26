# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Proyecto.objetivos'
        db.delete_column('proyectos_proyecto', 'objetivos')

        # Deleting field 'Proyecto.resultados'
        db.delete_column('proyectos_proyecto', 'resultados')

        # Adding field 'Proyecto.descripcion'
        db.add_column('proyectos_proyecto', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Proyecto.objetivos'
        db.add_column('proyectos_proyecto', 'objetivos', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Proyecto.resultados'
        db.add_column('proyectos_proyecto', 'resultados', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Proyecto.descripcion'
        db.delete_column('proyectos_proyecto', 'descripcion')


    models = {
        'proyectos.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150', 'db_index': 'True'})
        },
        'proyectos.financiador': {
            'Meta': {'object_name': 'Financiador'},
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('manorpa.proyectos.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150', 'db_index': 'True'})
        },
        'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'area': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['proyectos.Area']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_final': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['proyectos.Financiador']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['proyectos']
