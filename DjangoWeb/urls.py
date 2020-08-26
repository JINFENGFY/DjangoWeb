#coding=utf-8
"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from logging import DEBUG

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    #主页
    url(r'',include(('learning_log.urls','learning_log'),namespace='learning_log')),

    #用户
    url(r'^users/',include(('users.urls','users'),namespace='users')),

    #富文本编辑器
    url(r'^tinymce/', include('tinymce.urls')),


]
