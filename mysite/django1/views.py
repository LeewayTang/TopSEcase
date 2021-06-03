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
            return Response({'msg': 'Token not exists', 'data': -1, 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        uid = data_json.get('uid')
        if uid is not None:
            user.uid = uid
        pwd = data_json.get('pwd')
        if pwd is not None:
            user.pwd = pwd
        sex = data_json.get('sex')
        if sex is not None:
            user.sex = sex
        avatar = request.FILES.get('avatar')
        if avatar is not None:
            user.avatar = avatar
        isTeacher = data_json.get('isTeacher')
        if isTeacher is not None:
            user.isTeacher = isTeacher
        circle = data_json.get('circle')
        print(circle)
        if circle is not None:
            queryset = Circle.objects.filter(id=circle)
            if queryset.count() == 0:
                return Response({'msg': 'Circle not exists', 'status': '-1'})
            queryset = Circle.objects.get(id=circle)
            queryset.number += 1
            queryset.save()
            if user.circle is not None:
                queryset = Circle.objects.get(id=user.circle.id)
                queryset.number -= 1
                queryset.save()
            queryset = Circle.objects.get(id=circle)
            user.circle = Circle.objects.get(id=circle)
        circle = "none"
        if user.circle is not None:
            circle = user.circle.id
        ret = [{'uid': user.uid, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar.url,
                'isTeacher': user.isTeacher, 'circle': circle}]
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        # user.save()
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUserInfo(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        circle = "none"
        if user.circle is not None:
            circle = user.circle.id
        ret = [{'uid': user.uid, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar.url,
                'isTeacher': user.isTeacher, 'circle': circle}]
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=UidInfoSerializer)
    @action(methods=['POST'], detail=False)
    def delCircleByUid(self, request):
        data_json = json.loads(request.body)
        uid = data_json.get('uid')
        queryset = User.objects.filter(uid__exact=uid)
        if queryset.count() == 0:
            return Response({'msg': 'User not exists', 'status': -1})
        user = User.objects.get(uid__exact=uid)
        if user.circle is None:
            return Response({'msg': 'User has not circle', 'status': -1})
        user.circle = None
        user.save()
        return Response({'msg': 'Delete success', 'status': 1})


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
        queryset = User.objects.filter(uid=Uid)
        if queryset.count() != 0:
            return Response({'msg': '用户名已存在', 'status': -2})
        if not re.match('^[0-9a-zA-Z]+[@][0-9a-zA-Z]+.+[0-9a-zA-Z]+$', Mail):
            return Response({'msg': '邮箱格式错误', 'status': -1})
        time = datetime.date.today()
        User.objects.create(uid=Uid, pwd=Pwd, mail=Mail, createTime=time, circle=None)
        return Response({'msg': '注册成功', 'status': 1})

    # def register(self, request):
    #     data_json = json.loads(request.body, strict=False)
    #     Uid = data_json.get('uid')
    #     Pwd = data_json.get('pwd')
    #     Mail = data_json.get('mail')
    #     type = data_json.get('type')
    #     queryset = User.objects.filter(uid=Uid)
    #     if queryset.count() != 0:
    #         return Response({'msg': '用户名已存在', 'data': '-1'})
    #     if not re.match('^[0-9a-zA-Z]+[@][0-9a-zA-Z]+.+[0-9a-zA-Z]+$', Mail):
    #         return Response({'msg': '邮箱格式错误', 'data': '-1'})
    #     if type == 1:
    #         key = data_json.get('key')
    #         if key is None:
    #             return Response({'msg': '你逗我呢没有验证码', 'data': -1})
    #         queryset = MailKey.objects.filter(mail__exact=Mail, key=key)
    #         if queryset.count() == 0:
    #             return Response({'msg': '验证码错误', 'data': -1})
    #         queryset = MailKey.objects.get(mail__exact=Mail, key=key)
    #         queryset.delete()
    #         time = datetime.date.today()
    #         User.objects.create(uid=Uid, pwd=Pwd, mail=Mail, createTime=time, circle=None)
    #         return Response({'msg': '注册成功', 'data': '1'})
    #     else:
    #         key = generate_random_str(16)
    #         self.sendEmail(Mail, key)
    #         queryset = MailKey.objects.filter(mail__exact=Mail)
    #         if queryset.count() != 0:
    #             queryset = MailKey.objects.get(mail__exact=Mail)
    #             queryset.delete()
    #         MailKey.objects.create(mail=Mail, key=key)
    #         return Response({'msg': '验证码发送成功', 'key': key, 'data': 1})

    # def sendEmail(self, mail='1060555245.qq.com', key='None'):
    #     subject = '墨韵平台注册认证'  # 主题
    #     from_email = mysite.settings.EMAIL_HOST_USER  # 发件人，在settings.py中已经配置
    #     print(from_email)
    #     to_email = mail  # 邮件接收者列表
    #     # 发送的消息
    #     message = '注册验证码为' + key  # 发送普通的消息使用的时候message
    #     send_mail(subject, message, from_email, [to_email])

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
            return Response({'msg': '用户名或邮箱不正确', 'status': -1})
        queryset = User.objects.filter(uid__exact=Uid, pwd__exact=Pwd)
        queryset_mail = User.objects.filter(mail__exact=Uid, pwd__exact=Pwd)
        if queryset.count() == 0 and queryset_mail.count() == 0:
            return Response({'msg': '密码不正确', 'status': -1})
        # (user_list, many=True)
        user = User.objects.get(uid__exact=Uid, pwd__exact=Pwd)
        token = Token.objects.filter(usr__exact=user)
        if token.count() != 0:
            print('exists')
            token.delete()
        key = generate_random_str()
        Token.objects.create(key=key, usr=user)
        ret = {'msg': 'success', 'status': 1, 'token': key}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def loginTraveler(self, request):
        Uid = 'traveler'
        Pwd = 'traveler'
        user = User.objects.get(uid__exact=Uid, pwd__exact=Pwd)
        token = Token.objects.filter(usr__exact=user)
        if token.count() == 0:
            Token.objects.create(key=generate_random_str(), usr=user)
        key = Token.objects.get(usr__exact=user).key
        ret = {'msg': 'success', 'status': 1, 'token': key}
        ret.update({'avatar': '../assets/images/rzdf.jpg'})
        ret.update({'username': '123123'})
        ret.update({'title': '游客'})
        ret.update({'quanzi': [{'name': 'BUAA'}]})
        ret.update({'slogan': 'I do not wish to be horny any more.'})
        ret.update({'name': 'MoYun'})

        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def logout(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'No token exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        queryset.delete()
        return Response({'msg': 'success', 'status': 1})


class FileUpload(viewsets.GenericViewSet):
    """
    upload_avatar:
    需要登陆后使用，传入用户名与头像url
    """
    queryset = Book.objects.all()
    serializer_class = UploadBookSerializer

    @swagger_auto_schema(responses={200: ""},
                         request_body=UploadAvatarSerializer)
    @action(methods=['POST'], detail=False)
    def uploadAvatar(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('uid')
        avatar = data_json.get('avatar')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'failed', 'status': -1})
        queryset = Token.objects.get(key__exact=token).usr
        if queryset.uid == 'traveler':
            return Response({'msg': 'failed', 'status': -2})
        queryset.avatar = avatar
        queryset.save()
        return Response({'msg': 'upload success', 'status': 1})

    @swagger_auto_schema(responses={200: ""},
                         request_body=UploadBookSerializer,
                         queryset=Book.objects.all())
    @action(methods=['POST'], detail=False)
    def uploadBook(self, request):
        # data_json = json.loads(request.body)
        ISBN = request.POST.get('ISBN')
        file = request.FILES.get('file')
        queryset = Book.objects.get(ISBN=ISBN)
        queryset.file = file
        queryset.save()
        return Response({'msg': 'upload success', 'status': 1})


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
            return Response({'msg': 'Input illegal', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset = Book.objects.get(ISBN__exact=ISBN)
        queryset = queryset.booktag_set.all()
        if queryset.count() == 0:
            return Response({'msg': 'This book no tags', 'status': 0})
        ret = {'msg': 'success', 'data': queryset.values(), 'status': 1}
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
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'status': -1})
        tag = Tag.objects.get(tag__exact=tag)
        book = Book.objects.get(ISBN__exact=ISBN)
        queryset = BookTag.objects.filter(book=book, tag=tag)
        if queryset.count() != 0:
            return Response({'msg': 'Book tag exists', 'status': 0})
        BookTag.objects.create(book=book, tag=tag)
        return Response({'msg': 'upload success', 'status': 1})

    @swagger_auto_schema(responses={200: ""},
                         request_body=TagGetBook)
    @action(methods=['POST'], detail=False)
    def getBookByTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        print(tag)
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'No such tid', 'status': -1})
        queryset = Tag.objects.get(tag=tag).booktag_set.all()
        ret = {'msg': 'success', 'data': queryset.values(), 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getBook(self, request):
        queryset = Book.objects.all().values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getTag(self, request):
        queryset = Tag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getBookTag(self, request):
        queryset = BookTag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def getTagTid(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'status': -1})
        queryset = Tag.objects.get(tag__exact=tag).id
        return Response({'msg': 'success', 'data': queryset, 'status': 1})

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
            return Response({'msg': 'ISBN exists', 'status': -1})
        Book.objects.create(name=name, publishTime=publishTime,
                            ISBN=ISBN, author=author)
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def addTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag=tag)
        if queryset.count() != 0:
            return Response({'msg': 'Tag exists', 'status': -1})
        Tag.objects.create(tag=tag)
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
    @action(methods=['POST'], detail=False)
    def delTag(self, request):
        data_json = json.loads(request.body)
        tag = data_json.get('tag')
        queryset = Tag.objects.filter(tag__exact=tag)
        if queryset.count() == 0:
            return Response({'msg': 'Tag not exists', 'status': -1})
        queryset = Tag.objects.get(tag__exact=tag)
        tid = queryset.id
        queryset.delete()
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""}, request_body=BookISBN)
    @action(methods=['POST'], detail=False)
    def delBook(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        queryset = Book.objects.filter(ISBN=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset.delete()
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)


class TokenInfo(viewsets.GenericViewSet):
    queryset = Token.objects.all()

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getToken(self, request):
        queryset = Token.objects.all().values()
        return Response({'msg': 'success', 'data': queryset, 'status': 1})


class CircleInfo(viewsets.GenericViewSet):
    """
    getCircle:
    获取所有圈子信息

    addCircle:
    添加圈子，需要圈子类型，圈子名称，登录状态

    getDiscuss:
    获取一个圈子的所有讨论

    addDiscuss:
    在一个圈子中添加讨论，需要登录状态，圈子id，讨论内容
    """
    queryset = Circle.objects.all()

    # serializers = CircleInfoSerializer

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getCircle(self, request):
        queryset = Circle.objects.all().values()
        return Response({'msg': 'success', 'data': queryset, 'status': 1})

    @swagger_auto_schema(responses={200: ""}, request_body=CircleInfoSerializer)
    @action(methods=['POST'], detail=False)
    def addCircle(self, request):
        data_json = json.loads(request.body)
        type = data_json.get('type')
        name = data_json.get('name')
        token = data_json.get('token')
        if type is None or name is None or token is None:
            return Response({'msg': 'Parameter wrong', 'status': -1})
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Not login', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        if not queryset.usr.isTeacher:
            return Response({'msg': 'Not teacher', 'status': 0})
        Circle.objects.create(type=type, name=name, creator=queryset.usr.id)
        return Response({'msg': 'success', 'status': 1})

    @swagger_auto_schema(responses={200: ""}, request_body=GetCircleComment)
    @action(methods=['POST'], detail=False)
    def getDiscuss(self, request):
        data_json = json.loads(request.body)
        circle = data_json.get('circle')
        if circle is None:
            return Response({'msg': 'Parameter wrong', 'status': -1})
        queryset = Circle.objects.filter(id=circle)
        if queryset.count() == 0:
            return Response({'msg': 'Circle not exists', 'status': -1})
        queryset = Discuss.objects.filter(circle_id=circle).order_by('id', 'floor').values()
        return Response({'msg': 'success', 'status': 1, 'data': queryset})

    @swagger_auto_schema(responses={200: ""}, request_body=AddCircleComment)
    @action(methods=['POST'], detail=False)
    def addDiscuss(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        circle = data_json.get('circle')
        context = data_json.get('context')
        if token is None or circle is None or context is None:
            return Response({'msg': 'Parameter wrong', 'status': -1})
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Not login', 'status': -1})
        queryset = Circle.objects.filter(id=circle)
        if queryset.count() == 0:
            return Response({'msg': 'Circle not exists', 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        floor = Discuss.objects.filter(circle_id=circle).count() + 1
        circle = Circle.objects.get(id=circle)
        Discuss.objects.create(usr=user, circle=circle, context=context, floor=floor)
        return Response({'msg': 'success', 'status': 1})


class BookCommentInfo(viewsets.GenericViewSet):
    """
    getBookCommentFull:
    获取某个图书的全部评论

    getBookCommentPart:
    获取某个图书的前20个评论

    getBookCommentByPage:
    按页获取评论，需提供每页多少个，第几页

    addBookComment:
    添加书评
    """
    queryset = BookComment.objects.all()

    @swagger_auto_schema(responses={200: ""}, request_body=GetBookComment)
    @action(methods=['POST'], detail=False)
    def getBookCommentFull(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        if ISBN is None:
            return Response({'msg': 'No input', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset = BookComment.objects.filter(book__ISBN=ISBN).order_by('id', 'floor').values()
        return Response({'msg': 'success', 'status': 1, 'data': queryset})

    @swagger_auto_schema(responses={200: ""}, request_body=GetBookComment)
    @action(methods=['POST'], detail=False)
    def getBookCommentPart(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        if ISBN is None:
            return Response({'msg': 'No input', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset = BookComment.objects.filter(book__ISBN=ISBN, floor__lte=20).order_by('id', 'floor').values()
        return Response({'msg': 'success', 'status': 1, 'data': queryset})

    @swagger_auto_schema(responses={200: ""}, request_body=GetBookCommentByPage)
    @action(methods=['POST'], detail=False)
    def getBookCommentByPage(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        page = data_json.get('page')
        number = data_json.get('number')
        if ISBN is None or page is None or number is None:
            return Response({'msg': 'No input', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        mx = page * number
        mn = (page - 1) * number + 1
        queryset = BookComment.objects.filter(book__ISBN=ISBN, floor__lte=mx, floor__gte=mn).order_by('id',
                                                                                                      'floor').values()
        return Response({'msg': 'success', 'status': 1, 'data': queryset})

    @swagger_auto_schema(responses={200: ""}, request_body=AddBookComment)
    @action(methods=['POST'], detail=False)
    def addBookComment(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        token = data_json.get('token')
        context = data_json.get('context')
        if ISBN is None or token is None or context is None:
            return Response({'msg': 'No input', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Not login', 'status': -1})
        queryset = Book.objects.get(ISBN__exact=ISBN)
        queryset.comments += 1
        queryset.save()
        user = Token.objects.get(key__exact=token).usr
        book = Book.objects.get(ISBN__exact=ISBN)
        floor = BookComment.objects.filter(book__ISBN__exact=ISBN).count() + 1
        BookComment.objects.create(book=book, floor=floor, usr=user, context=context)
        return Response({'msg': 'success', 'status': 1})


class NoteInfo(viewsets.GenericViewSet):
    queryset = Note.objects.all()

    @swagger_auto_schema(responses={200: ""}, request_body=AddNote)
    @action(methods=['POST'], detail=False)
    def AddNote(self, request):
        data_json = json.loads(request.body)
        ISBN = data_json.get('ISBN')
        content = data_json.get('content')
        token = data_json.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Not login', 'status': -1})
        queryset = Book.objects.filter(ISBN__exact=ISBN)
        if queryset.count() == 0:
            return Response({'msg': 'Book not exists', 'status': -1})
        book = Book.objects.get(ISBN__exact=ISBN)
        user = Token.objects.get(key__exact=token).usr
        Note.objects.create(book=book, content=content, usr=user)
        return Response({'msg': 'success', 'status': 1})

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def GetNote(self, request):
        queryset = Note.objects.all().order_by('-date').values()
        return Response({'data': [{
            'name': 'essay1',
            'type': 'essay',
            'title': '刚发布！Python 一二线城市月薪 15K 起！12 月再夺语言榜首',
            'content': '',
            # imgUrl: require('../../assets/images/headImgDefault.png'),
            'forum': 'CSDNedu',
            'category': '',
            'date': '39分钟前',
            'read': '518',
            'comment': '1'
        }]})
        # return Response({'msg': 'success', 'data': queryset, 'status': 1})


class Search(viewsets.GenericViewSet):
    queryset = Book.objects.all()

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchBook(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': Book.objects.filter(name__icontains=context).order_by('ISBN').values(),
             'tag': 'Book',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchUser(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': User.objects.filter(uid__icontains=context).order_by('uid').values(),
             'tag': 'User',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchComment(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': Comment.objects.filter(context__icontains=context).order_by('ctime').values(),
             'tag': 'Comment',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchDiscuss(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': Discuss.objects.filter(context__icontains=context).order_by('dtime').values(),
             'tag': 'Discuss',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchCircle(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': Circle.objects.filter(type__icontains=context).order_by('id').values(),
             'tag': 'Circle',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchNote(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': Note.objects.filter(context__icontains=context).order_by('id').values(),
             'tag': 'Note',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchBookComment(self, request):
        context = json.loads(request.body).get('context')
        return Response(
            {'msg': 'success',
             'data': BookComment.objects.filter(context__icontains=context).order_by('id').values(),
             'tag': 'BookComment',
             'status': '1'})

    @swagger_auto_schema(responses={200: ""}, request_body=SearchInfo)
    @action(methods=['POST'], detail=False)
    def SearchAll(self, request):
        context = json.loads(request.body).get('context')
        Ret = {}
        Ret.update({'Book': Search.SearchBook(self, request=request).data})
        Ret.update({'User': Search.SearchUser(self, request=request).data})
        Ret.update({'Comment': Search.SearchComment(self, request=request).data})
        Ret.update({'Discuss': Search.SearchDiscuss(self, request=request).data})
        Ret.update({'Circle': Search.SearchCircle(self, request=request).data})
        Ret.update({'Note': Search.SearchNote(self, request=request).data})
        Ret.update({'BookComment': Search.SearchBookComment(self, request=request).data})
        return Response(
            {'msg': 'success',
             'data': Ret,
             'tag': 'All',
             'status': '1'})
