from django.db import models

# Create your models here.
class Registro(models.Model):
    pregunta = models.CharField(max_length=300)
    respuesta = models.TextField()
    fecha_de_creacion = models.DateField(auto_now_add=True)