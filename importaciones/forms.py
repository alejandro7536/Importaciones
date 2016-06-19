from django import forms
from django.core.exceptions import ValidationError
from importaciones.models import Estadistica
from importaciones.models import Producto
from importaciones.models import Categoria
import csv

class RegistroForm(forms.ModelForm):
	MES_CHOICES = (
		("01", "Enero"),
		("02", "Febrero"),
		("03", "Marzo"),
		("04", "Abril"),
		("05", "Mayo"),
		("06", "Junio"),
		("07", "Julio"),
		("08", "Agosto"),
		("09", "Septiembre"),
		("10", "Octubre"),
		("11", "Noviembre"),
		("12", "Diciembre")
	)
	
	# Sin resolver: Como enviar los productos de la base de datos a este ChoiceField?
	producto = forms.ChoiceField(required = True, label = "Producto:")
	valor = forms.DecimalField(max_digits = 30, decimal_places = 2, label = "Valor: $")
	cantidad = forms.DecimalField(max_digits = 30, decimal_places = 2, label = "Cantidad: Kg")
	mes = forms.ChoiceField(required = True, choices = MES_CHOICES, label = "Mes:")
	anho = forms.CharField(max_length = 4, required = True, label = "Anho:")

	class Meta:
		model = Estadistica
		fields = ('producto', 'valor', 'cantidad', 'mes', 'anho',)
		def clean_producto(self):
			producto = self.cleaned_data.get('producto')
			return producto
		def clean_valor(self):
			valor = self.cleaned_data.get('valor')
			return valor
		def clean_cantidad(self):
			cantidad = self.cleaned_data.get('cantidad')
			return cantidad
		def clean_mes(self):
			mes = self.cleaned_data.get('mes')
			return mes
		def clean_anho(self):
			anho = self.cleaned_data.get('anho')
			if len(anho) < 4:
				raise forms.ValidationError("Error: El anho debe ser de 4 digitos.")
			elif (re.match("\d\d\d\d", anho) == None):
				raise forms.ValidationError("Error: Solo puede digitar numeros.")
			return anho
			
class CategoriaImport(forms.ModelForm):
	archivo_a_importar = forms.FileField()

	class Meta:
		model = Categoria
		fields = ('nombre_categoria',)
	def save(self, commit=False, *args, **kwargs):
		form_ingreso = super(CategoriaImport,self).save(commit=False,*args,**kwargs)
		self.archivo_a_importar = self.cleaned_data['archivo_a_importar']
		registros = csv.reader(self.archivo_a_importar)
		for linea in registros:
			self.nombre_categoria = str(linea[2])
			form_ingreso.save()