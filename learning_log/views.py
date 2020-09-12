from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from learning_log.models import Category
from comment.form import CommentForm
from comment.models import Comment
from .forms import *
from django.urls import reverse
from .functions import *
import markdown


# Create your views here.
#显示主页
class Index (View):
    def get(self,request):
        return render (request, 'index.html')

#显示所有项目
class Topic (View):
    def get(self,request,page_num):
        #获取数据
        topics = LearningContent.objects.filter (private=1).order_by ('-createdTime')

        #调用自定义分页器
        pager,curpage_data=MyPager(topics,page_num,3)

        return render(request,'topics.html',{'pager':pager,'curpage_data':curpage_data,
                                             'page_num':int(page_num)})

class DetailedTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        topic.content=markdown.markdown(topic.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                        ])

        log = LearningContent.objects.get (lnum=topic_id)
        result = log.users_like.filter (username=request.user)
        comment_form=CommentForm()
        comment=Comment.objects.filter(learning_log=topic_id)
        flag=False
        if result:
            flag=True
        return render(request,'topic.html',{'topic':topic,
                                            'flag':flag,
                                            'comment_form':comment_form,
                                            'comment':comment})

def likeor_not(request):
    #接收参数
    likeornot=request.GET.get('likeornot')
    user=request.user
    learninglog_id=request.GET.get('learninglog_id')

    log = LearningContent.objects.get (lnum=learninglog_id)
    result = log.users_like.filter(username=user)

    if likeornot == "True":
        if result:
            return HttpResponse()
        else:
            log.users_like.add(user)
            log.like_count=log.like_count + 1
            log.save()
            return HttpResponse()
    else:
       log.users_like.remove(user)
       log.like_count = log.like_count - 1
       log.save ()
       return HttpResponse()

# dispatch 为所有方法添加修饰器， 例如‘get’，为单一方法提供修饰器，也可以放在方法头
@method_decorator (login_required (), name='dispatch')
class ShowMyTopics (View):
    def get(self,request,page_num):
        user=User.objects.get(username=request.user)
        mytopics=LearningContent.objects.filter(owner=user.id).order_by('-createdTime')
        #清除标题中的用户名（更加美观）
        len_user='5,-'+str(len(user.username)+5)

        pager,curpage_data=MyPager(mytopics,page_num,3)
        return render(request,'showmytopics.html',{'pager':pager,'curpage_data':curpage_data,
                                                   'len_user':len_user,'page_num':int(page_num)})

@method_decorator(login_required(),name='dispatch')
class NewTopic (View):
    def get(self,request):
        add_topic=TopicForm()
        categories = Category.objects.all ()
        return render(request,'addnewtopic.html',{'add_topic_form':add_topic,
                                                  'categories':categories})

    def post(self,request):
        form=TopicForm(request.POST)
        #返回的值必需能转换为int类型
        category = request.POST.getlist("category")

        if form.is_valid():
            add_topic=form.save(commit=False)
            add_topic.owner=request.user
            add_topic.save()

            #一定要先保存主体后再进行对多对多关系得保存，不然主题还没有生成主键
            #参考解决https://blog.csdn.net/fengyu09/article/details/17434795
            add_topic.categories.add (*category)
            return HttpResponseRedirect(reverse('learning_log:topics',args=[1]))

@method_decorator(login_required(),name='dispatch')
class EditTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        form=TopicForm(instance=topic)
        categories=Category.objects.all ()
        category=topic.categories.all()

        return render(request,'edittopic.html',{'topic':topic,'form':form,
                                                'categories':categories,
                                                'category':category})

    def post(self,request,topic_id):
        category = request.POST.getlist ("category")
        topic1 = LearningContent.objects.get (lnum=topic_id)

        #先删除掉多对多关系数据，再存储
        topic1.categories.clear()
        form=TopicForm(instance=topic1,data=request.POST)
        topic_img_old = topic1.content
        print (topic_img_old)
        if form.is_valid():
            fo=form.save(commit=False)
            fo.save()
            fo.categories.add (*category)

            # 更新图片
            topic2 = LearningContent.objects.get (lnum=topic_id)
            topic_img_new =topic2.content
            print(topic_img_new)
            delimg(topic_img_new,topic_img_old)

            return HttpResponseRedirect(reverse('learning_log:topic',args=[topic_id]))

@method_decorator(login_required(),name='dispatch')
class DelTopic (View):
    def get(self,request,topic_id):
        topic=LearningContent.objects.get(lnum=topic_id)
        #物理删除图片
        delimg(topic.content)
        topic.delete()

        return HttpResponseRedirect(reverse('learning_log:topics',args=[1]))

class OrCategory(View):
    def get(self,request,category_id,page_num):
        topics=LearningContent.objects.filter(categories=category_id).order_by('-createdTime')

        cate_name=Category.objects.get(cnum=category_id)

        pager, curpage_data = MyPager (topics, page_num, 3)
        return render(request,'show_category.html',{'pager':pager,'curpage_data':curpage_data,
                                             'page_num':int(page_num),'category_id':category_id,
                                                    'cate_name':cate_name})

class OrHotlog(View):
    def get(self,request,hotlog_id):
        topic=LearningContent.objects.get(lnum=hotlog_id)

        log = LearningContent.objects.get (lnum=hotlog_id)
        result = log.users_like.filter (username=request.user)
        flag = False
        if result:
            flag = True
        return render(request,'show_hotlog.html',{'topic':topic,'flag':flag})


