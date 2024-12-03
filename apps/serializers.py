from rest_framework import serializers
from apps.models import *


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentUser
        fields = '__all__'
