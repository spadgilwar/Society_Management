from rest_framework import serializers
from .models import vendor_info, vendor_invoices

class VendorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_info
        fields = "__all__"

class VendorInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_invoices
        fields = "__all__"
