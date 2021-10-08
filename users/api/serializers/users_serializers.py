from rest_framework import serializers

from users.models import User
from users.api.serializers.general_serializers import ProfileSerializer


class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')


class UserSerializer(serializers.ModelSerializer):
    
    profile = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
            'profile_image',
            'hide_email',
            'profile',
        )