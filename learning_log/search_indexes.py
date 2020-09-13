# coding=utf-8
from haystack import indexes
from .models import *


# 注意格式（模型类名+Index）
class LearningContentIndex (indexes.SearchIndex, indexes.Indexable):
    # 对现在来说是固定句式
    text = indexes.CharField (document=True, use_template=True)

    # 给title,content设置索引
    title = indexes.NgramField (model_attr='title')
    content = indexes.NgramField (model_attr='content')

    def get_model(self):
        return LearningContent

    # 最终查询的结果集
    def index_queryset(self, using=None):
        return self.get_model ().objects.order_by ('-createdTime')
