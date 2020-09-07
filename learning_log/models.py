#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mdeditor.fields import MDTextField

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
    content=MDTextField(null=True,blank=True,verbose_name=u'内容')
    createdTime=models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
    private=models.BooleanField(default=False,verbose_name=u'是否公开')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='learning_log',verbose_name=u'所有者')
    categories=models.ManyToManyField(Category,verbose_name=u'类型')
    users_like=models.ManyToManyField(User,related_name='log_like',verbose_name=u'点赞用户',blank=True)
    like_count=models.IntegerField(verbose_name=u'点赞个数',default=0)

#参考https://www.cnblogs.com/yunweiqiang/p/7391259.html
    def __str__(self):
        try:
            return u'学习笔记:%s-----%s' % (self.title, self.owner)
        except User.DoesNotExist:
            return u'学习笔记:%s' % (self.title,)

#评论模型
class Comment(models.Model):
    comnum=models.AutoField(primary_key=True)
    commentcontent=models.TextField(verbose_name=u'评论内容')
    owner = models.ForeignKey (User, on_delete=models.CASCADE, verbose_name=u'所有者')
    learning_log = models.ForeignKey (LearningContent,on_delete=models.CASCADE,verbose_name=u'所有贴')

    def __str__(self):
        return u'评论:%s--%s--%s' % (self.commentcontent, self.learning_log.title,self.owner)
