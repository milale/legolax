from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portal.views.index'),
    url(r'^produccion/$','portal.views.documentos'),
    url(r'^produccion/equipos-interesados-documentos/$','portal.views.eqindoc'),
    url(r'^ingreso/$','portal.views.ingreso'),
    url(r'^articulos/registro/$','portal.views.registroarticuloformu'),
    url(r'^admin/', include(admin.site.urls)),
)
