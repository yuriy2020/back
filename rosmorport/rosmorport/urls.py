from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    path('app/', views.AppList.as_view()),
    path('app/<int:pk>/', views.AppDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
