from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from health.models import ExampleProfile
from health.serializers import ExampleProfileSerializer


class ExampleProfileListCreateView(generics.ListCreateAPIView):
    """
    GET  → List all example profiles
    POST → Create a new example profile

    This class demonstrates how one endpoint
    can handle multiple HTTP methods cleanly.
    """

    serializer_class = ExampleProfileSerializer

    def get_queryset(self):
        """
        Return only non-deleted profiles.
        """
        return ExampleProfile.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        """
        Override list() to return custom response format.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                "success": True,
                "message": "Profiles retrieved successfully",
                "data": serializer.data,
            },
            status=HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        """
        Override create() to return custom response format.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "success": True,
                "message": "Profile created successfully",
                "data": serializer.data,
            },
            status=HTTP_201_CREATED,
        )
