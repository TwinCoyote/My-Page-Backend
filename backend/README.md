# Django Portfolio Backend (API + Admin)

Backend en **Django + Django REST Framework** que funciona como **CMS headless** para un portafolio en **React**.

El objetivo es administrar proyectos desde el **Django Admin** y exponerlos vía **API REST** para que el frontend en React los consuma automáticamente.

---

## Arquitectura

```
[Django + Admin]  →  [API REST]  →  [React]
```

* Django **no renderiza HTML**
* React es el único frontend
* Comunicación por JSON

---

## Funcionalidades

* CRUD de proyectos desde Django Admin
* API REST para listar proyectos
* Separación total frontend / backend
* Preparado para CORS

---

## Requisitos

* Python 3.10+
* pip
* Virtualenv (recomendado)

---

## Instalación

```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate     

pip install -r requirements.txt
```

---

## Configuración inicial

```bash
django-admin startproject backend
cd backend
python manage.py startapp portfolio
```

Agregar apps en `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'portfolio',
]
```

Configurar CORS:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

---

## Admin

```bash
python manage.py createsuperuser
python manage.py runserver
```

Accede a:

```
http://localhost:9001/admin
```

Desde ahí puedes agregar y editar proyectos.

---

## API

Ejemplo de endpoint:

```
GET /api/projects/
```

