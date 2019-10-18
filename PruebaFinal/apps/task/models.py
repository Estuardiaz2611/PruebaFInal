from django.db import models

from apps.encargado.models import Encargado

# Create your models here.

class Task(models.Model):
    titulo_task = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    encargado = models.ForeignKey(Encargado, null=True, blank=True, on_delete=models.CASCADE)