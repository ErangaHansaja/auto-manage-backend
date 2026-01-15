from django.urls import path
from customer.views.customer import CustomerListCreateView

urlpatterns = [
    # endpoints will be added later
    path('register-customer', CustomerListCreateView.as_view(), name='customer-list'),
]
