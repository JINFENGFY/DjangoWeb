from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import *
from django.urls import reverse
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


class NewTopic (View):
    def get(self,request):
        add_topic=TopicForm()
        return render(request,'addnewtopic.html',{'add_topic_form':add_topic})

    def post(self,request):
        form=TopicForm(request.POST)

        if form.is_valid():
            add_topic=form.save(commit=False)
            add_topic.owner=request.user
            add_topic.save
            return HttpResponseRedirect(reverse('learning_log:topics'))