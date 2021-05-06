from django.db import models


# Create your models here.

# 用户
class User(models.Model):
    uid = models.CharField(verbose_name='用户名', max_length=16, primary_key=True)
    pwd = models.CharField(verbose_name='密码', max_length=16)
    sex = models.IntegerField(verbose_name='性别', default=0)
    mail = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
    avatar = models.CharField(verbose_name='头像', max_length=2048, default="NO")
    createTime = models.DateField(verbose_name='注册时间', auto_now=False)
    isTeacher = models.BooleanField(verbose_name='是否为导师', default=False)
    cid = models.IntegerField(verbose_name='所属圈子id', max_length=16, default=0)


# 日志
class Journal(models.Model):
    uid = models.CharField(verbose_name='发布人id', max_length=16, default='0')
    jid = models.IntegerField(verbose_name='日志id', max_length=16, default=0)
    create_time = models.DateField(verbose_name='日志创建时间', auto_now=True)
    type = models.CharField(verbose_name='日志类型', max_length=16, default='0')
    context = models.FileField(verbose_name='正文', max_length=2048, upload_to='journal/%Y/%m/%d/')
    thumbsUp = models.IntegerField(verbose_name='点赞数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64, default='0')
    introduce = models.CharField(verbose_name='日志简介', max_length=256, default='0')
    pin = models.BooleanField(verbose_name='置顶', default=False)


# 日志评论
class Comment(models.Model):
    uid = models.CharField(verbose_name='评论人id', max_length=16, default='0')
    jid = models.IntegerField(verbose_name='日志id', max_length=16, default=0)
    create_time = models.DateField(verbose_name='评论时间', auto_now=True)
    context = models.FileField(verbose_name='正文', max_length=2048, upload_to='comment/%Y/%m/%d/')
    floor = models.IntegerField(verbose_name='评论楼层', default=0)


# 讨论
class Discuss(models.Model):
    uid = models.CharField(verbose_name='评论人id', max_length=16, default='0')
    create_time = models.DateField(verbose_name='发布时间', auto_now=True)
    context = models.FileField(verbose_name='内容', max_length=2048, upload_to='discuss/%Y/%m/%d/')
    cid = models.IntegerField(verbose_name='圈子id', max_length=16, default='0')
    floor = models.IntegerField(verbose_name='讨论楼层', default=0)


# 圈子
class Circle(models.Model):
    cid = models.IntegerField(verbose_name='圈子id', max_length=16, default="", primary_key=True)
    type = models.CharField(verbose_name='圈子类型', max_length=16, default="学习")


# 好友关系
class Friend(models.Model):
    uidL = models.CharField(verbose_name='关系A', max_length=16, default='0')
    uidR = models.CharField(verbose_name='关系B', max_length=16, default='0')


# 书本
class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=256, default='0')
    publishTime = models.DateField(verbose_name='出版时间', default='2000-01-01')
    ISBN = models.CharField(verbose_name='ISBN编号', max_length=32, primary_key=True)
    author = models.CharField(verbose_name='作者名字', max_length=32, default='author')


# 书评
class BookComment(models.Model):
    ISBN = models.CharField(verbose_name='ISBN编号', max_length=32, default="0")
    floor = models.IntegerField(verbose_name='评论楼层', default=0)
    context = models.CharField(verbose_name='书评内容', max_length=2048, default="0")
    uid = models.CharField(verbose_name='用户', max_length=16, default="0")


# 书与标签对应
class BookTag(models.Model):
    ISBN = models.CharField(verbose_name='ISBN编号', max_length=32, default='0')
    tid = models.IntegerField(verbose_name='标签编号', default=0)


# 标签
class Tag(models.Model):
    tid = models.IntegerField(verbose_name='标签编号', default=0)
    tag = models.CharField(verbose_name='标签内容', max_length=32, default='0')

# 信息
