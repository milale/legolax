from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm

class Equipo(models.Model):
	nombre = models.CharField(max_length=200,verbose_name='Nombre del equipo',unique=True)
	
	def __unicode__(self):
		return self.nombre

class EquipoForm(ModelForm):
	class Meta:
		model = Equipo
		
class Interesado(models.Model):
	nombre = models.CharField(max_length=200,unique=True)
	dni = models.CharField(max_length=8,blank=True)
	oficina = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre

class InteresadoForm(ModelForm):
	class Meta:
		model=Interesado

class TipoDocumento(models.Model):
	tipo = models.CharField(max_length=200,unique=True)
	
	def __unicode__(self):
		return self.tipo
		
class TipoDocumentoForm(ModelForm):
	class Meta:
		model=TipoDocumento

class Documento(models.Model):
	tdocumento = models.ForeignKey(TipoDocumento, verbose_name='Tipo de documento')
	codigo = models.CharField(max_length=200)
	interesado = models.ForeignKey(Interesado)
	equipo = models.ForeignKey(Equipo)
	asunto = models.CharField(max_length=200, blank=True)
	tiraje = models.CharField(max_length=200, blank=True)
	fentrega = models.DateField(verbose_name='Fecha de Entrega')
	contometro = models.CharField(max_length=50, blank=True)
	costo = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
	nexpediente = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return str(self.fentrega) + " " + self.codigo

class DocumentoForm(ModelForm):
	class Meta:
		model = Documento

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
	precio = models.DecimalField(max_digits=6,decimal_places=2,blank=True)
	preciototal = models.DecimalField(max_digits=6,decimal_places=2,blank=True)
	articulo = models.ForeignKey(Articulo)
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.articulo.nombre + " " + str(self.fregistro) + " "  + self.tipo + " " + str(self.cantidad) 

class RegistroArticuloForm(ModelForm):
	class Meta:
		model = RegistroArticulo
		exclude = ('usuario',)

class LoginForm(forms.Form):
	userform = forms.CharField(label='usuario')
	passform = forms.CharField(label='clave',widget=forms.PasswordInput(render_value=False))
