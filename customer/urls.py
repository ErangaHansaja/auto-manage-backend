from django.urls import path
from customer.views.customer import CustomerListCreateView
from customer.views.remove_customer import RemoveCustomerView

urlpatterns = [
    # endpoints will be added later
    path('register', CustomerListCreateView.as_view(), name='customer-list'),
    path('delete', RemoveCustomerView.as_view(), name='delete-customer'),
]
