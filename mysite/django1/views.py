import base64
import datetime
import json
import random
import re
import string

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from django1.serializers import *
from mysite.settings import MEDIA_ROOT, MEDIA_URL


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
    #     """
    #         retrieve:
    #             返回一组（查）
    #
    #         list:
    #             返回所有组（查）
    #
    #         create:
    #             创建新组（增）
    #
    #         delete:
    #             删除现有的一组（删）
    #
    #         partial_update:
    #             更新现有组中的一个或多个字段（改：部分更改）
    #
    #         update:
    #             更新一组（改：全部更改）
    #     """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer

    #
    #     @swagger_auto_schema(responses={200: ""},
    #                          request_body=UserInfoSerializer)
    #     @action(methods=['POST'], detail=False)
    #     def updateUserInfo(self, request):
    #         data_json = json.loads(request.body)
    #         token = data_json.get('token')
    #         queryset = Token.objects.filter(key__exact=token)
    #         if queryset.count() == 0:
    #             return Response({'msg': 'Token not exists', 'data': -1, 'status': -1})
    #         user = Token.objects.get(key__exact=token).usr
    #         uid = data_json.get('uid')
    #         if uid is not None:
    #             user.uid = uid
    #         pwd = data_json.get('pwd')
    #         if pwd is not None:
    #             user.pwd = pwd
    #         sex = data_json.get('sex')
    #         if sex is not None:
    #             user.sex = sex
    #         avatar = request.FILES.get('avatar')
    #         if avatar is not None:
    #             user.avatar = avatar
    #         isTeacher = data_json.get('isTeacher')
    #         if isTeacher is not None:
    #             user.isTeacher = isTeacher
    #         circle = data_json.get('circle')
    #         print(circle)
    #         if circle is not None:
    #             queryset = Circle.objects.filter(id=circle)
    #             if queryset.count() == 0:
    #                 return Response({'msg': 'Circle not exists', 'status': '-1'})
    #             queryset = Circle.objects.get(id=circle)
    #             queryset.number += 1
    #             queryset.save()
    #             if user.circle is not None:
    #                 queryset = Circle.objects.get(id=user.circle.id)
    #                 queryset.number -= 1
    #                 queryset.save()
    #             queryset = Circle.objects.get(id=circle)
    #             user.circle = Circle.objects.get(id=circle)
    #         circle = "none"
    #         if user.circle is not None:
    #             circle = user.circle.id
    #         ret = [{'uid': user.uid, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar.url,
    #                 'isTeacher': user.isTeacher, 'circle': circle}]
    #         Ret = {}
    #         Ret.update({'msg': 'success'})
    #         Ret.update({'data': ret})
    #         Ret.update({'status': 1})
    #         # user.save()
    #         return Response(Ret)
    #
    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUserInfo(self, request):
        # data_json = json.loads(request.body)
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
               'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title,
               'quanzi': user.quanzi_set.values()}
        for i in ret['quanzi']:
            print(i)
            qz = Quanzi.objects.get(name__exact=i['name'])
            creator = qz.creator
            i.update({'tutorInfo': {
                'avatar': creator.avatar,
                'trueName': creator.trueName,
                'iid': creator.iid,
            }
            })
            i.update({'studentsInfo': qz.member.exclude(username__exact=creator.username).values()})
            print(qz.member.exclude(username__exact=creator.username).values())
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=UsernameSerializer)
    @action(methods=['POST'], detail=False)
    def getUserInfoByName(self, request):
        # data_json = json.loads(request.body)
        print(request.data)
        username = request.data.get('username')
        queryset = User.objects.filter(username__exact=username)
        if queryset.count() == 0:
            return Response({'msg': 'User not exists', 'status': -1})
        user = User.objects.get(username__exact=username)
        ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
               'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title,
               'quanzi': user.quanzi_set.values()}
        for i in ret['quanzi']:
            print(i)
            qz = Quanzi.objects.get(name__exact=i['name'])
            creator = qz.creator
            i.update({'tutorInfo': {
                'avatar': creator.avatar,
                'trueName': creator.trueName,
                'iid': creator.iid,
            }
            })
            i.update({'studentsInfo': qz.member.exclude(username__exact=creator.username).values()})
            print(qz.member.exclude(username__exact=creator.username).values())
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=SetUserNameSerializer)
    @action(methods=['POST'], detail=False)
    def setUserName(self, request):
        token = request.data.get('token')
        username = request.data.get('username')
        print(token)
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = User.objects.filter(username__exact=username)
        if queryset.count() != 0:
            return Response({'msg': 'Username exists', 'status': -2})

        user = Token.objects.get(key__exact=token).usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        user.username = username
        user.save()
        ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
               'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title,
               'quanzi': user.quanzi_set.values()}
        print(ret)
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=SetUserSloganSerializer)
    @action(methods=['POST'], detail=False)
    def setUserSlogan(self, request):
        token = request.data.get('token')
        slogan = request.data.get('slogan')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        user.slogan = slogan
        user.save()
        ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
               'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title,
               'quanzi': user.quanzi_set.values()}
        print(ret)
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=SetUserAvatarSerializer)
    @action(methods=['POST'], detail=False)
    def setUserAvatar(self, request):
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        avB = request.data.get('avatarBase64')
        avatarBase64 = base64.b64decode(re.sub('^data:image/.*;base64,', '', avB))
        key = generate_random_str()
        form = avB.split(';')[0][11:]
        print(form)
        if not os.path.exists(MEDIA_ROOT + '/' + str(user.id) + '/avatar/'):
            os.makedirs(MEDIA_ROOT + '/' + str(user.id) + '/avatar/')
        file = open(MEDIA_ROOT + '/' + str(user.id) + '/avatar/' + key + '.' + form, 'wb')
        file.write(avatarBase64)
        file.close()
        user.avatar = MEDIA_URL + str(user.id) + '/avatar/' + key + '.' + form
        user.save()
        Article.objects.filter(user__exact=user).update(banner=user.avatar)
        Discuss.objects.filter(user__exact=user).update(banner=user.avatar)
        ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
               'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title,
               'quanzi': user.quanzi_set.values()}
        print(ret)
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUserQuanzi(self, request):
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        ret = {'quanzi': user.quanzi_set.values('name')}
        print(ret)
        Ret = {}
        Ret.update({'msg': 'success'})
        Ret.update({'data': ret})
        Ret.update({'status': 1})
        return Response(Ret)


