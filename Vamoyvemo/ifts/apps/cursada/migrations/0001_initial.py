<<<<<<< HEAD
# Generated by Django 5.1 on 2024-11-19 04:10
=======
# Generated by Django 5.1 on 2024-10-22 20:45
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('cicloLectivo', '0001_initial'),
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('estado', models.BooleanField()),
                ('fecha_inscripcion', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='alumno.alumno')),
                ('ciclolectivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='cicloLectivo.ciclolectivo')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='materia.materia')),
=======
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField(default=False)),
>>>>>>> 32541215ee602ad882f987b15e0facbc0b830a6d
            ],
        ),
    ]
