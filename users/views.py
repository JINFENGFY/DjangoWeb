from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse


# Create your views here.
class Register (View):
    form1 = UserCreationForm ()

    def get(self,request):
        return render(request,'register.html',{'form':self.form1})

    def post(self,request):
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()

            #自动登录
            authenticated_user=authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_log:index'))
        return render(request,'register.html',{'form':self.form1})