from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import VendorInfoSerializer, VendorInvoiceSerializer
from .models import vendor_info, vendor_invoices

import requests, json

# Create your views here.

class VendorInfoViewset(viewsets.ModelViewSet):
    serializer_class = VendorInfoSerializer
    queryset = vendor_info.objects.all()

class VendorInvoicesViewset(viewsets.ModelViewSet):
    serializer_class = VendorInvoiceSerializer
    queryset = vendor_invoices.objects.all()
