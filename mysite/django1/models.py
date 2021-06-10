import uuid

from django.db import models
import os


# Create your models here.

# 用户
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif", "jpeg", "bmp"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
    # print(os.path.join(instance.id, sub_folder, filename))
    return os.path.join(str(instance.id), sub_folder, filename)


class User(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=16, unique=True)
    pwd = models.CharField(verbose_name='密码', max_length=16)
    sex = models.IntegerField(verbose_name='性别', default=0)
    mail = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
    avatar = models.CharField(verbose_name='头像', max_length=1024, default='/media/1/file/dbf2c6b8.jpeg')
    createTime = models.DateField(verbose_name='注册时间', auto_now_add=True)
    isTeacher = models.BooleanField(verbose_name='是否为导师', default=False)
    # quanzi = models.ForeignKey(verbose_name='圈子', to='Quanzi', on_delete=models.CASCADE, null=True)
    slogan = models.CharField(verbose_name='签名', max_length=256, default="这个人很懒")
    title = models.CharField(verbose_name='这tmd到底是个啥', max_length=256, default='BUAA')


# 被弃用的功能
# 邮箱与验证码对应
# class MailKey(models.Model):
#     mail = models.EmailField(verbose_name='邮箱', max_length=32, unique=True)
#     key = models.CharField(verbose_name='验证码', max_length=16)


# Token
class Token(models.Model):
    key = models.CharField(verbose_name='token随机码', max_length=16, unique=True)
    usr = models.ForeignKey(verbose_name='token对应的用户', to='User', on_delete=models.CASCADE)


# 等待重新写
# 日志
# class Journal(models.Model):
#     usr = models.ForeignKey(verbose_name='发布人', to='User', on_delete=models.CASCADE, null=True)
#     create_time = models.DateField(verbose_name='日志创建时间', auto_now_add=True)
#     type = models.CharField(verbose_name='日志类型', max_length=16, default='None')
#     context = models.FileField(verbose_name='正文', max_length=2048, upload_to='journal/%Y/%m/%d/')
#     thumbsUp = models.IntegerField(verbose_name='点赞数', default=0)
#     title = models.CharField(verbose_name='标题', max_length=64, default='0')
#     introduce = models.CharField(verbose_name='日志简介', max_length=256, default='0')
#     pin = models.BooleanField(verbose_name='置顶', default=False)

# 文章
class Article(models.Model):
    viewsCount = models.IntegerField(verbose_name='阅读量', default=0)
    commentsCount = models.IntegerField(verbose_name='评论数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64)
    summary = models.CharField(verbose_name='文章简介', max_length=256)
    isTop = models.BooleanField(verbose_name='置顶', default=False)
    isHot = models.BooleanField(verbose_name='不知道干啥的', default=False)
    content = models.TextField(verbose_name='正文')
    user = models.ForeignKey(verbose_name='发布人', to='User', on_delete=models.CASCADE)
    pubTime = models.DateField(verbose_name='文章创建时间', auto_now_add=True)
    banner = models.CharField(verbose_name='文章头像', default='0', max_length=1024)


# 等待重新写
# 日志评论
# class Comment(models.Model):
#     usr = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='评论人用户名', null=True)
#     journal = models.ForeignKey(to='Journal', on_delete=models.CASCADE, verbose_name='评论日志', null=True)
#     ctime = models.DateField(verbose_name='评论时间', auto_now_add=True)
#     context = models.FileField(verbose_name='正文', max_length=2048, upload_to='comment/%Y/%m/%d/')
#     floor = models.IntegerField(verbose_name='评论楼层', default=0)


# 等待重新写
# 讨论
# class Discuss(models.Model):
#     usr = models.ForeignKey(to='User', on_delete=models.CASCADE, null=True)
#     circle = models.ForeignKey(to='Circle', on_delete=models.CASCADE, null=True)
#     dtime = models.DateField(verbose_name='发布时间', auto_now_add=True)
#     context = models.CharField(verbose_name='内容', max_length=256)
#     floor = models.IntegerField(verbose_name='讨论楼层', default=0)


# 等待重新写
# 圈子
# class Circle(models.Model):
#     type = models.CharField(verbose_name='圈子类型', max_length=16, default="学习")
#     name = models.CharField(verbose_name='圈子名字', max_length=32, default="root")
#     ctime = models.DateField(verbose_name='发布时间', auto_now_add=True)
#     number = models.IntegerField(verbose_name='圈子人数', default=1)
#     creator = models.IntegerField(verbose_name='创建者id', default=1)


# 等待重新写
# def book_directory_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
#     sub_folder = 'file'
#     if ext.lower() in ["pdf", "docx"]:
#         sub_folder = "document"
#     # print(os.path.join(instance.id, sub_folder, filename))
#     return os.path.join(instance.ISBN, sub_folder, filename)


# 等待重新写
# 书本
# class Book(models.Model):
#     name = models.CharField(verbose_name='书名', max_length=256, default='No name')
#     publishTime = models.DateField(verbose_name='出版时间', default='2000-01-01')
#     ISBN = models.CharField(verbose_name='ISBN编号', max_length=32, primary_key=True)
#     author = models.CharField(verbose_name='作者名字', max_length=32, default='author')
#     comments = models.IntegerField(verbose_name='评论数', default=0)
#     file = models.FileField(verbose_name='书', upload_to=book_directory_path, default="no")


# 等待重新写
# 读书笔记
# class Note(models.Model):
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
#     content = models.TextField(verbose_name='笔记内容', max_length=8195)
#     date = models.DateField(verbose_name='发布时间', auto_now_add=True)
#     usr = models.ForeignKey(verbose_name='笔记作者', to='User', on_delete=models.CASCADE)
#     thumb = models.IntegerField(verbose_name='点赞数', default=0)
#     titile = models.CharField(verbose_name='标题', max_length=256, default='NULL')
#     name = models.CharField(verbose_name='asdasdas', max_length=256, default='essay1')
#     type = models.CharField(verbose_name='类型', max_length=32, default='NULL')
#     forum = models.CharField(verbose_name='鬼知道是啥', max_length=32, default='NUll')
#     category = models.CharField(verbose_name='鬼知道是啥', max_length=32, default='NULL')
#     read = models.IntegerField(verbose_name='阅读数', default=0)
#     comment = models.IntegerField(verbose_name='评论数', default=0)


# 等待重新写
# 书评
# class BookComment(models.Model):
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE, null=True)
#     floor = models.IntegerField(verbose_name='评论楼层', default=0)
#     bctime = models.DateField(verbose_name='发布时间', auto_now_add=True)
#     context = models.TextField(verbose_name='书评内容', default="0")
#     usr = models.ForeignKey(verbose_name='评论人用户名', to='User', on_delete=models.CASCADE, null=True)
#     thumb = models.IntegerField(verbose_name='点赞数', default=0)


# 等待重新写


# 等待重新写
# 标签
class ArticleTag(models.Model):
    tag = models.CharField(verbose_name='标签内容', max_length=32)
    book = models.ManyToManyField('Article')

# 信息
