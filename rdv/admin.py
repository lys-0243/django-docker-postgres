from django.contrib import admin
from .models import Rendezvous
# Register your models here.

class RendezvousAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rendezvous, RendezvousAdmin)