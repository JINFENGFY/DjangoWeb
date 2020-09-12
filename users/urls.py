#coding=utf-8

from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from users import views

app_name='users'

urlpatterns =[
    #用户注册
    url(r'^register/$',views.Register.as_view(),name='register'),

    #登录页面
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login'),

    #退出
    url(r'loginout/$',LogoutView.as_view(),name='loginout'),

    #删除用户
    url(r'userdel/$',views.UserDel.as_view(),name='userdel'),

    #访问用户首页
    url(r'userhomepage/(?P<user_id>\d+)/(?P<page_num>\d+)/$',views.UserHome.as_view(),name='userhome'),

    #处理用户点赞
    url(r'^userlike/$',views.userlike,name='userlike'),

    #处理用户关注
    url(r'^follow/$',views.userfollow,name='follow'),
]