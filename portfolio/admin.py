from django.contrib import admin
from .models import (
    Proyectos,
    ImagenProyecto,
    VideoProyecto,
    Certifications,
    MyWorkExperience,
    Technology,
)


class ImagenProyectoInline(admin.TabularInline):
    model = ImagenProyecto
    extra = 1


class VideoProyectoInline(admin.TabularInline):
    model = VideoProyecto
    extra = 1


@admin.register(Proyectos)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_creacion",
                    "tecnologias_list", "link", "repositorio")
    search_fields = ("titulo", "descripcion", "tecnologias__nombre")
    list_filter = ("fecha_creacion",)
    filter_horizontal = ("tecnologias",)
    inlines = [ImagenProyectoInline, VideoProyectoInline]
    fieldsets = (
        ("Información General", {
            "fields": ("titulo", "descripcion", "fecha_creacion")
        }),
        ("Enlaces", {
            "fields": ("link", "repositorio")
        }),
        ("Multimedia", {
            "fields": ("imagen", "videos")
        }),
        ("Tecnologías", {
            "fields": ("tecnologias",)
        }),
    )
    readonly_fields = ("fecha_creacion",)

    def tecnologias_list(self, obj):
        return ", ".join(t.nombre for t in obj.tecnologias.all())


@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha", "tecnologias_list")
    search_fields = ("titulo", "descripcion", "tecnologias__nombre")
    list_filter = ("fecha",)
    filter_horizontal = ("tecnologias",)

    def tecnologias_list(self, obj):
        return ", ".join(t.nombre for t in obj.tecnologias.all())


@admin.register(MyWorkExperience)
class MyWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("titulo", "puesto", "fecha_years", "tecnologias_list")
    search_fields = ("titulo", "puesto", "descripcion", "tecnologias__nombre")
    filter_horizontal = ("tecnologias",)

    def tecnologias_list(self, obj):
        return ", ".join(t.nombre for t in obj.tecnologias.all())


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("nombre", "link")
    search_fields = ("nombre",)
