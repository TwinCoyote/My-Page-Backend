from django.shortcuts import render
from rest_framework import generics
from .models import Proyectos

class ProyectosListCreate(generics.ListCreateAPIView):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer