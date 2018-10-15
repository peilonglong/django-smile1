#! /usr/bin/python
# -*- coding:utf-8 -*-

from django.forms import forms


# view 对应的所有 Form 表单
class BorrowerForm(forms.Form):
    bookNo = forms.CharField()
    title = forms.CharField()
    email = forms.EmailField(required=False)
