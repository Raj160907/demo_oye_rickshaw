from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts_locations.models import *
from locations.models import *
from rickshaw.models import *

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField('latitude_dt')
    longitude = serializers.SerializerMethodField('longitude_dt')
    user_type = serializers.CharField(source='get_user_type_display')
    rickshaw_number = serializers.SerializerMethodField('rickshaw_number_dt')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'user_type', 'latitude', 'longitude', 'rickshaw_number')

    def latitude_dt(self, obj):
        return obj.user_locations_id.last().user_locations.x

    def longitude_dt(self, obj):
        return obj.user_locations_id.last().user_locations.y

    def rickshaw_number_dt(self, obj):
        if obj.user_rickshaw.filter(status=True).exists():
            return obj.user_rickshaw.filter(status=True).last().rickshaw_number
        else:
            return ""

class UserLocationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = UserLocation
        fields = ('id', 'user', 'user_locations', 'status')


class DriverRickshawSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = DriverRickshaw
        fields = ('id', 'user', 'rickshaw_number')
