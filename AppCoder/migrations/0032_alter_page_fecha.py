# Generated by Django 4.0.1 on 2022-02-13 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0031_alter_page_fecha_alter_page_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 4, 52, 46, 807206)),
        ),
    ]
