import os
import django
from django.contrib.auth import get_user_model

# Ajusta esto según tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'Nievesilla2001B%.'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username, email=email, password=password)
    print(f"Superuser '{username}' creado exitosamente.")
else:
    print(f"El usuario '{username}' ya existe.")
