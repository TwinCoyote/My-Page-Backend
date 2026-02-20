# pylint: disable=C0114, C0301, E0307, E1101
from django.db import models
from cloudinary.models import CloudinaryField


class Technology(models.Model):
    """Tecnología disponible para asociar en proyectos y certificaciones"""

    nombre = models.CharField(
        verbose_name="Nombre de la tecnología", max_length=50, unique=True)
    link = models.URLField(verbose_name="Link de referencia", blank=True)
    imagen = CloudinaryField(
        verbose_name="Logo de la tecnología",
        folder="proyectos/tecnologias",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre


class Proyectos(models.Model):
    """Class representing a person"""
    titulo = models.CharField(
        verbose_name="Título del proyecto", max_length=50)
    descripcion = models.TextField(verbose_name="Descripción")
    repositorio = models.URLField(
        verbose_name="Links del repositorio", blank=True)
    tecnologias = models.ManyToManyField(
        Technology,
        related_name="proyectos",
        verbose_name="Tecnologías usadas",
        blank=True,
    )
    link = models.URLField(verbose_name="Links del proyecto", blank=True)
    imagen = CloudinaryField(
        verbose_name="Imagen del proyecto", folder="proyectos/images", blank=True, null=True)
    videos = models.URLField(verbose_name="Video del proyecto", blank=True)
    fecha_creacion = models.DateField(
        verbose_name="Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.titulo


class ImagenProyecto(models.Model):
    """Clase para las Imagenes Extra"""
    proyecto = models.ForeignKey(
        Proyectos, related_name="imagenes", on_delete=models.CASCADE)
    imagen = CloudinaryField(
        verbose_name="Imagen del proyecto", folder="proyectos/images")
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=150, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.proyecto.titulo}"


class VideoProyecto(models.Model):
    """Clase para los videos Extra"""
    proyecto = models.ForeignKey(
        Proyectos, related_name="videos_archivo", on_delete=models.CASCADE)
    video = CloudinaryField(
        verbose_name="Video del proyecto", folder="proyectos/videos", resource_type="video", blank=True, null=True)
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=150, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video de {self.proyecto.titulo}"


class Certifications(models.Model):
    """Clase para las Certifiaciones"""
    titulo = models.CharField(
        verbose_name="Título de la certificacion", max_length=50)
    descripcion = models.TextField(verbose_name="Descripción")
    tecnologias = models.ManyToManyField(
        Technology,
        related_name="certifications",
        verbose_name="Tecnologías usadas",
        blank=True,
    )
    imagen = CloudinaryField(
        verbose_name="Imagen de la certificación", folder="proyectos/certificaciones", blank=True, null=True)
    fecha = models.DateField(
        verbose_name="Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.titulo


class MyWorkExperience(models.Model):
    """Clase para las Certifiaciones"""
    titulo = models.CharField(
        verbose_name="Título del Empleo", max_length=50)
    puesto = models.CharField(
        verbose_name="Puesto del Empleo", max_length=50)
    fecha_years = models.CharField(
        verbose_name="Fecha del proyecto ej: 2020-2025", max_length=50)
    descripcion = models.TextField(verbose_name="Descripción")
    tecnologias = models.ManyToManyField(
        Technology,
        related_name="work_experiences",
        verbose_name="Tecnologías usadas",
        blank=True,
    )
    logo = CloudinaryField(verbose_name="Logo de la empresa",
                           folder="proyectos/logos", blank=True, null=True)

    def __str__(self):
        return self.titulo


class tecnologias(models.Model):
    """Clase para las Certifiaciones"""
    nombre = models.CharField(verbose_name="Título del Empleo", max_length=50)
    link = models.CharField(verbose_name="Título del Empleo", max_length=100)
    imagen = CloudinaryField(
        verbose_name="Imagen del proyecto", folder="proyectos/certificaciones", blank=True, null=True)
