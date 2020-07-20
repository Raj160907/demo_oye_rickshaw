from django.conf.urls import include, url
from rest_framework import routers

from .views import UserDetail, UserLocationDetail, DriverAvailable, DriverRickshawView
router = routers.DefaultRouter()

urlpatterns = [
    url('^user-detail/$', UserDetail.as_view(), name='user_detail'),
    url('^user-location-detail/$', UserLocationDetail.as_view(), name='user_location_detail'),
    url('^available-drivers/$', DriverAvailable.as_view(), name='available_drivers'),
    url('^driver-rickshaw-details/$', DriverRickshawView.as_view(), name='driver_rickshaw_details'),
]

urlpatterns += router.urls
