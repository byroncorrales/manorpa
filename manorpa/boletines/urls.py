from django.conf.urls.defaults import *
from django.conf import settings
from models import Boletin

urlpatterns = patterns('boletines.views',
    (r'^publicaciones/$', 'boletin_lista'),
    (r'^publicaciones/(?P<slug>[-\w]+)/$', 'boletin_detalle'),
)
