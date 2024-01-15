from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Custom user model serializer"""
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']
