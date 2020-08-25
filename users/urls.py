#coding=utf-8

from django.conf.urls import url
from django.contrib.auth.views import LoginView

app_name='users'

urlpatterns =[
    #登录页面
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login')
]