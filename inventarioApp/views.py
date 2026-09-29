import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def cargar_productos():
    ruta = Path(settings.BASE_DIR) / 'inventarioApp' / 'data' / 'productos.json'
    with open(ruta, encoding='utf-8') as archivo:
        return json.load(archivo)


def procesar_catalogo(productos, plataforma_filtro=''):
    catalogo = []
    disponibles = 0
    agotados = 0
    valor_inventario = 0
    plataformas = []

    for item in productos:
        plataforma = item.get('plataforma', 'Otra')
        if plataforma not in plataformas:
            plataformas.append(plataforma)

        if plataforma_filtro and plataforma != plataforma_filtro:
            continue

        precio = int(item.get('precio', 0))
        stock = int(item.get('stock', 0))
        descuento = int(item.get('descuento', 0))
        disponible = stock > 0

        precio_final = precio
        if descuento > 0:
            precio_final = int(precio * (100 - descuento) / 100)

        if disponible:
            disponibles += 1
            valor_inventario += precio_final * stock
        else:
            agotados += 1

        catalogo.append({
            'id': item.get('id'),
            'nombre': item.get('nombre'),
            'plataforma': plataforma,
            'categoria': item.get('categoria'),
            'precio': precio,
            'precio_final': precio_final,
            'descuento': descuento,
            'stock': stock,
            'disponible': disponible,
            'imagen': item.get('imagen'),
            'descripcion': item.get('descripcion', ''),
        })

    return {
        'catalogo': catalogo,
        'disponibles': disponibles,
        'agotados': agotados,
        'valor_inventario': valor_inventario,
        'total': len(catalogo),
        'plataformas': plataformas,
        'filtro': plataforma_filtro,
    }


def inicio(request):
    productos = cargar_productos()
    destacados = []
    for item in productos:
        if int(item.get('descuento', 0)) > 0 and int(item.get('stock', 0)) > 0:
            destacados.append(item)
        if len(destacados) >= 3:
            break

    contexto = {
        'titulo': 'Pixel Arcade',
        'total_titulos': len(productos),
        'destacados': destacados,
    }
    return render(request, 'inventario/inicio.html', contexto)


def inventario(request):
    plataforma = request.GET.get('plataforma', '').strip()
    productos = cargar_productos()
    contexto = procesar_catalogo(productos, plataforma)
    contexto['titulo'] = 'Catálogo'
    return render(request, 'inventario/inventario.html', contexto)
