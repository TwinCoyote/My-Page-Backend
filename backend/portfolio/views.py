from django.shortcuts import render
from rest_framework import generics
from .models import Proyectos
from .serializers import ProyectosSerializer

class ProyectosListCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer

class ProyectosRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer
