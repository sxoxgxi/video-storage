from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.homePage, name='api'),
]
