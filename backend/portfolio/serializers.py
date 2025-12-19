# pylint: disable=C0115,C0114


from rest_framework import serializers
from .models import Proyectos, ImagenProyecto, VideoProyecto, Certifications, MyWorkExperience, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["id", "nombre", "link", "imagen"]


class ImagenProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProyecto
        fields = ["proyecto", "imagen", "descripcion", "fecha_creacion"]


class VideoProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProyecto
        fields = ["proyecto", "video", "descripcion", "fecha_creacion"]


class ProyectosSerializer(serializers.ModelSerializer):
    tecnologias = TechnologySerializer(many=True, read_only=True)
    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        source="tecnologias",
        many=True,
        queryset=Technology.objects.all(),
        write_only=True,
        required=False,
    )
    imagenes = ImagenProyectoSerializer(many=True, read_only=True)
    videos_archivo = VideoProyectoSerializer(many=True, read_only=True)

    class Meta:
        model = Proyectos
        fields = [
            "id",
            "titulo",
            "descripcion",
            "link",
            "imagen",
            "tecnologias",
            "tecnologias_ids",
            "videos",
            "fecha_creacion",
            "imagenes",
            "videos_archivo",
        ]


class CertificationsSerializer(serializers.ModelSerializer):
    tecnologias = TechnologySerializer(many=True, read_only=True)
    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        source="tecnologias",
        many=True,
        queryset=Technology.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Certifications
        fields = ["id", "titulo", "descripcion",
                  "tecnologias", "tecnologias_ids", "imagen", "fecha"]


class MyWorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWorkExperience
        fields = ["titulo", "puesto", "fecha_years", "descripcion", "logo"]
