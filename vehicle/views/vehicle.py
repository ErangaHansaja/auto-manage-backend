from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        return Vehicle.objects.filter(deleted=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "success": True,
                "message": "Vehicles retrieved successfully",
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
                "message": "Vehicle created successfully",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
