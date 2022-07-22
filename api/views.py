from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from datetime import timedelta
from .models import Video
from .serializers import VideoSerializer, VideoChargeSerializer, VideosSerializer
from .videoutils import *


def homepage(request):
    return render(request, 'api/home.html')


@api_view(['GET'])
def videosPage(request):
    if instance := Video.objects.all():
        data = VideosSerializer(instance, many=True).data
    else:
        data = {'Error': 'No video available.'}
    return Response(data)


@api_view(['POST'])
def checkParams(request):
    serializer = VideoChargeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) and serializer.data['video_type'] in ['mp4', 'mkv']:
        videosize = serializer.data['size']
        seconds = serializer.data['duration_in_seconds']
        length = timedelta(seconds=seconds)
        cost = rate(videosize, seconds)
        return Response({"Video size": videosize, "Length": f"{length}", "Upload cost": f"{cost}$"})
    return Response({"video_type": ['This field must be mp4 or mkv.']}, status=400)


class VideoDetailsApiView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


video_details_view = VideoDetailsApiView.as_view()


class VideoUploadView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


video_upload_view = VideoUploadView.as_view()
