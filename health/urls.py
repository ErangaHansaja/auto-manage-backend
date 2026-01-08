from django.urls import path
from health.views import *

urlpatterns = [
    path("check", HealthView.as_view(), name="health-check"),
]
