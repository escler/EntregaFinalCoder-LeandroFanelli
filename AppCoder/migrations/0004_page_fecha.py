# Generated by Django 4.0.1 on 2022-01-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_rename_blog_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='fecha',
            field=models.TimeField(auto_now=True),
        ),
    ]
