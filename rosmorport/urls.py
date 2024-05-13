# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from app import views
#
#
# urlpatterns = [
#     path('app/', views.AppList.as_view()),
#     path('app/<int:pk>/', views.AppDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


from django.urls import path

from app.views import *

urlpatterns = [
    path('Country/', CountryViewSet, name='Country'),
    path('User/', UserViewSet, name='User'),
]
