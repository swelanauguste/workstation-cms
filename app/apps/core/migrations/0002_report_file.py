# Generated by Django 4.0 on 2021-12-22 16:07

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=core.models.report_directory_path),
        ),
    ]
