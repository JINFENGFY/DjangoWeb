#coding=utf-8

from django.conf.urls import url

from learning_log import views

app_name='learning_log'
urlpatterns =[
    #显示主页
    url(r'^$',views.Index.as_view(),name='index'),

    #显示所有公开学习笔记
    url(r'^topics/(?P<page_num>\d+)/$',views.Topic.as_view(),name='topics'),

    #显示特定的读书笔记
    url(r'^topic/(?P<topic_id>\d+)/$',views.DetailedTopic.as_view(),name='topic'),

    #显示我的学习笔记
    url(r'^show_my_topics/(?P<page_num>\d+)/$',views.ShowMyTopics.as_view(),name='mytopic'),

    #增加新笔记
    url(r'^add_new_topic/$',views.NewTopic.as_view(),name='newtopic'),

    #编辑笔记
    url(r'^edit_topic/(?P<topic_id>\d+)/$',views.EditTopic.as_view(),name='edittopic'),

    #删除笔记
    url(r'^del_topic/(?P<topic_id>\d+)/$',views.DelTopic.as_view(),name='deltopic'),

    #根据分类信息查找
    url(r'orderby_category/(?P<category_id>\d+)/(?P<page_num>\d+)/$',views.OrCategory.as_view(),name='category')
]