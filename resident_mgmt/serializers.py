from rest_framework import serializers
from .models import Resident_info, ledger

class ResidentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident_info
        fields = "__all__"

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ledger
        fields = "__all__"
