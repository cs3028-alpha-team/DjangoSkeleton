from django.urls import path
from dashboard import views as dashboard
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('internship', views.internship, name='internship'),
    path('student', views.student, name='student'),
    path('submit-student', views.submit_student, name='submit-student'),
    path('submit-internship', views.submit_internship, name='submit-internship'),
    path('clean-data', views.clean_data, name='clean-data'),
    path('matching', views.matching_view, name='matching'),
    path('sysadmin', views.admin_page, name='sysadmin'),
    path('logadmin/', views.log_admin, name ='logadmin'),
    path('run_matching_algorithm', views.run_matching_algorithm, name='run_matching_algorithm'),
    path('send-email', views.send_email, name="send-email"),
    path('login_user', views.login_user, name = "login_user"),
    path('logout', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

