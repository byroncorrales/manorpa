from django.conf.urls.defaults import *
from django.conf import settings
from feeds import NoticiasFeed, NoticiasBinacionalFeed
from models import Noticia

urlpatterns = patterns('noticias.views',
    (r'^noticias/feed/$', NoticiasFeed()),
    (r'^noticias/binacional/feed/$', NoticiasBinacionalFeed()),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detalle'),
    (r'^noticias/categoria/(?P<cat_slug>[-\w]+)/$', 'noticia_lista_cat'),
    (r'^noticias/$', 'noticia_lista'),
    (r'^noticias/comentarios/', include('django.contrib.comments.urls')),
    (r'^editoriales/(?P<slug>[-\w]+)/$', 'editorial_detalle'),
    (r'^editoriales/$', 'editorial_lista'),
)
