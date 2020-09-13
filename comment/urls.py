# coding=utf-8
from django.conf.urls import url
from comment import views


urlpatterns = [
    # 评论
    url (r'^log_comment/(?P<topic_id>\d+)/$',
         views.ShowComments.as_view (),
         name='log_comment'
         ),

    # 二级评论
    url (r'log_comment/(?P<topic_id>\d+)/(?P<parent_comment_id>\d+)/$',
         views.ShowComments.as_view (),
         name='comment_reply'
         )
]
