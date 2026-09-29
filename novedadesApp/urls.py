from django.urls import path
from novedadesApp import views

urlpatterns = [
    path('', views.novedades, name='novedades'),
    path('<int:novedad_id>/', views.detalle, name='detalle_novedad'),
]