class Upload(viewsets.GenericViewSet):
    queryset = Article.objects.all()

    def UploadArticleTag(self, tag, article):
        for i in tag:
            print(i)
            queryset = ArticleTag.objects.filter(tag__exact=i)
            if queryset.count() == 0:
                ArticleTag.objects.create(tag=i)
            queryset = ArticleTag.objects.get(tag__exact=i)
            queryset.article.add(article)

    @swagger_auto_schema(responses={200: ""},
                         request_body=ArticleUploadSerializer)
    @action(methods=['POST'], detail=False)
    def UploadArticle(self, request):
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        title = request.data.get('title')
        content = request.data.get('content')
        summary = request.data.get('summary')
        tag = request.data.get('tag')
        print(tag)
        print(title)
        print(content)
        print(summary)
        article = Article.objects.create(title=title, content=content, summary=summary, user=user, banner=user.avatar)
        self.UploadArticleTag(tag, article)
        Ret = {}
        Ret.update({'msg': 'success', 'status': 1})
        return Response(Ret)

    def UploadDiscussTag(self, tag, discuss):
        for i in tag:
            print(i)
            queryset = DiscussTag.objects.filter(tag__exact=i)
            if queryset.count() == 0:
                DiscussTag.objects.create(tag=i)
            queryset = DiscussTag.objects.get(tag__exact=i)
            queryset.discuss.add(discuss)

    @swagger_auto_schema(responses={200: ""},
                         request_body=DiscussUploadSerializer)
    @action(methods=['POST'], detail=False)
    def UploadDiscuss(self, request):
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        title = request.data.get('title')
        summary = request.data.get('summary')
        tag = request.data.get('tag')
        print(tag)
        print(title)
        print(summary)
        discuss = Discuss.objects.create(title=title, summary=summary, user=user, banner=user.avatar)
        discuss.banner = user.avatar
        discuss.save()
        self.UploadDiscussTag(tag, discuss)
        # ret = {'username': user.username, 'pwd': user.pwd, 'sex': user.sex, 'avatar': user.avatar,
        #        'isTeacher': user.isTeacher, 'slogan': user.slogan, 'title': user.title, 'quanzi': [{'name': 'BUAA'}]}
        Ret = {}
        Ret.update({'msg': 'success', 'status': 1})
        # Ret.update({'data': ret})
        # Ret.update({'status': 1})
        return Response(Ret)

    def UploadBookTag(self, tag, book):
        for i in tag:
            print(i)
            queryset = BookTag.objects.filter(tag__exact=i)
            if queryset.count() == 0:
                BookTag.objects.create(tag=i)
            queryset = BookTag.objects.get(tag__exact=i)
            queryset.book.add(book)

    @swagger_auto_schema(responses={200: ""},
                         request_body=DiscussUploadSerializer)
    @action(methods=['POST'], detail=False)
    def uploadBook(self, request):
        token = request.POST.get('token')
        title = request.POST.get('title')
        print(token)
        print(title)

        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        if user.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        author = request.POST.get('author')
        language = request.POST.get('language')
        ISBN = request.POST.get('ISBN')
        description = request.POST.get('description')
        if description is None or description == '':
            description = '暂无简介'
        topic = request.POST.get('topic')
        press = '暂无出版社信息'
        tags = request.POST.get('tags')
        print(request.POST.get('ISBN'))
        file = request.FILES.getlist('file')
        tags = tags.split('#')
        if user.title == '导师':
            tags.append('tutor')
        else:
            tags.append('student')
        print(tags)
        book = Book.objects.create(title=title, author=author, language=language, ISBN=ISBN, introduction=description,
                                   press=press, img='/media/1/file/dbf2c6b8.jpeg', file=file[0], updater=user)
        self.UploadBookTag(tags, book)
        return Response({'status': 1})


