from pyexpat import model
from rest_framework import serializers
from .models import Video, VideoCharge


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
        model = VideoCharge
        fields = ['size', 'duration_in_seconds', 'video_type']
