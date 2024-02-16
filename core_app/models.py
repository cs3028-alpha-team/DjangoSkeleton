from django.db import models

# Create your models here.

#student model
class Student(models.Model):
    studentID = models.BigAutoField(primary_key=True)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    #field =
    #mode_study =
    #study_pattern =
    experience =models.CharField(max_length=300)


# view as first name last name and not as an object
    def __str__(self):
        return self.first_name + self.last_name

#internship model
class Internship(models.Model):
    intershipID = models.BigAutoField(primary_key=True)
    organisation = models.CharField(max_length=50)
    job_role = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200)
    #work_mode = 
    #field = 
    num_candidates = models.IntegerField()
    #work_pattern = 
# view as organisation and job role and not as an object
    def __str__(self):
        return self.organisation + self.job_role