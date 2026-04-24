from rest_framework import serializers
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "customer_name",
            "mechanic",
            "license_plate",
            "vehicle_model",
            "customer_request",
            "customer_request"
        ]
        read_only_fields = ["customer_name"]