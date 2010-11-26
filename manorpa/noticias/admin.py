from django.contrib import admin
from noticias.models import *
from django.contrib.contenttypes import generic
from manorpa.multimedia.models import Adjunto #importando el modelo de adjuntos genericos

class CategoriaNoticiaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 12

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']


class AdjuntoInline(generic.GenericStackedInline):
    model = Adjunto
    extra = 1
    max_num = 3

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','categoria']
    list_filter = ['categoria']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]

class EditorialAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','autor']
    list_filter = ['autor']
    search_fields = ['titulo']
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12
    
    class Media:
        js = ['../archivos/js/tiny_mce/tiny_mce.js',
              '../archivos/js/editores/textareas.js',]


admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
#admin.site.register(Comentario, ComentarioAdmin)
