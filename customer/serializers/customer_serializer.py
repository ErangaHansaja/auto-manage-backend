from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "nic",
            "email",
            "phone_number",
            "address"
        ]
        read_only_fields = ["id"]
