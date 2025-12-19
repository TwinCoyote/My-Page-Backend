from django.contrib import admin
from .models import Proyectos, ImagenProyecto, VideoProyecto


class ImagenProyectoInline(admin.TabularInline):
    model = ImagenProyecto
    extra = 1


class VideoProyectoInline(admin.TabularInline):
    model = VideoProyecto
    extra = 1


@admin.register(Proyectos)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_creacion")
    search_fields = ("titulo", "tecnologias")
    list_filter = ("fecha_creacion",)
    inlines = [ImagenProyectoInline, VideoProyectoInline]
