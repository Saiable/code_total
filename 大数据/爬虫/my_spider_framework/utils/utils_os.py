import os

# 文件夹相关操作

def my_mkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        pass
