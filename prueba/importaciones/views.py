from django.shortcuts import render
from importaciones.models import Estadistica
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from importaciones.forms import RegistroForm
from django.views.generic import DetailView

# Create your views here.
# Este es el views en el que debo trabajar.

def inicio(request):
    return render(request, 'Index.html')

def login(request):
    return render(request, 'login.html')

def gestion(request):
    return render(request, 'data.html')

def archivocsv(request):
	return render(request, 'archivocsv.html')

class ListRegistroView(ListView):
	model = Estadistica
	template_name = "registro_list.html"

class CreateRegistroView(CreateView):
	model = Estadistica
	template_name = 'edit_registro.html'
	form_class = RegistroForm
	def get_success_url(self):
		return reverse('registro-list')