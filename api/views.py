# from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from datetime import timedelta
from .models import Video
from .serializers import VideoSerializer
from .videoutils import *


@api_view(['GET'])
def homePage(request):
    if instance := Video.objects.all().order_by('?').first():
        data = VideoSerializer(instance).data
    else:
        data = {'error': 'no video available'}
    return Response(data)


@api_view(['POST'])
def checkParams(request):
    client_data = json.loads(request.body.decode('utf-8'))
    video_size = client_data['video_size']
    seconds = client_data['length']
    lenght = timedelta(seconds=seconds)
    videosize = round(byteconversion(video_size, 'mb'))
    return Response({"filesize": videosize, 'length': f"{lenght}"})
