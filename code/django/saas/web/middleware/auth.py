#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-04 20:37
@func: 用户登陆状态校验

'''

from django.utils.deprecation import MiddlewareMixin
from web import models

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 如果用户已登陆，则在request中赋值，否则设置为0
        user_id = request.session.get('user_id',0)

        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object