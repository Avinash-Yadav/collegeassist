from django.db import models

# Create your models here.
class Department(models.Model):
    name    = models.CharField(max_length = 50,blank=False,null=False)
    acronym = models.CharField(max_length=10,blank=False,null=False)

class Course(models.Model):
    name    = models.CharField(max_length=50,blank=False,null=False)
    dept    = models.ForeignKey('Department')
    