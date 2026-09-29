from django.urls import path
from inventarioApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inventario/', views.inventario, name='inventario'),
]
