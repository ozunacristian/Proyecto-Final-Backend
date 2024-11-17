from django.db import models

class Cursada(models.Model):
<<<<<<< HEAD
  alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE, related_name='cursadas')
  ciclo_lectivo = models.ForeignKey('cicloLectivo.CicloLectivo', on_delete=models.CASCADE, related_name='cursadas')
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='cursadas')

  estado = models.BooleanField()
  fecha_inscripcion = models.DateField()
=======
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  estado = models.BooleanField(default=False)
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d

def __str__(self):
  return f"{self.fecha_inicio} {self.fecha_fin} {self.estado}"
