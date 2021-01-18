from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



from datetime import datetime
import hashlib
# import os

# from phonenumber_field.modelfields import PhoneNumberField
# from django.template.loader import render_to_string
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from sendsms.message import SmsMessage


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    type_choice = [
        ('A', 'Admin'),
        ('U', 'User'),
        ('G', 'Guest'),
        ('S', 'Seller')
    ]
    myuser_choice = models.CharField(
        max_length=10,
        choices=type_choice
    )
    phone=models.CharField(max_length=50,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email+ " " +self.myuser_choice

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="My market place web site"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )




class ContactUsOTP(models.Model):
    phone = models.CharField(max_length=250, null=True, blank=True)
    otp = models.CharField(max_length=250, null=True, blank=True)
    generate_time = models.DateTimeField(default=datetime.now)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # class Meta:
    #     verbose_name = "OTP Token"
    #     verbose_name_plural = "OTP Tokens"

    def __str__(self):
        return "{} - {}".format(self.phone, self.otp)

    