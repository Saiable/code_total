#!/usr/bin/env python
'''
用户账户相关的功能：注册、短信、登陆、注销
'''
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from web.forms.account import RegisterModelForm, SendSmsForm, LoginSMSForm, LoginForm
from web import models
from utils.image_code import check_code
from io import BytesIO


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
        print(user_object)
        # request.session['user_id'] = user_object.id
        # request.session['user_name'] = user_object.username

        return JsonResponse({'status': True, 'data': "/index/"})
    return JsonResponse({'status': False, 'error': form.errors})


def login(request):
    '''用户名密码登陆'''
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()

        from django.db.models import Q
        user_object = models.UserInfo.objects.filter(Q(email=username)|Q(mobile_phone=username)).filter(password=password).first()
        if user_object:
            # 用户名密码正确
            return redirect('index')
        form.add_error('username', '用户名密码错误')

    return render(request, 'login.html', {'form': form})


def image_code(request):
    '''生成图片验证码'''

    image_object, code = check_code()
    request.session['image_code'] = code
    # 设置过期时间为60秒
    request.session.set_expiry(60)
    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())
