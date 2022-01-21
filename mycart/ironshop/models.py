from distutils.command.upload import upload
from django.db import models

# Create your models here.
class playlists(models.Model):
    list_id=models.AutoField
    list_name= models.CharField(max_length=50)
    list_des=models.CharField(max_length=200)
    list_date=models.DateField()
    list_price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="ironshop/image",default="")
    

def __str__(self):
    return self.list_name