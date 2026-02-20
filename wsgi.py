"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Ensure the parent directory of the project package is on sys.path
project_parent = Path(__file__).resolve().parent.parent
if str(project_parent) not in sys.path:
    sys.path.insert(0, str(project_parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
