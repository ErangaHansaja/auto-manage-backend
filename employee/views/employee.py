from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Employee.objects.filter(deleted=False)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
