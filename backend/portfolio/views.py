from rest_framework import generics
from django.shortcuts import render
from .models import Proyectos
from .serializers import ProyectosSerializer


class ProyectosListCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer


class ProyectosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer


def home_backend(request):
    return render(request, "home_backend.html")
