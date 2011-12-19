#code by neosergio - http://neosergio.net
import os
import sys
import csv

#project root directory
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#CSV files
csv_equipos = os.path.join(SITE_ROOT,'migration/equipos.csv')

#Calling Django settings
sys.path.append(SITE_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import models
from portal.models import Equipo

#Reading CSV
lectorDatos = csv.reader(open(csv_equipos), delimiter=',', quotechar='"')

#Create data in DB
for elemento in lectorDatos:
	equipo = Equipo()
	equipo.nombre = elemento[0]
	equipo.save()
