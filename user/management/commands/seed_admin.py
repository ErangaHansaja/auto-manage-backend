from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = "Seed a default admin user"

    def handle(self, *args, **options):
        if User.objects.filter(username="admin").exists():
            self.stdout.write(self.style.WARNING("Admin user already exists"))
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@automanage.com",
            password="admin123",
            role="admin",
        )
        self.stdout.write(self.style.SUCCESS("Admin user created successfully"))
