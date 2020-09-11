#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#拓展的用户信息
class User_more_info(models.Model):
    gender=models.CharField(max_length=10,choices=(('male','男'),('female','女')),default='male',verbose_name=u'性别')
    phone=models.CharField(max_length=20,blank=True,verbose_name=u'电话号码')
    brief_introduction=models.TextField(max_length=500,blank=True,verbose_name=u'简介')
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='moreinfo')

    def __str__(self):
        return 'user {}'.format(self.user.username)

