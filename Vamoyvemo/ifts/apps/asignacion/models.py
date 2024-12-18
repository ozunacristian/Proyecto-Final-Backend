from django.db import models


class Asignacion(models.Model):
  profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE, related_name='asignaciones')
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='asignaciones')
  cicloLectivo = models.ForeignKey('cicloLectivo.CicloLectivo', on_delete=models.CASCADE, related_name='asignaciones')

  def __str__(self):
    return f"{self.profesor} {self.materia} {self.cicloLectivo}"