from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Customer.objects.filter(deleted=False)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()