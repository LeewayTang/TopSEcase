from rest_framework import serializers
from rest_framework.views import APIView
from django1.models import *


class UserInfoSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'token',
        )


# class CircleInfoSerializer(serializers.ModelSerializer):
#     type = serializers.CharField(required=True, max_length=16)
#     name = serializers.CharField(required=True, max_length=32)
#     token = serializers.CharField(required=True, max_length=16)
#
#     class Meta:
#         model = Circle
#         fields = (
#             'type',
#             'name',
#             'token'
#         )


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


class SetUserNameSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)
    username = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'token',
            'username'
        )


class SetUserSloganSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)
    username = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'token',
            'username'
        )


class SetUserAvatarSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'token',
        )


class UsernameSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=16)

    class Meta:
        model = User
        fields = (
            'username',
        )


class ArticleUploadSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=16)
    title = serializers.CharField(required=True, max_length=64)
    summary = serializers.CharField(required=True, max_length=256)
    content = serializers.CharField(required=True, max_length=16384)
    tag= serializers.ListField(required=True)

    class Meta:
        model = Article
        fields = (
            'token',
            'title',
            'summary',
            'content',
            'tag'
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
            'pwd',
        )


class UploadAvatarSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True, max_length=32)
    avatar = serializers.CharField(required=True, max_length=256)

    class Meta:
        model = User
        fields = (
            'token',
            'avatar'
        )


# 等待重新写
# class UploadBookSerializer(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=16)
#     file = serializers.FileField(required=True, max_length=32)
#
#     class Meta:
#         model = Book
#         fields = (
#             'ISBN',
#             'file'
#         )
#
#
# class BookISBN(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Book
#         fields = (
#             'ISBN',
#         )
#
#
# class GetBookCommentByPage(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#     page = serializers.IntegerField(required=True)
#     number = serializers.IntegerField(required=True)
#
#     class Meta:
#         model = BookComment
#         fields = (
#             'ISBN',
#             'page',
#             'number'
#         )
#
#
# class AddCircleComment(serializers.ModelSerializer):
#     token = serializers.CharField(required=True, max_length=16)
#     circle = serializers.IntegerField(required=True)
#     context = serializers.CharField(required=True, max_length=256)
#
#     class Meta:
#         model = Discuss
#         fields = (
#             'token',
#             'circle',
#             'context'
#         )
#
#
# class GetCircleComment(serializers.ModelSerializer):
#     circle = serializers.IntegerField(required=True)
#
#     class Meta:
#         model = Discuss
#         fields = (
#             'circle',
#         )
#
#
# class BookInfo(serializers.ModelSerializer):
#     name = serializers.CharField(required=True, max_length=256)
#     publishTime = serializers.DateField(required=True)
#     ISBN = serializers.CharField(required=True, max_length=32)
#     author = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# class BookSetTag(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#     tag = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = BookTag
#         fields = (
#             'ISBN',
#             'tag'
#         )
#
#
# class CreateTag(serializers.ModelSerializer):
#     tag = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Tag
#         fields = (
#             'tag',
#         )
#
#
# class GetBookComment(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = BookComment
#         fields = (
#             'ISBN',
#         )
#
#
# class AddBookComment(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#     token = serializers.CharField(required=True, max_length=32)
#     context = serializers.CharField(required=True, max_length=2048)
#
#     class Meta:
#         model = BookComment
#         fields = (
#             'ISBN',
#             'token',
#             'context'
#         )
#
#
# class TagGetBook(serializers.ModelSerializer):
#     tag = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Tag
#         fields = (
#             'tag',
#         )
#
#
# class AddNote(serializers.ModelSerializer):
#     ISBN = serializers.CharField(required=True, max_length=32)
#     content = serializers.CharField(required=True, max_length=8195)
#     token = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Note
#         fields = (
#             'ISBN',
#             'content',
#             'token'
#         )
#
#
# class SearchInfo(serializers.ModelSerializer):
#     context = serializers.CharField(required=True, max_length=32)
#
#     class Meta:
#         model = Tag
#         fields = (
#             'context',
#         )