#
#     @swagger_auto_schema(responses={200: ""},
#                          request_body=UidInfoSerializer)
#     @action(methods=['POST'], detail=False)
#     def delCircleByUid(self, request):
#         data_json = json.loads(request.body)
#         uid = data_json.get('uid')
#         queryset = User.objects.filter(uid__exact=uid)
#         if queryset.count() == 0:
#             return Response({'msg': 'User not exists', 'status': -1})
#         user = User.objects.get(uid__exact=uid)
#         if user.circle is None:
#             return Response({'msg': 'User has not circle', 'status': -1})
#         user.circle = None
#         user.save()
#         return Response({'msg': 'Delete success', 'status': 1})


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
        trueName = data_json.get('trueName')
        iid = data_json.get('studentId')
        queryset = User.objects.filter(username__exact=Uid)
        if queryset.count() != 0:
            return Response({'msg': '用户名已存在', 'status': -2})
        if not re.match('^[0-9a-zA-Z]+[@][0-9a-zA-Z]+.+[0-9a-zA-Z]+$', Mail):
            return Response({'msg': '邮箱格式错误', 'status': -1})
        if User.objects.filter(iid__exact=iid).count() != 0:
            return Response({'msg': '学号已注册，请联系管理员', 'status': -3})
        time = datetime.date.today()
        user = User.objects.create(username=Uid, pwd=Pwd, trueName=trueName, mail=Mail, createTime=time, iid=iid)
        if Quanzi.objects.filter(name__exact='BUAA').count() == 0:
            Quanzi.objects.create(name="BUAA")
        qz = Quanzi.objects.get(name__exact="BUAA")
        qz.member.add(user)
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
        queryset_mail = User.objects.filter(mail__exact=Uid)
        if queryset_mail.count() == 0:
            return Response({'msg': '邮箱不正确', 'status': -1})
        queryset_mail = User.objects.filter(mail__exact=Uid, pwd__exact=Pwd)
        if queryset_mail.count() == 0:
            return Response({'msg': '密码不正确', 'status': -1})
        # (user_list, many=True)
        user = User.objects.get(mail__exact=Uid, pwd__exact=Pwd)
        token = Token.objects.filter(usr__exact=user)
        if token.count() != 0:
            print('exists')
            token.delete()
        key = generate_random_str()
        Token.objects.create(key=key, usr=user)
        ret = {'msg': 'success', 'status': 1, 'token': key}
        ret.update({'avatar': user.avatar})
        ret.update({'username': user.username})
        ret.update({'title': user.title})
        ret.update({'quanzi': user.quanzi_set.values()})
        ret.update({'slogan': user.slogan})
        ret.update({'name': 'MoYun'})
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def loginTraveler(self, request):
        Uid = 'traveler'
        Pwd = 'traveler'
        queryset = User.objects.filter(username__exact=Uid)
        if queryset.count() == 0:
            time = datetime.date.today()
            Mail = 'travel@example.com'
            user = User.objects.create(username=Uid, pwd=Pwd, mail=Mail, createTime=time)
            if Quanzi.objects.filter(name__exact='BUAA').count() == 0:
                Quanzi.objects.create(name="BUAA")
            qz = Quanzi.objects.get(name__exact="BUAA")
            qz.member.add(user)
        user = User.objects.get(username__exact=Uid, pwd__exact=Pwd)
        token = Token.objects.filter(usr__exact=user)
        if token.count() == 0:
            Token.objects.create(key=generate_random_str(), usr=user)
        key = Token.objects.get(usr__exact=user)
        ret = {'msg': 'success', 'status': 1, 'token': key.key}
        ret.update({'avatar': user.avatar})
        ret.update({'username': user.username})
        ret.update({'title': user.title})
        ret.update({'quanzi': user.quanzi_set.values()})
        ret.update({'slogan': user.slogan})
        ret.update({'name': 'MoYun'})
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def logout(self, request):
        data_json = json.loads(request.body)
        token = data_json.get('token')
        print(token)
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'No token exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        queryset.delete()
        return Response({'msg': 'success', 'status': 1})


