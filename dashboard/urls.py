
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('candidate-histogram/', views.candidate_histogram, name='candidate_histogram'),
    
]
