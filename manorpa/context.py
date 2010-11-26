from paginas.models import *
from municipios.models import Municipio

def elementos_fijos(request):
    #TODO: cache
    menu_primario = MenuPrimario.objects.all().order_by('orden')
    menu_secundario = MenuSecundario.objects.all().order_by('orden')
    municipio = Municipio.objects.all().order_by('nombre')
    dicc = {
            'menu_secundario': menu_secundario,
            'menu_primario':menu_primario,
            'municipio':municipio,
           }
    return dicc
