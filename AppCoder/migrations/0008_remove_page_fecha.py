# Generated by Django 4.0.1 on 2022-01-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_page_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='fecha',
        ),
    ]
