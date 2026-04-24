from django.db import models


class ExampleProfile(models.Model):
    """
    Example model to demonstrate
    basic CRUD structure using Django + DRF.
    """

    class VehicleType(models.TextChoices):
        CAR = "car", "Car"
        VAN = "van", "Van"
        BUS = "bus", "Bus"
        LORRY = "lorry", "Lorry"

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    vehicle_type = models.CharField(
        max_length=10,
        choices=VehicleType.choices
    )

    is_deleted = models.BooleanField(
        default=False,
        help_text="Soft delete flag"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"
