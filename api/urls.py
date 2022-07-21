from django.urls import path

from . import views

urlpatterns = [
    path('videos/', views.homePage, name='api'),
    path('videos/<str:pk>/', views.VideoDetailsApiView.as_view()),
    path('charge/', views.checkParams, name='charge'),
]
