from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'Index.html')

def login(request):
    return render(request, 'login.html')

def gestion(request):
    return render(request, 'data.html')

def archivocsv(request):
	return render(request, 'archivocsv.html')