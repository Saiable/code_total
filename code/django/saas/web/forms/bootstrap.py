#!/usr/bin/env python
# encoding: utf-8
'''
@author: huihui
@time: 2021-09-27 6:44
@func:初始化字段，给字段添加bootstrap类

@time: 2021-10-7 13:14:42
@func:修改：新增  bootstrap_class_exclude = [] 并进行判断
    实例化时，可定义上述bootstrap_class_exclude = ['color'],就可以指定color字段不应用bootstrap样式
'''
class BootstrapForm(object):
    bootstrap_class_exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_class_exclude:
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)