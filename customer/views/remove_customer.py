from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from customer.models import Customer
from customer.serializers.customer import CustomerSerializer

class RemoveCustomerView(generics.UpdateAPIView):
    serializer_class = CustomerSerializer

    def update(self, request, *args, **kwargs):
        nic = request.data.get("nic")

        if not Customer.objects.filter(nic=nic).exists():
            return Response(
                {
                    "success": False,
                    "message": "NIC not found in the database",
                    "data": {},
                },
                status=HTTP_404_NOT_FOUND,
            )

        customer = Customer.objects.get(nic=nic)
        customer.deleted = True
        customer.save()

        serializer = self.get_serializer(customer)

        return Response(
            {
                "success": True,
                "message": "Customer removed successfully",
                "data": {},
            },
            status=HTTP_200_OK,
        )