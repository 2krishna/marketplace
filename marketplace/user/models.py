from django.db import models
from marketapp.models import *

class UserRegister(models.Model):
    user=models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile=models.CharField(max_length=50,null=True,blank=True)
    language=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.user.email



class UserOtp(models.Model):
    phone = models.CharField(max_length=250, null=True, blank=True)
    otp = models.CharField(max_length=250, null=True, blank=True)
    generate_time = models.DateTimeField(default=datetime.now)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
