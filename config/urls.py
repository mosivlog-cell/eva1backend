"""
URL configuration for config project.
El archivo principal solo actúa como punto de entrada e incluye
las rutas de cada aplicación.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventarioApp.urls')),
    path('novedades/', include('novedadesApp.urls')),
]
