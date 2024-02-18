from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    pass

class TestTemplatesContents(TestCase):

    def test_homepage_template_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "<h2>Welcome to SkillPilot</h2>")
        self.assertNotContains(response, "This string should not be in the homepage!")

    # ensures the internship template contains the internship registration form
    def test_internship_template_contents(self):
        response = self.client.get(reverse('internship'))
        self.assertContains(response, '<input type="submit" value="Complete application" id="submit" />')
        self.assertNotContains(response, "This string should not be in the internship page!")

    # ensures the student template contains the student registration form
    def test_student_template_contents(self):
        response = self.client.get(reverse('student'))
        self.assertContains(response, '<input type="submit" value="Complete application" id="submit2" />')
        self.assertNotContains(response, "This string should not be in the internship page!")

    # ensures the sysadmin template contains the form to trigger gale-shapley algorithm
    def test_sysadmin_page_contains_algorithm_trigger(self):
        sysadmin_res = self.client.get(reverse('sysadmin'))
        algorithm_form_html = '<button type="submit">Run Matching Algorithm</button>'
        self.assertContains(sysadmin_res, algorithm_form_html)