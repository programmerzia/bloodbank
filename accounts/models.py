from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    contact = models.CharField(max_length=13,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    zip_code = models.CharField(max_length=10,null=True,blank=True)
    area = models.CharField(max_length=100)
    photo = models.ImageField(default='default.png',upload_to='user_photo')
    blood_group = models.CharField(max_length=3,blank=True,null=True)
    designation = models.CharField(max_length=100, default="General Admin")
    def __str__(self):
        return self.first_name + " "+ self.last_name

