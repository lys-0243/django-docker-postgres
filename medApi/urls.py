
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('patient.urls')),
    path('api/', include('medecin.urls')),
    path('api/', include('clinique.urls')),
    path('api/', include('rdv.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
