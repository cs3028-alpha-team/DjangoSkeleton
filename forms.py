from django import forms
from .models import Student, Internship
from django.forms import ModelForm

class InternshipForm(ModelForm):
    class Meta:
        model = Internship
        fields = ['organisation', 'job_role', 'email_address', 'num_candidates']
            
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'experience']
    