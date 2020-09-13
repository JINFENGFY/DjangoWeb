# coding=utf-8
from django.contrib.auth.models import User

from .models import User_more_info
from django import forms
from django.contrib.auth.forms import UserCreationForm


# 拓展用户数据表单
class MoreInfoFrom (forms.ModelForm):
    class Meta:
        model = User_more_info
        fields = ('gender', 'phone', 'brief_introduction')


# 内置创建用户表单添加邮箱
class UserCreationExpandFrom (UserCreationForm):
    email = forms.EmailField (label=("邮箱"), widget=forms.EmailInput, help_text='为方便找回密码，请输入一个邮箱')

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, commit=True):
        user = super (UserCreationExpandFrom, self).save (commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save ()
        return user
