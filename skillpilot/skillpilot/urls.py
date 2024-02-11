
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('internship', views.internship, name='internship'),
    path('student', views.student, name='student'),
    path('submit-student/', views.submit_student, name='submit-student'),
    path('submit-internship/', views.submit_internship, name='submit-internship'),
    path('clean-data/', views.clean_data, name='clean-data'),
]

