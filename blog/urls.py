from django.urls import path
from . import views

urlpatterns = [
    path('', views.entradas, name='entradas.html'),
]
