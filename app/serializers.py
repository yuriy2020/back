from rest_framework import serializers
from app.models import *


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    country = CountryModelSerializer()

    class Meta:
        model = UserModel
        fields = ('family',
                  'name',
                  'surname',
                  'country',
                  'sex',
                  'traditional',
                  'dietician',
                  'vegan',)

    def get_country(self, obj):
        return CountryModelSerializer(obj.country).data


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentUser
        fields = '__all__'
