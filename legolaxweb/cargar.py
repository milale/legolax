#code by neosergio - http://neosergio.net
import os
import sys
import csv

#project root directory
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#CSV files
csv_equipos = os.path.join(SITE_ROOT,'migration/equipos.csv')
csv_tdocumentos = os.path.join(SITE_ROOT,'migration/tdocumentos.csv')
csv_interesados = os.path.join(SITE_ROOT,'migration/interesados.csv')

#Calling Django settings
sys.path.append(SITE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import models
from portal.models import Equipo
from portal.models import TipoDocumento
from portal.models import Interesado

#Reading CSV
lectorDatosEquipos = csv.reader(open(csv_equipos), delimiter=',', quotechar='"')
lectorDatosTdocs = csv.reader(open(csv_tdocumentos), delimiter=',', quotechar='"')
lectorDatosInteresados = csv.reader(open(csv_interesados), delimiter=',', quotechar='"')

#Create data in DB
for elemento in lectorDatosEquipos:
	equipo = Equipo()
	equipo.nombre = elemento[0]
	try:
		equipo.save()
	except:
		pass

	
for elemento in lectorDatosTdocs:
	tdocs = TipoDocumento()
	tdocs.tipo = elemento[0]
	try:
		tdocs.save()
	except:
		pass
		
for elemento in lectorDatosInteresados:
	interesados = Interesado()
	if elemento:
		interesados.nombre = elemento[0]
	else:
		interesados.nombre = "Lic. Miriam Montero"
	try:
		interesados.save()
	except:
		pass