# 等待重新写
# class FileUpload(viewsets.GenericViewSet):
#     """
#     upload_avatar:
#     需要登陆后使用，传入用户名与头像url
#     """
#     queryset = Book.objects.all()
#     serializer_class = UploadBookSerializer
#
#     @swagger_auto_schema(responses={200: ""},
#                          request_body=UploadAvatarSerializer)
#     @action(methods=['POST'], detail=False)
#     def uploadAvatar(self, request):
#         data_json = json.loads(request.body)
#         token = data_json.get('uid')
#         avatar = data_json.get('avatar')
#         queryset = Token.objects.filter(key__exact=token)
#         if queryset.count() == 0:
#             return Response({'msg': 'failed', 'status': -1})
#         queryset = Token.objects.get(key__exact=token).usr
#         if queryset.uid == 'traveler':
#             return Response({'msg': 'failed', 'status': -2})
#         print(avatar)
#         queryset.avatar = avatar
#         queryset.save()
#         return Response({'msg': 'upload success', 'status': 1})
#
#     @swagger_auto_schema(responses={200: ""},
#                          request_body=UploadBookSerializer,
#                          queryset=Book.objects.all())
#     @action(methods=['POST'], detail=False)
#     def uploadBook(self, request):
#         # data_json = json.loads(request.body)
#         ISBN = request.POST.get('ISBN')
#         file = request.FILES.get('file')
#         queryset = Book.objects.get(ISBN=ISBN)
#         queryset.file = file
#         queryset.save()
#         return Response({'msg': 'upload success', 'status': 1})


# 圈子
class QuanziInfo(viewsets.GenericViewSet):
    queryset = Quanzi.objects.all()

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['POST'], detail=False)
    def setQuanzi(self, request):
        token = request.data.get('token')
        name = request.data.get('name')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        queryset = Token.objects.get(key__exact=token)
        user = queryset.usr
        member = request.data.get('member')
        for i in member:
            if User.objects.filter(iid__exact=i).count() == 0:
                return Response({'status': -1})
        if Quanzi.objects.filter(name__exact=name).count() != 0:
            return Response({'status': -2})
        qz = Quanzi.objects.create(creator=user, name=name, number=1 + len(member))
        user.quanzi_set.add(qz)
        for i in member:
            usr = User.objects.get(iid__iexact=i)
            usr.quanzi_set.add(qz)
        return Response({'status': 1})

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['POST'], detail=False)
    def delQuanzi(self, request):
        token = request.data.get('token')
        name = request.data.get('name')
        print(name)
        user = Token.objects.get(key__exact=token).usr
        qz = Quanzi.objects.get(name__exact=name)
        if user != qz.creator:
            return Response({'status': -1})
        print(qz)
        qz.delete()
        return Response({'status': 1})


# 文章
class ArticleTagInfo(viewsets.GenericViewSet):
    queryset = ArticleTag.objects.all()

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getTag(self, request):
        queryset = ArticleTag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=ArticleListSerializer)
    @action(methods=['POST'], detail=False)
    def getArticle(self, request):
        page = 1
        size = 10
        if request.data.get('page') is not None:
            page = request.data.get('page')
        if request.data.get('size') is not None:
            size = request.data.get('size')
        lNum = (page - 1) * size + 1
        rNum = min(page * size, Article.objects.all().count())
        queryset = Article.objects.order_by('-isTop', '-viewsCount').values()[lNum - 1:rNum]
        hasNextPage = False
        if rNum < Article.objects.all().count():
            hasNextPage = True
        ret = {'msg': 'success', 'data': queryset, 'status': 1, 'page': page, 'hasNextPage': hasNextPage}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUsernameArticle(self, request):
        username = request.data.get('username')
        user = User.objects.get(username__exact=username)
        queryset = Article.objects.filter(user=user).order_by('-pubTime', '-viewsCount').values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getAllArticle(self, request):
        queryset = Article.objects.all().order_by('-pubTime', '-viewsCount').values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getIdArticle(self, request):
        Id = request.data.get('id')
        print(Id)
        queryset = Article.objects.filter(id__exact=Id)
        if queryset.count() == 0:
            return Response({'status': -1})
        article = Article.objects.get(id__exact=Id)
        article.viewsCount += 1
        article.save()
        Ret = {}
        Ret.update({'username': article.user.username})
        Ret.update({'avatar': article.user.avatar})
        Ret.update({'header': article.title})
        Ret.update({'content': article.content})
        Ret.update({'views': article.viewsCount})
        Ret.update({'comments': article.commentsCount})
        tag = article.articletag_set.values()
        print(tag)
        Ret.update({'tag': tag})
        ret = {'msg': 'success', 'data': Ret, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=IdSerializer)
    @action(methods=['POST'], detail=False)
    def getIdComment(self, request):
        Id = request.data.get('id')
        print("ID" + Id)
        queryset = ArticleComment.objects.filter(article_id=Id).order_by('createTime')
        ret = {'msg': 'success', 'data': queryset.values(), 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def setComment(self, request):
        Id = request.data.get('id')
        content = request.data.get('content')
        token = request.data.get('token')
        fromUser = Token.objects.get(key__exact=token).usr
        if fromUser.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        article = Article.objects.get(id=Id)
        fromUserAvatar = fromUser.avatar
        fromUserName = fromUser.username
        toUser = None
        toUserId = 0
        toUserName = request.data.get('toUserName')
        if toUserName is not None:
            toUser = User.objects.get(username__exact=toUserName)
            toUserId = toUser.id
        else:
            toUserName = ''
        article.commentsCount += 1
        article.save()
        ArticleComment.objects.create(content=content, article=article, fromUserAvatar=fromUserAvatar,
                                      fromUserName=fromUserName, toUser=toUser, toUserId=toUserId,
                                      toUserName=toUserName, fromUser=fromUser)
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)


