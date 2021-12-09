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



class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password'
        )

    def validate(self, attrs):

        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})

        username = attrs.get('username', '')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('Username is already in use')})

        return super().validate(attrs)

    def create(self, validated_data):

        username = validated_data.get('username', '')
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')

        user = User.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.save()

        return user