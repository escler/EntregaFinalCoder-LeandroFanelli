# Generated by Django 4.0.1 on 2022-02-13 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0035_rename_user_page_usuario_alter_page_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 4, 55, 13, 76210)),
        ),
        migrations.AlterField(
            model_name='page',
            name='usuario',
            field=models.CharField(editable=False, max_length=30),
        ),
    ]
