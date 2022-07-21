from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.homePage, name='api'),
    path('videos/<str:pk>/', views.video_details_view, name='detail'),
    path('create/', views.video_create_view, name='create'),
    path('charge/', views.checkParams, name='charge'),
]
