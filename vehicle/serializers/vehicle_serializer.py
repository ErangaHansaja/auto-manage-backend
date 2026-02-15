from rest_framework import serializers

from customer.serializers import CustomerSerializer
from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomerSerializer.Meta.model.objects.all(),
        source="customer",
        write_only=True,
    )

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "customer",
            "customer_id",
            "type",
            "model",
            "year",
            "vin",
            "number_plate",
            "color",
            "driving_type",
            "last_service_date",
            "fuel_type",
            "current_mileage",
        ]
        read_only_fields = ["id"]
