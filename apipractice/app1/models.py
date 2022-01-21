#from email.policy import default
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=2)
    father_name=models.CharField(max_length=20)