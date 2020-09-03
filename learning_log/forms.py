#coding=utf-8
from django import forms
from .models import LearningContent

class TopicForm(forms.ModelForm):
    class Meta:
        model=LearningContent

        fields=('title','private')
        labels={'title':'','private':u'是否公开'}

