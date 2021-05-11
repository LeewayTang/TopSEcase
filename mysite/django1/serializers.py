from rest_framework import serializers
from rest_framework.views import APIView
from django1.models import *


class UserInfoSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)
    uid = serializers.CharField(max_length=16)
    pwd = serializers.CharField(max_length=16)
    sex = serializers.IntegerField(default=0)
    avatar = serializers.CharField(max_length=2048)
    isTeacher = serializers.BooleanField(default=False)
    circle = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            'token',
            'uid',
            'pwd',
            'sex',
            'avatar',
            'isTeacher',
            'circle'
        )


class CircleInfoSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True, max_length=16)
    name = serializers.CharField(required=True, max_length=32)
    token = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = Circle
        fields = (
            'type',
            'name',
            'token'
        )


class LoginInfoSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)
    pwd = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'uid',
            'pwd'
        )


class UidInfoSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'uid',
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


class AddCircleComment(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)
    circle = serializers.IntegerField(required=True)
    context = serializers.CharField(required=True, max_length=256)

    class Meta:
        model = Discuss
        fields = (
            'token',
            'circle',
            'context'
        )


class GetCircleComment(serializers.ModelSerializer):
    circle = serializers.IntegerField(required=True)

    class Meta:
        model = Discuss
        fields = (
            'circle',
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
