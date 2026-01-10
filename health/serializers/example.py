from rest_framework import serializers
from health.models import ExampleProfile


class ExampleProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for ExampleProfile model.
    Handles validation and JSON conversion.
    """

    class Meta:
        model = ExampleProfile
        fields = [
            "id",
            "name",
            "age",
            "vehicle_type",
            "is_deleted",
        ]
        read_only_fields = ["id"]
