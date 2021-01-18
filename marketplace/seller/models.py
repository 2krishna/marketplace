from django.db import models
from marketapp.models import *


class SellerRegister(models.Model):
    myuser=models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name=models.CharField(max_length=50,blank=True)
    middile_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    designation=models.CharField(max_length=50,blank=True)
    business_of_name=models.CharField(max_length=50,blank=True)
    mobile_no=models.CharField(max_length=50,blank=True)
    phone=models.CharField(max_length=50,blank=True)
    
    mobile=models.CharField(max_length=50,blank=True)
    date_corporation=models.DateField()

    def __str__(self):
        return self.first_name + " "+self.business_of_name + " "+self.myuser.email


class SellerOtp(models.Model):
    phone = models.CharField(max_length=250,  blank=True)
    otp = models.CharField(max_length=250,blank=True)
    generate_time = models.DateTimeField(default=datetime.now)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # class Meta:
    #     verbose_name = "OTP Token"
    #     verbose_name_plural = "OTP Tokens"

    def __str__(self):
        return "{} - {}".format(self.phone, self.otp)


class Company_Address(models.Model):
    seller_register=models.ForeignKey(SellerRegister,on_delete=models.CASCADE,related_name='seller')
    company_name=models.CharField(max_length=256,blank=True)
    address1=models.CharField(max_length=256,blank=True)
    address12=models.CharField(max_length=256,blank=True)
    city=models.CharField(max_length=256,blank=True)
    country=models.CharField(max_length=256,blank=True)
    pincode=models.CharField(max_length=256,blank=True)
    def __str__(self):
        return self.seller_register.myuser.email + " "+self.seller_register.first_name + " "+self.city






   
