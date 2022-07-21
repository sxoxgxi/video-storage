# from django.shortcuts import render
import json
from rest_framework.decorators import api_view
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from datetime import timedelta
from .models import Video
from .serializers import VideoSerializer, VideoChargeSerializer
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
    serializer = VideoChargeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        videosize = serializer.data['size']
        seconds = serializer.data['duration']
        length = timedelta(seconds=seconds)
        cost = rate(videosize, seconds)
        return Response({"Video size": videosize, "Length": f"{length}", "Upload cost": f"{cost}$"})
        # return Response(serializer.data)
    return Response({"error": "invalid params"})
