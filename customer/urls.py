from django.urls import path
from customer.views import CustomerListCreateView, RemoveCustomerView

urlpatterns = [
    # endpoints will be added later
    path('register', CustomerListCreateView.as_view(), name='customer-list'),
    path('delete', RemoveCustomerView.as_view(), name='delete-customer'),
]
