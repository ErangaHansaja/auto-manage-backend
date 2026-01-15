from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from customer.models import Customer
from customer.serializers import CustomerSerializer

class CustomerListCreateView(generics.GenericAPIView):
    serializer_class = CustomerSerializer

    def retrieve_customer_data(self):
        return Customer.objects.filter(deleted=False)

    def list(self, request, *args, **kwargs):
        dataset = Customer.objects.filter(deleted=False)
        serializer = self.get_serializer(dataset, many=True)

        return Response(
            {
                "success": True,
                "message": "Profiles retrieved successfully",
                "data": serializer.data,
            },
            status=HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        nic = request.POST.get("nic")

        if Customer.objects.filter(nic=nic).exists():
            return Response(
                {
                    "success": False,
                    "message": "NIC already registered within the database",
                    "data": {},
                },
                status=HTTP_400_BAD_REQUEST,
            )

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