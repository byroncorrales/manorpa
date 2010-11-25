# -*- coding: UTF-8 -*-
from django.db import models
from manorpa.multimedia.models import Adjunto #importando el modelo de adjuntos genericos
from django.template.defaultfilters import slugify
from thumbs import ImageWithThumbsField

class Pagina(models.Model):
    '''Modelo Gpara representar a paginas estaticas'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    fecha = models.DateField()
    contenido = models.TextField('Contenido',blank = True, null = True)

    def __unicode__(self):
        return self.titulo

    def get_full_url(self):
        return "/paginas/%s/" % self.slug

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
    
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.titulo)
        super(Pagina, self).save(force_insert, force_update)
        
        
class MenuPrimario(models.Model):
    '''Modelo Gpara representar los menu primario'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    imagen = ImageWithThumbsField(upload_to='attachments/banners', sizes=((420,160),))
    orden = models.IntegerField('Orden', help_text = '0 para el primero 1 para el segundo ... etc')

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Menu Primario"
        verbose_name_plural = "Menus Primarios"

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.titulo)
        super(MenuPrimario, self).save(force_insert, force_update)


class MenuSecundario(models.Model):
    '''Modelo Gpara representar a paginas estaticas'''
    titulo = models.CharField('Título', max_length = 120, unique = True,blank = False, null = False)
    slug = models.SlugField(max_length = 120, unique = True,help_text = 'unico Valor',editable=False)
    menuprimario = models.ForeignKey(MenuPrimario)
    pagina = models.ForeignKey(Pagina,blank = True, null = True)
    url = models.CharField('URL',max_length = 150,blank = True, null = True)
    orden = models.IntegerField('Orden', help_text = '0 para el primero 1 para el segundo ... etc')

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Menu Secundario"
        verbose_name_plural = "Menus Secundarios"
        
    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.titulo)
        super(MenuSecundario, self).save(force_insert, force_update)

