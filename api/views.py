from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("hello world  this is api page")