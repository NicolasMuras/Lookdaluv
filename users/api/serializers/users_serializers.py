from rest_framework import serializers
from users.models import Account



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
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
        )