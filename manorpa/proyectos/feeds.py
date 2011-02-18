from django.contrib.syndication.views import Feed
from models import Proyecto
from manorpa.tagging.models import Tag, TaggedItem
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


class ProyectoFeed(Feed):
    title = "Proyectos de MANORPA"
    link = "/proyectos/feed/"
    description = 'Proyectos de MANORPA'
    
    def items(self):
        return Proyecto.objects.all()[:10]

    def item_title(self, item):
        return item.nombre

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return item.get_full_url()
        
class ProyectoBinacionalFeed(Feed):
    title = "Proyectos de Manorpa"
    link = "/proyectos/binacional0feed/"
    description = 'Proyectos de MANORPA'
    
    def items(self):
        tag = get_object_or_404(Tag, name="Binacional")
        #return Proyecto.objects.all()[:10]
        return TaggedItem.objects.get_by_model(Proyecto, tag)

    def item_title(self, item):
        return item.nombre

    def item_description(self, item):
        return item.descripcion

    def item_link(self, item):
        return item.get_full_url()
