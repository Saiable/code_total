#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-05 12:49
@func:

'''
import django,os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','saas.settings')
django.setup()