from django.contrib import admin
from .models import Comensal

# Register your models here.
@admin.register(Comensal)
class ComensalAdmin(admin.ModelAdmin):
    list_display = ('nombre_comensal', "apellido_comensal", "dni")
