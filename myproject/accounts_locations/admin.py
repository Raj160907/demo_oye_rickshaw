from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = 'Oye Rickshaw'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Oye Rickshaw'

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (_('Personal info'), {'fields': (('first_name', 'last_name'),
                                         'phone_number', 'email',
                                         'password')}),
        (_('Permissions'), {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        #(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'email', 'first_name', 'last_name','date_joined')
    search_fields = ('phone_number','email', 'first_name', 'last_name')
    ordering = ('email',)

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

class DriverRickshawAdmin(admin.ModelAdmin):
    list_display = ['user', 'rickshaw_number', 'status']


admin.site.register(UserLocation,UserLocationAdmin)
admin.site.register(DriverRickshaw,DriverRickshawAdmin)
