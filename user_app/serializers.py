from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Custom user model serializer"""

    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(required=False)
    username = serializers.CharField(read_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        try:
            user = instance
            new_password = validated_data.pop('password')
            old_password = validated_data.pop('old_password')
            if user.check_password(old_password):
                user.set_password(new_password)
            else:
                raise Exception('Old password is incorrect')
            user.save()
        except Exception as err:
            raise serializers.ValidationError({'message': err})
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'username', 'email', 'password', 'old_password']
