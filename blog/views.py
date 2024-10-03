from django.shortcuts import render
from .models import Animal, Colaborador, Protectora
# Create your views here.

def entradaAnimales(request):
    entrada = Animal.objects.all() 
    return render(request, 'blog/entradaAnimales.html', {'Animal_mostrar': entrada})

def entradaColaboradores(request):
    entrada = Colaborador.objects.all() 
    return render(request, 'blog/entradaColaboradores.html', {'Colaborador_mostrar': entrada})

def entradaProtectoras(request):
    entrada = Protectora.objects.all() 
    return render(request, 'blog/entradaProtectoras.html', {'Protectora_mostrar': entrada})


