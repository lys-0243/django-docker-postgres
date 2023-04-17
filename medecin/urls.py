from django.urls import path
from medecin import views

urlpatterns = [
    path('medecins/', views.MedecinAPIView.as_view()),
    path('medecins/<int:pk>', views.MedecinAPIView.as_view()),
    path('medecins/<slug:slug>', views.search),

]