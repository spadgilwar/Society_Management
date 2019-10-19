from rest_framework import serializers
from .models import Property_Info, Unit_types, Unit_status, Unit

class PropertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Info
        fields = "__all__"

class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_types
        fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

class UnitStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_status
        fields = '__all__'
