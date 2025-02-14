from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['username', 'password']


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"
