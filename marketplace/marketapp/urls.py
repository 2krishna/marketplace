
from rest_framework.routers import DefaultRouter
from marketapp.views import *
router = DefaultRouter()
router.register(r'register', RegisterView, basename='user')
router.register(r'login', LoginView, basename='login')
router.register(r'logout', LogOutView, basename='logout')
router.register(r'change_password', ChangePasswordView, basename='change')
router.register(r'updateuserprofile', UpdateUserProfileView, basename='updateprofile')
router.register(r'generate_otp', SendContactUsOTPViewSet, basename='generate_otp')
router.register(r'verify_otp', VerifiedotpView, basename='verifyotp')
urlpatterns = router.urls
