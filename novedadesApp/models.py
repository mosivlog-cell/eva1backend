from django.db import models
from django.utils import timezone

from inventarioApp.models import Producto


class TipoNovedad(models.Model):
	nombre = models.CharField(max_length=60, unique=True, verbose_name='Tipo de Novedad')

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'tipos_novedad'
		verbose_name = 'Tipo de Novedad'
		verbose_name_plural = 'Tipos de Novedad'
		ordering = ['nombre']


class Novedad(models.Model):
	titulo = models.CharField(max_length=150, verbose_name='Título')
	resumen = models.TextField(verbose_name='Resumen')
	imagen = models.CharField(max_length=200, blank=True, verbose_name='Ruta de imagen (static)')
	fecha = models.DateField(default=timezone.localdate, verbose_name='Fecha')
	publicada = models.BooleanField(default=True, verbose_name='Publicada')
	tipo = models.ForeignKey(
		TipoNovedad, on_delete=models.RESTRICT, related_name='novedades', verbose_name='Tipo'
	)
	producto = models.ForeignKey(
		Producto, null=True, blank=True, on_delete=models.SET_NULL,
		related_name='novedades', verbose_name='Producto relacionado'
	)

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'novedades'
		verbose_name = 'Novedad'
		verbose_name_plural = 'Novedades'
		ordering = ['-fecha']


class Evento(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Nombre del Evento')
	descripcion = models.TextField(blank=True, verbose_name='Descripción')
	fecha_evento = models.DateTimeField(verbose_name='Fecha y hora')
	lugar = models.CharField(max_length=150, verbose_name='Lugar')
	cupos = models.PositiveIntegerField(default=0, verbose_name='Cupos')
	imagen = models.CharField(max_length=200, blank=True, verbose_name='Ruta de imagen (static)')

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'eventos'
		verbose_name = 'Evento'
		verbose_name_plural = 'Eventos'
		ordering = ['fecha_evento']
