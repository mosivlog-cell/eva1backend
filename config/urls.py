"""
URL configuration for config project.
El archivo principal solo actúa como punto de entrada e incluye
las rutas de cada aplicación.
"""
from django.contrib import admin
from django.urls import include, path

from novedadesApp.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('inventario/', include('inventarioApp.urls')),
    path('novedades/', include('novedadesApp.urls')),
]
