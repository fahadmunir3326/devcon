# Generated by Django 3.0.5 on 2020-05-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0019_auto_20200527_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='Linked_in',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='Personal_site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='fb_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='github_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='devconnector/images'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='insta_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='Degree_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='Institute',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]