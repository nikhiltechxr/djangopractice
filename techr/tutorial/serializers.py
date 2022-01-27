from .models import Product, product, MyRegisterUser
from rest_framework import serializers



class MyRegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyRegisterUser
        fields='__all__'


class MyProductSerializer(serializers.ModelSerializer):
    myregisteruser=MyRegisterUserSerializer()
    class Meta:
        model=Product
        fields='__all__'