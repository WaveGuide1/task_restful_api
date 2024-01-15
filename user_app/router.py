from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = 'user_app'

router = DefaultRouter()

router.register('profile', UserViewSet)
