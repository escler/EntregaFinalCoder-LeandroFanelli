# Generated by Django 4.0.1 on 2022-02-13 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0039_page_usuario_alter_page_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 5, 31, 35, 134263)),
        ),
    ]
