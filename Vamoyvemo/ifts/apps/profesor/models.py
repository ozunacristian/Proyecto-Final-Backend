from django.db import models

# Create your models here.
class Profesor(models.Model):
<<<<<<< HEAD
    legajo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
=======
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=100)
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d

def __str__(self):
    return f"{self.nombre} {self.especialidad}"
    