# 讨论
class DiscussTagInfo(viewsets.GenericViewSet):
    queryset = DiscussTag.objects.all()

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getTag(self, request):
        queryset = DiscussTag.objects.all().values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=DiscussListSerializer)
    @action(methods=['POST'], detail=False)
    def getDiscuss(self, request):
        page = 1
        size = 10
        if request.data.get('page') is not None:
            page = request.data.get('page')
        if request.data.get('size') is not None:
            size = request.data.get('size')
        lNum = (page - 1) * size + 1
        rNum = min(page * size, Discuss.objects.all().count())
        queryset = Discuss.objects.order_by('-isTop', '-viewsCount').values()[lNum - 1:rNum]
        hasNextPage = False
        if rNum < Discuss.objects.all().count():
            hasNextPage = True
        ret = {'msg': 'success', 'data': queryset, 'status': 1, 'page': page, 'hasNextPage': hasNextPage}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getUsernameDiscuss(self, request):
        username = request.data.get('username')
        user = User.objects.get(username__exact=username)
        queryset = Discuss.objects.filter(user=user).order_by('-pubTime', '-viewsCount').values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getAllDiscuss(self, request):
        queryset = Discuss.objects.all().order_by('-pubTime', '-viewsCount').values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def getIdDiscuss(self, request):
        Id = request.data.get('id')
        print(Id)
        queryset = Discuss.objects.filter(id__exact=Id)
        if queryset.count() == 0:
            return Response({'status': -1})
        discuss = Discuss.objects.get(id__exact=Id)
        discuss.viewsCount += 1
        discuss.save()
        Ret = {}
        Ret.update({'username': discuss.user.username})
        Ret.update({'avatar': discuss.user.avatar})
        Ret.update({'header': discuss.title})
        Ret.update({'views': discuss.viewsCount})
        Ret.update({'comments': discuss.commentsCount})
        tag = discuss.discusstag_set.values()
        print(tag)
        Ret.update({'tag': tag})
        ret = {'msg': 'success', 'data': Ret, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=IdSerializer)
    @action(methods=['POST'], detail=False)
    def getIdComment(self, request):
        Id = request.data.get('id')
        print("ID" + Id)
        queryset = DiscussComment.objects.filter(discuss_id=Id).order_by('createTime')
        ret = {'msg': 'success', 'data': queryset.values(), 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""},
                         request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def setComment(self, request):
        Id = request.data.get('id')
        content = request.data.get('content')
        token = request.data.get('token')
        fromUser = Token.objects.get(key__exact=token).usr
        if fromUser.username == 'traveler':
            return Response({'msg': 'You can\'t do this', 'status': -3})
        discuss = Discuss.objects.get(id=Id)
        fromUserAvatar = fromUser.avatar
        fromUserName = fromUser.username
        toUser = None
        toUserId = 0
        toUserName = request.data.get('toUserName')
        if toUserName is not None:
            toUser = User.objects.get(username__exact=toUserName)
            toUserId = toUser.id
        else:
            toUserName = ''
        discuss.commentsCount += 1
        discuss.save()
        DiscussComment.objects.create(content=content, discuss=discuss, fromUserAvatar=fromUserAvatar,
                                      fromUserName=fromUserName, toUser=toUser, toUserId=toUserId,
                                      toUserName=toUserName, fromUser=fromUser)
        ret = {'msg': 'success', 'status': 1}
        return Response(ret)


