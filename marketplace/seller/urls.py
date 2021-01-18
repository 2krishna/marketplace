from seller.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('seller_registration',SellerRegisterViewSet,basename='seller_registrations')
router.register('seller_login',Seller_Login,basename='seller_login')
router.register(r'seller_verifyotp', Seller_VerifyOtp, basename='seller_verifyotp')
router.register(r'company_address', Company_Address_ViewSet, basename='company_address')

urlpatterns=router.urls