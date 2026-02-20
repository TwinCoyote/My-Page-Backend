from rest_framework import generics
from django.shortcuts import render
from .models import Proyectos, Certifications, MyWorkExperience, Technology
from .serializers import (
    ProyectosSerializer,
    CertificationsSerializer,
    MyWorkExperienceSerializer,
    TechnologySerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProyectosListCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["titulo", "descripcion", "tecnologias__nombre"]
    ordering_fields = ["fecha_creacion"]


class ProyectosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer


class CertificationsListCreate(generics.ListCreateAPIView):
    queryset = Certifications.objects.all()
    serializer_class = CertificationsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["titulo", "descripcion", "tecnologias__nombre"]
    ordering_fields = ["fecha"]


class CertificationsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certifications.objects.all()
    serializer_class = CertificationsSerializer


class MyWorkExperienceListCreate(generics.ListCreateAPIView):
    queryset = MyWorkExperience.objects.all()
    serializer_class = MyWorkExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["titulo", "puesto", "descripcion", "tecnologias__nombre"]
    ordering_fields = ["fecha_years", "titulo"]


class MyWorkExperienceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyWorkExperience.objects.all()
    serializer_class = MyWorkExperienceSerializer


class TechnologyListCreate(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TechnologyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


def home_backend(request):
    return render(request, "home_backend.html")
