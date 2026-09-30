from django.urls import path
from novedadesApp import views

urlpatterns = [
    path('', views.novedades, name='novedades'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('<int:novedad_id>/', views.detalle, name='detalle_novedad'),
]
