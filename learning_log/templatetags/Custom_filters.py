# coding=utf-8
from django.template import Library

#获得过滤器对象
register = Library ()

# 剪切字符串
@register.filter
def split_str(value, args):
    start, end = args.split (',')
    result = str (value)
    length = len (result)
    if end == '':
        return result[int (start):length]
    return result[int (start):int (end)]


# 剪切字符串，剩余部分用省略号代替
@register.filter
def split_str_cut(value, args):
    lens = int (args)
    result = str (value)
    length = len (result)
    return result[:lens] + '...'

#过滤markdown语法
@register.filter
def markdown(value):
    import markdown
    return markdown.markdown (value)
