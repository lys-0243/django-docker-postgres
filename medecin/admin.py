from django.contrib import admin
from .models import Medecin
# Register your models here.

class MedecinAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medecin, MedecinAdmin)