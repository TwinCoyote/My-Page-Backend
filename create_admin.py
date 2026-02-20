import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

User = get_user_model()

username = 'admin'
password = 'Nievesilla2001B%.'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print(f"Superuser '{username}' creado exitosamente.")
else:
    print(f"El usuario '{username}' ya existe.")
