from django.contrib import admin
<<<<<<< HEAD

=======
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d
from apps.materia.models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'codigo')

