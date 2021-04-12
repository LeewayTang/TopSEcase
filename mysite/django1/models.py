from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    uid = models.CharField(verbose_name='用户名', max_length=16, primary_key=True)
    pwd = models.CharField(verbose_name='密码', max_length=16)
    mail = models.CharField(verbose_name='邮箱', max_length=32, unique=True)
    avatar = models.CharField(verbose_name='头像', max_length=32, unique=True)
    createTime = models.DateField(verbose_name='注册时间', auto_now=False)
    isTeacher = models.BooleanField(verbose_name='是否为导师', default=False)
    cid = models.CharField(verbose_name='所属圈子id', max_length=16, default="")

# 日志
class Journal(models.Model):
    uid = models.CharField(verbose_name='发布人id', max_length=16)
    jid = models.CharField(verbose_name='日志id', max_length=16)
    create_time = models.DateField(verbose_name='日志创建时间', auto_now=True)
    type = models.CharField(verbose_name='日志类型', max_length=16)
    context = models.CharField(verbose_name='正文', max_length=3000)
    thumbsUp = models.IntegerField(verbose_name='点赞数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64)
    introduce = models.CharField(verbose_name='日志简介', max_length=256)
    pin = models.BooleanField(verbose_name='置顶', default=False)

# 评论
class Comment(models.Model):
    uid = models.CharField(verbose_name='评论人id', max_length=16)
    jid = models.CharField(verbose_name='日志id', max_length=16)
    create_time = models.DateField(verbose_name='评论时间', auto_now=True)
    context = models.CharField(verbose_name='正文', max_length=3000)
    floor = models.IntegerField(verbose_name='评论楼层')

# 讨论
class Discuss(models.Model):
    uid = models.CharField(verbose_name='评论人id', max_length=16)
    create_time = models.DateField(verbose_name='发布时间', auto_now=True)
    context = models.CharField(verbose_name='内容', max_length=3000)
    cid = models.CharField(verbose_name='圈子id', max_length=16)


# 圈子
class Circle(models.Model):
    cid = models.CharField(verbose_name='圈子id', max_length=16, default="", primary_key=True)
    type = models.CharField(verbose_name='圈子类型', max_length=16, default="学习")

# 好友关系
class Friend(models.Model):
    uidL = models.CharField(verbose_name='关系A', max_length=16)
    uidR = models.CharField(verbose_name='关系B', max_length=16)


# 信息

