#coding=utf-8
from .models import User_more_info
from django import forms

class MoreInfoFrom(forms.ModelForm):
    class Meta:
        model=User_more_info
        fields=('gender','phone','brief_introduction')