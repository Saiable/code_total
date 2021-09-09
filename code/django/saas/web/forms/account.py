# 引入ModelForm模块
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# 自定义注册model类
class RegisterModelForm(forms.ModelForm):
    # 变量名要和model中的保持一致
    # validator中，可以放一个或多个正则表达式
    # RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息
    mobile_phone = forms.CharField(label='手机号', validators=[
        RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])
    # 重写密码字段
    password = forms.CharField(label='密码', widget=forms.PasswordInput())  # 重复密码
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    # 验证码
    code = forms.CharField(label='验证码')

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)