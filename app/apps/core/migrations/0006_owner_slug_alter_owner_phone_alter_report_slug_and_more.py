# Generated by Django 4.0 on 2021-12-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_workstation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
