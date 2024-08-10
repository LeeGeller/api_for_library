import secrets

from rest_framework import serializers

from library.models import LogService
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.token = secrets.token_hex(16)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', ]
