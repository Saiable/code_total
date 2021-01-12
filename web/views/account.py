#!/usr/bin/env python
'''
用户账户相关的功能：注册、短信、登陆、注销
'''
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm, SendSmsForm, LoginSMSForm
from web import models


def register(request):
    '''注册'''
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})
    # print(request.POST)

    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证通过后，写入数据库(密码钥匙密文)
        # form.instance.password = "sdlfhsikdfsjdolfso"
        instance = form.save()
        # data = form.cleaned_data
        # data.pop('code')
        # data.pop('confirm_passwords')
        # instance = models.UserInfo.objects.create(**data)
        return JsonResponse({'status': True, 'data': '/login/'})
    return JsonResponse({'status': False, 'error': form.errors})


def send_sms(request):
    '''发送短信'''
    # mobile_phone = request.GET.get('mobile_phone')
    # tpl = request.GET.get('tpl')
    # print(request.GET)
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号不能为空、格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def login_sms(request):
    '''短信登陆'''
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request, 'login_sms.html', {'form': form})

    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # 用户输入正确，登陆成功
        user_object = form.cleaned_data['mobile_phone']
        # 用户信息放入session
        # print(user_object)
        request.session['user_id'] = user_object.id
        request.session['user_name'] = user_object.username

        return JsonResponse({'status': True, 'data': "/index/"})
    return JsonResponse({'status': False, 'error': form.errors})
