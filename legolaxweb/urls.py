from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'portal.views.index'),
    
    #produccion 
    url(r'^produccion/$','portal.views.documentos'),
    url(r'^produccion/equipos/$','portal.views.equipos'),
    url(r'^produccion/equipos/nuevo/$','portal.views.equiposregistrar'),
    url(r'^produccion/equipos/editar/(?P<equipo_id>\d+)/$','portal.views.equiposeditar'),
    url(r'^produccion/interesados/$','portal.views.interesados'),
    url(r'^produccion/interesados/nuevo/$','portal.views.interesadosregistrar'),
    url(r'^produccion/interesados/editar/(?P<interesado_id>\d+)/$','portal.views.interesadoseditar'),
    url(r'^produccion/tipo-documentos/$','portal.views.tdocumentos'),
    url(r'^produccion/tipo-documentos/nuevo/$','portal.views.tdocumentosregistrar'),
    url(r'^produccion/tipo-documentos/editar/(?P<tdocumento_id>\d+)/$','portal.views.tdocumentoseditar'),
    url(r'^produccion/trabajos/$','portal.views.documentos'),
    url(r'^produccion/trabajos/detalle/(?P<documento_id>\d+)/$','portal.views.documentosdetalle'),
    url(r'^produccion/trabajos/editar/(?P<documento_id>\d+)/$','portal.views.documentoseditar'),
    url(r'^produccion/trabajos/nuevo/$','portal.views.documentosregistrar'),
    url(r'^produccion/reportes/anuales/$','portal.views.raprodform'),
    url(r'^produccion/reportes/periodo/$','portal.views.rpprodform'),
    url(r'^produccion/reportes/periodo/equipo/$','portal.views.rpeprodform'),
    
    #almacen
    url(r'^almacen/articulos/$','portal.views.articulos'),
    url(r'^almacen/articulos/detalle/(?P<articulo_id>\d+)/$','portal.views.articulosdetalle'),
    url(r'^almacen/articulos/editar/(?P<articulo_id>\d+)/$','portal.views.articuloseditar'),
    url(r'^almacen/articulos/nuevo/$','portal.views.articulosregistrar'),
    url(r'^almacen/articulos/registro/$','portal.views.registros'),
    url(r'^almacen/articulos/registro/entradas/$','portal.views.registrosentradas'),
    url(r'^almacen/articulos/registro/nuevo/$','portal.views.registrosnuevo'),
    
    #administrativo
    url(r'^ingreso/$','portal.views.ingreso'),
    url(r'^salida/$','portal.views.salida'),
    url(r'^admin/', include(admin.site.urls)),
)
