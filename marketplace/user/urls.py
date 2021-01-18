from user.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_regisert', UserRegisterView, basename='userregisert')
router.register(r'user_login', LoginView, basename='user_login')
router.register(r'otp_verify', Verify_otp_Mobile_use, basename='otp_verify')

urlpatterns = router.urls
