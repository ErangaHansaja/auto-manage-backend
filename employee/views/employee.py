from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return Employee.objects.filter(deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "success": True,
                "message": "Employees retrieved successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "success": True,
                "message": "Employee created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
