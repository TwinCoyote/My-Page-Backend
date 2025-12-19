from django.urls import path
from .views import ProyectosListCreate, ProyectosRetrieveUpdateDestroy, home_backend

urlpatterns = [
    path("", home_backend, name="home_backend"),
    path("proyectos/", ProyectosListCreate.as_view(), name="proyectos-list"),
    path("proyectos/<int:pk>/", ProyectosRetrieveUpdateDestroy.as_view(), name="proyectos-detail"),
]
