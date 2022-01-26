from email.policy import default
from django.db import models
from django.forms import NullBooleanField


class Mystudent(models.Model):
    name=models.CharField(max_length=50, null=True)
    scholornum=models.IntegerField(default=0, )

class Myteacher(models.Model):
    name=models.CharField(max_length=50)
    serialno=models.IntegerField(default=0)
    