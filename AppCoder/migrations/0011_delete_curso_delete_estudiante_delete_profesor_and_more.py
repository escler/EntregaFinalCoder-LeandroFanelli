# Generated by Django 4.0.1 on 2022-01-28 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_alter_page_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 19, 30, 41, 324239)),
        ),
    ]