#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-04 16:39
@func:

'''
from django.shortcuts import render

def index(request):

    return render(request,'web/index.html')