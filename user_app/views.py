from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework import viewsets, mixins
from .permission import IsUserOwner, IsProfileOwner
from .models import UserProfile

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwner,]


class UserProfileViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [IsProfileOwner,]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
