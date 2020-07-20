from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.gis import admin
class UserLocationAdmin(admin.OSMGeoAdmin):
    fields = ('user', 'user_locations', 'status')
    list_display = ['user', 'latitude', 'longitude', 'status']

    def latitude(self,obj):
        return obj.user_locations.x
    latitude.short_description = 'Latitude'

    def longitude(self,obj):
        return obj.user_locations.y
    longitude.short_description = 'Longitude'



admin.site.register(UserLocation,UserLocationAdmin)
