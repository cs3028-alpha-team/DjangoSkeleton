from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core_app.views import *

# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('internship', views.internship, name='internship'),
#     path('student', views.student, name='student'),
#     path('submit-student', views.submit_student, name='submit-student'),
#     path('submit-internship', views.submit_internship, name='submit-internship'),
#     path('clean-data', views.clean_data, name='clean-data'),
#     path('matching', views.matching_view, name='matching'),
#     path('sysadmin', views.admin_page, name='sysadmin')
# ]

class TestURLs(SimpleTestCase):

    # ERROR WHEN TESTING URL FOR HOMEPAGE, MAYBE THERE IS A SPECIAL WAY TO TEST THIS VIEW?

    def test_internship_url_is_resolved(self):
        url = reverse('internship')
        self.assertEquals(resolve(url).func, internship)

    # copy above test for all app urls

    # TODO