# coding=utf-8
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from DjangoWeb import settings
import notifications.urls

urlpatterns = [path ('admin/', admin.site.urls),

    # 主页
    url (r'', include (('learning_log.urls', 'learning_log'), namespace='learning_log')),

    # 用户
    url (r'^users/', include (('users.urls', 'users'), namespace='users')),

    # 评论
    url (r'comment/', include (('comment.urls', 'comment'), namespace='comment')),

    # 富文本编辑器
    url (r'mdeditor/', include ('mdeditor.urls')),

    # 转到搜索引擎内部
    url (r'search/', include ('haystack.urls')),

    # 消息通知
    url (r'inbox/notifications/', include (notifications.urls, namespace='notifications')),

    # 消息通知处理
    url (r'notice/', include (('notice.urls', 'notice'), namespace='notice')),

    # 重置密码
    url (r'password-reset/', include ('password_reset.urls')), ]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
