from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User_more_info


# 定义一个行内 admin
class MoreInfoInline (admin.StackedInline):
    model = User_more_info
    can_delete = False
    verbose_name_plural = 'User_more_info'


# 将 MoreInfoInline 关联到 User 中
class UserAdmin (BaseUserAdmin):
    inlines = (MoreInfoInline,)


# 重新注册 User
admin.site.unregister (User)
admin.site.register (User, UserAdmin)
