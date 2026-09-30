from django.urls import path
from inventarioApp import views

urlpatterns = [
    path('', views.lista_productos, name='inventario'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
]
