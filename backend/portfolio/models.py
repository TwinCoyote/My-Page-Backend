# pylint: disable=C0114, C0301, E0307, E1101
from django.db import models


class Proyectos(models.Model):
    """Class representing a person"""
    titulo = models.CharField(
        verbose_name="Título del proyecto", max_length=50)
    descripcion = models.TextField(verbose_name="Descripción")
    tecnologias = models.CharField(
        verbose_name="Tecnologías usadas", max_length=150, help_text="Ejemplo: Python, Django, React")
    link = models.URLField(verbose_name="Links del proyecto", blank=True)
    imagen = models.ImageField(
        verbose_name="Imagen del proyecto", upload_to="proyectos/", blank=True, null=True)
    videos = models.URLField(verbose_name="Video del proyecto", blank=True)
    fecha_creacion = models.DateField(
        verbose_name="Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.titulo


class ImagenProyecto(models.Model):
    """Clase para las Imagenes Extra"""
    proyecto = models.ForeignKey(
        Proyectos, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(
        verbose_name="Imagen del proyecto", upload_to="proyectos/images/")
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=150, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagen de {self.proyecto.titulo}"


class VideoProyecto(models.Model):
    """Clase para los videos Extra"""
    proyecto = models.ForeignKey(
        Proyectos, related_name="videos_archivo", on_delete=models.CASCADE)
    video = models.FileField(verbose_name="Video del proyecto",
                             upload_to="proyectos/videos/", blank=True, null=True)
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=150, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video de {self.proyecto.titulo}"
