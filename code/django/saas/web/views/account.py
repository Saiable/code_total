"""用户账户相关的功能：注册、短信、登录、注销"""
from django.shortcuts import render
from web.forms.account import RegisterModelForm,SendSmsForm
from django.conf import settings
from django.http import JsonResponse


def register(request):
    form = RegisterModelForm()
    return render(request, 'web/register.html', {'form': form})


def send_sms(request):
    mobile_phone = request.GET.get('mobilePhone')
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE[tpl]

    # 实例化Form对象，实例化时，会执行该对象的init方法
    form = SendSmsForm(request, data=request.GET)
    # print(form.is_valid())
    # 只校验手机号不能为空，格式是否正确
    if form.is_valid():
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})
