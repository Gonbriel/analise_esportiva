from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create superuser if it does not exist"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv('USERNAME')
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv('PASSWORD')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' criado!"))
        else:
            self.stdout.write(f"Superuser '{username}' já existe.")