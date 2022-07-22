from django.core.exceptions import ValidationError
from .videoutils import *


def validate_file_length(value):
    if get_length_seconds(value) > 600:
        raise ValidationError('Video length cannot exceed 10 minutes.')
    else:
        return value


def validate_file_size(value):
    if filesize(value, 'mb') > 1024:
        return ValidationError('Video size cannot exceed 1GB.')
    else:
        return value
