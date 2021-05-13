from django.db import models
from django.utils.timezone import now


# Create your models here.

# 用户


class User(models.Model):
    uid = models.CharField(verbose_name='用户名', max_length=16, unique=True)
    pwd = models.CharField(verbose_name='密码', max_length=16)
    sex = models.IntegerField(verbose_name='性别', default=0)
    mail = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
    avatar = models.CharField(verbose_name='头像', max_length=2048, default="NO")
    createTime = models.DateField(verbose_name='注册时间', auto_now=False, default=now)
    isTeacher = models.BooleanField(verbose_name='是否为导师', default=False)
    circle = models.ForeignKey(verbose_name='圈子', to='Circle', on_delete=models.CASCADE, null=True)


# 邮箱与验证码对应
class MailKey(models.Model):
    mail = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
    key = models.CharField(verbose_name='验证码', max_length=16)


# Token
class Token(models.Model):
    key = models.CharField(verbose_name='token随机码', max_length=16, unique=True)
    usr = models.ForeignKey(verbose_name='token对应的用户', to='User', on_delete=models.CASCADE)


# 日志
class Journal(models.Model):
    usr = models.ForeignKey(verbose_name='发布人', to='User', on_delete=models.CASCADE, null=True)
    create_time = models.DateField(verbose_name='日志创建时间', auto_now=True)
    type = models.CharField(verbose_name='日志类型', max_length=16, default='None')
    context = models.FileField(verbose_name='正文', max_length=2048, upload_to='journal/%Y/%m/%d/')
    thumbsUp = models.IntegerField(verbose_name='点赞数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64, default='0')
    introduce = models.CharField(verbose_name='日志简介', max_length=256, default='0')
    pin = models.BooleanField(verbose_name='置顶', default=False)


# 日志评论
class Comment(models.Model):
    usr = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='评论人用户名', null=True)
    journal = models.ForeignKey(to='Journal', on_delete=models.CASCADE, verbose_name='评论日志', null=True)
    ctime = models.DateField(verbose_name='评论时间', auto_now=True)
    context = models.FileField(verbose_name='正文', max_length=2048, upload_to='comment/%Y/%m/%d/')
    floor = models.IntegerField(verbose_name='评论楼层', default=0)


# 讨论
class Discuss(models.Model):
    usr = models.ForeignKey(to='User', on_delete=models.CASCADE, null=True)
    circle = models.ForeignKey(to='Circle', on_delete=models.CASCADE, null=True)
    dtime = models.DateField(verbose_name='发布时间', auto_now=True)
    context = models.CharField(verbose_name='内容', max_length=256)
    floor = models.IntegerField(verbose_name='讨论楼层', default=0)


# 圈子
class Circle(models.Model):
    type = models.CharField(verbose_name='圈子类型', max_length=16, default="学习")
    name = models.CharField(verbose_name='圈子名字', max_length=32, default="root")
    ctime = models.DateField(verbose_name='发布时间', auto_now=False, default=now)
    number = models.IntegerField(verbose_name='圈子人数', default=1)
    creator = models.IntegerField(verbose_name='创建者id', default=1)


# 书本
class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=256, default='No name')
    publishTime = models.DateField(verbose_name='出版时间', default='2000-01-01')
    ISBN = models.CharField(verbose_name='ISBN编号', max_length=32, primary_key=True)
    author = models.CharField(verbose_name='作者名字', max_length=32, default='author')


# 读书笔记
class Note(models.Model):
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    context = models.TextField(verbose_name='笔记内容', max_length=8195)
    ntime = models.DateField(verbose_name='发布时间', auto_now=False)
    usr = models.ForeignKey(verbose_name='笔记作者', to='User', on_delete=models.CASCADE)


# 书评
class BookComment(models.Model):
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE, null=True)
    floor = models.IntegerField(verbose_name='评论楼层', default=0)
    bctime = models.DateField(verbose_name='发布时间', auto_now=True)
    context = models.TextField(verbose_name='书评内容', default="0")
    usr = models.ForeignKey(verbose_name='评论人用户名', to='User', on_delete=models.CASCADE, null=True)


# 书与标签对应
class BookTag(models.Model):
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE, null=True)


# 标签
class Tag(models.Model):
    tag = models.CharField(verbose_name='标签内容', max_length=32, default='0')

# 信息
