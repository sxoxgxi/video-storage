from django.urls import path

from . import views

urlpatterns = [
    path('video', views.homePage, name='api'),
    path('post', views.checkParams, name='post'),
]
