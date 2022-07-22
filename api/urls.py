from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api/videos/', views.videosPage, name='videos'),
    path('api/videos/<str:pk>/', views.video_details_view, name='detail'),
    path('api/create/', views.video_upload_view, name='create'),
    path('api/charge/', views.checkParams, name='charge'),
]
