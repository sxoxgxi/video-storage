# import uuid
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    size = models.IntegerField()
    duration = models.IntegerField()
    video_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