# 书
class BookTagInfo(viewsets.GenericViewSet):
    queryset = BookTag.objects.all()

    @swagger_auto_schema(responses={200: ""},
                         request_body=IdSerializer)
    @action(methods=['POST'], detail=False)
    def getIdBook(self, request):
        Id = request.data.get('id')
        print("ID" + Id)
        queryset = Book.objects.filter(id=Id).values()
        if queryset.count() == 0:
            return Response({'status': -1})
        book = Book.objects.get(id=Id)
        book.viewsCount += 1
        book.save()
        print(queryset)
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getTag(self, request):
        queryset = BookTag.objects.exclude(Q(tag__exact='student') |
                                           Q(tag__exact='tutor')).values()
        ret = {'msg': 'success', 'data': queryset, 'status': 1}
        return Response(ret)
#
#     @swagger_auto_schema(responses={200: ""})
#     @action(methods=['GET'], detail=False)
#     def getBookTag(self, request):
#         queryset = BookTag.objects.all().values()
#         ret = {'msg': 'success', 'data': queryset, 'status': 1}
#         return Response(ret)
#
#     @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
#     @action(methods=['POST'], detail=False)
#     def getTagTid(self, request):
#         data_json = json.loads(request.body)
#         tag = data_json.get('tag')
#         queryset = Tag.objects.filter(tag__exact=tag)
#         if queryset.count() == 0:
#             return Response({'msg': 'Tag not exists', 'status': -1})
#         queryset = Tag.objects.get(tag__exact=tag).id
#         return Response({'msg': 'success', 'data': queryset, 'status': 1})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=BookInfo)
#     @action(methods=['POST'], detail=False)
#     def addBook(self, request):
#         data_json = json.loads(request.body)
#         name = data_json.get('name')
#         publishTime = data_json.get('publishTime')
#         ISBN = data_json.get('ISBN')
#         author = data_json.get('author')
#         queryset = Book.objects.filter(ISBN=ISBN)
#         if queryset.count() != 0:
#             return Response({'msg': 'ISBN exists', 'status': -1})
#         Book.objects.create(name=name, publishTime=publishTime,
#                             ISBN=ISBN, author=author)
#         ret = {'msg': 'success', 'status': 1}
#         return Response(ret)
#
#     @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
#     @action(methods=['POST'], detail=False)
#     def addTag(self, request):
#         data_json = json.loads(request.body)
#         tag = data_json.get('tag')
#         queryset = Tag.objects.filter(tag=tag)
#         if queryset.count() != 0:
#             return Response({'msg': 'Tag exists', 'status': -1})
#         Tag.objects.create(tag=tag)
#         ret = {'msg': 'success', 'status': 1}
#         return Response(ret)
#
#     @swagger_auto_schema(responses={200: ""}, request_body=CreateTag)
#     @action(methods=['POST'], detail=False)
#     def delTag(self, request):
#         data_json = json.loads(request.body)
#         tag = data_json.get('tag')
#         queryset = Tag.objects.filter(tag__exact=tag)
#         if queryset.count() == 0:
#             return Response({'msg': 'Tag not exists', 'status': -1})
#         queryset = Tag.objects.get(tag__exact=tag)
#         tid = queryset.id
#         queryset.delete()
#         ret = {'msg': 'success', 'status': 1}
#         return Response(ret)
#
#     @swagger_auto_schema(responses={200: ""}, request_body=BookISBN)
#     @action(methods=['POST'], detail=False)
#     def delBook(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         queryset = Book.objects.filter(ISBN=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         queryset.delete()
#         ret = {'msg': 'success', 'status': 1}
#         return Response(ret)


class TokenInfo(viewsets.GenericViewSet):
    queryset = Token.objects.all()

    @swagger_auto_schema(responses={200: ""})
    @action(methods=['GET'], detail=False)
    def getToken(self, request):
        queryset = Token.objects.all().values()
        return Response({'msg': 'success', 'data': queryset, 'status': 1})


