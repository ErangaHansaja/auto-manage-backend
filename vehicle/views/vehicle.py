from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Vehicle.objects.filter(deleted=False)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
