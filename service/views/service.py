from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from service.models import Service
from service.serializers import ServiceSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        dataset = Service.objects.filter(deleted=False)
        serializer = self.get_serializer(dataset, many=True)

        return Response(
            {
                "success": True,
                "message": "Services retrieved successfully",
                "data": serializer.data,
            },
            status=HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "success": True,
                "message": "Service created successfully",
                "data": serializer.data,
            },
            status=HTTP_201_CREATED,
        )