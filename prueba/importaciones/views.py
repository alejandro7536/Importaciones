from django.shortcuts import render
from importaciones.models import Estadistica
from django.views.generic import ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from importaciones.forms import RegistroForm
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

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
	def get_context_data(self, **kwargs):
		context = super(CreateRegistroView,self).get_context_data(**kwargs)
		context['action'] = reverse('registro-new')
		return context
	def get_success_url(self):
		return reverse('registro-list')

class DetailRegistro(DetailView):
	model = Estadistica
	template_name = "detalle_registro.html"

class DeleteRegistro(DetailView):
	model = Estadistica
	template_name = 'delete_registro.html'
	def get_success_url(self):
		return reverse('articulo-list')

class UpdateRegistroView(UpdateView):
	model = Estadistica
	template_name = 'edit_registro.html'
	form_class = RegistroForm
	def get_context_date(self, **kwargs):
		context = super(UpdateRegistroView,self).get_context_data(**kwargs)
		context['action'] = reverse('registro-edit', kwargs={'pk':self.get_object().id})
		return context
	def get_success_url(self):
		return reverse('registro-list')