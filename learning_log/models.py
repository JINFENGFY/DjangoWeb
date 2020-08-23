#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#类型模型
class Category (models.Model):
    cnum=models.AutoField(primary_key=True)
    category=models.CharField(max_length=10,unique=True,verbose_name=u'类别')


    def __str__(self):
        return u'类型:%s' % self.category

#学习笔记主体模型
class LearningContent(models.Model):
    lnum=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30,verbose_name=u'题目')
    content=models.TextField(verbose_name=u'内容')
    createdTime=models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='learning_log',verbose_name=u'所有者')
    categories=models.ManyToManyField(Category,verbose_name=u'类型')

    def __str__(self):
        return u'学习笔记:%s--%s' % (self.title, self.owner)

#评论模型
class Comment(models.Model):
    comnum=models.AutoField(primary_key=True)
    commentcontent=models.TextField(verbose_name=u'评论内容')
    owner = models.ForeignKey (User, on_delete=models.CASCADE, verbose_name=u'所有者')
    learning_log = models.ForeignKey (LearningContent,on_delete=models.CASCADE,verbose_name=u'所有贴')

    def __str__(self):
        return u'评论:%s--%s--%s' % (self.commentcontent, self.learning_log.title,self.owner)
