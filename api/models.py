import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import *


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    video_file = models.FileField(upload_to='video_files', validators=[
                                  FileExtensionValidator(allowed_extensions=['mp4', 'mkv']), validate_file])
    thumbnail = models.FileField(upload_to='thumbnails', validators=[
                                 FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class VideoCharge(models.Model):
    size = models.IntegerField()
    duration_in_seconds = models.IntegerField()
    video_type = models.CharField(max_length=255)
