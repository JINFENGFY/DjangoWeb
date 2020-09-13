# coding=utf-8
from django.conf.urls import url
from . import views

app_name = 'notice'
urlpatterns = [
    # 通知列表
    url ('list/', views.CommentNoticeListView.as_view (), name='list'),
    #更新通知
    url ('update/', views.CommentNoticeUpdateView.as_view (), name='update'),
]
