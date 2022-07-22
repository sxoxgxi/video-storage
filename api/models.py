# import uuid
from turtle import update
from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import *


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    size = models.IntegerField()
    video_file = models.FileField(upload_to='video_files', validators=[
                                  FileExtensionValidator(allowed_extensions=['mp4', 'mkv']), validate_file_length, validate_file_size])
    thumbnail = models.FileField(upload_to='thumbnails', validators=[
                                 FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    duration = models.IntegerField()
    video_type = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
