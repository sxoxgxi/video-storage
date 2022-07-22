from django.core.exceptions import ValidationError
from .videoutils import get_length_seconds, filesize


def validate_file(value):
    if get_length_seconds(value) > 600:
        raise ValidationError('Video length cannot exceed 10 minutes.')
    elif filesize(value, 'mb') > 500:
        raise ValidationError('Video size cannot exceed 1GB.')
    else:
        return value
