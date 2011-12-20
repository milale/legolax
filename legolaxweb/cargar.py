#code by neosergio - http://neosergio.net
import os
import sys
import csv

#project root directory
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#CSV files
csv_trabajos = os.path.join(SITE_ROOT,'migration/trabajos.csv')

#Calling Django settings
sys.path.append(SITE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import models
from portal.models import Equipo
from portal.models import TipoDocumento
from portal.models import Interesado
from portal.models import Documento

#Reading CSV
lectorDatos = csv.reader(open(csv_trabajos), delimiter=',', quotechar='"')

#~ #Create data in DB
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
	documentos.save()

	contador += 1
	print str(contador)
