# coding=utf-8
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
import re
import os
from DjangoWeb.settings import MEDIA_ROOT


# 将整个learning_log所用到的自定义方法整合到一个文件中
# 分页器
def MyPager(data, page_num, perpage):
    #获取当前页数
    int_num = int (page_num)
    # 创建分页器对象
    pager = Paginator (data, perpage)
    # 获取当前页数据
    try:
        curpage_data = pager.page (int_num)
    except PageNotAnInteger:
        curpage_data = pager.page (1)
    # 输入越界
    except EmptyPage:
        curpage_data = pager.page (pager.num_pages)

    return pager, curpage_data


# 更新图片（最新图片列表，旧的图片列表）
def delimg(post, *args):
    pattern = re.compile (r'\w*\.(?:jpg|png|gif|bmp)')
    imagename = pattern.findall (post)
    if args:
        imagename_old = pattern.findall (args[0])
        for i in imagename:
            for j in imagename_old:
                if i == j:
                    imagename_old.remove (j)
        if imagename_old:
            for image in imagename_old:
                imageurl = os.path.join (MEDIA_ROOT, 'editor\\' + image)
                os.remove (imageurl)
    elif imagename:
        for image in imagename:
            imageurl = os.path.join (MEDIA_ROOT, 'editor\\' + image)
            os.remove (imageurl)
    else:
        pass
