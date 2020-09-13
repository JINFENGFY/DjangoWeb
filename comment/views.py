#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from notifications.signals import notify
from .models import Comment
from learning_log.models import LearningContent
from .form import CommentForm
from django.views import View


# Create your views here.
#评论视图
class ShowComments (View):
    def get(self, request, topic_id, parent_comment_id=None):
        comment_form = CommentForm ()
        content={'comment_form': comment_form,
                 'topic_id': topic_id,
                 'parent_comment_id': parent_comment_id
                 }
        return render (request, 'reply.html',content)

    def post(self, request, topic_id, parent_comment_id=None):
        learning_log = get_object_or_404 (LearningContent, lnum=topic_id)
        comment_form = CommentForm (request.POST)
        if comment_form.is_valid ():
            new_comment = comment_form.save (commit=False)
            new_comment.learning_log = learning_log
            new_comment.owner = request.user

            # 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get (comnum=parent_comment_id)
                # 评论层级限制在二级，超过二级则转换为二级
                new_comment.parent_id = parent_comment.get_root ().comnum
                # 记录超过三级的回复的正真回复人
                new_comment.reply_to = parent_comment.owner
                new_comment.save ()
                # 给被评论用户发送通知
                if not parent_comment.owner.is_superuser \
                        and not \
                        parent_comment.owner == request.user:
                    #发送消息提醒被评论
                    notify.send (request.user,
                                 recipient=parent_comment.owner,
                                 verb='{0}在文章{1}回复了你的评论'.format (request.user, learning_log.title),
                                 target=learning_log,
                                 action_object=new_comment,
                                 description='comment',
                                 )
                return HttpResponse ('success')
            new_comment.save ()

            # 发送消息提醒评论
            if not request.user == learning_log.owner:
                notify.send (request.user,
                             recipient=learning_log.owner,
                             verb='{0}评论了你的文章《{1}》'.format (request.user, learning_log.title),
                             target=learning_log,
                             action_object=new_comment,
                             description='comment',
                             )
            return HttpResponse ('success')
        else:
            return HttpResponse ('表单有错误')
