from django.shortcuts import render_to_response
from portal.models import LoginForm
from portal.models import RegistroArticuloForm
from django.template import RequestContext
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

def registroarticuloform(request):
	formulario = RegistroArticuloForm(auto_id=True)
	return render_to_response('registroarticuloform.html',{'formulario':formulario},context_instance=RequestContext(request))
