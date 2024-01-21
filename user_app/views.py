from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework import viewsets
from .permission import IsUserProfileOwner
from .models import UserProfile

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserProfileOwner]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
