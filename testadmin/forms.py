#coding=utf-8
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()

#上传文档
class UploadFileForm(forms.Form):
    uploadfile = forms.FileField()

#创建数据库
class CreateDatabaseInfoForm(forms.Form):
    name = forms.CharField(required=True)
    account = forms.CharField(required=True)
    password = forms.CharField(required=True)
    address = forms.CharField(required=True)

#创建系统
class CreateSystemInfoForm(forms.Form):
    name = forms.CharField(required=True)
    address = forms.URLField(required=True)
    account = forms.CharField(required=True)
    password = forms.CharField(required=True)
    database_name = forms.CharField(required=True)
    remark = forms.Textarea()
class CreateTestCaseForm(forms.Form):
    project_name = forms.CharField(required=True)
    number = forms.CharField(required=True)
    function_model = forms.CharField(required=True)
    title = forms.CharField(required=True)
    precondition = forms.CharField(widget=forms.Textarea)
    procedure = forms.CharField(widget=forms.Textarea)
    ex_result = forms.CharField(widget=forms.Textarea)
    grade = forms.CharField(required=True)