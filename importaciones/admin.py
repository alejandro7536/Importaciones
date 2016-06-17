from django.contrib import admin
from importaciones.models import Categoria, Producto, Estadistica

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre_categoria',)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre_producto', 'categoria')

class EstadisticaAdmin(admin.ModelAdmin):
	list_display = ('producto', 'valor', 'cantidad', 'mes', 'anho')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Estadistica, EstadisticaAdmin)