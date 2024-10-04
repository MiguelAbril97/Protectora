from django.urls import path
from . import views

urlpatterns = [
    path('', views.entradaAnimales, name='entradaAnimales.html'),
    path('animales/', views.entradaAnimales, name='entradaAnimales.html'),
    path('colaboradores/', views.entradaColaboradores, name='entradaColaboradores.html'),
    path('protectoras/', views.entradaProtectoras, name='entradaProtectoras.html'),
]
