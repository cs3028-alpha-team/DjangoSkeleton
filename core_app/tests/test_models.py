from django.test import TestCase
from ..models import Student, Internship

# #internship model
# class Internships(models.Model):
#     intershipID = models.BigAutoField(primary_key=True)
#     organisation = models.CharField(max_length=50)
#     job_role = models.CharField(max_length=50)
#     email_address = models.EmailField(max_length=200)
#     #work_mode = 
#     #field = 
#     num_candidates = models.IntegerField()
#     #work_pattern = 
# # view as organisation and job role and not as an object
#     def __str__(self):
#         return self.organisation + self.job_role

class TestStudentModel(TestCase):

    def setUp(self):
        self.student1 = Student.objects.create(
            studentID=1234, 
            first_name="John", 
            last_name="Deez", 
            experience="nursing"
        )

    def test_stringify_method(self):
        self.assertEquals("JohnDeez", str(self.student1))


class TestInternshipModel(TestCase):

    def setUp(self):
        self.internship1 = Internship.objects.create(
            intershipID = 939,
            organisation = "GSK",
            job_role = "Nurse Trainee",
            email_address = "GSK@pharma.com",
            num_candidates = 3,
        )

    def test_stringify_method(self):
        self.assertEquals("GSKNurse Trainee", str(self.internship1))