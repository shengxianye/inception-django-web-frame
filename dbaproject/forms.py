# -*- coding:utf-8 -*-
#coding=utf-8
from django import forms

class InceptionTableStructure(forms.Form):
    subject = forms.CharField(initial='ospxxxx')
    ip = forms.CharField(initial='mysql服务器地址')   
    port = forms.CharField(initial='mysql服务器端口')
    dbname = forms.CharField(initial='数据库名')
    sql = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':6}))


#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/
#about django forms.value 