# 等待重新写
# class CircleInfo(viewsets.GenericViewSet):
#     """
#     getCircle:
#     获取所有圈子信息
#
#     addCircle:
#     添加圈子，需要圈子类型，圈子名称，登录状态
#
#     getDiscuss:
#     获取一个圈子的所有讨论
#
#     addDiscuss:
#     在一个圈子中添加讨论，需要登录状态，圈子id，讨论内容
#     """
#     queryset = Circle.objects.all()
#
#     # serializers = CircleInfoSerializer
#
#     @swagger_auto_schema(responses={200: ""})
#     @action(methods=['GET'], detail=False)
#     def getCircle(self, request):
#         queryset = Circle.objects.all().values()
#         return Response({'msg': 'success', 'data': queryset, 'status': 1})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=CircleInfoSerializer)
#     @action(methods=['POST'], detail=False)
#     def addCircle(self, request):
#         data_json = json.loads(request.body)
#         type = data_json.get('type')
#         name = data_json.get('name')
#         token = data_json.get('token')
#         if type is None or name is None or token is None:
#             return Response({'msg': 'Parameter wrong', 'status': -1})
#         queryset = Token.objects.filter(key__exact=token)
#         if queryset.count() == 0:
#             return Response({'msg': 'Not login', 'status': -1})
#         queryset = Token.objects.get(key__exact=token)
#         if not queryset.usr.isTeacher:
#             return Response({'msg': 'Not teacher', 'status': 0})
#         Circle.objects.create(type=type, name=name, creator=queryset.usr.id)
#         return Response({'msg': 'success', 'status': 1})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=GetCircleComment)
#     @action(methods=['POST'], detail=False)
#     def getDiscuss(self, request):
#         data_json = json.loads(request.body)
#         circle = data_json.get('circle')
#         if circle is None:
#             return Response({'msg': 'Parameter wrong', 'status': -1})
#         queryset = Circle.objects.filter(id=circle)
#         if queryset.count() == 0:
#             return Response({'msg': 'Circle not exists', 'status': -1})
#         queryset = Discuss.objects.filter(circle_id=circle).order_by('id', 'floor').values()
#         return Response({'msg': 'success', 'status': 1, 'data': queryset})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=AddCircleComment)
#     @action(methods=['POST'], detail=False)
#     def addDiscuss(self, request):
#         data_json = json.loads(request.body)
#         token = data_json.get('token')
#         circle = data_json.get('circle')
#         context = data_json.get('context')
#         if token is None or circle is None or context is None:
#             return Response({'msg': 'Parameter wrong', 'status': -1})
#         queryset = Token.objects.filter(key__exact=token)
#         if queryset.count() == 0:
#             return Response({'msg': 'Not login', 'status': -1})
#         queryset = Circle.objects.filter(id=circle)
#         if queryset.count() == 0:
#             return Response({'msg': 'Circle not exists', 'status': -1})
#         user = Token.objects.get(key__exact=token).usr
#         floor = Discuss.objects.filter(circle_id=circle).count() + 1
#         circle = Circle.objects.get(id=circle)
#         Discuss.objects.create(usr=user, circle=circle, context=context, floor=floor)
#         return Response({'msg': 'success', 'status': 1})


# 等待重新写
# class BookCommentInfo(viewsets.GenericViewSet):
#     """
#     getBookCommentFull:
#     获取某个图书的全部评论
#
#     getBookCommentPart:
#     获取某个图书的前20个评论
#
#     getBookCommentByPage:
#     按页获取评论，需提供每页多少个，第几页
#
#     addBookComment:
#     添加书评
#     """
#     queryset = BookComment.objects.all()
#
#     @swagger_auto_schema(responses={200: ""}, request_body=GetBookComment)
#     @action(methods=['POST'], detail=False)
#     def getBookCommentFull(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         if ISBN is None:
#             return Response({'msg': 'No input', 'status': -1})
#         queryset = Book.objects.filter(ISBN__exact=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         queryset = BookComment.objects.filter(book__ISBN=ISBN).order_by('id', 'floor').values()
#         return Response({'msg': 'success', 'status': 1, 'data': queryset})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=GetBookComment)
#     @action(methods=['POST'], detail=False)
#     def getBookCommentPart(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         if ISBN is None:
#             return Response({'msg': 'No input', 'status': -1})
#         queryset = Book.objects.filter(ISBN__exact=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         queryset = BookComment.objects.filter(book__ISBN=ISBN, floor__lte=20).order_by('id', 'floor').values()
#         return Response({'msg': 'success', 'status': 1, 'data': queryset})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=GetBookCommentByPage)
#     @action(methods=['POST'], detail=False)
#     def getBookCommentByPage(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         page = data_json.get('page')
#         number = data_json.get('number')
#         if ISBN is None or page is None or number is None:
#             return Response({'msg': 'No input', 'status': -1})
#         queryset = Book.objects.filter(ISBN__exact=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         mx = page * number
#         mn = (page - 1) * number + 1
#         queryset = BookComment.objects.filter(book__ISBN=ISBN, floor__lte=mx, floor__gte=mn).order_by('id',
#                                                                                                       'floor').values()
#         return Response({'msg': 'success', 'status': 1, 'data': queryset})
#
#     @swagger_auto_schema(responses={200: ""}, request_body=AddBookComment)
#     @action(methods=['POST'], detail=False)
#     def addBookComment(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         token = data_json.get('token')
#         context = data_json.get('context')
#         if ISBN is None or token is None or context is None:
#             return Response({'msg': 'No input', 'status': -1})
#         queryset = Book.objects.filter(ISBN__exact=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         queryset = Token.objects.filter(key__exact=token)
#         if queryset.count() == 0:
#             return Response({'msg': 'Not login', 'status': -1})
#         queryset = Book.objects.get(ISBN__exact=ISBN)
#         queryset.comments += 1
#         queryset.save()
#         user = Token.objects.get(key__exact=token).usr
#         book = Book.objects.get(ISBN__exact=ISBN)
#         floor = BookComment.objects.filter(book__ISBN__exact=ISBN).count() + 1
#         BookComment.objects.create(book=book, floor=floor, usr=user, context=context)
#         return Response({'msg': 'success', 'status': 1})


