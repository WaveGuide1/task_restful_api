from django.shortcuts import render
from rest_framework import viewsets
from .models import House
from .serializer import HouseSerializer
from .permission import IsManager

# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsManager]

