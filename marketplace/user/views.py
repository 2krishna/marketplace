from django.shortcuts import render
from marketapp.models import *
from rest_framework.response import Response
from rest_framework import viewsets,status
from django.contrib.auth import authenticate
import traceback
import random
from django.utils.timezone import now, timedelta
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
import traceback
from user.models import *
import re 
from marketapp.views import send_otp_in_mobile

# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def email_validation(value):
    emailvalue=re.compile("[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}")
    return emailvalue.match(value)
def mobile_no_validation(value):
    patterns=re.compile("(0/91)?[6-9][0-9]{9}")
    return patterns.match(value)



class UserRegisterView(viewsets.ViewSet):
    def create(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            mobile=request.data.get('mobile')
            email_exist=MyUser.objects.filter(email=email)
            mobile_exist=UserRegister.objects.filter(mobile=mobile)
            if email_exist:
                raise Exception("Email Id already exist ")
            
            if mobile_exist:
                raise Exception("Mobile no already exist please enter the valid Mobile no")
            if not mobile_no_validation(mobile):
                raise Exception('Please valid mobile no just like a 6354655.... to 12 digit  valid mobile no')
            if not email_validation(email):
                raise Exception('please enter the valid email id ')
            user_obj=MyUser()
            user_obj.myuser_choice='U'
            user_obj.email=email
            user_obj.set_password(password)
            user_obj.is_active=True
            user_obj.save()
            user_register_object=UserRegister() 
            user_register_object.user=user_obj
            user_register_object.mobile=mobile
            user_register_object.save()
            app = Application.objects.create(user=user_obj)
            token = generate_token()
            refresh_token = generate_token()
            expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
            scope = "read write"
            access_token = AccessToken.objects.create(user=user_obj,
                                                application=app,
                                                expires=expires,
                                                token=token,
                                                scope=scope,
                                                )
            print("access token ------->", access_token)
            RefreshToken.objects.create(user=user_obj,
                                        application=app,
                                        token=refresh_token,
                                        access_token=access_token
                                        )
            response = {
                'access_token': access_token.token,
                'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
                'token_type': 'Bearer',
                'refresh_token': access_token.refresh_token.token,
                'client_id': app.client_id,
                'client_secret': app.client_secret
                }
            return Response({'response':'creaded successfully'})
    
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
  



class LoginView(viewsets.ViewSet):
    # permission_classes = [TokenHasReadWriteScope]
    def create(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            
            if email and password:
                myuser=authenticate(email=email,password=password)

                if myuser is not None and myuser.myuser_choice=='U' :
                    app = Application.objects.get(user=myuser)  
                    # token = get_access_token(user)
                    token = generate_token()
                    refresh_token = generate_token()
                    expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
                    scope = "read write"
                    access_token = AccessToken.objects.create(user=myuser,
                                                            application=app,
                                                            expires=expires,
                                                            token=token,
                                                            scope=scope,
                                                            )
                        
                    RefreshToken.objects.create(user=myuser,
                                            application=app,
                                            token=refresh_token,
                                            access_token=access_token
                                            )
                    response = {
                        # 'name':user.username,
                        'access_token': access_token.token,
                        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,                    'token_type': 'Bearer',
                        'refresh_token': access_token.refresh_token.token,
                        'client_id': app.client_id,
                        'client_secret': app.client_secret
                        }
                    
                    return Response({'response':response,'message':True,'status':status.HTTP_200_OK})
                else:
                    email=MyUser.objects.filter(email=email)
                    if not email:
                        return Response({'response':'email is not valid plz enter valid email id','message':False,'status':status.HTTP_200_OK})
                    password=MyUser.objects.filter(password=password)
                    if not password:
                        return Response({'response':'password is not valid plz enter valid paasword id','message':False,'status':status.HTTP_200_OK})

            else:
                phone=request.data.get('phone')
                otp=random.randint(100000,999999)
                contactobject= UserOtp()
                contactobject.phone=phone
                contactobject.otp=otp
                contactobject.save()
                send_otp_in_mobile(phone,otp)
                return Response({'response':"your otp is"+ otp})

        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
  
class Verify_otp_Mobile_use(viewsets.ViewSet):
    def create(self,request):
        try: 
            otp=request.data.get('otp')
            otp_obj_check = UserOtp.objects.filter(otp=otp)

            if otp_obj_check:
                userotpobject=UserOtp.objects.filter(otp=otp).order_by('-id')[0]
                import datetime
                current_date_time = datetime.datetime.now()
                print(current_date_time)
                otp_generated_time = userotpobject.generate_time
                print(otp_generated_time)
                time_difference = current_date_time-otp_generated_time.replace(tzinfo=None)
                if time_difference.seconds > 180:
                    raise Exception(" yor otp is  experied")
            else:
                raise Exception("your otp is invalid please enter the valid otp")

            data={
                'mobile':userotpobject.phone,
                'otp':userotpobject.otp,
            }
       
            return Response({'response':'you are succesfull and also','data':data,'message':False,'status':status.HTTP_200_OK})

        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
  