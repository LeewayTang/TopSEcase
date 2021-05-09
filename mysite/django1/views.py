import datetime

from django.core.mail import send_mail
from django.db.models import Max
from django.http import JsonResponse
from drf_yasg.openapi import Parameter, IN_PATH, TYPE_STRING, IN_QUERY
from rest_framework import viewsets
from rest_framework import generics
from django1.models import *
from django1.serializers import *
from django.core import serializers
from drf_yasg import openapi
import random
import string
import json
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.decorators import action
import mysite.settings
import re


# Create your views here.
# swagger_schema = None 忽略整个class
# 邮箱授权码 gfhkjvxwtketbege

# @method_decorator(
#     name="list",
#     decorator=swagger_auto_schema(
#         auto_schema=None,
#     )
# )
class UserInfoView(viewsets.GenericViewSet):
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

    @swagger_auto_schema(responses={200: ""},
                         request_body=UserInfoSerializer)
    @action(methods=['POST'], detail=False)
    def updateUserInfo(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'data': -1})
        ret = {}
        user = Token.objects.get(key__exact=token).usr
        uid = data_json.get('uid')
        if uid is not None:
            user.uid = uid
        ret.update({'uid': user.uid})
        pwd = data_json.get('pwd')
        if pwd is not None:
            user.pwd = pwd
        ret.update({'pwd': user.pwd})
        sex = data_json.get('sex')
        if sex is not None:
            user.sex = sex
        ret.update({'sex': user.sex})
        avatar = data_json.get('avatar')
        if avatar is not None:
            user.avatar = avatar
        ret.update({'avatar': user.avatar})
        isTeacher = data_json.get('isTeacher')
        if isTeacher is not None:
            user.isTeacher = isTeacher
        ret.update({'isTeacher': user.isTeacher})
        circle = data_json.get('circle')
        if circle is not None:
            user.circle = circle
        ret.update({'circle': user.circle})
        ret.update({'msg': 'success'})
        ret.update({'data': 1})
        user.save()
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUserInfo(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'data': -1})
        user = Token.objects.get(key__exact=token).usr
        ret = {}
        ret.update({'uid': user.uid})
        ret.update({'pwd': user.pwd})
        ret.update({'sex': user.sex})
        ret.update({'avatar': user.avatar})
        ret.update({'isTeacher': user.isTeacher})
        ret.update({'circle': user.circle})
        ret.update({'msg': 'success'})
        ret.update({'data': 1})
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=UidInfoSerializer)
    @action(methods=['POST'], detail=False)
    def delCircleByUid(self, request):
        data_json = json.loads(request.body)
        uid = data_json.get('uid')
        queryset = User.objects.filter(uid__exact=uid)
        if queryset.count() == 0:
            return Response({'msg': 'User not exists', 'data': -1})
        user = User.objects.get(uid__exact=uid)
        if user.circle is None:
            return Response({'msg': 'User has not circle', 'data': -1})
        user.circle = None
        user.save()
        return Response({'msg': 'Delete success', 'data': 1})


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

def generate_random_str(randomlength=16):
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str


class LoginRegister(viewsets.GenericViewSet):
    """
    login:
    用户名或邮箱，密码

    register:
    用户名，邮箱，密码
    type = 0表示需要发送验证码
    type = 1前端需要发送验证码
    """
    queryset = User.objects.all()
    serializer_class = LoginInfoSerializer

    # test_param =
    # openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(responses={200: ""},
                         request_body=RegisterInfoSerializer)
    @action(methods=['POST'], detail=False)
    def register(self, request):
        data_json = json.loads(request.body, strict=False)
        Uid = data_json.get('uid')
        Pwd = data_json.get('pwd')
        Mail = data_json.get('mail')
        type = data_json.get('type')
        queryset = User.objects.filter(uid=Uid)
        if queryset.count() != 0:
            return Response({'msg': '用户名已存在', 'data': '-1'})
        if not re.match('^[0-9a-zA-Z]+[@][0-9a-zA-Z]+.+[0-9a-zA-Z]+$', Mail):
            return Response({'msg': '邮箱格式错误', 'data': '-1'})
        if type == 1:
            key = data_json.get('key')
            if key is None:
                return Response({'msg': '你逗我呢没有验证码', 'data': -1})
            queryset = MailKey.objects.filter(mail__exact=Mail, key=key)
            if queryset.count() == 0:
                return Response({'msg': '验证码错误', 'data': -1})
            queryset = MailKey.objects.get(mail__exact=Mail, key=key)
            queryset.delete()
            time = datetime.date.today()
            User.objects.create(uid=Uid, pwd=Pwd, mail=Mail, createTime=time, circle=None)
            return Response({'msg': '注册成功', 'data': '1'})
        else:
            key = generate_random_str(16)
            self.sendEmail(Mail, key)
            queryset = MailKey.objects.filter(mail__exact=Mail)
            if queryset.count() != 0:
                queryset = MailKey.objects.get(mail__exact=Mail)
                queryset.delete()
            MailKey.objects.create(mail=Mail, key=key)
            return Response({'msg': '验证码发送成功', 'key': key, 'data': 1})

    def sendEmail(self, mail='1060555245.qq.com', key='None'):
        subject = '墨韵平台注册认证'  # 主题
        from_email = mysite.settings.EMAIL_HOST_USER  # 发件人，在settings.py中已经配置
        print(from_email)
        to_email = mail  # 邮件接收者列表
        # 发送的消息
        message = '注册验证码为' + key  # 发送普通的消息使用的时候message
        send_mail(subject, message, from_email, [to_email])

    @swagger_auto_schema(responses={200: ""},
                         request_body=LoginInfoSerializer)
    @action(methods=['POST'], detail=False)
    def login(self, request):
        data_json = json.loads(request.body, strict=False)
        Uid = data_json.get('uid')
        Pwd = data_json.get('pwd')
        queryset = User.objects.filter(uid__exact=Uid)  # .filter(uid=Uid, mail=Mail, pwd=Pwd)
        queryset_mail = User.objects.filter(mail__exact=Uid)
        if queryset.count() == 0 and queryset_mail.count() == 0:
            return Response({'msg': '用户名或邮箱不正确', 'data': -1})
        queryset = User.objects.filter(uid__exact=Uid, pwd__exact=Pwd)
        queryset_mail = User.objects.filter(mail__exact=Uid, pwd__exact=Pwd)
        if queryset.count() == 0 and queryset_mail.count() == 0:
            return Response({'msg': '密码不正确', 'data': -1})
        # (user_list, many=True)
        user = User.objects.get(uid__exact=Uid, pwd__exact=Pwd)
        token = Token.objects.filter(usr__exact=user)
        if token.count() != 0:
            print('exists')
            token.delete()
        key = generate_random_str()
        Token.objects.create(key=key, usr=user)
        ret = {'msg': 'success', 'data': 1, 'token': key}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def logout(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'No token exists', 'data': -1})
        queryset = Token.objects.get(key__exact=token)
        queryset.delete()
        return Response({'msg': 'success', 'data': 1})


