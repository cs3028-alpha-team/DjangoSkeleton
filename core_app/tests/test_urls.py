from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core_app.views import *

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