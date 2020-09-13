# coding=utf-8
from django.db.models import Count
from .models import *

#侧边栏全局上下文
def Side_navigation_bar_data(request):
    # 分类归档
    categories = LearningContent.objects.values ('categories__category', 'categories').annotate (
        c=Count ('*')).order_by ('-c')

    # 热点文章
    hot_log = LearningContent.objects.values ('lnum', 'title', 'like_count').order_by ('-like_count')[:5]
    return {'Side_nav_categories': categories, 'Side_nav_hot': hot_log}
