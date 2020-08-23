#coding=utf-8

from django.template import Library

register=Library()

#剪切字符串
@register.filter
def split_str(value,args):
    start,end=args.split(',')
    result=str(value)
    length=len(result)
    if end=='':
        return result[int (start):length]
    return result[int(start):int(end)]