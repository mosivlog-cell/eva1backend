from django.contrib import admin

from novedadesApp.models import Evento, Novedad, TipoNovedad


class NovedadInline(admin.TabularInline):
	model = Novedad
	extra = 0
	fields = ('titulo', 'fecha', 'publicada', 'producto')
	show_change_link = True


@admin.register(TipoNovedad)
class TipoNovedadAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	search_fields = ('nombre',)
	inlines = [NovedadInline]


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'tipo', 'producto', 'fecha', 'publicada')
	list_filter = ('tipo', 'publicada', 'fecha')
	search_fields = ('titulo', 'resumen', 'producto__nombre')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha_evento', 'lugar', 'cupos')
	list_filter = ('fecha_evento',)
	search_fields = ('nombre', 'lugar', 'descripcion')
