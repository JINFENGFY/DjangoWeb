import pytz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from datetime import datetime
from learning_log.functions import MyPager
from learning_log.models import LearningContent
from .forms import MoreInfoFrom,UserCreationExpandFrom
from .models import User_more_info


# Create your views here.
class Register (View):
    form1 = UserCreationExpandFrom ()
    form2 = MoreInfoFrom()
    flag=True

    def get(self,request):
        return render(request,'register.html',{'form1':self.form1,'form2':self.form2,'flag':self.flag})

    def post(self,request):
        form_user=UserCreationExpandFrom(data=request.POST)
        form_info=MoreInfoFrom(data=request.POST)

        if form_user.is_valid() and form_info.is_valid():
            new_user=form_user.save()
            more_info=form_info.save(commit=False)
            more_info.user=new_user
            more_info.save()

            #自动登录
            authenticated_user=authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_log:topics',args=[1]))

        self.flag=False
        return render(request,'register.html',{'form1':self.form1,'form2':self.form2,'flag':self.flag})

@method_decorator (login_required (), name='dispatch')
class UserDel(View):
    def get(self,request):
        user=User.objects.get(id=request.user.id)
        logout(request)
        user.delete()
        return HttpResponseRedirect(reverse('learning_log:index'))


class UserHome(View):
    def get(self,request,user_id,page_num):
        user_page=User.objects.get(id=user_id)
        user_info=User_more_info.objects.get(user_id=user_id)
        result1=user_info.appreciate.filter(username=request.user)
        result2 = user_info.follow.filter (username=request.user)
        flag1=False
        if result1:
            flag1=True
        flag2=False
        if result2:
            flag2=True

        page_owner_topics = LearningContent.objects.filter (owner=user_id).order_by ('-createdTime')
        pager, curpage_data = MyPager (page_owner_topics, page_num, 3)

        years=int((datetime.now().replace(tzinfo=pytz.timezone('UTC'))-user_info.usercreated).total_seconds()/86400+1)
        return render(request,'user_home_page.html',{'user_page':user_page,'user_info':user_info,'years':years,'flag1':flag1,'flag2':flag2,
                                                     'pager':pager,'curpage_data':curpage_data,'page_num':int(page_num)})


def userlike(request):
    # 接收参数
    dianzan = request.GET.get ('dianzan')
    user = request.user
    homepage_owner = request.GET.get ('homepage_owner')
    homepage_ownerobj = User_more_info.objects.get (user_id=homepage_owner)

    if dianzan == "True":
        homepage_ownerobj.appreciate.add (user)
        homepage_ownerobj.appreciate_count = homepage_ownerobj.appreciate_count + 1
        homepage_ownerobj.save ()
        return HttpResponse()
    else:
        homepage_ownerobj.appreciate.remove (user)
        homepage_ownerobj.appreciate_count = homepage_ownerobj.appreciate_count - 1
        homepage_ownerobj.save ()
        return HttpResponse()


def userfollow(request):
    # 接收参数
    guanzhu = request.GET.get ('guanzhu')
    user = request.user
    homepage_owner = request.GET.get ('homepage_owner')

    homepage_ownerobj = User_more_info.objects.get (user_id=homepage_owner)
    result = homepage_ownerobj.follow.filter (username=user)

    if guanzhu == "True":
        homepage_ownerobj.follow.add (user)
        homepage_ownerobj.save ()
        return HttpResponse()
    else:
        homepage_ownerobj.follow.remove (user)
        homepage_ownerobj.save ()
        return HttpResponse()


def modify_data(request,user_id):
    content = User_more_info.objects.filter (user_id=user_id).first ()
    form = MoreInfoFrom (instance=content)

    if request.method=='GET':
        return render (request, 'modify_data.html', {'form':form,'user_id':user_id})
    else:
        form_info = MoreInfoFrom (data=request.POST)
        var = User_more_info.objects.filter (user_id=user_id)
        var.delete()
        if form_info.is_valid ():
            more_info = form_info.save (commit=False)
            more_info.user = request.user
            more_info.save ()

            return HttpResponseRedirect (reverse ('learning_log:topics', args=[1]))
