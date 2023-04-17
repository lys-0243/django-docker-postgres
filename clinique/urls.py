from django.urls import path
from clinique import views

urlpatterns = [
    path('clinique/', views.CliniqueAPIView.as_view()),
    path('clinique/<int:pk>', views.CliniqueAPIView.as_view()),

]