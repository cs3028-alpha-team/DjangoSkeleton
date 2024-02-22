from django.test import SimpleTestCase
from ..forms import InternshipForm, StudentForm

class TestForms(SimpleTestCase):

    # test student form submission with valid data 
    def test_student_form_valid(self):
        # instantiate a local form using the StudentForm Form
        form = StudentForm(data={
            'first_name' : 'John',
            'last_name' : 'Deez',
            'experience' : 'Nursing', 
        })

        self.assertTrue(form.is_valid())

    # test student form submission with invalid data
    def test_student_form_not_valid(self):
        # instantiate a local invalid form using the StudentForm Form
        form = StudentForm(data={})
        self.assertFalse(form.is_valid())

    # test internship form submission with valid data
    def test_internship_form_valid(self):
        # instantiate a local form using the StudentForm Form
        form = InternshipForm(data={
            'organisation' : 'NHS',
            'job_role' : 'Trainee Nurse',
            'email_address' : 'recruitment@nhs.com',
            'num_candidates' : 5,
        })

        self.assertTrue(form.is_valid())

    # test student form submission with invalid data
    def test_internship_form_not_valid(self):
        # instantiate a local invalid form using the InternshipForm Form
        form = InternshipForm(data={})
        self.assertFalse(form.is_valid())