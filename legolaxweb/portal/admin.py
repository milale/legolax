from django.contrib import admin
from portal.models import Equipo
from portal.models import Interesado
from portal.models import TipoDocumento
from portal.models import Documento

admin.site.register(Equipo)
admin.site.register(Interesado)
admin.site.register(TipoDocumento)
admin.site.register(Documento)
