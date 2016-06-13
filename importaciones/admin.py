from django.contrib import admin
from importaciones.models import Categoria, Producto, Estadistica

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Estadistica)