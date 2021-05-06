from drf_yasg.openapi import Parameter, IN_PATH, TYPE_STRING, IN_QUERY
from rest_framework import viewsets
from rest_framework import generics
from django1.models import *
from django1.serializers import *
from drf_yasg import openapi
import json
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.decorators import action
import re


# Create your views here.
# swagger_schema = None 忽略整个class

# @method_decorator(
#     name="list",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     )
# )
class UserInfoView(viewsets.ModelViewSet):
    """
        retrieve:
            返回一组（查）

        list:
            返回所有组（查）

        create:
            创建新组（增）

        delete:
            删除现有的一组（删）

        partial_update:
            更新现有组中的一个或多个字段（改：部分更改）

        update:
            更新一组（改：全部更改）
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


# 防止ModelViewSet的多余接口
# @method_decorator(
#     name="list",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="update",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="destroy",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="create",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="partial_update",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )
# @method_decorator(
#     name="retrieve",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     ),
# )


class LoginRegister(viewsets.GenericViewSet):
    """
    login:
    用户名或邮箱，密码

    register:
    用户名，邮箱，密码
    """
    queryset = User.objects.all()
    serializer_class = LoginInfoSerializer

    # test_param =
    # openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(responses={200: ""},
                         request_body=RegisterInfoSerializer)
    @action(methods=['POST'], detail=False)
    def register(self, request, pk):
        print(request)
        data_json = json.loads(request.body, strict=False)
        print(data_json)
        Uid = data_json.get('uid')
        Pwd = data_json.get('pwd')
        Mail = data_json.get('mail')
        print(Uid)
        print(Mail)
        print(Pwd)
        queryset = User.objects.filter(uid=Uid)
        if queryset.count() != 0:
            return Response({'msg': '用户名已存在', 'data': '-1'})
        if not re.match('^[0-9a-zA-Z]+[@][0-9a-zA-Z]+.+[0-9a-zA-Z]+$', Mail):
            return Response({'msg': '邮箱格式错误', 'data': '-1'})
        User.objects.create(uid=Uid, pwd=Pwd, mail=Mail, createTime='2000-01-01')
        return Response({'msg': '注册成功', 'data': '1'})

    @swagger_auto_schema(responses={200: ""},
                         request_body=LoginInfoSerializer)
    # manual_parameters=[test_param])
    @action(methods=['POST'], detail=False)
    def login(self, request):
        print(request)
        # Uid = request.POST.get('uid')
        # Pwd = request.POST.get('pwd')
        data_json = json.loads(request.body, strict=False)
        print(data_json)
        Uid = data_json.get('uid')
        Pwd = data_json.get('pwd')
        print(Uid, Pwd)
        queryset = User.objects.filter(uid__contains=Uid)  # .filter(uid=Uid, mail=Mail, pwd=Pwd)
        queryset_mail = User.objects.filter(mail__contains=Uid)
        if queryset.count() == 0 and queryset_mail.count() == 0:
            return Response({'msg': '用户名或邮箱不正确', 'data': -1})
        queryset = User.objects.filter(uid__contains=Uid, pwd__contains=Pwd)
        queryset_mail = User.objects.filter(mail__contains=Uid, pwd__contains=Pwd)
        if queryset.count() == 0 and queryset_mail.count() == 0:
            return Response({'msg': '密码不正确', 'data': -1})
        # (user_list, many=True)
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)


class FileUpload(viewsets.GenericViewSet):
    """
    upload_avatar:
    需要登陆后使用，传入用户名与头像url
    """
    queryset = User.objects.all()

    @swagger_auto_schema(responses={200: ""},
                         request_body=UploadAvatarSerializer)
    @action(methods=['POST'], detail=False)
    def upload_avatar(self, request, pk):
        data_json = json.loads(request.body)
        Uid = data_json.get('uid')
        Avatar = data_json.get('avatar')
        queryset = User.objects.get(uid=Uid)
        queryset.avatar = Avatar
        queryset.save()
        return Response({'msg': 'upload success', 'data': '1'})


class BookTagInfo(viewsets.GenericViewSet):
    """
    get_tag_by_book:
    获取指定图书的标签

    set_tag_by_book:
    给指定图书添加标签

    get_book_by_tag:
    获取指定标签的图书

    get_book:
    获取所有图书

    get_tag:
    获取所有标签

    add_book:
    添加图书

    add_tag:
    添加标签
    """
    queryset = Book.objects.all()
    serializer_class = BookSetTag

    @swagger_auto_schema(responses={200: ""}, request_body=BookGetTag)
    @action(methods=['POST'], detail=False)
    def get_tag_by_book(self, request):
        print(request)
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        if ISBN is None:
            return Response({'msg': 'Book not exists', 'data': '-1'})
        queryset = Book.objects.filter(ISBN__contains=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'data': '-1'})
        queryset = BookTag.objects.filter(ISBN__contains=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'This book no tags', 'data': '0'})
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=BookSetTag)
    @action(methods=['POST'], detail=False)
    def set_tag_by_book(self, request, pk):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        tid = data_json.get('tid')
        queryset = Book.objects.filter(ISBN__contains=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'data': '-1'})
        queryset = Tag.objects.get(tid=tid)
        if queryset is None:
            return Response({'msg': 'Tag not exists', 'data': '-1'})
        queryset = BookTag.objects.get(ISBN=ISBN, tid=tid)
        if queryset is not None:
            return Response({'msg': 'Book tag exists', 'data': '0'})
        BookTag.objects.create(ISBN=ISBN, tid=tid)
        return Response({'msg': 'upload success', 'data': '1'})

    @swagger_auto_schema(responses={200: ""},
                         request_body=TagGetBook)
    @action(methods=['POST'], detail=False)
    def get_book_by_tag(self, request):
        data_json = json.loads(request.body)
        tid = data_json.get('tid')
        queryset = Tag.objects.filter(tid=tid)
        if queryset.count() == 0:
            return Response({'msg': 'No such tid', 'data': '-1'})
        queryset = BookTag.objects.filter(tid__contains=tid)
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def get_book(self, request):
        queryset = Book.objects.all()
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def get_tag(self, request):
        queryset = Tag.objects.all()
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=BookInfo)
    @action(methods=['POST'], detail=False)
    def add_book(self, request):
        data_json = json.loads(request.body)
        name = data_json.get('name')
        publishTime = data_json.get('publishTime')
        ISBN = data_json.get('ISBN')
        author = data_json.get('author')
        queryset = Book.objects.filter(ISBN=ISBN)
        if queryset.count() != 0:
            return {'msg': 'ISBN exists', 'data': -1}
        Book.objects.create(name=name, publishTime=publishTime,
                            ISBN=ISBN, author=author)
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def add_tag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag=tag)
        if queryset.count() != 0:
            return {'msg': 'Tag exists', 'data': -1}
        mx = Tag.objects.all()
        mx = mx.count()
        Tag.objects.create(tid=mx, tag=tag)
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)
