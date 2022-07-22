# Generated by Django 4.0.6 on 2022-07-22 10:15

import api.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='video_files', validators=[django.core.validators.FileExtensionValidator(
                allowed_extensions=['mp4', 'mkv']), api.validators.validate_file]),
        ),
    ]