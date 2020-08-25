#coding=utf-8

from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

app_name='users'

urlpatterns =[
    #登录页面
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login'),

    #退出
    url(r'loginout/$',LogoutView.as_view(),name='loginout')
]