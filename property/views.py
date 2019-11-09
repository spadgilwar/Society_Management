from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PropertyInfoSerializer, UnitTypeSerializer, UnitSerializer, UnitStatusSerializer
from .models import Property_Info, Unit_types, Unit, Unit_status

import requests, json

# Create your views here.

class PropertyViewset(viewsets.ModelViewSet):
    serializer_class = PropertyInfoSerializer
    queryset = Property_Info.objects.all()

class UnitTypeViewset(viewsets.ModelViewSet):
    serializer_class = UnitTypeSerializer
    queryset = Unit_types.objects.all()

class UnitViewset(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

class UnitStatusViewset(viewsets.ModelViewSet):
    serializer_class = UnitStatusSerializer
    queryset = Unit_status.objects.all()

class A():
    print('hi')

