from rest_framework import serializers
from rest_framework.views import APIView
from django1.models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoginInfoSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)
    pwd = serializers.CharField(required=True, max_length=16)
    class Meta:
        model = User
        fields = (
            'uid',
            'pwd'
        )
class RegisterInfoSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)
    pwd = serializers.CharField(required=True, max_length=16)
    mail = serializers.EmailField(required=True, max_length=32)
    class Meta:
        model = User
        fields = (
            'uid',
            'mail',
            'pwd'
        )

