from django.contrib import admin
from .models import *


class DriverRickshawAdmin(admin.ModelAdmin):
    list_display = ['user', 'rickshaw_number', 'status']

admin.site.register(DriverRickshaw,DriverRickshawAdmin)
