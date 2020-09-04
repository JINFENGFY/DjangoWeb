#coding=utf-8
from django.db.models import Count

from .models import *

def Side_navigation_bar_data(request):
    #分类归档
    categories=LearningContent.objects.values('categories__category','id')\
        .annotate(c=Count('*')).order_by('-c')

    #近期文章
    recent_log=LearningContent.objects.all().order_by('-createdTime')[0:5]

    return {'Side_nav_categories':categories,'Side_nav_recentlog':recent_log}
