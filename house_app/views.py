from django.shortcuts import render
from rest_framework import viewsets, status
from .models import House
from .serializers import HouseSerializer
from .permission import IsManager
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsManager]

    @action(methods=['post'], detail=True, name='join', permission_classes=[])
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
                return Response({'message': 'User is already a member of this house'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True, name='leave', permission_classes=[])
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
