# Generated by Django 5.1 on 2024-10-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]