# coding=utf-8
from django import forms

SEX_CHOICES=(
    ("leve1","男"),
    ("leve2","女"),
)

class UserForm(forms.Form):
    name = forms.CharField(max_length=100,label="姓名")
    sex = forms.ChoiceField(choices=SEX_CHOICES,label="性别")
    telephone = forms.CharField(max_length=12,label="手机号码")
    mail = forms.EmailField(label="电子邮件")
