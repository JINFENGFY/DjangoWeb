from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from learning_log.models import Category
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

#dispatch 为所有方法添加修饰器， 例如‘get’，为单一方法提供修饰器，也可以放在方法头
@method_decorator(login_required(),name='dispatch')
class DetailedTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        comment=topic.comment_set.values('commentcontent')

        return render(request,'topic.html',{'topic':topic,'comment':comment})

@method_decorator(login_required(),name='dispatch')
class NewTopic (View):
    def get(self,request):
        add_topic=TopicForm()
        categories = Category.objects.all ()
        return render(request,'addnewtopic.html',{'add_topic_form':add_topic,
                                                  'categories':categories})

    def post(self,request):
        form=TopicForm(request.POST)
        category = request.POST.getlist ("category")

        if form.is_valid():
            add_topic=form.save(commit=False)
            add_topic.categories.add(category)
            add_topic.owner=request.user
            add_topic.save()
            return HttpResponseRedirect(reverse('learning_log:topics'))

@method_decorator(login_required(),name='dispatch')
class EditTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        form=TopicForm(instance=topic)

        return render(request,'edittopic.html',{'topic':topic,'form':form})

    def post(self,request,topic_id):
        topic = LearningContent.objects.get (lnum=topic_id)
        form=TopicForm(instance=topic,data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('learning_log:topic',args=[topic_id]))