from django.db import models


class Vehicle(models.Model):
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=50, unique=True, verbose_name="VIN")
    number_plate = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20)
    driving_type = models.CharField(max_length=20)  # e.g., manual, automatic
    last_service_date = models.DateField(null=True, blank=True)
    fuel_type = models.CharField(max_length=20)
    current_mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.number_plate} - {self.model}"
