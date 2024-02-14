from django.test import TestCase
from ..models import Student, Internship

# test the methods on the Student model
class TestStudentModel(TestCase):

    # setup method recognised by django to instantiate the model to be tested
    def setUp(self):
        self.student1 = Student.objects.create(
            studentID=1234, 
            first_name="John", 
            last_name="Deez", 
            experience="nursing"
        )

    # test the __str__ method on the student model
    def test_stringify_method(self):
        self.assertEquals("JohnDeez", str(self.student1))

# test the methods on the Internship model
class TestInternshipModel(TestCase):

    # setup method recognised by django to instantiate the model to be tested
    def setUp(self):
        self.internship1 = Internship.objects.create(
            intershipID = 939,
            organisation = "GSK",
            job_role = "Nurse Trainee",
            email_address = "GSK@pharma.com",
            num_candidates = 3,
        )

    # test the __str__ method on the internship model
    def test_stringify_method(self):
        self.assertEquals("GSKNurse Trainee", str(self.internship1))