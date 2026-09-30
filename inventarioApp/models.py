from django.db import models
from django.utils import timezone

from inventarioApp.choices import tipos_producto


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre de la Categoría')
	descripcion = models.TextField(blank=True, verbose_name='Descripción')
	creado = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'categorias'
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['nombre']


class Proveedor(models.Model):
	nombre = models.CharField(max_length=120, verbose_name='Nombre del Proveedor')
	correo = models.EmailField(blank=True, verbose_name='Correo')
	telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
	creado = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'proveedores'
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'
		ordering = ['nombre']


class Producto(models.Model):
	nombre = models.CharField(max_length=150, verbose_name='Nombre')
	descripcion = models.TextField(blank=True, verbose_name='Descripción')
	tipo = models.CharField(max_length=1, choices=tipos_producto, default='V', verbose_name='Tipo')
	precio = models.PositiveIntegerField(verbose_name='Precio (CLP)')
	stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
	imagen = models.CharField(max_length=200, blank=True, verbose_name='Ruta de imagen (static)')
	activo = models.BooleanField(default=True, verbose_name='Activo')
	categoria = models.ForeignKey(
		Categoria, on_delete=models.RESTRICT, related_name='productos', verbose_name='Categoría'
	)
	proveedor = models.ForeignKey(
		Proveedor, null=True, blank=True, on_delete=models.SET_NULL,
		related_name='productos', verbose_name='Proveedor'
	)
	creado = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'productos'
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'
		ordering = ['nombre']
