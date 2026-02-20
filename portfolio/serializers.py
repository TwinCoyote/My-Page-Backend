# pylint: disable=C0115,C0114


from rest_framework import serializers
from .models import Proyectos, ImagenProyecto, VideoProyecto, Certifications, MyWorkExperience, Technology


class TechnologySerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Technology
        fields = ["id", "nombre", "link", "imagen", "imagen_url"]

    def get_imagen_url(self, obj):
        return getattr(obj.imagen, "url", None)

    def get_imagen(self, obj):  # Devuelve directamente la URL en el campo principal
        return getattr(obj.imagen, "url", None)


class ImagenProyectoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = ImagenProyecto
        fields = ["proyecto", "imagen", "imagen_url",
                  "descripcion", "fecha_creacion"]

    def get_imagen_url(self, obj):
        return getattr(obj.imagen, "url", None)

    def get_imagen(self, obj):
        return getattr(obj.imagen, "url", None)


class VideoProyectoSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = VideoProyecto
        fields = ["proyecto", "video", "video_url",
                  "descripcion", "fecha_creacion"]

    def get_video_url(self, obj):
        return getattr(obj.video, "url", None)

    def get_video(self, obj):
        return getattr(obj.video, "url", None)


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
    imagen = serializers.SerializerMethodField()
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Proyectos
        fields = [
            "id",
            "titulo",
            "descripcion",
            "link",
            "imagen",
            "imagen_url",
            "tecnologias",
            "tecnologias_ids",
            "videos",
            "fecha_creacion",
            "imagenes",
            "videos_archivo",
        ]

    def get_imagen_url(self, obj):
        return getattr(obj.imagen, "url", None)

    def get_imagen(self, obj):
        return getattr(obj.imagen, "url", None)


class CertificationsSerializer(serializers.ModelSerializer):
    tecnologias = TechnologySerializer(many=True, read_only=True)
    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        source="tecnologias",
        many=True,
        queryset=Technology.objects.all(),
        write_only=True,
        required=False,
    )
    imagen = serializers.SerializerMethodField()
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Certifications
        fields = ["id", "titulo", "descripcion",
                  "tecnologias", "tecnologias_ids", "imagen", "imagen_url", "fecha"]

    def get_imagen_url(self, obj):
        return getattr(obj.imagen, "url", None)

    def get_imagen(self, obj):
        return getattr(obj.imagen, "url", None)


class MyWorkExperienceSerializer(serializers.ModelSerializer):
    tecnologias = TechnologySerializer(many=True, read_only=True)
    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        source="tecnologias",
        many=True,
        queryset=Technology.objects.all(),
        write_only=True,
        required=False,
    )
    logo = serializers.SerializerMethodField()
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = MyWorkExperience
        fields = [
            "id",
            "titulo",
            "puesto",
            "fecha_years",
            "descripcion",
            "logo",
            "logo_url",
            "tecnologias",
            "tecnologias_ids",
        ]

    def get_logo_url(self, obj):
        return getattr(obj.logo, "url", None)

    def get_logo(self, obj):
        return getattr(obj.logo, "url", None)
