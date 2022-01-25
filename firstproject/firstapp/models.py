from concurrent.futures.process import _chain_from_iterable_of_lists
from email.policy import default
from unicodedata import name
from django.db import models

class MyStudentdata(models.Model):
    name=models.CharField(max_length=50)
    scholornumber=models.IntegerField(default=0)
    is_verified=models.BooleanField(default=True)




