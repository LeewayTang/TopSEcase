from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    uid = models.CharField(verbose_name='用户名', max_length=16, primary_key=True)
    pwd = models.CharField(verbose_name='密码', max_length=16)
    mail = models.CharField(verbose_name='邮箱', max_length=32, unique=True)
    createTime = models.DateField(verbose_name='注册时间', auto_now=False)

# 日志
class Journal(models.Model):
    uid = models.CharField(verbose_name='发布日志id', max_length=16)
    jid = models.CharField(verbose_name='日志id', max_length=16)
    create_time = models.DateField(verbose_name='日志创建时间', auto_now=True)
    type = models.CharField(verbose_name='日志类型', max_length=16)
    context = models.CharField(verbose_name='正文', max_length=30000)
    thumbsUp = models.IntegerField(verbose_name='点赞数', default=0)
    title = models.CharField(verbose_name='标题', max_length=64)
    introduce = models.CharField(verbose_name='日志简介', max_length=256)


