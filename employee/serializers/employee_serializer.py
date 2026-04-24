from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_no",
            "address",
            "nic",
            "role",
            "department",
        ]
        read_only_fields = ["id"]
