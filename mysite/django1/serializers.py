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


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = Token
        fields = (
            'token',
        )


class RegisterInfoSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)
    pwd = serializers.CharField(required=True, max_length=16)
    mail = serializers.EmailField(required=True, max_length=32)
    type = serializers.IntegerField(required=True)
    key = serializers.CharField(max_length=16)

    class Meta:
        model = User
        fields = (
            'uid',
            'mail',
            'pwd',
            'type',
            'key'
        )


class UploadAvatarSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)
    avatar = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = User
        fields = (
            'uid',
            'avatar'
        )


class BookISBN(serializers.ModelSerializer):
    ISBN = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = Book
        fields = (
            'ISBN',
        )


class BookInfo(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=256)
    publishTime = serializers.DateField(required=True)
    ISBN = serializers.CharField(required=True, max_length=32)
    author = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = Book
        fields = '__all__'


class BookSetTag(serializers.ModelSerializer):
    ISBN = serializers.CharField(required=True, max_length=32)
    tag = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = BookTag
        fields = (
            'ISBN',
            'tag'
        )


class CreateTag(serializers.ModelSerializer):
    tag = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = Tag
        fields = (
            'tag',
        )


class TagGetBook(serializers.ModelSerializer):
    tag = serializers.CharField(required=True, max_length=32)

    class Meta:
        model = Tag
        fields = (
            'tag',
        )
