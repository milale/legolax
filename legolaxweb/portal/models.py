from django.db import models

# Create your models here.
class Equipo(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre
		
class Interesado(models.Model):
	nombre = models.CharField(max_length=200)
	dni = models.CharField(max_length=8,blank=True)
	oficina = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre

class TipoDocumento(models.Model):
	tipo = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.tipo
		
class Documento(models.Model):
	codigo = models.CharField(max_length=200)
	fentrega = models.DateField(verbose_name='Fecha de Entrega')
	contometro = models.CharField(max_length=50, blank=True)
	costo = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
	tiraje = models.CharField(max_length=200, blank=True)
	nexpediente = models.CharField(max_length=200, blank=True)
	equipo = models.ForeignKey(Equipo)
	interesado = models.ForeignKey(Interesado)
	tdocumento = models.ForeignKey(TipoDocumento, verbose_name='Tipo de documento')

	def __unicode__(self):
		return str(self.fentrega) + " " + self.codigo
