from rest_framework import serializers
from mechanic_assist.models import AssistRequest

class AssistRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistRequest
        fields = [
            "id",
            "customer_id",
            "vehicle_id",
            "issue"
        ]
        read_only_fields = ["id"]
