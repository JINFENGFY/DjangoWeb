from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Comment
from  learning_log.models import LearningContent
from django.contrib.auth.models import User
from .form import CommentForm
from django.views import View

# Create your views here.
class ShowComments(View):
    def get(self,request,topic_id,parent_comment_id=None):
        comment_form=CommentForm()
        return render(request,'reply.html',{'comment_form':comment_form,
                                            'topic_id':topic_id,
                                            'parent_comment_id':parent_comment_id})

    def post(self,request,topic_id,parent_comment_id=None):
        learning_log = get_object_or_404 (LearningContent, lnum=topic_id)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.learning_log=learning_log
            new_comment.owner=request.user

            #二级回复
            if parent_comment_id:
                parent_comment=Comment.objects.get(comnum=parent_comment_id)
                #评论层级限制在二级，超过二级则转换为二级
                new_comment.parent_id=parent_comment.get_root().comnum
                #记录超过三级的回复的正真回复人
                new_comment.reply_to=parent_comment.owner
                new_comment.save()
                return HttpResponse('success')

            new_comment.save()
            return HttpResponse('success')
        else:
            return HttpResponse('表单有错误')