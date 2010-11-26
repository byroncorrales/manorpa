 # -*- coding: UTF-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from manorpa.documentos.models import SubCategoriaDocumento


class Municipio(models.Model):
    '''Modelo que representa el tipo de contenido para los municipios'''
    nombre = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    documentacion = models.ForeignKey(SubCategoriaDocumento,verbose_name='categoria en documentación')
    caracterizacion = models.TextField('Caracterizacion General',blank = True, null = True)
    pontencialidades = models.TextField('Potencialidades',blank = True, null = True)
    gobierno = models.TextField('Gobierno local',blank = True, null = True)
    enlaces = models.TextField('Enlaces locales',blank = True, null = True)
#    adjunto = generic.GenericRelation(Adjunto)

    def __unicode__(self):
        return self.nombre

    def get_full_url(self):
        return '/municipios/%s/' % self.slug

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Municipio, self).save(force_insert, force_update)
