from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core_app.views import *

# test that the view obtained by 'reversing' the url given 
# in each step corresponds to the expected one 
class TestURLs(SimpleTestCase):

    def test_internship_url(self):
        url = reverse('internship')
        self.assertEquals(resolve(url).func, internship)

    def test_student_url(self):
        url = reverse('student')
        self.assertEquals(resolve(url).func, student)

    def test_submit_student_url(self):
        url = reverse('submit-student')
        self.assertEquals(resolve(url).func, submit_student)

    def test_submit_internship_url(self):
        url = reverse('submit-internship')
        self.assertEquals(resolve(url).func, submit_internship)

    def test_clean_data_url(self):
        url = reverse('clean-data')
        self.assertEquals(resolve(url).func, clean_data)

    def test_matching_url(self):
        url = reverse('matching')
        self.assertEquals(resolve(url).func, matching_view)

    def test_sysadmin_url(self):
        url = reverse('sysadmin')
        self.assertEquals(resolve(url).func, admin_page) 
        
    def test_logadmin_url(self):
        url = reverse('logadmin')
        self.assertEquals(resolve(url).func, log_admin)    
        
    def test_run_matching_algorithm_url(self):
        url = reverse('run_matching_algorithm')
        self.assertEquals(resolve(url).func, run_matching_algorithm)  
    
    def test_send_email_url(self):
        url = reverse('send-email')
        self.assertEquals(resolve(url).func, send_email) 
    
    def test_login_user_url(self):
            url = reverse('login_user')
            self.assertEquals(resolve(url).func, login_user) 
    
    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user) 

    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)        