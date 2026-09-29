import json
from pathlib import Path

from django.conf import settings
from django.http import Http404
from django.shortcuts import render


def cargar_novedades():
    ruta = Path(settings.BASE_DIR) / 'novedadesApp' / 'data' / 'novedades.json'
    with open(ruta, encoding='utf-8') as archivo:
        return json.load(archivo)


def novedades(request):
    datos = cargar_novedades()
    tipo_filtro = request.GET.get('tipo', '').strip()
    lista = []
    tipos = []
    eventos = 0
    lanzamientos = 0
    ofertas = 0

    for item in datos:
        tipo = item.get('tipo', 'Otro')
        if tipo not in tipos:
            tipos.append(tipo)

        if tipo == 'Evento':
            eventos += 1
        elif tipo == 'Lanzamiento':
            lanzamientos += 1
        elif tipo == 'Oferta':
            ofertas += 1

        if tipo_filtro and tipo != tipo_filtro:
            continue
        lista.append(item)

    contexto = {
        'titulo': 'Novedades y eventos',
        'novedades': lista,
        'tipos': tipos,
        'filtro': tipo_filtro,
        'eventos': eventos,
        'lanzamientos': lanzamientos,
        'ofertas': ofertas,
        'total': len(datos),
    }
    return render(request, 'novedades/novedades.html', contexto)


def detalle(request, novedad_id):
    datos = cargar_novedades()
    encontrada = None

    for item in datos:
        if int(item.get('id', 0)) == int(novedad_id):
            encontrada = item
            break

    if encontrada is None:
        raise Http404('No encontramos esa novedad.')

    relacionadas = []
    for item in datos:
        mismo_tipo = item.get('tipo') == encontrada.get('tipo')
        distinta = int(item.get('id', 0)) != int(novedad_id)
        if mismo_tipo and distinta:
            relacionadas.append(item)

    contexto = {
        'titulo': encontrada.get('titulo'),
        'novedad': encontrada,
        'relacionadas': relacionadas,
    }
    return render(request, 'novedades/detalle.html', contexto)
