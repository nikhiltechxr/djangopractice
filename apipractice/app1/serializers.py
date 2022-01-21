#created by me
from rest_framework import serializers
from .models import *

class mystudentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name', 'age']

