from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from inventarioApp.models import Categoria, Producto
from novedadesApp.models import Evento, Novedad, TipoNovedad


def inicio(request):
    productos = Producto.objects.filter(activo=True)
    contexto = {
        'titulo': 'Pixel Arcade',
        'total_productos': productos.count(),
        'total_categorias': Categoria.objects.count(),
        'destacados': productos.filter(stock__gt=0).select_related('categoria').order_by('-creado')[:4],
        'ultimas_novedades': Novedad.objects.filter(publicada=True).select_related('tipo').order_by('-fecha')[:3],
        'proximo_evento': Evento.objects.filter(fecha_evento__gte=timezone.now()).order_by('fecha_evento').first(),
    }
    return render(request, 'inicio.html', contexto)


def novedades(request):
    tipo_filtro = request.GET.get('tipo', '').strip()
    lista = Novedad.objects.select_related('tipo', 'producto').filter(publicada=True)
    if tipo_filtro:
        lista = lista.filter(tipo__nombre=tipo_filtro)

    contexto = {
        'titulo': 'Novedades y eventos',
        'novedades': lista,
        'tipos': TipoNovedad.objects.values_list('nombre', flat=True),
        'filtro': tipo_filtro,
        'eventos': Novedad.objects.filter(publicada=True, tipo__nombre='Evento').count(),
        'lanzamientos': Novedad.objects.filter(publicada=True, tipo__nombre='Lanzamiento').count(),
        'ofertas': Novedad.objects.filter(publicada=True, tipo__nombre='Oferta').count(),
        'total': Novedad.objects.filter(publicada=True).count(),
    }
    return render(request, 'novedades/novedades.html', contexto)


def detalle(request, novedad_id):
    novedad = get_object_or_404(
        Novedad.objects.select_related('tipo', 'producto'), pk=novedad_id, publicada=True
    )
    relacionadas = Novedad.objects.filter(publicada=True, tipo=novedad.tipo).exclude(pk=novedad.pk)
    return render(request, 'novedades/detalle.html', {
        'titulo': novedad.titulo,
        'novedad': novedad,
        'relacionadas': relacionadas,
    })


def lista_novedades(request):
    return novedades(request)


def lista_eventos(request):
    eventos = Evento.objects.order_by('fecha_evento')
    return render(request, 'novedades/lista_eventos.html', {'eventos': eventos})
