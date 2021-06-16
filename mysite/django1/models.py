import datetime
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
    slogan = models.CharField(verbose_name='签名', max_length=256, default="这个人很懒")
    title = models.CharField(verbose_name='这tmd到底是个啥', max_length=256, default='学生')
    trueName = models.CharField(verbose_name='姓名', max_length=16, default='游客')
    iid = models.CharField(verbose_name='学号', max_length=16, default='00000000')


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
    isTop = models.IntegerField(verbose_name='置顶', default=0)
    isHot = models.IntegerField(verbose_name='不知道干啥的', default=0)
    content = models.TextField(verbose_name='正文')
    user = models.ForeignKey(verbose_name='发布人', to='User', on_delete=models.CASCADE)
    pubTime = models.DateField(verbose_name='文章创建时间', auto_now_add=True)
    banner = models.CharField(verbose_name='文章头像', max_length=1024)
    type = models.CharField(verbose_name='type', max_length=32, default='article')


# 等待重新写
# 文章评论
class ArticleComment(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    createTime = models.DateField(verbose_name='评论时间', auto_now_add=True)
    content = models.TextField(verbose_name='正文')
    fromUser = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='评论人', related_name='fromUser')
    fromUserAvatar = models.CharField(verbose_name='评论者', max_length=512)
    fromUserName = models.CharField(verbose_name='评论者名字', max_length=512)
    toUser = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='回复人', default=None,
                               related_name='toUser', null=True)
    toUserId = models.IntegerField(verbose_name='回复者id', default=0)
    toUserName = models.CharField(verbose_name='回复者名字', max_length=512, default='')


# 等待重新写
# 讨论
class Discuss(models.Model):
    viewsCount = models.IntegerField(verbose_name='阅读量', default=0)
    commentsCount = models.IntegerField(verbose_name='评论数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64)
    summary = models.CharField(verbose_name='文章简介', max_length=256)
    isTop = models.IntegerField(verbose_name='置顶', default=0)
    isHot = models.IntegerField(verbose_name='不知道干啥的', default=0)
    user = models.ForeignKey(verbose_name='发布人', to='User', on_delete=models.CASCADE)
    pubTime = models.DateField(verbose_name='文章创建时间', auto_now_add=True)
    banner = models.CharField(verbose_name='文章头像', max_length=1024)
    type = models.CharField(verbose_name='type', max_length=32, default='discuss')


# 讨论评论
class DiscussComment(models.Model):
    discuss = models.ForeignKey(to='Discuss', on_delete=models.CASCADE)
    createTime = models.DateField(verbose_name='评论时间', auto_now_add=True)
    content = models.TextField(verbose_name='正文')
    fromUser = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='评论人',
                                 related_name='discussFromUser')
    fromUserAvatar = models.CharField(verbose_name='评论者', max_length=512)
    fromUserName = models.CharField(verbose_name='评论者名字', max_length=512)
    toUser = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='回复人', default=None,
                               related_name='discussToUser', null=True)
    toUserId = models.IntegerField(verbose_name='回复者id', default=0)
    toUserName = models.CharField(verbose_name='回复者名字', max_length=512, default='')


def getTraveler():
    queryset = User.objects.filter(username__exact='traveler')
    if queryset.count() == 0:
        time = datetime.date.today()
        Mail = 'travel@example.com'
        Uid = 'traveler'
        Pwd = 'traveler'
        User.objects.create(username=Uid, pwd=Pwd, mail=Mail, createTime=time)
    user = User.objects.get(username__exact='traveler')
    return user


# 等待重新写
# 圈子
class Quanzi(models.Model):
    name = models.CharField(verbose_name='圈子名字', max_length=32)
    ctime = models.DateField(verbose_name='发布时间', auto_now_add=True)
    number = models.IntegerField(verbose_name='圈子人数', default=1)
    creator = models.ForeignKey(verbose_name='创建者', to='User', on_delete=models.CASCADE,
                                related_name='creator', default=getTraveler)
    member = models.ManyToManyField('User')
    dialogVisible = models.BooleanField(verbose_name='鬼知道是啥', default=False)


# 等待重新写
def book_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["pdf", "mobi", "epub"]:
        sub_folder = "document"
    # print(os.path.join(instance.id, sub_folder, filename))
    return os.path.join(instance.ISBN, sub_folder, filename)


# 等待重新写
# 书本
class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=256, default='No name')
    introduction = models.TextField(verbose_name='简介')
    ISBN = models.CharField(verbose_name='ISBN编号', max_length=32)
    author = models.CharField(verbose_name='作者名字', max_length=32)
    press = models.CharField(verbose_name='出版社', max_length=32)
    img = models.CharField(verbose_name='封面', max_length=1024)
    language = models.CharField(verbose_name='语言', max_length=16)
    downloadCount = models.IntegerField(verbose_name='下载数', default=0)
    viewsCount = models.IntegerField(verbose_name='阅读数', default=0)
    comments = models.IntegerField(verbose_name='评论数', default=0)
    updater = models.ForeignKey(verbose_name='上传者', to='User', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='文本', upload_to=book_directory_path)
    review = models.TextField(verbose_name='评论')


# 书本标签
class BookTag(models.Model):
    book = models.ManyToManyField('Book')
    tag = models.CharField(verbose_name='标签名', max_length=32)


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
# 文章标签
class ArticleTag(models.Model):
    tag = models.CharField(verbose_name='标签内容', max_length=32)
    article = models.ManyToManyField('Article')


# 讨论标签
class DiscussTag(models.Model):
    tag = models.CharField(verbose_name='标签内容', max_length=32)
    discuss = models.ManyToManyField('Discuss')
