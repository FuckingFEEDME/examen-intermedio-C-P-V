from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre_mesero = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
    dni = models.IntegerField(max_length=8, default='00000000')