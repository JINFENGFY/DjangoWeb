# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
# 拓展的用户信息
class User_more_info (models.Model):
    gender = models.CharField (max_length=10, choices=(('male', '男'), ('female', '女')), default='male',
                               verbose_name=u'性别')
    phone = models.CharField (max_length=20, blank=True, verbose_name=u'电话号码')
    brief_introduction = models.TextField (max_length=500, blank=True, verbose_name=u'简介', default=u'这个人很懒什么都没有留下')
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='moreinfo')
    usercreated = models.DateTimeField (default=timezone.now, verbose_name=u'创建时间')
    appreciate = models.ManyToManyField (User, related_name='appreciate', verbose_name=u'赞赏', blank=True)
    appreciate_count = models.IntegerField (verbose_name=u'点赞个数', default=0)
    follow = models.ManyToManyField (User, related_name='follow', verbose_name=u'关注', blank=True)

    def __str__(self):
        return 'user {}'.format (self.user.username)
