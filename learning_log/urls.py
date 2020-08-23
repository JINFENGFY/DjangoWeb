#coding=utf-8

from django.conf.urls import url

from learning_log import views

app_name='learning_log'
urlpatterns =[
    #显示主页
    url(r'^$',views.Index.as_view(),name='index'),

    #显示所有学习笔记
    url(r'^topic/',views.Topic.as_view(),name='topic')
]