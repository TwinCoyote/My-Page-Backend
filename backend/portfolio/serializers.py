# pylint: disable=C0115,C0114


from rest_framework import serializers
from .models import Proyectos, ImagenProyecto, VideoProyecto


class ImagenProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProyecto
        fields = ["proyecto", "imagen", "descripcion", "fecha_creacion"]


class VideoProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProyecto
        fields = ["proyecto", "video", "descripcion", "fecha_creacion"]


class ProyectosSerializer(serializers.ModelSerializer):
    imagenes = ImagenProyectoSerializer(many=True, read_only=True)
    videos_archivo = VideoProyectoSerializer(many=True, read_only=True)

    class Meta:
        model = Proyectos
        fields = ["id", "titulo", "descripcion", "link",
                  "imagen", "tecnologias", "videos", "fecha_creacion", "imagenes", "videos_archivo"]
