from django.contrib import admin
from .models import Clinique
# Register your models here.

class CliniqueAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clinique, CliniqueAdmin)