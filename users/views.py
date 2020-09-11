from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from .forms import MoreInfoFrom


# Create your views here.
class Register (View):
    form1 = UserCreationForm ()
    form2 = MoreInfoFrom()
    flag=True

    def get(self,request):
        return render(request,'register.html',{'form1':self.form1,'form2':self.form2,'flag':self.flag})

    def post(self,request):
        form_user=UserCreationForm(data=request.POST)
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