# Generated by Django 4.0.1 on 2022-02-13 08:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0038_remove_page_usuario_alter_page_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 5, 31, 30, 554677)),
        ),
    ]
