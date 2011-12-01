from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portal.views.index'),
    url(r'^produccion/$','portal.views.documentos'),
    url(r'^produccion/equipos/$','portal.views.equipos'),
    url(r'^produccion/equipos/editar/(?P<equipo_id>\d+)/$','portal.views.equiposeditar'),
    url(r'^produccion/interesados/$','portal.views.interesados'),
    url(r'^produccion/interesados/editar/(?P<interesado_id>\d+)/$','portal.views.interesadoseditar'),
    url(r'^ingreso/$','portal.views.ingreso'),
    url(r'^articulos/registro/$','portal.views.registroarticuloformu'),
    url(r'^admin/', include(admin.site.urls)),
)
