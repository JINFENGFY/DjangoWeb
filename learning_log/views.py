from django.shortcuts import render
from .models import *
from django.views import View
# Create your views here.

#显示主页
class Index (View):
    def get(self,request):
        return render (request, 'index.html')

#显示所有项目
class Topic (View):
    def get(self,request):
        topics=LearningContent.objects.all().order_by('-createdTime')
        return render(request,'topics.html',{'topics':topics})


class DetailedTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        comment=topic.comment_set.values('commentcontent')

        return render(request,'topic.html',{'topic':topic,'comment':comment})