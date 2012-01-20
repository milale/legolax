#encoding:utf-8
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm, TextInput
import datetime

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
	oficina = models.CharField(max_length=200,blank=True)
	
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
	codigo = models.CharField(max_length=200,blank=True,verbose_name='Código')
	interesado = models.ForeignKey(Interesado)
	equipo = models.ForeignKey(Equipo)
	asunto = models.TextField(blank=True)
	tiraje = models.TextField(blank=True)
	fentrega = models.DateField(verbose_name='Fecha de Entrega',default=datetime.date.today)
	contometro = models.CharField(max_length=50, blank=True,verbose_name='Contómetro')
	costo = models.DecimalField(max_digits=7,decimal_places=2,default=0)
	nexpediente = models.CharField(max_length=200, blank=True, verbose_name='Número de expediente')
	
	def __unicode__(self):
		return str(self.fentrega) + " " + self.codigo

class InteresadoField(forms.CharField):
	def clean(self, value):
		if not value:
			raise forms.ValidationError('Este campo es obligatorio')
		try:
			interesadoid = Interesado.objects.get(nombre__exact=value)
			return interesadoid
		except:
			raise forms.ValidationError('No existe el interesado')

class DocumentoForm(ModelForm):
	interesado = InteresadoField()
	class Meta:
		model = Documento

class Articulo(models.Model):
	nombre = models.CharField(max_length=250,unique=True) 
	marca = models.CharField(max_length=50,blank=True)
	codigo = models.CharField(max_length=50,blank=True,verbose_name='Código')
	caracteristica = models.TextField(blank=True,verbose_name='Característica')
	umedida = models.CharField(max_length=50,verbose_name="Unidad de medida",blank=True)
	sactual = models.DecimalField(max_digits=8,decimal_places=3,verbose_name="Saldo actual",default=0)
	precioref = models.DecimalField(max_digits=8,decimal_places=3,default=0, verbose_name='Precio referencial')
	preciototalref = models.DecimalField(max_digits=10,decimal_places=3,default=0, verbose_name='Precio total referencial')
	
	def __unicode__(self):
		return self.nombre

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
		exclude = ('preciototalref',)

class RegistroArticulo(models.Model):
	articulo = models.ForeignKey(Articulo,verbose_name='Artículo')
	detalle = models.TextField(blank=True)
	cantidad = models.DecimalField(max_digits=8,decimal_places=3)
	fregistro = models.DateField(verbose_name='Fecha de registro',default=datetime.date.today)
	tipo_options = (('e','entrada'),('s','salida'))
	tipo = models.CharField(max_length=1,choices=tipo_options)
	preciouni = models.DecimalField(max_digits=8,decimal_places=3,default=0, verbose_name='Precio Unitario')
	preciototal = models.DecimalField(max_digits=8,decimal_places=3,default=0, verbose_name='Precio Total')
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.articulo.nombre + " " + str(self.fregistro) + " "  + self.tipo + " " + str(self.cantidad) 

class ArticuloField(forms.CharField):
	def clean(self, value):
		if not value:
			raise forms.ValidationError('Este campo es obligatorio')
		try:
			articuloid = Articulo.objects.get(nombre__exact=value)
			return articuloid
		except:
			raise forms.ValidationError('No existe el artículo')

class RegistroArticuloForm(ModelForm):
	articulo = ArticuloField(label='Artículo')
	class Meta:
		model = RegistroArticulo
		exclude = ('usuario',)

class LoginForm(forms.Form):
	userform = forms.CharField(label='usuario')
	passform = forms.CharField(label='clave',widget=forms.PasswordInput(render_value=False))

#Para el formulario de reporte anual de produccion, raprod = reporte anual de produccion
class raprod(forms.Form):
	anio = forms.IntegerField(label='Año:',max_value=2013,min_value=2010)

#Para el formulario de reporte mensual de produccion, rpprod = reporte por periodo de produccion
class rpprod(forms.Form):
	finicial = forms.DateField(label='Fecha inicial',initial=datetime.date.today)
	ffinal = forms.DateField(label='Fecha final',initial=datetime.date.today)
	
#Para el formulario de reporte mensual de produccion por equipo, rpeprod = reporte por periodod y por equipo de produccion	
class rpeprod(forms.Form):
	finicial = forms.DateField(label='Fecha inicial',initial=datetime.date.today)
	ffinal = forms.DateField(label='Fecha final',initial=datetime.date.today)
	equipo = forms.ModelChoiceField(queryset=Equipo.objects.all())
