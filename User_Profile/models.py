from django.db import models
from django.contrib import auth
# Create your models here.

class User_Profile(models.Model):
    user=models.OneToOneField(auth.models.User,on_delete=models.CASCADE,related_name='profile')
    nickname=models.CharField(max_length=100,blank=True)
