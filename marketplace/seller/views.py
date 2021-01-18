from django.shortcuts import render
from rest_framework import viewsets
from marketapp.views import *
from seller.models import *
from rest_framework.response import Response
import traceback
from rest_framework import status
import datetime

class SellerRegisterViewSet(viewsets.ViewSet):
    def create(self,request):
        try:
            myuserobject=MyUser()
        
            myuserobject.email=request.data.get('email')
            myuserobject.myuser_choice='S'
            myuserobject.set_password(request.data.get('password'))
            myuserobject.save()
            seller_object=SellerRegister()
            seller_object.first_name=request.data.get('first_name')
            seller_object.middile_name=request.data.get('middile_name')
            seller_object.last_name=request.data.get('last_name')
            seller_object.designation=request.data.get('designation')
            seller_object.business_of_name=request.data.get('business_of_name')
            seller_object.mobile_no=request.data.get('mobile_no')
            seller_object.phone=request.data.get('phone')
            seller_object.date_corporation=request.data.get('date_corporation')
            seller_object.myuser=myuserobject
            seller_object.save()
            generate_access_token(myuserobject)
            return Response({'response':"Seller regisration Succesfull ",'message':True,'status':status.HTTP_200_OK})
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})

    def retrieve(self, request, pk=None):
        Sell


class Seller_Login(viewsets.ViewSet):
    # permission_classes = [TokenHasReadWriteScope]
    def create(self,request):
        try:
            email=request.data.get('email')
            password=request.data.get('password')
            
            if email and password:
                myuser=authenticate(email=email,password=password)

                if myuser is not None and myuser.myuser_choice=='S' :
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
                contactobject= SellerOtp()
                contactobject.phone=phone
                contactobject.otp=otp
                contactobject.save()
                send_otp_in_mobile(phone,otp)
                return Response({'response':'otp is send to your phone is'+ otp})

        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
  
class Seller_VerifyOtp(viewsets.ViewSet):
    def create(self,request):

        try:
            otp=request.data.get('otp')
            seller_object=SellerOtp.objects.filter(otp=otp)
            if seller_object:
                seller_object_check=SellerOtp.objects.filter(otp=otp).order_by('-id')[0]
                currentrime=datetime.datetime.now()
                print('currentrime,',currentrime,)
                otp_generatetime=seller_object_check.generate_time
                time_difference=currentrime-otp_generatetime.replace(tzinfo=None)
                if time_difference.seconds > 150:
                    raise Exception('your otp is expired')
                data={
                    'seller_phone':seller_object_check.phone,
                    'otp':seller_object_check.otp
                }
                return Response({'response':'you are login successfull your phone and otp is ' + data})
            else:
                raise Exception('your otp is not valid  please enter the valid otp')
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})



class Company_Address_ViewSet(viewsets.ViewSet):
    def create(self,request):
        try:
            company_address_object=Company_Address(user=request.seller_register.seller_register_myuser.get())
            return Response({'response':"created successfull"})
        
        except Exception as error:
            traceback.print_exc()
            return Response({'response':str(error),'message':False,'status':status.HTTP_200_OK})
