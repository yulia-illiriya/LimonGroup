from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = "__all__"
    read_only_fields = ('full_name',)
    extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }