from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Categoria(models.Model):

	nombre_categoria = models.TextField()
	def __unicode__(self):
		return self.nombre_categoria


class Producto(models.Model):

	codigo = models.CharField(max_length = 8, primary_key = True, unique = True)
	nombre_producto = models.TextField()
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.nombre_producto


class Estadistica(models.Model):

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

	producto = models.ForeignKey(Producto)
	valor = models.DecimalField(max_digits = 30, decimal_places = 2)
	cantidad = models.DecimalField(max_digits = 30, decimal_places = 2)
	mes = models.CharField(max_length = 2, choices = MES_CHOICES, default = "01")
	anho = models.PositiveSmallIntegerField()
	def __unicode__(self):
		return self.producto.nombre_producto


	class Meta:
		unique_together = [("producto", "mes", "anho")]
