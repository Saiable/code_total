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
import datetime


class Trace(object):
    def __init__(self):
        self.user = None
        self.price_policy = None
        self.project = None


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        request.tracer = Trace()

        # 如果用户已登陆，则在request中赋值，否则设置为0
        user_id = request.session.get('user_id', 0)
        user_object = models.UserInfo.objects.filter(id=user_id).first()

        request.tracer.user = user_object
        # 白名单，没有登陆都可以访问的url
        '''
            1.获取当前用户访问的url
            2.检查url是否在白名单中，如果在则可以继续访问，否则进行判断是否已登录
        '''
        # print(request.path_info)
        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return
        # 检查用户是否已登陆，已登陆继续往后走，未登陆则返回登陆页面
        if not request.tracer.user:
            return redirect('web:login')

        # 登陆成功后，访问后台管理时，获取当前用户所拥有的额度
        # 方式一：免费额度在交易记录中存储

        # 获取当前用户ID值最大（最近交易记录）
        _object = models.Transaction.objects.filter(user=user_object, status=2).order_by('-id').first()
        # 判断是否已过期
        current_datetime = datetime.datetime.now()
        if _object.end_datetime and _object.end_datetime < current_datetime:
            # 过期
            _object = models.Transaction.objects.filter(user=user_object, status=2, price_policy__category=1).first()
        # request.transaction = _object
        request.tracer.price_policy = _object.price_policy
        '''

        # 方式二：免费额度存储在配置文件
        _object = models.Transaction.objects.filter(user=user_object, status=2).order_by('-id').first()
        if not _object:
            # 没有购买
            request.price_policy = models.PricePolicy.objects.filter(category=1, title='个人免费版').first()
        else:
            # 付费版
            current_datetime = datetime.datetime.now()
            if _object.end_datetime and _object.end_datetime < current_datetime:
                # 过期
                request.price_policy = models.PricePolicy.objects.filter(category=1, title='个人免费版').first()
            else:
                request.price_policy = _object.price_policy

        '''

    def process_view(self, request, view, args, kwargs):
        # 判断url是否以manage开头
        if not request.path_info.startswith('/web/manage/'):
            return
        # 判断project_id是我创建的 or 我参与的
        project_id = kwargs.get('project_id')
        # 是否是我创建的
        project_object = models.Project.objects.filter(creator=request.tracer.user, id=project_id).first()
        if project_object:
            request.tracer.project = project_object
            return
        # 是否是我参与的
        project_user_object = models.ProjectUser.objects.filter(user=request.tracer.user, project_id=project_id).first()
        if project_user_object:
            request.tracer.project = project_user_object.project
            return
        return redirect('web:project_list')
