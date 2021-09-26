#!/usr/bin/env python
# encoding: utf-8
'''
@author: huihui
@time: 2021-09-27 6:44
@func:初始化字段，给字段添加bootstrap类

'''
class BootstrapForm(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)