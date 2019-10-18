from django.db import models

# Create your models here.

class Encargado(models.Model):
    nombre_encargado = models.CharField(max_length=50)
    apellido_encargado = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre_encargado)
