#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-05 8:46
@func: 价格策略离线脚本

'''

import base
from web import models

def run():
    exsits = models.PricePolicy.objects.filter(category=1,title='个人免费版').exists()
    if not exsits:
        models.PricePolicy.objects.create(
            category=1,
            title='个人免费版',
            project_num=3,
            project_member=3,
            project_space=20,
            per_file_size=5,
        )


if __name__=='__main__':
    run()
