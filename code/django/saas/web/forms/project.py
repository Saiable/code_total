#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-07 9:01
@func:

'''

from django import forms
from web.forms.bootstrap import BootstrapForm
from web import models
from django.core.exceptions import ValidationError
from web.forms.widgets import ColorRadioSelect

class ProjectModelForms(BootstrapForm, forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea())
    bootstrap_class_exclude = ['color']

    class Meta:
        model = models.Project
        fields = ['name', 'color', 'desc']
        widgets = {
            'desc': forms.Textarea,
            'color': ColorRadioSelect(attrs={'class':'color-radio'}),
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_name(self):
        '''项目校验'''
        name = self.cleaned_data['name']
        # 1.当前用户是否已经创建过此项目
        exists = models.Project.objects.filter(name=name,creator=self.request.tracer.user).exists()
        if exists:
            raise ValidationError('项目名已存在')
        # 2.当前用户是否还有额度进行创建项目
        # 最多创建N个项目
        max_num = self.request.tracer.price_policy.project_num
        # 现在已创建多少项目
        count = models.Project.objects.filter(creator=self.request.tracer.user).count()

        if count >= max_num:
            raise ValidationError('项目个数超限，请购买套餐')
        return name
