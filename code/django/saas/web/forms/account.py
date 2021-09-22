# 引入ModelForm模块
from django import forms
from web import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings


class SendSmsForm(forms.Form):
    mobile_phone = forms.CharField(label='手机号', validators=[
        RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')])

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # 手机号校验的钩子函数
    def clean_mobile_phone(self):
        moblie_phone = self.cleaned_data('mobile_phone')

        # 判断短信模板是否有问题
        tpl = self.request.GET.get('tpl')
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError('模板错误')

        # 检查数据库中，是否有手机号
        # django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
        exsits = models.UserInfo.objects.filter(moblie_phone=moblie_phone).exists()
        if exsits:
            raise ValidationError('手机号已存在')
        return moblie_phone


# 自定义注册model类
class RegisterModelForm(forms.ModelForm):
    # 变量名要和model中的保持一致
    # validator中，可以放一个或多个正则表达式
    # RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息
    mobile_phone = forms.CharField(label='手机号', validators=[
        RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')])
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
