#coding=utf-8
from django import forms
from .models import LearningContent

class TopicForm(forms.ModelForm):
    class Meta:
        model=LearningContent

        fields=('title','content',)
        labels={'title':'题目','content':'内容'}
        widgets={'content':forms.Textarea(attrs={'cols':80})}
