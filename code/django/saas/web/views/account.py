"""用户账户相关的功能：注册、短信、登录、注销"""
from django.shortcuts import render,HttpResponse
from web.forms.account import RegisterModelForm,SendSmsForm,LoginSMSForm
from django.conf import settings
from django.http import JsonResponse
from web import models

def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    # print(request.POST)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证通过，写入数据库，密码要是密文
        instance = form.save()
        # data = form.cleaned_data
        # data.pop('code')
        # data.pop('confirm_password')
        # instance = models.UserInfo.objects.create(**data)
        return JsonResponse({'status': True,'data':'/login/'})
    else:
        # print(form.errors)
        return JsonResponse({'status': False, 'error': form.errors})
    return JsonResponse({})
def send_sms(request):
    # mobile_phone = request.GET.get('mobilePhone')
    # tpl = request.GET.get('tpl')
    # template_id = settings.TENCENT_SMS_TEMPLATE[tpl]
    print(request.GET)
    # 实例化Form对象，实例化时，会执行该对象的init方法
    form = SendSmsForm(request, data=request.GET)
    # print(form.is_valid())
    # 只校验手机号不能为空，格式是否正确
    if form.is_valid():
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})
def login_sms(request):
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request,'web/login_sms.html',{'form':form})
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # user_object = form.cleaned_data['mobile_phone']
        mobile_phone = form.cleaned_data.get('mobile_phone')
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        # 用户信息放入session
        # print(user_object)
        request.session['user_id'] = user_object.id
        request.session['user_name'] = user_object.user_name

        return JsonResponse({'status': True,'data':'/index/'})
    return JsonResponse({'status': False, 'error': form.errors})