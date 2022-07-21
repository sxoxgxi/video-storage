# from django.shortcuts import render
# import json
from rest_framework.decorators import api_view
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from datetime import timedelta
from .models import Video
from .serializers import VideoSerializer, VideoChargeSerializer, VideosSerializer
from .videoutils import *


@api_view(['GET'])
def homePage(request):
    if instance := Video.objects.all():
        data = VideosSerializer(instance, many=True).data
    else:
        data = {'Error': 'No video available.'}
    return Response(data)


@api_view(['POST'])
def checkParams(request):
    serializer = VideoChargeSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True) and serializer.data['video_type'] in ['mp4', 'mkv']:
        videosize = serializer.data['size']
        seconds = serializer.data['duration']
        length = timedelta(seconds=seconds)
        cost = rate(videosize, seconds)
        return Response({"Video size": videosize, "Length": f"{length}", "Upload cost": f"{cost}$"})
        # return Response(serializer.data)
    return Response({"video_type": ['This field must be mp4 or mkv.']}, status=400)


class VideoDetailsApiView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
