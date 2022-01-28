from django.forms import fields, models
from .models import ProductTable,CategoryTable
from rest_framework import serializers


class ProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductTable
        fields= '__all__'

class CategoryTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryTable
        fields='__all__'