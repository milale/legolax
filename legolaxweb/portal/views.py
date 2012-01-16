#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from portal.models import Documento, DocumentoForm
from portal.models import LoginForm
from portal.models import RegistroArticulo, RegistroArticuloForm
from portal.models import Equipo, EquipoForm
from portal.models import Interesado, InteresadoForm
from portal.models import TipoDocumento, TipoDocumentoForm
from portal.models import Articulo, ArticuloForm
from portal.models import raprod, rpprod, rpeprod
from django.template import RequestContext
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Sum
import datetime

@login_required(login_url='/ingreso/')
def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def ingreso(request):
	if request.method == 'POST':
		formu = LoginForm(request.POST)
		loginuser = request.POST['userform']
		loginpass = request.POST['passform']
		loginaccess = authenticate(username=loginuser,password=loginpass)
		if loginaccess is not None:
			if loginaccess.is_active:
				login(request,loginaccess)
				return HttpResponseRedirect('/')
			else:
				return render_to_response('noactivo.html')
		else:
			return render_to_response('nousuario.html')
	else:
		formu = LoginForm(auto_id=True)
	return render_to_response('ingreso.html',{'formu':formu},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def salida(request):
	logout(request)
	return render_to_response('salir.html')

#view of persons, documents and equipment
@login_required(login_url='/ingreso/')
def equipos(request):
	datos = Equipo.objects.all().order_by('nombre')
	return render_to_response('equipos.html',{'datos':datos},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def equiposregistrar(request):
	if request.method == 'POST':
		formulario = EquipoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/equipos/')
	else:
		formulario = EquipoForm(auto_id=True)
	return render_to_response('equiposeditar.html',{'formulario':formulario},context_instance=RequestContext(request))
		
@login_required(login_url='/ingreso/')
def equiposeditar(request, equipo_id):
	dato = get_object_or_404(Equipo, pk=equipo_id)
	if request.method == 'POST':
		formulario = EquipoForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/equipos/')
	else:
		formulario = EquipoForm(instance=dato)
	return render_to_response('equiposeditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def interesados(request):
	datos = Interesado.objects.all().order_by('nombre')
	return render_to_response('interesados.html',{'datos':datos},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def interesadosregistrar(request):
	if request.method == 'POST':
		formulario = InteresadoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/interesados/')
	else:
		formulario = InteresadoForm(auto_id=True)
	return render_to_response('interesadoseditar.html',{'formulario':formulario},context_instance=RequestContext(request))
	
@login_required(login_url='/ingreso/')
def interesadoseditar(request, interesado_id):
	dato = get_object_or_404(Interesado, pk=interesado_id)
	if request.method == 'POST':
		formulario = InteresadoForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/interesados/')
	else:
		formulario = InteresadoForm(instance=dato)
	return render_to_response('interesadoseditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def tdocumentos(request):
	datos = TipoDocumento.objects.all()
	return render_to_response('tdocumento.html',{'datos':datos},context_instance=RequestContext(request))	

@login_required(login_url='/ingreso/')
def tdocumentosregistrar(request):
	if request.method == 'POST':
		formulario = TipoDocumentoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/tipo-documentos/')
	else:
		formulario = TipoDocumentoForm(auto_id=True)
	return render_to_response('tdocumentoeditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def tdocumentoseditar(request, tdocumento_id):
	dato = get_object_or_404(TipoDocumento, pk=tdocumento_id)
	if request.method == 'POST':
		formulario = TipoDocumentoForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/tipo-documentos/')
	else:
		formulario = TipoDocumentoForm(instance=dato)
	return render_to_response('tdocumentoeditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def documentos(request):
	datos = Documento.objects.all().order_by('-fentrega')
	return render_to_response('documentos.html',{'datos':datos},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def documentosregistrar(request):
	interesados = Interesado.objects.all()
	if request.method == 'POST':
		formulario = DocumentoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/produccion/trabajos/')
	else:
		formulario = DocumentoForm(auto_id=True)
	return render_to_response('docnuevo.html',{'formulario':formulario,'interesados':interesados},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def documentosdetalle(request, documento_id):
	dato = get_object_or_404(Documento, pk=documento_id)
	return render_to_response('detalledocumento.html',{'dato':dato},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def documentoseditar(request, documento_id):
	interesados = Interesado.objects.all()
	dato = get_object_or_404(Documento, pk=documento_id)
	if request.method == 'POST':
		formulario = DocumentoForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			redireccion = '/produccion/trabajos/detalle/'+str(documento_id)
			return HttpResponseRedirect(redireccion)
	else:
		formulario = DocumentoForm(initial={'interesado':dato.interesado.nombre},instance=dato)
	return render_to_response('doceditar.html',{'formulario':formulario,'interesados':interesados},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def articulos(request):
	datos = Articulo.objects.all().order_by('nombre')
	total = datos.count()
	suma = Articulo.objects.all().aggregate(Sum('preciototalref'))['preciototalref__sum']
	fecha = datetime.date.today
	return render_to_response('articulos.html',{'datos':datos,'total':total,'fecha':fecha,'suma':suma},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def articulosdetalle(request, articulo_id):
	dato = get_object_or_404(Articulo, pk=articulo_id)
	return render_to_response('articulosdetalle.html',{'dato':dato},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def articuloseditar(request, articulo_id):
	dato = get_object_or_404(Articulo, pk=articulo_id)
	if request.method == 'POST':
		formulario = ArticuloForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			modificar = Articulo.objects.get(pk=articulo_id)
			modificar.preciototalref = modificar.sactual * modificar.precioref
			modificar.save()
			redireccion = '/almacen/articulos/detalle/'+str(articulo_id)
			return HttpResponseRedirect(redireccion)
	else:
		formulario = ArticuloForm(instance=dato)
	return render_to_response('articuloseditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def articulosregistrar(request):
	if request.method == 'POST':
		formulario = ArticuloForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			ultimo = Articulo.objects.latest('id')
			ultimo.preciototalref = ultimo.sactual * ultimo.precioref
			ultimo.save()
			return HttpResponseRedirect('/almacen/articulos/')
	else:
		formulario = ArticuloForm(auto_id=True)
	return render_to_response('articuloseditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def registros(request):
	datos = RegistroArticulo.objects.filter(tipo='s').order_by("-pk").order_by('-fregistro')
	total = datos.count()
	return render_to_response('registroarticulo.html',{'datos':datos,'total':total},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def registrosentradas(request):
	datos = RegistroArticulo.objects.filter(tipo='e').order_by("-pk").order_by('-fregistro')
	total = datos.count()
	return render_to_response('registroarticuloentradas.html',{'datos':datos,'total':total},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def registrosnuevo(request):
	articulos = Articulo.objects.all()
	if request.method == 'POST':
		formulario = RegistroArticuloForm(request.POST)
		if formulario.is_valid():
			detalle = formulario.cleaned_data['detalle']
			cantidad = formulario.cleaned_data['cantidad']
			fregistro = formulario.cleaned_data['fregistro']
			tipo = formulario.cleaned_data['tipo']
			preciouni = formulario.cleaned_data['preciouni']
			preciototal = formulario.cleaned_data['preciototal']
			articulo = Articulo.objects.get(nombre=formulario.cleaned_data['articulo'])
			usuario = request.user
			
			#validacion para la cantidad solo positiva
			if cantidad < 0:
				return HttpResponseRedirect('/negativo/')
			
			#actualizacion del saldo de producto
			if tipo == 'e':
				saldo = articulo.sactual + cantidad
				articulo.precioref = preciouni
			elif tipo == 's':
				saldo = articulo.sactual - cantidad
			articulo.sactual = saldo
			articulo.preciototalref = articulo.sactual * articulo.precioref
			articulo.save()
			
			#guardar el registro de entrada o salida
			guardarregistro = RegistroArticulo(detalle=detalle,cantidad=cantidad,
												fregistro=fregistro,tipo=tipo,
												preciouni=preciouni,preciototal=preciototal,
												articulo=articulo,usuario=usuario)
			guardarregistro.save()
			return HttpResponseRedirect('/almacen/articulos/')
	else:
		formulario = RegistroArticuloForm(auto_id=True)
	return render_to_response('registroarticuloform.html',{'formulario':formulario,'articulos':articulos},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def raprodform(request):
	if request.method == 'POST':
		formulario = raprod(request.POST)
		if formulario.is_valid():
			anio = formulario.cleaned_data['anio']
			datos = Documento.objects.filter(fentrega__year=anio).order_by('fentrega')
			total = datos.count()
			if total == 0:
				raise Http404
			
			#calculo del costo por año
			suma = 0
			for i in datos:
				suma += i.costo
			
			return render_to_response('raprod.html',{'datos':datos,'anio':anio,'suma':suma,'total':total},context_instance=RequestContext(request))
	else:
		formulario = raprod(auto_id=True)
	return render_to_response('raprod.html',{'formulario':formulario},context_instance=RequestContext(request))
		
@login_required(login_url='/ingreso/')
def rpprodform(request):
	if request.method == 'POST':
		formulario = rpprod(request.POST)
		if formulario.is_valid():
			finicial = formulario.cleaned_data['finicial']
			ffinal = formulario.cleaned_data['ffinal']
			fecha = {'inicial':finicial,'final':ffinal}
			datos = Documento.objects.filter(fentrega__range=(finicial,ffinal)).order_by('fentrega')
			total = datos.count()
			if total == 0:
				raise Http404
			
			#calculo de costo por periodo
			suma = 0
			for i in datos:
				suma += i.costo
			
			return render_to_response('rpprod.html',{'datos':datos,'fecha':fecha,'suma':suma,'total':total},context_instance=RequestContext(request))
	else:
		formulario = rpprod(auto_id=True)
	return render_to_response('rpprod.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def rpeprodform(request):
	if request.method == 'POST':
		formulario = rpeprod(request.POST)
		if formulario.is_valid():
			finicial = formulario.cleaned_data['finicial']
			ffinal = formulario.cleaned_data['ffinal']
			equipoform = formulario.cleaned_data['equipo']
			referencia = {'inicial':finicial,'final':ffinal,'equipo':equipoform}
			datos = Documento.objects.filter(fentrega__range=(finicial,ffinal),equipo=equipoform).order_by('fentrega')
			total = datos.count()
			if total == 0:
				raise Http404
				
			#calculo de costo por periodo y por equipo
			suma = 0
			for i in datos:
				suma += i.costo
			
			return render_to_response('rpeprod.html',{'datos':datos,'referencia':referencia,'suma':suma,'total':total},context_instance=RequestContext(request))
	else:
		formulario = rpeprod(auto_id=True)
	return render_to_response('rpeprod.html',{'formulario':formulario},context_instance=RequestContext(request))
