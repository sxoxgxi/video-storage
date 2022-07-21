from pyexpat import model
from rest_framework import serializers
from .models import Video


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class VideoChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['size', 'duration', 'video_type']
