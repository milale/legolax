from django.shortcuts import render_to_response, get_object_or_404
from portal.models import Documento, DocumentoForm
from portal.models import LoginForm
from portal.models import RegistroArticulo, RegistroArticuloForm
from portal.models import Equipo, EquipoForm
from portal.models import Interesado, InteresadoForm
from portal.models import TipoDocumento, TipoDocumentoForm
from portal.models import Articulo, ArticuloForm
from django.template import RequestContext
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

@login_required(login_url='/ingreso/')
def index(request):
    return render_to_response('index.html')

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

#view of persons, documents and equipment
@login_required(login_url='/ingreso/')
def equipos(request):
	datos = Equipo.objects.all()
	return render_to_response('equipos.html',{'datos':datos})

@login_required(login_url='/ingreso/')
def equiposregistrar(request):
	if request.method == 'POST':
		formulario = EquipoForm(request.POST)
		if formulario.is_valid():
			nombre = formulario.cleaned_data['nombre']
			equiponuevo = Equipo(nombre=nombre)
			equiponuevo.save()
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
	datos = Interesado.objects.all()
	return render_to_response('interesados.html',{'datos':datos})

@login_required(login_url='/ingreso/')
def interesadosregistrar(request):
	if request.method == 'POST':
		formulario = InteresadoForm(request.POST)
		if formulario.is_valid():
			nombre = formulario.cleaned_data['nombre']
			dni = formulario.cleaned_data['dni']
			oficina = formulario.cleaned_data['oficina']
			interesadonuevo = Interesado(nombre=nombre,dni=dni,oficina=oficina)
			interesadonuevo.save()
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
	return render_to_response('tdocumento.html',{'datos':datos})	

@login_required(login_url='/ingreso/')
def tdocumentosregistrar(request):
	if request.method == 'POST':
		formulario = TipoDocumentoForm(request.POST)
		if formulario.is_valid():
			tipo = formulario.cleaned_data['tipo']
			tdocumentonuevo = TipoDocumento(tipo=tipo)
			tdocumentonuevo.save()
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
	return render_to_response('documentos.html',{'datos':datos})

@login_required(login_url='/ingreso/')
def documentosregistrar(request):
	if request.method == 'POST':
		formulario = DocumentoForm(request.POST)
		if formulario.is_valid():
			codigo = formulario.cleaned_data['codigo']
			asunto = formulario.cleaned_data['asunto']
			fentrega = formulario.cleaned_data['fentrega']
			contometro = formulario.cleaned_data['contometro']
			costo = formulario.cleaned_data['costo']
			tiraje = formulario.cleaned_data['tiraje']
			nexpediente = formulario.cleaned_data['nexpediente']
			equipo = formulario.cleaned_data['equipo']
			interesado = formulario.cleaned_data['interesado']
			tdocumento = formulario.cleaned_data['tdocumento']
			docnuevo = Documento(codigo=codigo,asunto=asunto,fentrega=fentrega,
								contometro=contometro,costo=costo,tiraje=tiraje,
								nexpediente=nexpediente,equipo=equipo,interesado=interesado,tdocumento=tdocumento)
			docnuevo.save()
			return HttpResponseRedirect('/produccion/trabajos/')
	else:
		formulario = DocumentoForm(auto_id=True)
	return render_to_response('doceditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def documentosdetalle(request, documento_id):
	dato = get_object_or_404(Documento, pk=documento_id)
	return render_to_response('detalledocumento.html',{'dato':dato})

@login_required(login_url='/ingreso/')
def documentoseditar(request, documento_id):
	dato = get_object_or_404(Documento, pk=documento_id)
	if request.method == 'POST':
		formulario = DocumentoForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
			redireccion = '/produccion/trabajos/detalle/'+str(documento_id)
			return HttpResponseRedirect(redireccion)
	else:
		formulario = DocumentoForm(instance=dato)
	return render_to_response('doceditar.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/ingreso/')
def articulos(request):
	datos = Articulo.objects.all().order_by('nombre')
	return render_to_response('articulos.html',{'datos':datos})

@login_required(login_url='/ingreso/')
def articulosdetalle(request, articulo_id):
	dato = get_object_or_404(Articulo, pk=articulo_id)
	return render_to_response('articulosdetalle.html',{'dato':dato})

@login_required(login_url='/ingreso/')
def articuloseditar(request, articulo_id):
	dato = get_object_or_404(Articulo, pk=articulo_id)
	if request.method == 'POST':
		formulario = ArticuloForm(request.POST, instance=dato)
		if formulario.is_valid():
			formulario.save()
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
			nombre = formulario.cleaned_data['nombre']
			marca = formulario.cleaned_data['marca']
			codigo = formulario.cleaned_data['codigo']
			caracteristica = formulario.cleaned_data['caracteristica']
			umedida = formulario.cleaned_data['umedida']
			sactual = formulario.cleaned_data['sactual']
			articulonuevo = Articulo(nombre=nombre,marca=marca,codigo=codigo,
									caracteristica=caracteristica,
									umedida=umedida,sactual=sactual)
			articulonuevo.save()
			return HttpResponseRedirect('/almacen/articulos/')
	else:
		formulario = ArticuloForm(auto_id=True)
	return render_to_response('articuloseditar.html',{'formulario':formulario},context_instance=RequestContext(request))

def registroarticuloformu(request):
	if request.method == 'POST':
		formulario = RegistroArticuloForm(request.POST)
		if formulario.is_valid():
			detalle = formulario.cleaned_data['detalle']
			cantidad = formulario.cleaned_data['cantidad']
			fregistro = formulario.cleaned_data['fregistro']
			tipo = formulario.cleaned_data['tipo']
			precio = formulario.cleaned_data['precio']
			preciototal = formulario.cleaned_data['preciototal']
			articulo = formulario.cleaned_data['articulo']
			usuario = request.user
			guardarregistro = RegistroArticulo(detalle=detalle,cantidad=cantidad,fregistro=fregistro,tipo=tipo,precio=precio,preciototal=preciototal,articulo=articulo,usuario=usuario)
			guardarregistro.save()
			return HttpResponseRedirect('/')
	else:
		formulario = RegistroArticuloForm(auto_id=True)
	return render_to_response('registroarticuloform.html',{'formulario':formulario},context_instance=RequestContext(request))
