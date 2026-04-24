from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.roles import ROLE_CHOICES, ADMIN


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ADMIN)

    def __str__(self):
        return self.username
