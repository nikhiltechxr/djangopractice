from email.policy import default
from unicodedata import name
from django.db import models
from django.forms import NullBooleanField
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _



class Mystudent(models.Model):
    name=models.CharField(max_length=50, null=True)
    scholornum=models.IntegerField(default=0, )

class Myteacher(models.Model):
    name=models.CharField(max_length=50)
    serialno=models.IntegerField(default=0)
    
class MyRegisterUser(AbstractUser):
    
    email=models.EmailField(max_length=50, unique=True,blank=True, null=True)
    name=models.CharField(max_length=50,blank=True, null=True)
    mobile=models.IntegerField(null=True, blank=True)
    is_verified=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]