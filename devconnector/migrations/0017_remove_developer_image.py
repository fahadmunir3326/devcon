# Generated by Django 3.0.5 on 2020-05-27 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0016_auto_20200527_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='image',
        ),
    ]
