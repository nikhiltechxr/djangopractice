import email
from enum import unique
from itertools import product
from operator import truediv
from pickle import TRUE
from shutil import _ntuple_diskusage
from traceback import print_exception
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from .managers import CustomizeUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


    

class MyRegisterUser(AbstractUser):
    user_name=None
    user_password=models.CharField(max_length=10, null=True, blank=TRUE)
    email=models.EmailField(max_length=50,null=True, blank=True, unique=TRUE)
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True, blank=True)
    objects=CustomizeUser()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]



class Product(models.Model):
    myregisteruser=models.ForeignKey(MyRegisterUser, on_delete=models.CASCADE)
    title=models.CharField(max_length=50,null=True, blank=True)
    description=models.CharField(max_length=200,null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    