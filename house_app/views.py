from django.shortcuts import render
from rest_framework import viewsets, status
from .models import House
from .serializers import HouseSerializer
from .permissions import IsManager
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsManager]

    @action(methods=['post'], detail=True, name='Join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.userprofile
            if user_profile.house is None:
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif user_profile in house.members.all():
                return Response({'message': 'User is already a member of this house'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'User is already a member of another house'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True, name='Leave', permission_classes=[])
    def leave(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.userprofile
            if user_profile in house.members.all():
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'User is not a member of this house'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True, name='Remove Member')
    def remove(self, request, pk=None):
        try:
            house = self.get_object()
            user_id = request.data.get('user_id', None)
            if user_id is None:
                return Response({'message': 'Action not allowed'}, status=status.HTTP_400_BAD_REQUEST)
            user_profile = User.objects.get(pk=user_id).userprofile
            house_members = house.members
            if user_profile in house_members.all():
                house_members.remove(user_profile)
                house.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'User is not a member of this group'})
        except Exception as err:
            return Response({'message': 'Invalid credential'}, status=status.HTTP_400_BAD_REQUEST)

