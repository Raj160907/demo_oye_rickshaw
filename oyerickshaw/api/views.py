from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts_locations.models import *
from locations.models import *
from rickshaw.models import *
from .serializers import *
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import authentication, permissions, generics
User = get_user_model()
# Create your views here.
class UserDetail(APIView):

    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    def get(self, request, format=None):
        user = UserDetailSerializer(self.request.user)
        msg = {'is_success': True,
                'message': None,
                'response_data': user.data}
        return Response(msg,
                        status=status.HTTP_200_OK)

    def put(self, request, format=None):
        user = self.request.user
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'is_success': True,
                    'message': ["User details updated!"],
                    'response_data': serializer.data}
            return Response(msg,
                            status=status.HTTP_200_OK)
        else:
            errors = []
            for field in serializer.errors:
                for error in serializer.errors[field]:
                    if 'non_field_errors' in field:
                        result = error
                    else:
                        result = ''.join('{} : {}'.format(field,error))
                    errors.append(result)
            msg = {'is_success': False,
                    'message': [error for error in errors],
                    'response_data': None }
            return Response(msg,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

class DriverRickshawView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.BasicAuthentication,)

    def post(self,request):
        rickshaw_number = self.request.POST.get('rickshaw_number')
        msg = {'is_success': False,'message': [''],'response_data': None}
        if rickshaw_number is None or rickshaw_number=='':
            msg['message'] = ["No Number Specified"]
            return Response(msg, status=status.HTTP_200_OK)
        if DriverRickshaw.objects.filter(rickshaw_number=rickshaw_number, status = True).exists():
            msg['message'] = ["Rickshaw number already registerd."]
            return Response(msg, status=status.HTTP_200_OK)
        rickshaw= DriverRickshaw(user = self.request.user, rickshaw_number = rickshaw_number, status = True)
        rickshaw.save()
        rickshaw_detail_serializer = DriverRickshawSerializer(rickshaw)
        return Response({"message":[''], "response_data": rickshaw_detail_serializer.data ,"is_success": True})

class UserLocationDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.BasicAuthentication,)
    def get(self,*args,**kwargs):
        user_location_id = self.request.GET.get('user_location_id')
        msg = {'is_success': False,'message': [''],'response_data': None}
        try:
           user_location = UserLocation.objects.get(id=user_location_id)
        except ObjectDoesNotExist:
           msg['message'] = ["Invalid User Location ID"]
           return Response(msg, status=status.HTTP_200_OK)

        user_location_detail= UserLocation.objects.get(id=user_location_id)
        user_location_detail_serializer = UserLocationSerializer(user_location_detail)
        return Response({"message":[''], "response_data": user_location_detail_serializer.data ,"is_success": True})

    def post(self,request):
        user_location = self.request.POST.get('user_location')
        msg = {'is_success': False,'message': [''],'response_data': None}

        user_location_detail= UserLocation(user = self.request.user, user_locations = user_location, status=True)
        user_location_detail.save()
        user_location_detail_serializer = UserLocationSerializer(user_location_detail)
        return Response({"message":[''], "response_data": user_location_detail_serializer.data ,"is_success": True})

class DriverAvailable(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.BasicAuthentication,)
    def get(self,*args,**kwargs):
        distance = self.request.GET.get('distance')
        msg = {'is_success': False,'message': [''],'response_data': None}
        if distance is None or distance=='':
            msg['message'] = ["No Distance Specified"]
            return Response(msg, status=status.HTTP_200_OK)
        current_location = User.objects.get(id=self.request.user.id).user_locations_id.filter(status=True).last().user_locations
        available_drivers_locations = UserLocation.objects.filter(status = True, user_locations__distance_lt=(current_location,Distance(m=distance))).values_list('user')
        available_drivers =  User.objects.filter(id__in = available_drivers_locations, user_type = 2)
        available_drivers_data = UserDetailSerializer(available_drivers, many=True)
        return Response({"message":['Available Drivers'], "response_data": available_drivers_data.data ,"is_success": True})
