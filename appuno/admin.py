from django.contrib import admin
from .models import Registro


class AdminRegistro(admin.ModelAdmin):
    list_display = ["pregunta", "respuesta", "fecha_de_creacion" ]
admin.site.register(Registro, AdminRegistro)

# Register your models here.
