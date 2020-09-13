from django.contrib import admin
from .models import *


# 为后台站点提供样式
class Learning_log_Admin (admin.ModelAdmin):
    # 显示表格列表字段
    list_display = ('title', 'owner', 'createdTime',)
    # 条件查询字段
    list_filter = ('createdTime', 'owner',)
    # 搜索框中根据某些字段进行查询
    search_fields = ('title', 'content',)
    # 在admin后台类中加入下面的字段会显示外键的详细信息
    raw_id_fields = ('owner',)
    # 以某个日期字段分层次查询
    date_hierarchy = 'createdTime'
    # 排序字段
    ordering = ['-createdTime']


# Register your models here.
admin.site.register (Category),
admin.site.register (LearningContent, Learning_log_Admin),
