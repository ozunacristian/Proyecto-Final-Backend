from django.db import models

# Create your models here.
class Directivo(models.Model):
    nombre = models.CharField(max_length=255)