# 等待重新写
# class NoteInfo(viewsets.GenericViewSet):
#     queryset = Note.objects.all()
#
#     @swagger_auto_schema(responses={200: ""}, request_body=AddNote)
#     @action(methods=['POST'], detail=False)
#     def AddNote(self, request):
#         data_json = json.loads(request.body)
#         ISBN = data_json.get('ISBN')
#         content = data_json.get('content')
#         token = data_json.get('token')
#         queryset = Token.objects.filter(key__exact=token)
#         if queryset.count() == 0:
#             return Response({'msg': 'Not login', 'status': -1})
#         queryset = Book.objects.filter(ISBN__exact=ISBN)
#         if queryset.count() == 0:
#             return Response({'msg': 'Book not exists', 'status': -1})
#         book = Book.objects.get(ISBN__exact=ISBN)
#         user = Token.objects.get(key__exact=token).usr
#         Note.objects.create(book=book, content=content, usr=user)
#         return Response({'msg': 'success', 'status': 1})
#
#     @swagger_auto_schema(responses={200: ""})
#     @action(methods=['GET'], detail=False)
#     def GetNote(self, request):
#         queryset = Note.objects.all().order_by('-date').values()
#         return Response({'data': [{
#             'name': 'essay1',
#             'type': 'essay',
#             'title': '刚发布！Python 一二线城市月薪 15K 起！12 月再夺语言榜首',
#             'content': '',
#             # imgUrl: require('../../assets/images/headImgDefault.png'),
#             'forum': 'CSDNedu',
#             'category': '',
#             'date': '39分钟前',
#             'read': '518',
#             'comment': '1'
#         }]})
#         # return Response({'msg': 'success', 'data': queryset, 'status': 1})


# 搜索
class Search(viewsets.GenericViewSet):
    queryset = User.objects.all()

    @swagger_auto_schema(responses={200: ""}, request_body=SerchQuanziSerializer)
    @action(methods=['POST'], detail=False)
    def searchQuanzi(self, request):
        qz = request.data.get('qz')
        print(qz)
        queryset = Quanzi.objects.filter(name__exact=qz)
        if queryset.count() == 0:
            return Response({'status': -1})
        return Response(
            {'user': Quanzi.objects.get(name__exact=qz).member.all().order_by('username').values('username'),
             'status': 1})

    @swagger_auto_schema(responses={200: ""}, request_body=SerchArticleSerializer)
    @action(methods=['POST'], detail=False)
    def searchArticle(self, request):
        key = request.data.get('key')
        print(key)
        queryset = Article.objects.filter(Q(summary__icontains=key) |
                                          Q(content__icontains=key) |
                                          Q(title__icontains=key))
        print(queryset.values())

        return Response({'data': queryset.values(), 'status': 1})

    @swagger_auto_schema(responses={200: ""}, request_body=SerchBookSerializer)
    @action(methods=['POST'], detail=False)
    def searchBook(self, request):
        tag = request.data.get('tag')
        print(tag)
        number = -1
        number = request.data.get('number')
        if request.data.get('number') is None:
            number = request.data.get('number')
        queryset = BookTag.objects.filter(tag__exact=tag).count()
        print(number)
        if queryset == 0:
            return Response({'status': -1, 'data': []})
        queryset = BookTag.objects.get(tag__exact=tag).book.values()[:number]
        print(queryset)
        return Response({'data': queryset, 'status': 1})

    @swagger_auto_schema(responses={200: ""}, request_body=TokenSerializer)
    @action(methods=['POST'], detail=False)
    def searchUsername(self, request):
        token = request.data.get('token')
        queryset = Token.objects.filter(key__exact=token)
        if queryset.count() == 0:
            return Response({'msg': 'Token not exists', 'status': -1})
        user = Token.objects.get(key__exact=token).usr
        queryset = User.objects.exclude(username__exact=user.username)
        mx = min(4, queryset.count())
        queryset = queryset.values('username')[:mx]
        return Response({'data': queryset, 'status': 1})
