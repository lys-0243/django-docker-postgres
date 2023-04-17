from django.urls import path
from rdv import views

urlpatterns = [
    path('rdv/', views.RdvAPIView.as_view()),
    path('rdv/<int:pk>', views.RdvAPIView.as_view()),

]