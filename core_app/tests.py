from django.test import TestCase
from django.urls import reverse, resolve
from .views import homepage, internship, student

class HttpResponseTest(TestCase):
  def test_homepage_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_pagenotfound_status_code(self):
    response = self.client.get('/this-page-doesnt-exist')
    self.assertEqual(response.status_code, 404)

  # more tests here

class URLsTest(TestCase):
  def test_homepage_template_rendering(self):
    response = self.client.get(reverse('homepage'))
    self.assertTemplateUsed(response, "homepage.html")

  # more tests here

class ViewContentsTest(TestCase):
  def test_homepage_contents(self):
    response = self.client.get(reverse('homepage'))
    self.assertContains(response, "<h2>Welcome to SkillPilot</h2>")
    self.assertNotContains(response, "This string should not be in the homepage!")

  # more tests here
