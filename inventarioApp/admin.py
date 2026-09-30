from django.contrib import admin

from inventarioApp.models import Categoria, Producto, Proveedor


class ProductoInline(admin.TabularInline):
	model = Producto
	extra = 0
	fields = ('nombre', 'tipo', 'precio', 'stock', 'activo')
	show_change_link = True


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'creado')
	search_fields = ('nombre', 'descripcion')
	inlines = [ProductoInline]


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'correo', 'telefono', 'creado')
	search_fields = ('nombre', 'correo')
	inlines = [ProductoInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'categoria', 'proveedor', 'precio', 'stock', 'activo')
	list_filter = ('tipo', 'categoria', 'proveedor', 'activo')
	search_fields = ('nombre', 'descripcion', 'categoria__nombre')
