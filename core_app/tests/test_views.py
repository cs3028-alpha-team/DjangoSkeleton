from django.test import TestCase, Client
from django.urls import reverse
from ..models import Student, Internship
from ..forms import StudentForm, InternshipForm
import json  

class TestViews(TestCase):
    
    # this method runs before all other in the class, recognised by Django by default
    def setUp(self):
        self.client = Client()
        self.submit_student_url = reverse('submit-student')
        self.submit_internship_url = reverse('submit-internship')
        self.matching_view_url = reverse('matching')

    # test student form submission renders the correct output - submit_student View
    def test_submit_student_POST(self):
        form = {
            'fullname' : 'John John', 
            'course' : 'Nursing', 
            'score' : 79, 
            'experience' : 'lots of nursing experience', 
            'study_mode' : 'full-time', 
            'study_pattern' : 'on-campus'
        }

        # simulate a POST request to the given url, and assert the output matches the expected
        response = self.client.post(self.submit_student_url, form)
        self.assertContains(response, 'Form submitted')

    # test student form submission rendenrs the correct output - submit_student View
    def test_submit_internship_POST(self):
        form = {
            'title' : 'Junior Doctor', 
            'company' : 'NHS', 
            'field' : 'Medicine', 
            'min_score' : 75, 
            'positions' : 5, 
        }

        # simulate a POST request to the given url, and assert the output matches the expected
        response = self.client.post(self.submit_internship_url, form)
        self.assertContains(response, 'Form submitted')

    # test the matching View
    def test_matching_view_POST(self):
        # carry out a POST and a GET request on the given url
        success_response = self.client.post(self.matching_view_url, data={})
        failure_response = self.client.get(self.matching_view_url)

        # expected output is a success response and a failure one, caused by the GET method
        self.assertContains(success_response, 'Matching process completed. Compatibility matrix saved to CSV file.')
        self.assertContains(failure_response, 'Error: POST request expected.')

    
class TestTemplatesContents(TestCase):

    def test_homepage_template_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "<h2>Welcome to SkillPilot</h2>")
        self.assertNotContains(response, "This string should not be in the homepage!")

    # tests for the run_matching_algorithm view
    def test_run_matching_algorithm_view(self):
        response = self.client.get(reverse('run_matching_algorithm'))
        self.assertContains(response, 'Matching algorithm executed successfully. Results saved to CSV file.')

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