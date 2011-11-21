from django.contrib import admin
from portal.models import Equipo
from portal.models import Interesado
from portal.models import TipoDocumento
from portal.models import Documento
from portal.models import Articulo
from portal.models import RegistroArticulo

admin.site.register(Equipo)
admin.site.register(Interesado)
admin.site.register(TipoDocumento)
admin.site.register(Documento)
admin.site.register(Articulo)
admin.site.register(RegistroArticulo)
