# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from learning_log.models import LearningContent
from notifications.models import *

@method_decorator (login_required (), name='dispatch')
class CommentNoticeListView (LoginRequiredMixin, ListView):
    """通知列表"""
    # 上下文的名称
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notics.html'
    # 登录重定向
    login_url = '/users/login/'

    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notifications.unread ()

@method_decorator (login_required (), name='dispatch')
class CommentNoticeUpdateView (View):
    """更新通知状态"""

    # 处理 get 请求
    def get(self, request):
        # 获取未读消息
        notice_id = request.GET.get ('notice_id')

        # 删除数据库中的已读记录
        Notification.objects.filter (unread=0).delete ()

        # 更新单条通知
        if notice_id:
            learning_log = LearningContent.objects.get (lnum=request.GET.get ('topic_id'))
            request.user.notifications.get (id=notice_id).mark_as_read ()

            return redirect (reverse ('learning_log:topic', args=[learning_log.lnum]))
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read ()
            return redirect (reverse ('learning_log:topics', args=[1]))
