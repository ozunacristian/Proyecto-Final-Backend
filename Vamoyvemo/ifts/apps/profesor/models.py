from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=100)

def __str__(self):
    return f"{self.nombre} {self.especialidad}"
    