class FileUpload(viewsets.GenericViewSet):
    """
    upload_avatar:
    需要登陆后使用，传入用户名与头像url
    """
    queryset = User.objects.all()

    @swagger_auto_schema(responses={200: ""},
                         request_body=UploadAvatarSerializer)
    @action(methods=['POST'], detail=False)
    def upload_avatar(self, request):
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

    get_book_tag:
    获取所有图书与标签关系

    get_tag_tid:
    获取标签内容所对应的标签id

    add_book:
    添加图书

    add_tag:
    添加标签

    del_tag:
    删除标签

    del_book:
    删除图书
    """
    queryset = Book.objects.all()
    serializer_class = BookSetTag

    @swagger_auto_schema(responses={200: ""}, request_body=BookISBN)
    @action(methods=['POST'], detail=False)
    def getTagByBook(self, request):
        print(request)
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        if ISBN is None:
            return Response({'msg': 'Input illegal', 'data': '-1'})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'data': '-1'})
        queryset = Book.objects.get(ISBN__exact=ISBN)
        queryset = queryset.booktag_set.all()
        if queryset.count() == 0:
            return Response({'msg': 'This book no tags', 'data': '0'})
        ret = {'msg': 'success', 'data': queryset.values()}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=BookSetTag)
    @action(methods=['POST'], detail=False)
    def setTagByBook(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        tag = data_json.get('tag')
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'data': '-1'})
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'data': '-1'})
        tag = Tag.objects.get(tag__exact=tag)
        book = Book.objects.get(ISBN__exact=ISBN)
        queryset = BookTag.objects.filter(book=book, tag=tag)
        if queryset.count() != 0:
            return Response({'msg': 'Book tag exists', 'data': '0'})
        BookTag.objects.create(book=book, tag=tag)
        return Response({'msg': 'upload success', 'data': '1'})

    @swagger_auto_schema(responses={200: ""},
                         request_body=TagGetBook)
    @action(methods=['POST'], detail=False)
    def getBookByTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        print(tag)
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'No such tid', 'data': '-1'})
        queryset = Tag.objects.get(tag=tag).booktag_set.all()
        ret = {'msg': 'success', 'data': queryset.values()}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getBook(self, request):
        queryset = Book.objects.all().values()
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getTag(self, request):
        queryset = Tag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getBookTag(self, request):
        queryset = BookTag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def getTagTid(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'data': -1})
        queryset = Tag.objects.get(tag__exact=tag).id
        return Response({'msg': 'success', 'data': queryset})

    @swagger_auto_schema(responses={200: ""}, request_body=BookInfo)
    @action(methods=['POST'], detail=False)
    def addBook(self, request):
        data_json = json.loads(request.body)
        name = data_json.get('name')
        publishTime = data_json.get('publishTime')
        ISBN = data_json.get('ISBN')
        author = data_json.get('author')
        queryset = Book.objects.filter(ISBN=ISBN)
        if queryset.count() != 0:
            return Response({'msg': 'ISBN exists', 'data': -1})
        Book.objects.create(name=name, publishTime=publishTime,
                            ISBN=ISBN, author=author)
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def addTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag=tag)
        if queryset.count() != 0:
            return Response({'msg': 'Tag exists', 'data': -1})
        Tag.objects.create(tag=tag)
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def delTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'data': -1})
        queryset = Tag.objects.get(tag__exact=tag)
        tid = queryset.id
        queryset.delete()
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=BookISBN)
    @action(methods=['POST'], detail=False)
    def delTook(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        queryset = Book.objects.filter(ISBN=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'data': -1})
        queryset.delete()
        ret = {'msg': 'success', 'data': 1}
        return Response(ret)


# class CircleInfo(viewsets.GenericViewSet):
#     queryset = Circle.objects.all()