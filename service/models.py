from django.db import models

# Create your models here.
class Service(models.Model):
    customer_name = models.CharField(max_length=100, blank=False, null=False)
    mechanic = models.CharField(max_length=100, blank=False, null=False) 
    license_plate = models.CharField(max_length=20, blank=False, null=False)
    vehicle_model = models.CharField(max_length=50)
    customer_request = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Service for {self.customer_name} - {self.vehicle_model}"