from django.db import models

# Create your models here.
class Comensal(models.Model):
    nombre_comensal = models.CharField(max_length=40)
    apellido_comensal = models.CharField(max_length=30)
    dni = models.CharField(max_length=8, default='00000000')