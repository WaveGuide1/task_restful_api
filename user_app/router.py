from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet

app_name = 'user_app'

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('profiles', UserProfileViewSet)
