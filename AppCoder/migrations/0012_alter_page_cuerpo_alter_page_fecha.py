# Generated by Django 4.0.1 on 2022-01-29 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_delete_curso_delete_estudiante_delete_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cuerpo',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 29, 19, 18, 59, 287507)),
        ),
    ]