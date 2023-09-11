

# Create your models here
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import datetime
# from django.utils import timezone
import uuid
from django.core.validators import RegexValidator





#============exm=========
class Student01(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    user_name = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100,null=True)
    phone_number=models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)  # Verification status
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)  # Verification token

    def __str__(self):
        return self.user_name
    


#===================


from django.db import models

class Student02(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    # Add any other fields you need for the student table

    def __str__(self):
        return self.username




#=========================








    




class StudentUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_course = models.CharField(max_length=100)
    user_room = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, default='')
    user_mobile = models.CharField(max_length=15, default='') 
    user_start = models.TimeField()
    user_end = models.TimeField()
    current_date = models.CharField(max_length=20)
    current_day=models.CharField(max_length=20) 

    
