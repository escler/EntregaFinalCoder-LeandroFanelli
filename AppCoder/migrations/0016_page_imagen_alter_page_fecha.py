# Generated by Django 4.0.1 on 2022-02-02 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_alter_page_cuerpo_alter_page_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='imagen',
            field=models.ImageField(null=True, upload_to='ImagenesBlog'),
        ),
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 18, 6, 49, 471896)),
        ),
    ]
