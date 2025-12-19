from rest_framework import serializers
from .models import Proyectos

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields=["id","titulo","descripcion","link","imagen","videos","fecha_creacion"]