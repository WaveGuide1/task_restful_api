from rest_framework import routers
from .views import HouseViewSet

app_name = 'house_app'

router = routers.DefaultRouter()

router.register('houses', HouseViewSet)
