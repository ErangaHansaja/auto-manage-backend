from django.urls import path
from service.views import ServiceListCreateView

urlpatterns = [
    path('book_service', ServiceListCreateView.as_view(), name='create-service'),
]