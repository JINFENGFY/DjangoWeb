#coding=utf-8

from django.conf.urls import url

from learning_log import views

app_name='learning_log'
urlpatterns =[
    #显示主页，显示所有项目
    url(r'',views.Index.as_view(),name='index'),
]