# Generated by Django 3.0.5 on 2020-05-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='c',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='c_plus2',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='c_sharp',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='css',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='dotnet',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='html',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='java',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='js',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='node',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='python',
        ),
        migrations.AddField(
            model_name='developer',
            name='github_id',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.TextField(blank=True),
        ),
    ]