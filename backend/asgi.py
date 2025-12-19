"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

# Ensure the parent directory of the project package is on sys.path
project_parent = Path(__file__).resolve().parent.parent
if str(project_parent) not in sys.path:
    sys.path.insert(0, str(project_parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_asgi_application()
