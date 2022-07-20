# import uuid
from pydoc import describe
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
