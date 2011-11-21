from django.db import models

# Create your models here.
class Entrada(models.Model):
	codigo = models.CharField(max_length=200,blank=True)
	detalle_entrada = models.CharField(max_length=200,blank=True)	
	cantidad_entrada = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.cantidad_entrada
		
class Salida(models.Model):
	codigo = models.CharField(max_length=200,blank=True)
	detalle_salida = models.CharField(max_length=200,blank=True)	
	cantidad_salida = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.cantidad_salida
		
class Articulo(models.Model):
	nombre = models.CharField(max_length=200)
	marca = models.CharField(max_length=200,blank=True)
	serie = models.CharField(max_length=50, blank=True)
	codigo = models.CharField(max_length=200,blank=True)
	caracteristicas = models.CharField(max_length=200, blank=True)
	unidad_medida = models.CharField(max_length=200, blank=True)
	saldo = 
	fecha_registro = models.DateField(verbose_name='Fecha de Registro')
	entrada = models.ForeignKey(Entrada)
	salida = models.ForeignKey(Salida)
	
	def __unicode__(self):
		return str(self.) + " " + self.
