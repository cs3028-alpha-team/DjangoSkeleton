from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

#student model
class Student(models.Model):

    #enum for mode 
    class mode(models.TextChoices): 
        ONLINE = 'online', _('Online')
        IN_PERSON = 'in-person', _('In-Person')
        HYBRID = 'hybrid', _('Hybrid')


    #enum for pattern
    class pattern(models.TextChoices):
        FULL_TIME = 'FT', _('Full-Time')
        PART_TIME = 'PT', _('Part-Time')


    studentID = models.BigAutoField(primary_key=True)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    field = models.CharField(max_length=100, default = 'Nursing') 
    mode_study = models.CharField(max_length=10, choices= mode.choices, default =mode.IN_PERSON )
    study_pattern = models.CharField(max_length = 2, choices= pattern.choices, default = pattern.FULL_TIME)
    experience =models.CharField(max_length=300)


# view as first name last name and not as an object
    def __str__(self):
        return self.first_name + self.last_name

#internship model
class Internship(models.Model):


    #enum for mode 
    class mode(models.TextChoices): 
        ONLINE = 'online', _('Online')
        IN_PERSON = 'in-person', _('In-Person')
        HYBRID = 'hybrid', _('Hybrid')

    #enum for pattern
    class pattern(models.TextChoices):
        FULL_TIME = 'FT', _('Full-Time')
        PART_TIME = 'PT', _('Part-Time')


    intershipID = models.BigAutoField(primary_key=True)
    organisation = models.CharField(max_length=50)
    job_role = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=200)
    work_mode =  models.CharField(max_length=10, choices= mode.choices, default =mode.IN_PERSON )
    field = models.CharField(max_length=100, default='Nursing') 
    num_candidates = models.IntegerField()
    work_pattern = models.CharField(max_length = 2, choices= pattern.choices, default = pattern.FULL_TIME)

# view as organisation and job role and not as an object
    def __str__(self):
        return self.organisation + self.job_role
