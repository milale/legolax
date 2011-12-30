#encoding:utf-8
#code by neosergio - http://neosergio.net
import os
import sys
import csv
from decimal import *

#project root directory
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#CSV files
csv_trabajos = os.path.join(SITE_ROOT,'migration/trabajos.csv')
csv_almacen = os.path.join(SITE_ROOT,'migration/almacen.csv')

#Calling Django settings
sys.path.append(SITE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import models
from portal.models import Equipo
from portal.models import TipoDocumento
from portal.models import Interesado
from portal.models import Documento
from portal.models import Articulo
from portal.models import RegistroArticulo
from django.contrib.auth.models import User

print "Migrando datos de articulos para almacén"
lector_almacen = csv.reader(open(csv_almacen), delimiter=',', quotechar='"')
contador_almacen = 0
for elemento in lector_almacen:
	if elemento[0] != "artículo":
		articulo = Articulo()
		articulo.nombre = elemento[0]
		articulo.marca = elemento[1]
		articulo.codigo = elemento[2]
		articulo.caracteristica = elemento[3]
		articulo.umedida = elemento[4]
		articulo.sactual = 0
		try:
			articulo.save()
			contador_almacen += 1
			print contador_almacen
		except:
			pass
print "Fin de la migración de datos de articulos para almacén"

#Descomentar estas líneas solamente si se esta seguro de migrar los datos de almacen de entrada y salida
#si no se tiene cuidado se registraran duplicados
#~ print "Migrando datos de registros de entradas y salidas en almacén"
#~ lector_almacen = csv.reader(open(csv_almacen), delimiter=',', quotechar='"')
#~ contador = 0
#~ for elemento in lector_almacen:
	#~ if elemento[0] != "artículo":
		#~ registro = RegistroArticulo()
		#~ articulorelacionado = Articulo.objects.get(nombre__exact=elemento[0]) 
		#~ registro.articulo = articulorelacionado
		#~ registro.detalle = elemento[7]
		#~ registro.cantidad = Decimal(str(float(elemento[8])))
		#~ registro.fregistro = elemento[5]
		#~ 
		#~ if elemento[6] == 'entrada':
			#~ registro.tipo = 'e'
			#~ articulorelacionado.sactual += registro.cantidad
		#~ elif elemento[6] == 'salida':
			#~ registro.tipo = 's'
			#~ articulorelacionado.sactual -= registro.cantidad
		#~ articulorelacionado.save()
		#~ 
		#~ if elemento[10] == '': elemento[10] = 0
		#~ registro.preciouni = Decimal(str(float(elemento[10])))
		#~ if elemento[11] == '': elemento[11] = 0
		#~ registro.preciototal = Decimal(str(float(elemento[11])))
		#~ registro.usuario = User.objects.get(pk=2)
		#~ registro.save()
		#~ contador +=1 
		#~ print contador
#~ print "Fin de migración de datos de entrada y salida"

print "Migrando datos de trabajos de producción"
lectorDatos = csv.reader(open(csv_trabajos), delimiter=',', quotechar='"')
contador = 0
for elemento in lectorDatos:
	equipo = Equipo()
	equipo.nombre = elemento[0]
	try:
		equipo.save()
	except:
		pass
	
	tdocs = TipoDocumento()
	tdocs.tipo = elemento[3]
	try:
		tdocs.save()
	except:
		pass
		
	interesados = Interesado()
	interesados.nombre = elemento[5]
	try:
		interesados.save()
	except:
		pass
	
	documentos = Documento()
	documentos.tdocumento = TipoDocumento.objects.get(tipo__exact=elemento[3])
	documentos.codigo = elemento[4]
	documentos.interesado = Interesado.objects.get(nombre__exact=elemento[5])
	documentos.equipo = Equipo.objects.get(nombre__exact=elemento[0])
	documentos.asunto = elemento[6]
	documentos.tiraje = elemento[7]
	documentos.fentrega = elemento[2]
	documentos.contometro = elemento[8]
	documentos.costo = elemento[9]
	documentos.nexpediente = elemento[1]
	try:
		documentos.save()
	except:
		pass

	contador += 1
	print str(contador)
print "Fin de migración de datos de entrada y salida"
