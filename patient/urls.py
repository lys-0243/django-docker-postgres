from django.urls import path
from patient import views

urlpatterns = [
    path('patients/', views.PatientAPIView.as_view()),
    path('patients/<int:pk>', views.PatientAPIView.as_view()),

]