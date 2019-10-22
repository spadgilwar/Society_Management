from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ResidentInfoSerializer, LedgerSerializer
from .models import Resident_info, ledger

import requests, json

# Create your views here.

class ReidentInfoViewset(viewsets.ModelViewSet):
    serializer_class = ResidentInfoSerializer
    queryset = Resident_info.objects.all()

class LedgerViewset(viewsets.ModelViewSet):
    serializer_class = LedgerSerializer
    queryset = ledger.objects.all()
