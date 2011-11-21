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

class Articulo(models.Model):
	nombre = models.CharField(max_length=250)
	marca = models.CharField(max_length=50,blank=True)
	serie = models.CharField(max_length=50,blank=True)
	codigo = models.CharField(max_length=50,blank=True)
	caracteristica = models.TextField(blank=True)
	umedida = models.CharField(max_length=50,verbose_name="Unidad de medida",blank=True)
	
	def __unicode__(self):
		return self.nombre
		
class RegistroArticulo(models.Model):
	detalle = models.TextField(blank=True)
	cantidad = models.DecimalField(max_digits=6,decimal_places=2)
	fregistro = models.DateField(verbose_name='Fecha de registro')
	tipo_options = (('e','entrada'),('s','salida'))
	tipo = models.CharField(max_length=1,choices=tipo_options)
	precio = models.DecimalField(max_digits=6,decimal_places=2)
	articulo = models.ForeignKey(Articulo)
	
	def __unicode__(self):
		return self.articulo.nombre + " " + str(self.fregistro) + " "  + self.tipo + " " + str(self.cantidad) 
