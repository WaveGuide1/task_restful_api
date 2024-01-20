from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Custom user model serializer"""

    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(required=False)
    username = serializers.CharField(read_only=True)

    def validate(self, attrs):
        request_method = self.context['request'].method
        password = attrs.get('password', None)
        if request_method == 'POST':
            if password is None:
                raise serializers.ValidationError({'message': 'Provide a password'})
        elif request_method == 'PUT' or request_method == 'PATCH':
            old_password = attrs.get('old_password', None)
            if password is not None and old_password is None:
                raise serializers.ValidationError({'message': 'Provide old password'})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        try:
            user = instance
            if 'password' in validated_data:
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
