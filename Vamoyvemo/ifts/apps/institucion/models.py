from django.db import models

# Create your models here.
class Institucion(models.Model):
  nombre = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.nombre}"
