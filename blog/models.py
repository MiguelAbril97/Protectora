from django.db import models
from django.conf import settings

# Create your models here.

class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    

class Protectora(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField()
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    fecha_entrada_protectora = models.DateTimeField()