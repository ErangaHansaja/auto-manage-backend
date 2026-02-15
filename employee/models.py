from django.db import models


class Employee(models.Model):
    ROLE_CHOICES = [
        ("mechanic", "Mechanic"),
        ("electrician", "Electrician"),
        ("painter", "Painter"),
        ("supervisor", "Supervisor"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    nic = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
