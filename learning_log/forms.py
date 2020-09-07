#coding=utf-8
from django import forms
from mdeditor.fields import MDTextFormField

from .models import LearningContent

class TopicForm(forms.ModelForm):
    class Meta:
        model=LearningContent

        fields=('title','private','content')
        labels={'private':u'是否公开'}
