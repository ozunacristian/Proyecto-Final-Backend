from django.contrib import admin
from apps.cursada.models import Cursada

@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
<<<<<<< HEAD
  list_display = ['alumno', 'ciclolectivo', 'materia', 'estado', 'fecha_inscripcion']
=======
  list_display = ('fecha_inicio', 'fecha_fin', 'estado')
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d
