    # -*- coding: UTF-8 -*-
from manorpa.multimedia.models import Adjunto
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from south.modelsinspector import add_introspection_rules
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from thumbs import ImageWithThumbsField
from manorpa.utils import get_image_path
add_introspection_rules([], ["^manorpa\.tagging_autocomplete\.models\.TagAutocompleteField"]) 

class CategoriaNoticia(models.Model):
    '''Modelo que representa la categorias de las noticias'''
    nombre = models.CharField('Título', max_length=40, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, help_text='unico Valor', editable=False)
    
    def __unicode__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(CategoriaNoticia, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Categoria de Noticia"
        verbose_name_plural = "Categorias de Noticias"

class Autor(models.Model):
    '''Modelo que representa los autores de noticas y editoriales'''
    nombre = models.CharField('Nombre', max_length=40, unique=True, blank=False, null=False)
    cargo = models.CharField('Cargo', max_length=40, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=40, unique=True, help_text='unico Valor', editable=False)
    imagen = ImageWithThumbsField(verbose_name='Foto del autor', upload_to=get_image_path, sizes=((75, 95), (200, 250)),  blank=True, null=True)
    imgDir = 'attachments/imagenes'
    
    def __unicode__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(Autor, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Noticia(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length=120, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=120, unique=True, help_text='unico Valor', editable=False)
    fecha = models.DateField()
    autor = models.ForeignKey(Autor)
    categoria = models.ForeignKey(CategoriaNoticia)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((160, 90), (255, 190)))
    contenido = models.TextField('Contenido', blank=True, null=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')
    adjunto = generic.GenericRelation(Adjunto)

    imgDir = 'attachments/imagenes'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Noticia.objects.get(pk=self.id)            
        except:
            n = Noticia.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Noticia, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    #metodo para devolver la url exacta del objeto
    def get_full_url(self):
        return "/noticias/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo

class Editorial(models.Model):
    '''Modelo que representa el tipo de contenido Editorial'''
    titulo = models.CharField('Título', max_length=120, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=120, unique=True, help_text='unico Valor', editable=False)
    fecha = models.DateField()
    autor = models.ForeignKey(Autor)
    contenido = models.TextField('Contenido', blank=True, null=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')

    imgDir = 'attachments/imagenes'

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
    
    def save(self, force_insert=False, force_update=False):
        try:
            Editorial.objects.get(pk=self.id)            
        except:
            n = Editorial.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Editorial, self).save(force_insert, force_update)

    #Para jalar las tags
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    #metodo para devolver la url exacta del objeto
    def get_full_url(self):
        return "/editoriales/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo

