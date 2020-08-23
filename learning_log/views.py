from django.shortcuts import render
from .models import *

# Create your views here.
#显示主页，显示所有项目
from django.views import View


class Index (View):
    def get(self,request):
        post = LearningContent.objects.all ()
        return render (request, 'index.html', {'post': post})