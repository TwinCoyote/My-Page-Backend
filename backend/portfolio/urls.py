from django.urls import path
from .views import (
    ProyectosListCreate,
    ProyectosRetrieveUpdateDestroy,
    CertificationsListCreate,
    CertificationsRetrieveUpdateDestroy,
    MyWorkExperienceListCreate,
    MyWorkExperienceRetrieveUpdateDestroy,
    home_backend,
)

urlpatterns = [
    path("", home_backend, name="home_backend"),
    path("proyectos/", ProyectosListCreate.as_view(), name="proyectos-list"),
    path("proyectos/<int:pk>/", ProyectosRetrieveUpdateDestroy.as_view(),
         name="proyectos-detail"),
    path("certifications/", CertificationsListCreate.as_view(),
         name="certifications-list"),
    path("certifications/<int:pk>/",
         CertificationsRetrieveUpdateDestroy.as_view(), name="certifications-detail"),
    path("work-experience/", MyWorkExperienceListCreate.as_view(),
         name="work-experience-list",),
    path("work-experience/<int:pk>/", MyWorkExperienceRetrieveUpdateDestroy.as_view(),
         name="work-experience-detail",),
]
