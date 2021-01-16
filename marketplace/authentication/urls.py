from authentication.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', RegisterView, basename='user')
router.register(r'login', LoginView, basename='login')
router.register(r'logout', LogOutView, basename='logout')
router.register(r'change_password', ChangePasswordView, basename='change')
router.register(r'updateuserprofile', UpdateUserProfileView, basename='updateprofile')


urlpatterns = router.urls
