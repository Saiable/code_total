#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-04 20:37
@func: 用户登陆状态校验

'''

from django.utils.deprecation import MiddlewareMixin
from web import models
from django.shortcuts import redirect
from django.conf import settings

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 如果用户已登陆，则在request中赋值，否则设置为0
        user_id = request.session.get('user_id',0)

        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object
        # 白名单，没有登陆都可以访问的url
        '''
            1.获取当前用户访问的url
            2.检查url是否在白名单中，如果在则可以继续访问，否则进行判断是否已登录
        '''
        # print(request.path_info)
        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return
        # 检查用户是否已登陆，已登陆继续往后走，未登陆则返回登陆页面
        if not request.tracer:
            return redirect('web:login')