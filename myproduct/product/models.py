from ast import Delete
from django.db import models

# Create your models here.



class CategoryTable(models.Model):
    category_name=models.CharField(max_length=50)
    category_detail=models.CharField(max_length=100)


class ProductTable(models.Model):
    productrelation=models.ManyToManyField(CategoryTable)
    prod_name=models.CharField(max_length=50)
    pro_detail=models.CharField(max_length=100)
    price=models.IntegerField()

    def categorised_by(self):
        return self.productrelation

