#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-05 8:46
@func:

'''

import django,os,sys

# 获取saas的总目录的路径，并添加到环境变量中
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 模拟manage.py，加载配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE','saas.settings')
django.setup()


from web import models
# 新增数据
models.UserInfo.objects.create(username='testaa',email='jkjk@qq.com',mobile_phone='123123',password='123123')