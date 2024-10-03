from django.shortcuts import render
from .models import Animal, Colaborador, Protectora
# Create your views here.

def entradas(request):
    entrada = Animal.objects.all() 
    return render(request, 'blog/entradas.html', {'Animal_mostrar': entrada})

def entradas(request):
    entrada = Colaborador.objects.all() 
    return render(request, 'blog/entradas.html', {'Colaborador_mostrar': entrada})

def entradas(request):
    entrada = Protectora.objects.all() 
    return render(request, 'blog/entradas.html', {'Protectora_mostrar': entrada})


