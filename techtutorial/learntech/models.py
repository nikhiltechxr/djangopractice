from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class tutoriallist(models.Model):
    tutorial_name=models.CharField(max_length=50)
    tutorial_catgry=models.CharField(max_length=50)
    tutorial_price=models.IntegerField(default=0)
    tutorial_detail=models.CharField(max_length=200)
    tutorialthmbnil=models.ImageField(upload_to="learntech/image", default='')

    def __str__(self):
       return self.tutorial_name