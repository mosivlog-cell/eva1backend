from django.db.models import Count
from django.shortcuts import render

from inventarioApp.models import Categoria, Producto, Proveedor


def inicio(request):
    productos = Producto.objects.filter(activo=True)
    contexto = {
        'titulo': 'Pixel Arcade',
        'total_titulos': productos.count(),
        'destacados': productos.filter(stock__gt=0).select_related('categoria').order_by('-creado')[:3],
    }
    return render(request, 'inicio.html', contexto)


def inventario(request):
    return lista_productos(request)


def lista_productos(request):
    tipos = dict(Producto._meta.get_field('tipo').choices)
    filtro = request.GET.get('plataforma', '').strip()
    productos = Producto.objects.select_related('categoria', 'proveedor').filter(activo=True)
    if filtro in tipos.values():
        codigo_tipo = next(codigo for codigo, nombre in tipos.items() if nombre == filtro)
        productos = productos.filter(tipo=codigo_tipo)

    catalogo = []
    disponibles = 0
    agotados = 0
    valor_inventario = 0
    for producto in productos:
        disponible = producto.stock > 0
        disponibles += int(disponible)
        agotados += int(not disponible)
        if disponible:
            valor_inventario += producto.precio * producto.stock
        catalogo.append({
            'id': producto.pk,
            'nombre': producto.nombre,
            'plataforma': producto.get_tipo_display(),
            'categoria': producto.categoria,
            'precio': producto.precio,
            'precio_final': producto.precio,
            'descuento': 0,
            'stock': producto.stock,
            'disponible': disponible,
            'imagen': producto.imagen,
            'descripcion': producto.descripcion,
        })

    contexto = {
        'titulo': 'Catálogo',
        'catalogo': catalogo,
        'disponibles': disponibles,
        'agotados': agotados,
        'valor_inventario': valor_inventario,
        'total': len(catalogo),
        'plataformas': list(tipos.values()),
        'filtro': filtro,
    }
    return render(request, 'inventario/lista_productos.html', contexto)


def lista_categorias(request):
    categorias = Categoria.objects.annotate(total=Count('productos')).order_by('nombre')
    return render(request, 'inventario/lista_categorias.html', {'categorias': categorias})


def lista_proveedores(request):
    proveedores = Proveedor.objects.annotate(total=Count('productos')).order_by('nombre')
    return render(request, 'inventario/lista_proveedores.html', {'proveedores': proveedores})
