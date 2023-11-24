from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class UserAuthSerializer(serializers.ModelSerializer):
    # it was use in sign up page, there are also other field in request.data
    email = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {'allow_extra_fields': True}

    def get_username(obj):
        return obj.email

    def get_password(obj):
        return obj.password

    def get_first_name(obj):
        return obj.first_name

    def get_last_name(obj):
        return obj.last_name
