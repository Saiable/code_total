[TOC]

## 来源说明

[学习视频网址](https://www.bilibili.com/video/BV1uA411b77M?p=81)



## 项目开发

- 一期：用户认证（短信验证、图片验证码、django ModelForm组件） - 3天
- 二期：wiki、文件、问题管理 - 5~7天
- 三期：支付、部署（linux） - 2天

## Day01.今日概要

### 今日概要

- 虚拟环境（项目环境）
- 项目框架：local_settings
- git实战应用（代码每天都提交）
- 通过python & 腾讯云发送短信

### 1.虚拟环境 virtualenv

- 前提准备：

  安装python：[python官方网站下载](https://www.python.org/downloads/)，选择`Maintenance status`为`security`的下载。（python3.6到2021-12-23就不支持维护了，我电脑上环境是python3.7。）

#### 1.1.安装virtualenv模块

```python
pip3 install virtualenv
```

在本地可以新建文件夹`py_virtual_env`专门管理所有的虚拟环境`F:\workspace\py_virtual_env`

cmd打开该路径，执行`pip3 install virtualenv`

警告提示：

```python
WARNING: You are using pip version 21.0.1; however, version 21.1.2 is available.

You should consider upgrading via the 'c:\users\administrator\appdata\local\programs\python\python37\python.exe -m pip install --upgrade pip' command.
```

按照提示升级pip，执行

```python
c:\users\administrator\appdata\local\programs\python\python37\python.exe -m pip install --upgrade pip
```

安装成功，提示`Successfully installed pip-21.1.2`，再执行`pip3 install virtualenv`；

我的电脑之前安装过，运行`pip3 uninstall virtualenv`卸载后，重新安装；

`pip3 install virtualenv`安装成功，提示`Successfully installed virtualenv-20.4.7` ，我的电脑安装的版本是**virtualenv-20.4.7**

#### 1.2.创建虚拟环境

```python
virtualenv 环境名称

# 注意：创建[环境名称]文件夹，放置所有的环境，进入指定目录F:\workspace\py_virtual_env
```

进入到py_virtual_env，执行`virtualenv myproject`

```python
created virtual environment CPython3.7.7.final.0-64 in 1217ms
  creator CPython3Windows(dest=F:\workspace\py_virtual_env\myproject, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Administrator\AppData\Local\pypa\virtualenv)
    added seed packages: pip==21.1.2, setuptools==57.0.0, wheel==0.36.2
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

基于自己电脑的环境，新建了一个虚拟环境，运行结果如上，同时py_virtual_env下新增了`myproject目录`，文件结构如下：

```python
myproject
	|----Lib # 该文件下的site-packages文件夹，存放python相关的模块
	|----Scripts # 该文件夹存放pip.exe、python.exe等
	|----.gitignore
	|----pyvenv.cfg
```

`pyvenv.cfg`配置内容如下：

```python
home = c:\users\administrator\appdata\local\programs\python\python37
implementation = CPython
version_info = 3.7.7.final.0
virtualenv = 20.4.7
include-system-site-packages = false
base-prefix = c:\users\administrator\appdata\local\programs\python\python37
base-exec-prefix = c:\users\administrator\appdata\local\programs\python\python37
base-executable = c:\users\administrator\appdata\local\programs\python\python37\python.exe
```

- 安装指定的python版本

假设电脑上已经安装了python2.7和python3.5环境



可以指定虚拟环境的版本：

```python
virtualenv 环境名称 --python=python2.7
virtualenv 环境名称 --python=python3.5

# 如果提示找不到，可以直接复制路径
virtualenv 环境名称 --python='D:\python\python3.6.exe' # 前提是已经加入环境变量了
```

例如在上面的例子中，如果想安装python3.6，可以执行`virtualenv s36 --python=python3.6`

因为当前电脑上并没有安装python3.6，所以会报错，报错信息如下：

```python
F:\workspace\py_virtual_env>virtualenv s36 --python=python3.6
RuntimeError: failed to find interpreter for Builtin discover of python_spec='python3.6'
```

这里不指定版本，使用第一次安装的虚拟环境即可。

#### 1.2.5.安装virtualenv小结

- 1.打开终端
- 2.执行 pip3 install virtualenv
- 3.退出终端，再重新打开
- 4.进入到指定目录，执行 virtualenv 环境名称

#### 1.3.激活/退出虚拟环境

win7环境下：

```python
cd Scriptsactivate # 激活虚拟环境deactivate.bat # 退出虚拟环境
```

实操如下：

```	python
F:\workspace\py_virtual_env\myproject>cd ScriptsF:\workspace\py_virtual_env\myproject\Scripts>activate  # 激活虚拟环境(myproject) F:\workspace\py_virtual_env\myproject\Scripts>deactivate.bat # 退出虚拟环境F:\workspace\py_virtual_env\myproject\Scripts>
```

#### 1.4.虚拟环境中安装Django模块

- 激活虚拟环境（见1.3）

- 在激活的虚拟环境中，进入到Scripts目录中，安装Django模块

  ```python
  pip3 install django==1.11.28
  ```

  注意：先激活虚拟环境，再安装；

- 补充：

  - python3.7 + django1.11.7，后续使用时会报错，这里**安装django-1.11.28版本**

### 2.搭建Django项目

#### 2.1.窗口模式搭建Django（不推荐）

- 打开pycharm（自行搜索下载pycharm破解版）

- File --> New Project -->Django 

- 选择项目所在路径，并更改项目名称`F:\workspace\python\saas`

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021061822023297.png)

- 选择Existing interpreter --> 在Interpreter选择上一节新建的虚拟环境中的Scripts/python.exe

- 在`More Settings`中，设置`Application name`为`app01`，其他保持默认

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210618214625673.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

- 点击`create`

- 打开terminal，可以看到，使用是上一节安装的虚拟环境，以及1.11.28的Django版本

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210618220448995.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

- 打开`saas/saas/setting.py`，查看最后倒数第二行，显示了`# https://docs.djangoproject.com/en/1.11/howto/static-files/`，就表示当前安装的是1.11的版本

#### 2.3命令行模式搭建Django项目（推荐）

- 激活指定的virtualenv环境

  ```python
  F:\workspace\py_virtualenv\myproject\Scripts>activate
  ```

- 创建Django项目

  ```python
  django-admin startproject saas    #创建一个名称为saasdjango项目
  ```


- 进入到新建的项目中，再创建app

  ```python
  # 进入saas目录cd saas# 创建一个新的appdjango-admin startapp app01
  ```

  文件解析

  ```
  manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
  
  settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
  
  urls.py ----- 负责把URL模式映射到应用程序。
  
  wsgi.py ---- runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。
  ```

- 启动django项目

  ```python
  python manage.py runserver 127.0.0.1:8080  #此时已经可以启动django项目了
  ```

#### 2.2.警醒

企业做项目开发，必须使用虚拟环境，避免不同版本带来的问题

### 3.本地配置 local_settings.py

- 在settings.py末尾，导入local_settings

  ```python
  try:
      from .local_settings import *
  except ImportError as errr:
      print('import error',err)
  
  ```

- saas/saas目录下，创建local_settings.py文件

  ```python
  # 设置中文
  LANGUAGE_CODE = 'zh-hans'
  
  # 短信模板SMS = 666
  SMS = 666
  ```

- 如果在local_settings.py中增加了settings.py中不存在的字段，需要在settings.py中指定一下默认值

  settings.py末尾修改如下：

  ```python
  '''
  local_settings.field
  '''
  SMS = 0
  
  try:
      from local_settings import *
  except ImportError as err:
      print('import error:',err)
  ```

- **切记：**给别人代码时(上传git、gitee时)，不要给local_settings

### 4.公司开发规范和分享代码

#### 4.1.使用gitee创建远程仓库

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210618223821791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### 4.2.本地代码推送到gitee

- 项目根目录创建.gitignore

  ```
  # pycharm
  .idea/
  .DS_Store
  
  __pycache__/
  *.py[cod]
  *$py.class
  
  # Django stuff:
  local_settings.py
  *.sqlite3
  
  # database migrations
  */migrations/*.py
  !*/migrations/__init__.py
  ```

- 让gitee管理项目

  ```
  (myproject) F:\workspace\python\saas>git init    (myproject) F:\workspace\python\saas>git add .    
  (myproject) F:\workspace\python\saas>git commit -m '第一次提交'
  ```

  这三个命令，将代码管理在了本地

- gitee本地项目，推送到远程仓库

  ```
  # 给仓库路径添加别名(myproject) F:\workspace\python\saas>git remote add origin https://gitee.com/mindcons/saas_codereview.git
  
  # 推送到远程仓库，第一次推送的话，需要输入账户密码(myproject) F:\workspace\python\saas>git push origin master
  ```

  第一次提交需要输入账号密码，账号只能是邮箱账号。windows可在：“控制面板\所有控制面板项\凭据管理器”路径下管理账号密码；
  
  我的gitee地址：[点击查看](https://gitee.com/mindcons/saas_codereview)
  
- 使用bat管理git命令

  ```bat
  @echo off
  
  echo git add .
  git add .
  
  echo git commit -m 'auto-push'
  git commit -m 'auto-push'
  
  git push
  echo 'git push finish!'
  pause
  ```

  

#### 4.3.测试人员拿代码

测试进入到自己的目录，执行`git clone https://gitee.com/mindcons/saas_codereview.git`

  ```python
(venv) F:\workspace\test>git clone https://gitee.com/mindcons/saas_codereview.git
  ```

### 5.今日作业

- 创建名为tracer的虚拟环境，指定的python版本为python3.7
  - 在虚拟环境中，安装Djagno，版本为1.11.28
- 创建Django项目，命名为tracer
  - 配置local_settings.py
- 创建gitee仓库，命名为tracer
  - 配置.gitignore
- 在评论区，提交你的gitee项目地址
- 额外作业：自己查询资料，使用python代码实现，把一个文件上传到腾讯对象存储中

## Day02.今日概要

### 内容回顾

1.local_settings的作用？

```
本地配置信息- 开发- 测试- 运维
```

2.gitignore的作用？

```
git软件，本地进行版本管理的时候，需要忽略的文件	
git init    
git add .    
git commit -m up
码云/github/gitlab	
代码托管
```

3.虚拟环境的作用？

```python
项目环境之间的隔离开发：本地环境线上：比较抠的公司，一台服务器跑两个项目，做多环境隔离
```

执行`pip freeze > requirements.txt`，将当前虚拟环境中，安装的所有的模块及版本，写入该文件中

```
asgiref==3.3.4Django==1.11.28pytz==2021.1sqlparse==0.4.1typing-extensions==3.10.0.0
```

其他人员从gitee上拉取代码后，，进入到项目根目录，执行`pip install -r requirements.txt`，可快速搭建开发环境

```
(venv) F:\workspace\test\saas_codereview>pip install -r requirements.txt    

Requirement already satisfied: asgiref==3.3.4 in f:\workspace\python\test3\venv\lib\site-packages (from -r requirements.txt (line 1)) (3.3.4)       

Requirement already satisfied: Django==1.11.28 in f:\workspace\python\test3\venv\lib\site-packages (from -r requirements.txt (line 2)) (1.11.28)        

Requirement already satisfied: pytz==2021.1 in f:\workspace\python\test3\venv\lib\site-packages (from -r requirements.txt (line 3)) (2021.1)        

Requirement already satisfied: sqlparse==0.4.1 in f:\workspace\python\test3\venv\lib\site-packages (from -r requirements.txt (line 4)) (0.4.1)        

Requirement already satisfied: typing-extensions==3.10.0.0 in f:\workspace\python\test3\venv\lib\site-packages (from -r requirements.txt (line 5)) (3.10.0.0)
```

### 今日概要

- 腾讯发送短信
- Django中的ModelForm组件
- Redis
- 注册逻辑的设计
- 开发
- 详解

### 1.云短信

#### 1.1腾讯云短信

##### 1）准备工作

- 注册一个腾讯云账户，[注册地址](https://cloud.tencent.com)

- 根据流程开通之后，搜索`云短信`,进入[云短信平台](https://console.cloud.tencent.com/smsv2)

- 创建应用

  创建应用，并将应用中生成的`SDK AppID`和`App Key`记录下来，之后通过python发送云短信时要用到

  在`应用管理-->应用列表`中创建应用

- 创建签名

  在`国内短信-->签名管理`中，创建签名	

  在腾讯云短信签名时需要认证，证明上传：使用公众号（或者小程序）的设置页面截图即可-

- 创建正文模板

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210620215747850.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

- 发送短信

  上述准备工作做完，我们开通相关服务并获取到如下几个值：

  - 创建应用，获取到`appid`和`appkey`
  - 创建签名，获取`签名内容`
  - 创建模板，获取`模板ID`

  接下来使用开始使用python发送短信
  
- 配置参数

  ```python
  # 腾讯云短信应用的app_id
  TENCENT_SMS_APP_ID = 666
  # 腾讯云短信应用的app_key
  TENCENT_SMS_APP_KEY = "666"
  # 腾讯云短信签名内容
  TENCENT_SMS_SIGN = "python之路"
  
  TENCENT_SMS_TEMPLATE = {
      'register': 832736,
      'login': 840501
  }
  ```
  
  

##### 2）qcloudsmsm-py-0.1.4源码解析

##### 3）使用python发送短信

第一步：安装SDK

```python
pip install qcloudsms_py
```

`Successfully installed qcloudsms-py-0.1.4`

第二步：基于SDK，封装方法，发送短信

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from django.conf import settings


def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = settings.TENCENT_SMS_APP_ID
    appkey = settings.TENCENT_SMS_APP_KEY
    sms_sign = settings.TENCENT_SMS_SIGN

    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response
```

在saas根目录中，运行`manage.py runserver 8000`，将在本地启动服务`127.0.0.1:8000`



##### 4）结果

```
{'result': 0, 'errmsg': 'OK', 'ext': '', 'sid': '2019:7700303814781734360', 'fee': 1, 'isocode': 'CN'}[21/Jun/2021 23:18:32] "GET /send/sms HTTP/1.1" 200 7
```

页面每刷新一次，就会发送一次短信，腾讯云短信第一次充值，1000条/40元，测试用足够了。[购买链接](https://cloud.tencent.com/act/pro/csms?from=12055)

- saas/saas/urls.py中添加路由：

  ```python
  urlpatterns = [    url(r'^admin/', admin.site.urls),    url(r'^send/sms/', views.send_sms)]
  ```

- app01/views.py中添加视图函数：

  ```python
  from django.shortcuts import render,HttpResponsefrom utils.tencent.sms import send_sms_singleimport random# Create your views here.def send_sms(request):    # 将模板id写在配置文件中，根据传过来的类型，取对应的短信模板	tpl = request.GET.get('tpl')	template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)	if not template_id:		return HttpResponse('模板不存在')			code = random.randrange(100000,999999)	res = send_sms_single('11111111', template_id, [code,])	# print(res)    	if res['result'] == 0:		return HttpResponse('发送成功')	else:		return HttpResponse(res['errmsg'])
  ```

- saas/saas/settings.py添加的内容

  ```python
  # 短信的配置# 腾讯云短信应用的app_id
  TENCENT_SMS_APP_ID = 111111
  # 腾讯云短信的app_key
  TENCENT_SMS_APP_KEY = "111111"
  # 腾讯云短信的签名内容
  TENCENT_SMS_SIGN = "aaaaaa"
  # 配置短信模板
  TENCENT_SMS_TEMPLATE = {	
      'register' : 832736,	
      'login' : 840501,	
      'reset_password' : 1005457
  }
  try:	
      from .local_settings import *
  except ImportError:	
      pass
  ```

#### 1.2华为云短信

仅支持企业用户

#### 1.3阿里云短信



### 2.ModelForm生成注册字段

#### 2.1.在model.py创建表

```python
from django.db import models
# Create your models here.
class UserInfo(models.Model):    
    username = models.CharField(verbose_name = "用户名", max_length = 32)    
    # EmailField在数据库中，存储的实际还是字符串，区别在于ModelForm在页面上做展示的时候    
    email = models.EmailField(verbose_name = "邮箱", max_len
gth = 32)    
    mobile_phone = models.CharField(verbose_name = "手机号", max_length = 32)    
    password = models.CharField(verbose_name = "密码", max_length = 32)
```

#### 2.2.settings.py中挂载app01

```python
INSTALLED_APPS = [    
    'django.contrib.admin',    
    'django.contrib.auth',    
    'django.contrib.contenttypes',    
    'django.contrib.sessions',    
    'django.contrib.messages',    
    'django.contrib.staticfiles',    
    # 挂载app01	
    'app01.apps.App01Config',
]
```

#### 2.3.数据库迁移，生成表

```
python manage.py makemigrationspython manage.py migrate
```

生成类似如下的提示信息，表示数据库迁移成功：

```
Operations to perform:  Apply all migrations: admin, auth, contenttypes, sessionsRunning migrations:  Applying contenttypes.0001_initial... OK  Applying auth.0001_initial... OK  Applying admin.0001_initial... OK  Applying admin.0002_logentry_remove_auto_add... OK  Applying contenttypes.0002_remove_content_type_name... OK  Applying auth.0002_alter_permission_name_max_length... OK  Applying auth.0003_alter_user_email_max_length... OK  Applying auth.0004_alter_user_username_opts... OK  Applying auth.0005_alter_user_last_login_null... OK  Applying auth.0006_require_contenttypes_0002... OK  Applying auth.0007_alter_validators_add_error_messages... OK  Applying auth.0008_alter_user_username_max_length... OK  Applying sessions.0001_initial... OK
```

django中执行`python manage.py migrate`，底层发生了什么？

#### 2.4.注册路由，并编写视图函数

- saas/saas/urls.py中新增

```python
# 创建注册功能的路由
url(r'^app01/register/', views.register)
```

- saas/app01/views.py中新增

```python
# 引入ModelForm模块
from django import forms
from app01 import models

# 自定义注册model类
class RegisterModeForm(forms.ModelForm):	
    class Meta:		
        model = models.UserInfo		
        fields = '__all__'
    
    # 注册功能对应的视图函数
    def register(request):	
        # 生成model字段	
        form = RegisterModeForm()	
        # 根据模板，渲染注册功能的model字段	
        return render(request, 'register.html', {'form':form})
```

#### 2.5.创建模板

- 在app01中创建templates目录（注意不要拼写错误，不能少了s），并创建register.html
- django默认会先从根目录中找模板，然后会根据settings中的app的注册顺序来找

saas/app01/templates/register.html

```html
<!DOCTYPE html><html>	
    <head>		
        <meta charset="utf-8">		
        <title>注册</title>	
    </head>	
    <body>		
        <h1>注册</h1>		
        <!-- 对form字段进行循环，然后展示，类似于vue中的v-for -->		
        {% for field in form%}			
        <!-- ModelForm的字段有哪些属性？ -->			
        <!-- .label获取的实际上就是verbose_name -->			
        <p>{{field.label}} : {{ field }}</p>		
        {% endfor %}			
    </body>
</html
```

#### 2.6.结果

- 执行`python manage.py runserver 8080`，在浏览器中访问`127.0.0.1:8080/app01/register`，效果如下：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623192323464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### 2.7.ModelForm自定义字段

- 可以在views视图函数中，在自定义的ModelForm类中，重写model中生成的字段，如下，可以利用正则重写手机号规则(Django中不提供手机号的格式校验)

  vies.py

  ```python
  # 导入django中正则的模块
  from django.core.validators import RegexValidator
  from django.core.exceptions import ValidationError
  class RegisterModeForm(forms.ModelForm):	
      # 变量名要和model中的保持一致	
      # validator中，可以放一个或多个正则表达式	
      # RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息	
      mobile_phone = forms.CharField(label = '手机号', validators = [RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])	
      class Meta:		
          model = models.UserInfo		
          fields = "__all__"
  ```

- 重写`密码`字段

  - [Forms之widget部件一览](https://blog.csdn.net/qq_39620483/article/details/89465180)

  ```python
  #重写密码字段password = forms.CharField(label = '密码', widget = forms.PasswordInput())
  ```

- 在views.py中，定义`重复密码`字段

  ```python
  # 重复密码，该字段数据库中是没有的，因为没有定义在model中confirm_password = forms.CharField(label = '重复密码', widget = forms.PasswordInput())
  ```

  如果变量名，和model中一样，则会覆盖；如果不一样，则会新增该字段

  问：上述所有的字段，可不可以都写在ModelFom中？如果可以，语法应该是怎样的？

- 定义`验证码`字段

  ```python
  # 验证码# 如果不加widget，默认生成的是input标签
  code = forms.CharField(label = '验证码')
  ```

#### 2.8.基于bootstrap美化页面

这是使用v3版本，[bootstrap-v3版本下载](https://v3.bootcss.com/getting-started/#download)

也可以直接使用官网提供的cdn.

也可以下载，然后在django本地引入，具体原理查看，[django项目如何引入css文件](https://www.py.cn/kuangjia/django/11612.html)、具体配置见[Django使用本地css/js文件](https://www.cnblogs.com/lizm166/p/9414156.html)

settings.py中的测试代码

```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 这里打印的就是项目文件所在的绝对路径BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR) F:\workspace\py_virtualenv\myproject\Scripts\saas

# 基于BASE_DIR构建static路径STATIC_ROOT= os.path.join(BASE_DIR,'static')# print(STATIC_ROOT) 

F:\workspace\py_virtualenv\myproject\Scripts\saas\static

# 追加css文件路径STATICFILES_DIRS=[os.path.join(STATIC_ROOT,'css'),]

# print(STATICFILES_DIRS) ['F:\\workspace\\py_virtualenv\\myproject\\Scripts\\saas\\static\\css']
```

- 实际配置

  - 根目录下新建`static`，在里面再新建`static`文件夹，放入下载的css文件

  - settinsg.py中，在`STATIC_URL`下面，配置

    ```python
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]
    ```

    然后再register.html末班中，使用相对路径访问

    ```html
    <link rel="stylesheet" href="../../static/css/bootstrap.min.css">
    ```

  - 启动server，访问`http://127.0.0.1:8080/static/css/bootstrap.min.css`，可以访问到css文件了。

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623221301445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

  - 前台表单样式调用成功

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210624061226608.png)- 

- 以上引入静态文件的方式不可取

  - `register.html`
  
    ```html
    {% load static %}
    
    ...
    
    <link rel="stylesheet" href="{% static 'app01/static/css/account.css' %}">
    
    ```
  
    
  
- 完善register.html中的登录界面代码

  ```html
  <div class="account">
      <h1>注册</h1>
      <form>
          {% for field in form %}
          <div class="form-group">
              <label for="{{ filed.id_for_label }}">{{ field.label }}</label>
              {{ field }}
          </div>
          {% endfor %}
  
          <button type="submit" class="btn btn-default">注 册</button>
      </form>
  </div>
  ```
  
  此时`field`的字段是没有`form-control`的类名的，要借助ModelForm中的`attrs`，重写字段时，给每个字段加上类名

  ```python
  confirm_password = forms.CharField(label = '重复密码', widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : '请重复输入密码'}))
  ```
  
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210624063221205.png)

  重写`RegisterModelForm`的初始化方法，批量给字段添加`form-control`类属性以及`placeholder`属性

  ```python
      def __init__(self,*args,**kwargs):
          super().__init__(*args,**kwargs)
          for name,field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'
              field.widget.attrs['placeholder'] = '请输入{0}'.format(field.label)
  ```
  
  自定义字段顺序
  
  ```python
  # fields = "__all__"
  fields = ['username','email','password','confirm_password','mobile_phone','code']
  ```
  
  完善register模板
  
  ```html
  <div class="account">
      <h1 style="text-align: center">注册</h1>
      <form>
          {% for field in form %}
          {% if field.name == 'code' %}
          <div class="form-group">
              <label for="{{ filed.id_for_label }}">{{ field.label }}</label>
              <div class="clearfix">
                  <div class="col-md-6" style="padding-left: 0;">{{ field }}</div>
                  <div class="col-md-6">
                      <input type="button" class="btn btn-default" value="点击获取验证码">
                  </div>
              </div>
          </div>
          {% else %}
          <div class="form-group">
              <label for="{{ filed.id_for_label }}">{{ field.label }}</label>
              {{ field }}
          </div>
          {% endif %}
          {% endfor %}
          <button type="submit" class="btn btn-primary">注 册</button>
      </form>
  </div>
  ```
  
  account.css
  
  ```css
  .account{
      width: 400px;
      margin: 0 auto;
  }
  ```
  
  

### 3.注册实现思路

- 点击获取验证
  - 获取手机号
  - 向后台发送ajax
    - 手机
    - tpl=register
  - 向手机发送验证码（ajax/sms/redis）
  - 验证码失效处理（60s）

#### 3.1.windows安装redis

补充：可直接看我的redis基础，部署在linux上进行访问

- 安装redis

  - [官方下载链接](https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504)
  - 下载版本：3.0.504  Redis-x64-3.0.504.msi
  - 安装时勾选配置环境变量选项

- 修改配置文件：redis.windows-service.conf

  - 60行：bind 0.0.0.0
  - 386行：requirepass foobared，取消注释
  - 控制面板--管理（工具）--服务，随便点击一个服务，再按“r”搜索到redis
    右键选择重启redis服务

- python操作redis，方法一

  - 安装python操作redis模块

    ```python
    pip install redis
    ```

  - 写代码操作redis

    ```python
    import redis
    conn = redis.Redis(host='127.0.0.1',port='6379',password='foobared',encoding='utf-8')# 设置k1的值为v1，过期时间为10秒
    conn.set('k1','v1',ex=10)
    value = conn.get('k1')
    print(value)
    ```
    
    激活虚拟环境，运行该python文件，结果如下
    
    ```
    b'v1'
    ```

4.作业

- ModelForm页面
- register页面写ajax，手机号和模板字符串tpl，csrf问题
- 校验
- sms + redis
- 进阶
  - 倒计时效果
  - 注册按钮：字段校验 + 手机验证码校验
  - python操作redis，django-redis

## Day03.今日概要

### 内容回顾

- 虚拟环境virtualenv（每个项目创建独立虚拟环境）

- requirement.txt(pip freeze > requirements.txt)

- local_settings.py

- .gitignore

- 腾讯云短信/阿里云短信（阅读官方文档，文档不清晰，使用搜索引擎）

  - API：提供URL，自己去访问这些URL并根据提示传递参数（所有第三方工具都有）

    ```python
    requests.get("http://www.xxx.com/asdf/asdf",json={...})
    ```

  - SDK：是一个模块，基于模块完成功能（不一定都有SDK）

    ```python
    # sms.pydef func():    return requests.get("http://www.xxx.com/asdf/asdf",json={...})
    ```

    ```python
    pip install sms
    ```

    ```python
    sms.func()
    ```

- redis，[详细了解请点此查看](https://blog.csdn.net/qq_17273727/article/details/118205770)

  - 在A主机安装redis&配置&启动

  - 连接redis

    - 利用redis提供的客户端

    - 使用模块【不推荐】

      ```python
      import redis
      
      conn = redis.Redis(host='127.0.0.1',port='6379',password='foobared',encoding='utf-8')
      # 设置k1的值为v1，过期时间为10秒
      conn.set('k1','v1',ex=10)
      value = conn.get('k1')
      print(value)
      ```

    - 上面的python操作redis示例，是以直接创建连接的方式实现，每次操作redis如果重新连接一次，效率会比较低，建议使用redis连接池来替换【推荐】，例如：
    
      ```python
      import redis
      #创建redis连接池（默认连接池最大连接数 2**31=2147483648）
      pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='foobared',encoding='utf-8',max_connections=1000)
      #去连接池中获取一个连接
      conn = redis.Redis(connection_pool = pool)
      #设置键值，且超时时间为10秒（写入redis时，会自动转换为字符串）
      conn.set('k1','v1',ex=10)
      #根据键获取值，如果值存在，获取到的是字符串类型；不存在则返回None
      value = conn.get('k1')print(value)
      ```

      ```python
      # 在django中使用
      import redis
      from django.shortcuts import HttpResponse
      #创建redis连接池（默认连接池最大连接数 2**31=2147483648）
      pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='foobared',encoding='utf-8',max_connections=1000)
      def index(request):    
          #去连接池中获取一个连接    
          conn = redis.Redis(connection_pool = pool)    
          #设置键值，且超时时间为10秒（写入redis时，会自动转换为字符串）    
          conn.set('k1','v1',ex=10)    
          #根据键获取值，如果值存在，获取到的是字符串类型；不存在则返回None    
          value = conn.get('k1')    
          print(value)        
          return HttpResponse('ok')
      ```
    
      这种方式可以实现在django中操作redis，但是，这种形式有点非主流，一般不这么干，而是采用一种更简洁的方式。
    
    - django连接redis，django-redis
    
      - 在django中`方便的`使用redis
    
        ```python
        不方便：redis模块+连接池方便：django-redis
        ```
    
      - 安装`django-redis`，注意版本，不能直接安装django-redis，默认是安装最新的django-redis，导致升级django版本
    
        ```python
        pip install django-redis==4.0.0
        ```
    
      - `local_settings.py`配置：
    
        ```python
        # django-redis的配置
        CACHES = {	
            "default": {		
                "BACKEND": "django_redis.cache.RedisCache",		
                "LOCATION": "redis://127.0.0.1:6379", 
                # 安装redis的主机的IP和端口		
                "OPTIONS": {			
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",			
                    "CONNECTION_POOL_KWARGS": {				
                        "max_connections": 1000,				
                        "encoding": "utf-8"			
                    },			
                    "PASSWORD": "foorbared" # redis密码，放在local_settings.py中		
                }	
        	},
        }
        ```
        
        ```python
        # 链接到数据库
        from django.shortcuts import HttpResponse
        from django_redis import get_redis_connection
        
        def index(request):    
            #去连接池中获取一个连接    
            conn = get_redis_connection("defalut") 
            # 默认读取defalut的配置，也可以读取其他的，比如master的配置，在settings.py中配置好即可    
            # 后期读写分离的时候可以用到        
            conn.set('k1','v1',ex=10)    
            value = conn.get('k1')    
            print(value)        
            return HttpResponse('ok')
        ```

### 今日概要

- 注册
- 短信验证码登录
- 用户密码登录

### 1.实现注册

#### 1.1.展示注册页面

##### 1.1.1.web的应用创建&&app应用注册

- 创建名为`web`的新的app

  ```python
  django-admin startapp web
  ```

- 在`settinsg.py`的`INSTALLED_APPS`最后一行中注册

  ```python
  'web.apps.WebConfig',
  ```

- 删除web/views.py，创建views文件夹，创建web/views/account.py文件

- 创建web/templates文件夹

  - 不同app的templates目录，一般还会创建和app名称相同的文件夹，然后再放模板文件，即web/templates/web/register.html
  - 模板和静态文件的查找顺序是，现在项目的根目录查找，然后按照app在配置文件中的配置顺序查找

- 创建母版目录web/templates/layout/basic.html

  basic.html

  ```html
  {% load static %}<!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <title>{% block title %}{% endblock %}</title>
  
      <link rel="stylesheet" href="{% static '/web/plugin/bootstrap/css/bootstrap.min.css' %}">
      <link rel="stylesheet" href="{% static '/web/plugin/font-awesome/css/font-awesome.min.css' %}">
  
      <style>
          .navbar-default {
              border-radius: 0;
          }
      </style>
  
      {% block css %}{% endblock %}
  </head>
  
  <body>
      <nav class="navbar navbar-default">
          <div class="container">            <!-- Brand and toggle get grouped for better mobile display -->
              <div class="navbar-header">
                  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                          data-target="#bs-example-navbar-collapse-1" aria-expanded="false"><span class="sr-only">Toggle navigation</span>
                      <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span></button>
                  <a class="navbar-brand" href="#">Tracer</a></div>
              <!-- Collect the nav links, forms, and other content for toggling -->
              <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                  <ul class="nav navbar-nav">
                      <!-- <li class="active"><a href="#">产品功能 <span class="sr-only">(current)</span></a></li> -->
                      <li><a href="#">产品功能</a></li>
                      <li><a href="#">企业方案</a></li>
                      <li><a href="#">帮助文档</a></li>
                      <li><a href="#">价格</a></li>
                  </ul>
                  <ul class="nav navbar-nav navbar-right">
                      <li><a href="#">Link</a></li>
                      <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                              aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                          <ul class="dropdown-menu">
                              <li><a href="#">Action</a></li>
                              <li><a href="#">Another action</a></li>
                              <li><a href="#">Something else here</a></li>
                              <li role="separator" class="divider"></li>
                              <li><a href="#">Separated link</a></li>
                          </ul>
                      </li>
                  </ul>
              </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
      </nav>
  
  {% block content %}{% endblock %}
  
  <script src="{% static '/web/js/jquery-3.4.1.min.js' %}"></script>
  <script src="{% static '/web/plugin/bootstrap/js/bootstrap.js' %}"></script>
  
  {% block js %}{% endblock %}
  
  </body>
  </html>
  ```
  
  

##### 1.1.2.路由分发

- 做路由匹配的时候，最前面不需要加`/`符号

- 总路由saas/urls.py

  ```python
  from django.conf.urls import url,include
  from django.contrib import admin
  
  urlpatterns = [    
      url(r'^admin/', admin.site.urls),    
      url(r'^app01/', include('app01.urls',namespace='app01')),    
      url(r'^', include('web.urls',namespace='web')),
  ]
  ```
  
  app01/urls.py
  
  ```python
  from django.conf.urls import url
  from django.contrib import admin
  from app01 import view
  
  surlpatterns = [    
      url(r'^send/sms/', views.send_sms),    
      url(r'^register/', views.register, name='register'),
  ]
  ```
  
  web/urls.py
  
  ```python
  from django.conf.urls import url,include
  from web.views import account
  
  urlpatterns = [    
      url(r'^register/', account.register, name='register'),
  ]
  ```

##### 1.1.3.register.html

- account.css

  ```css
  .account {
      width: 400px;
      margin-top: 30px;
      margin-left: auto;
      margin-right: auto;
      border: 1px solid #f0f0f0;
      padding: 10px 30px 30px 30px;
      -webkit-box-shadow: 5px 10px 10px rgba(0, 0, 0, .05);
      box-shadow: 5px 10px 10px rgba(0, 0, 0, .05);
  }
  
  .account .title {
      font-size: 25px;
      font-weight: bold;
      text-align: center;
  }
  
  .account .form-group {
      margin-bottom: 20px;
  }
  
  ```

  register.html

  ```html
  {% extends 'web/layout/basic.html' %}
  {% load static %}
  
  {% block title %}用户注册{% endblock %}
  
  {% block css %}
      <link rel="stylesheet" href="{% static 'web/css/account.css' %}">
  {% endblock %}
  
  {% block content %}
      <div class="account">
          <div class="title">用户注册</div>
          <form id="regForm" method="POST" novalidate>
              {% csrf_token %}
              {% for field in form %}
              {% if field.name == 'code' %}
                  <div class="form-group"><label for="{{ field.id_for_label }}">{{ field.label }}</label>
                      <div class="row">
                          <div class="col-xs-7">
                              {{ field }}
                              <span class="error-msg"></span>
                          </div>
                          <div class="col-xs-5">
                              <input id="btnSms" type="button" class="btn btn-default" value="点击获取验证码">
                          </div>
                      </div>
                  </div>
              {% else %}
                  <div class="form-group">
                      <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                      {{ field }}
                      <span class="error-msg"></span>
                  </div>
              {% endif %}
              {% endfor %}
              <div class="row">
                  <div class="col-xs-3">
                      <input id="btnSubmit" type="button" class="btn btn-primary" value="注  册"/>
                  </div>
              </div>
          </form>
      </div>
  {% endblock %}
  
  {% block js %}
  
  {% endblock %}
  ```

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/cde5358aa7344741b337d9d6069bd4d3.png)

- 新建web/forms文件夹，后面用到的Forms，都统一放在该目录

  该目录下，新建account.py

  ```python
  # 引入ModelForm模块
  from django import forms
  from app01 import models
  from django.core.validators import RegexValidator
  from django.core.exceptions import ValidationError
  
  # 自定义注册model类
  class RegisterModelForm(forms.ModelForm):
      # 变量名要和model中的保持一致	
      # validator中，可以放一个或多个正则表达式	
      # RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息	
      mobile_phone = forms.CharField(label='手机号', validators=[
          RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')])
      # 重写密码字段
      password = forms.CharField(label='密码', widget=forms.PasswordInput())  # 重复密码
      confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
      # 验证码	
      code = forms.CharField(label='验证码')
  
      class Meta:
          model = models.UserInfo
          # fields = "__all__"		
          fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']
  
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for name, field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'
              field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
  ```

  新建web/views文件夹，后面用到的views，都统一放在该目录

  views/account.py

  ```python
  """用户账户相关的功能：注册、短信、登录、注销"""
  from django.shortcuts import render
  from web.forms.account import RegisterModelForm
  def register(request):
      form = RegisterModelForm()
      return render(request,'web/register.html',{'form': form})
  ```

- 把web的models.py按照app01的方式，重新生成一遍

  web/models.py

  ```python
  from django.db import models# Create your models here.
  class UserInfo(models.Model):	
      username = models.CharField(verbose_name = "用户名", max_length = 32)		
      # EmailField在数据库中，存储的实际还是字符串，区别在于ModelForm在页面上做展示的时候	
      email = models.EmailField(verbose_name = "邮箱", max_length = 32)		
      mobile_phone = models.CharField(verbose_name = "手机号", max_length = 32)	
      password = models.CharField(verbose_name = "密码", max_length = 32)
  ```
  
  运行`python manage.py makemigrations`和`python manage.py migrate`
  
  修改web/forms/account.py的导包路径
  
  ```python
  # from app01 import modelsfrom web import models
  ```


#### 1.2.点击获取验证码

##### 1.2.1.按钮绑定点击事件

##### 1.2.2.获取手机号

```javascript
{% block js %}    
    <script>        
        // 页面加载完成后执行        
        $(function() {            
        bindClickBtnSms()        
    })        
 // 绑定获取短信验证码的点击操作        
 function bindClickBtnSms() {            
     $('#btnSms').click(function () {                
         // 获取用户输入的手机号                
         // django 会对由forms生成的字段，加上id_+字段名的id属性                
         console.log($('#id_mobile_phone').val())
         var mobilePhone = $('#id_mobile_phone').val()
     })        
 }    
 </script>
 {% endblock%}
```

##### 1.2.3.发送ajax

```javascript
//发送ajax请求
$.ajax({	
    // 反向生成url，等价于send/sms	
    // 总路由分发时，加了namspace="web"，反向生成时，要加web:	
    url: "{% url 'web:send_sms' %}",	
    type: 'GET',	
    data: {mobile_phone:mobilePhone, tpl:'register'},	
    success: function(res) {		
        // ajax请求成功后，返回的值存储在res中		
        console.log(res)	
    }
})
```

##### 1.2.4.手机号校验

- 不能为空
- 格式正确
- 没有注册过

form中如果要拿到视图函数中的request值，可以重写`__init__`方法

```python
def __init__(self, request, *args, **kwargs):    
    super().__init__(*args, **kwargs)    
    self.request = request
```

forms/account.py

```python
# 引入ModelForm模块
from django import forms
from django.forms.utils import from_current_timezone
from web import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings

class SendSmsForm(forms.Form):
	mobile_phone = forms.CharField(label='手机号',validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$'', '手机号格式错误')])

	def __init__(self, request, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.request = request


	# 手机号校验的钩子函数
	def clean_mobile_phone(self):
		mobile_phone = self.cleaned_data['mobile_phone']

		# 判断短信模板是否有问题
		tpl = self.request.GET.get('tpl')
		template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
		if not template_id:
			raise ValidationError('模板错误')

		# 检查数据库中，是否有手机号
		# django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
		exsits = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
		if exsits:
			raise ValidationError('手机号已存在')
		return mobile_phone

# 自定义注册model类
class RegisterModeForm(forms.ModelForm):
	# 变量名要和model中的保持一致
	# validator中，可以放一个或多个正则表达式
	# RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息
	mobile_phone = forms.CharField(label = '手机号', validators = [RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')])
	
	#重写密码字段
	password = forms.CharField(label = '密码', widget = forms.PasswordInput())
	
	# 重复密码
	confirm_password = forms.CharField(label = '重复密码', widget = forms.PasswordInput())
	
	# 验证码
	code = forms.CharField(label = '验证码')
	
	class Meta:
		model = models.UserInfo
		# fields = "__all__"
		fields = ['username','email','password','confirm_password','mobile_phone','code']
	def __init__(self, *args,**kwargs):
		super().__init__(*args, **kwargs)
		for name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
```

views/account.py

```python
"""
用户账户相关的功能：注册、短信、登录、注销
"""

from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModeForm, SendSmsForm
from django.conf import settings

def register(request):
	form = RegisterModeForm()
	return render(request,'register.html',{'form': form})

def send_sms(request):
	mobile_phone = request.GET.get('mobilePhone')
	tpl = request.GET.get('tpl')
	template_id = settings.TENCENT_SMS_TEMPLATE[tpl]

	# 实例化Form对象，实例化时，会执行该对象的init方法
	form = SendSmsForm(request, data=request.GET)
	# print(form.is_valid())
	# 只校验手机号不能为空，格式是否正确
	if form.is_valid():
		pass
	return HttpResponse('ok')

```

1.2.5.校验通过

- 发送短信

  - 生成验证码
  - 调用发送短信函数，将需要的`moblie_phone`、`template_id`、`[code,]`参数传入
  - 对发送结果进行异常校验

- 将短信保存在redis中（60s）

  - 安装django-redis，版本为4.11.0：`pip install django-redis==4.11.0`

  - 在local_settings.py中进行配置

    ```python
    CACHES = {
    	"default": {
    		"BACKEND": "django_redis.cache.RedisCache",
    		"LOCATION": "redis://127.0.0.1:6379", # 安装redis的主机的IP和端口
    		"OPTIONS": {
    			"CLIENT_CLASS": "django_redis.client.DefaultClient",
    			"CONNECTION_POOL_KWARGS": {
    				"max_connections": 1000,
    				"encoding": "utf-8"
    			},
    			"PASSWORD": "foorbared" # redis密码，放在local_settings.py中
    		}
    	},
    }
    ```

    保存验证码

    ```python
    # 将短信验证码写入redis中(django_redis来操作)
    conn = get_redis_connection()
    conn.set(moblie_phone, code, ex=60)
    ```

- 校验通过结果显示

  ```python
  if form.is_valid():
      return JsonResponse({'status': True})
  return JsonResponse({'status': False},{'errror': form.errors})
  ```

##### 1.2.5.验证通过

- 发送短信
- 将短信保存在redis中（60s）

forms/account.py

```python
import random
from utils.tencent.sms import send_sms_single
from django_redis import get_redis_connection
```



```python
        if exsits:
            raise ValidationError('手机号已存在')

        # 发短信 & 写redis
        # 发送短信
        code = random.randrange(1000, 9999)
        sms = send_sms_single(mobile_phone, template_id, [code, ])
        if sms['result'] != 0:
            raise ValidationError('短信验证码发送失败，{}'.format(sms['errmsg']))
        # 写redis(django-redis)
        conn = get_redis_connection()
        conn.set(mobile_phone,code,ex=60)


        return mobile_phone
```

views/account.py

```python
from django.http import JsonResponse
```



```python
    if form.is_valid():
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})
```

##### 1.2.6.成功失败

- 失败，错误信息
- 成功，倒计时

register.html

```javascript
{% block js %}
    <script>
        // 页面加载完成后执行
        $(function () {
            bindClickBtnSms()
        })

        // 绑定获取短信验证码的点击操作
        function bindClickBtnSms() {
            $('#btnSms').click(function () {
                //开始置空error-msg内容
                $('.error-msg').empty()

                // 获取用户输入的手机号
                // django 会对由forms生成的字段，加上id_+字段名的id属性
                {#console.log($('#id_mobile_phone').val())#}
                var mobilePhone = $('#id_mobile_phone').val()
                //发送ajax请求
                $.ajax({
                    // 反向生成url，等价于send/sms
                    // 总路由分发时，加了namspace="web"，反向生成时，要加web:
                    url: "{% url 'web:send_sms' %}",
                    type: "GET",
                    data: {mobile_phone: mobilePhone, tpl: 'register'},
                    dataType: "JSON", //将服务器返回的数据反序列化为字典
                    success: function (res) {
                        // ajax请求成功后，返回的值存储在res中
                        {#console.log(res)#}
                        if (res.status) {
                            console.log('发送成功，倒计时')
                        } else {
                            //错误信息
                            console.log(res) //{status:False,error:{mobile_phone:["错误信息"]}}
                            $.each(res.error,function(key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}
```

settings.py

```python
LANGUAGE_CODE = 'zh-hans'
```

- disabled属性
- 定时器

```javascript
        //发送短信倒计时
        function sendSmsReminder() {
            var $smsBtn = $('#btnSms')

            $smsBtn.prop('disabled',true)

            var time = 60
            var remind = setInterval(function () {
                $smsBtn.val(time+'秒重新发送')
                time = time - 1
                if (time < 1){
                    clearInterval(remind)
                    $smsBtn.val('点击获取验证码').prop('disabled',false)
                }
            },1000)
```



#### 1.3.点击注册

##### 内容总结

- 视图 view.py -> view目录

- 模板，根目录templates -> 根据app注册顺序去每个app的templates中

- 静态文件，同上static

- 项目中多个app想要各自的模板， 静态文件隔离，建议通过app名称在进行嵌套即可

- 路由分发

  - include
  - namespace

- 母版

  ```
  title
  css
  content
  js
  ```

- bootstrap导航条、去除圆角、container

- ModelForm生成HTML标签，自动ID`id_字段名`

- 发送ajax请求

  ```javascript
  $.ajax({
      // 反向生成url，等价于send/sms
      // 总路由分发时，加了namspace="web"，反向生成时，要加web:
      url: "{% url 'web:send_sms' %}",
      type: "GET",
      data: {mobile_phone: mobilePhone, tpl: 'register'},
      dataType: "JSON", //将服务器返回的数据反序列化为字典
      success: function (res) {
          // ajax请求成功后，返回的值存储在res中
          {#console.log(res)#}
          if (res.status) {
              {#console.log('发送成功，倒计时')#}
              sendSmsReminder()
  
              } else {
                  //错误信息
                  console.log(res) //{status:False,error:{mobile_phone:["错误信息"]}}
                  $.each(res.error,function(key, value) {
                      $("#id_" + key).next().text(value[0])
                  })
              }
          }
  })
  ```

- Form&ModelForm可以进行表单验证

  ```python
  form = SendSmsForm(data=request.POST) # QueryDict
  form = SendSmsForm(data=request.GET) # QueryDict
  ```

- Form&ModelForm中如果想要用视图中的值（request）

  ```python
  class SendSmsForm(forms.Form):
      mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
  
      def __init__(self, request, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.request = request
  ```

- 短信

- redis(django-redis)

- 倒计时



## Day04.今日概要

### 内容回顾

- 项目规则

  - 创建项目：静态文件、视图、路由等

- ajax

  ```javascript
  $.ajax({
      url: '...',
      type: 'GET',
      data: {},
      dataType: 'JSON',
      success: function(res) {
          
      }
  })
  ```

- ModelForm/Form中想要使用视图中的数据，例如：request

  ```
  重写ModelForm/Form的__init__方法，把想要的数据传递
  ```

- django-redis

### 今日概要

- 点击注册
- 用户登陆
  - 短信验证码登陆
  - 手机或者邮箱/密码登陆
- 项目管理

### 1.点击注册

#### 1.1.点击收集数据&ajax

register.html

```javascript
        // 页面加载完成后执行
        $(function () {
            bindClickBtnSms()
            btnClickSubmit()
        })
        
        //点击提交（注册）
        function btnClickSubmit() {
            $('#btnSubmit').click(function () {
                //收集表单中的数据(找到每一个字段)
                {#/$('#regForm').serialize() //所有的字段+csrf token#}
                //数据ajax发送到后台
                $.ajax({
                    url: "{% url 'web:register' %}",
                    type: "POST",
                    data: $('#regForm').serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        console.log(res)
                    }
                })

            })
        }
```

views/account.py

```python
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    print(request.POST)
    return JsonResponse({})
```



#### 1.2.数据校验（每个字段）

forms/account.py

```python
class RegisterModelForm(forms.ModelForm):
    # 变量名要和model中的保持一致
    # validator中，可以放一个或多个正则表达式
    # RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    # mobile_phone = forms.CharField(label='手机号')
    # 重写密码字段
    password = forms.CharField(
        label='密码',
        min_length=8,
        max_length=64,
        error_messages={
            'min_length':'密码长度不能小于8个字符',
            'max_length':'密码长度不能大于64个字符'
        },
        widget=forms.PasswordInput())  # 重复密码
    confirm_password = forms.CharField(
        label='重复密码',
        min_length=8,
        max_length=64,
        error_messages={
            'min_length': '密码长度不能小于8个字符',
            'max_length': '密码长度不能大于64个字符'
        },
        widget=forms.PasswordInput())
    # 验证码
    code = forms.CharField(label='验证码')

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)

    def clean_username(self):
        username = self.cleaned_data['username']
        exsits = models.UserInfo.objects.filter(username=username).exsits()
        if exsits:
            raise ValidationError('用户名已存在')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        exsits = models.UserInfo.objects.filter(email=email).exsits()
        if exsits:
            raise ValidationError('邮箱已存在')
        return email
    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        confirm_pwd = self.cleaned_data['confirm_password']
        if pwd != confirm_pwd:
            raise ValidationError('两次密码不一致')
        return confirm_pwd
    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exsits = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exsits()
        if exsits:
            raise ValidationError('手机号已注册')
        return mobile_phone
    def clean_code(self):
        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data['mobile_phone']

        conn = get_redis_connection()
        redis_code = conn.get(mobile_phone)
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')
        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误，请重新输入')
        return code
```

```python
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,db_index=True)
```

views/account.py

```python
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    # print(request.POST)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.errors)
    return JsonResponse({})
```



#### 1.3.写入数据库

需要手动选取，sqlite3文件所在的目录才行

![在这里插入图片描述](https://img-blog.csdnimg.cn/fb0d847fd81f47a9bbdaa49f8020be7c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAU2FpYWJsZQ==,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/8ad0b8c0b31740aaa6aad4d1429d4e2c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAU2FpYWJsZQ==,size_20,color_FFFFFF,t_70,g_se,x_16)

如上图，用户注册数据，已成功入库

#### 1.4.bug

当用户注册成功之后，如果立即返回，再进行注册

则会报以下错误

```
File "F:\workspace\git\code_total\code\django\saas\web\forms\account.py", line 88, in clean_code
    mobile_phone = self.cleaned_data['mobile_phone']
KeyError: 'mobile_phone'
```

我们看下mobile_phone的钩子函数

```python
    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()
        if exists:
            raise ValidationError('手机号已注册')
        return mobile_phone
```

再看下code的钩子函数

```python
    def clean_code(self):
        code = self.cleaned_data['code']
        mobile_phone = self.cleaned_data['mobile_phone']

        conn = get_redis_connection()
        redis_code = conn.get(mobile_phone)
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')
        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误，请重新输入')
        return code
```

上面的情景下，第二次点时，mobile_phone是已经存在的，所以会抛出“手机号已注册”的异常，因此cleaned_data就不会有mobile_phone，所以你在code的钩子函数里，取mobile_phone自然会报错

解决方案一：不通过索引，通过get方式

```python
        mobile_phone = self.cleaned_data.get('mobile_phone')
        if not mobile_phone:
            return code
```

解决方案二：mobile_phone的错误信息添加到add_error中，即使校验失败了，也是认为，这个值是可以放在cleaned_data中的，mobile_phone会正常返回

```python
        if exists:
            # raise ValidationError('手机号已注册')
            self.add_error('username','手机号已注册')
        return mobile_phone
```

同上，修改下password和confirm_password的钩子函数中，获取key的方式

### 2.短信登陆

#### 2.1.展示页面

路由

```python
    url(r'^login/sms$', account.login_sms, name='login_sms'),
```

视图函数

```python
def login_sms(request):
    form = LoginSMSForm()
    return render(request,'web/login_sms.html',{'form':form})
```

Form

```python
class BootstrapForm(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)

class LoginSMSForm(BootstrapForm, forms.Form):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    code = forms.CharField(label='验证码',widget=forms.TextInput())
```



#### 2.2.点击发送短信

js和register中的类似，唯一不同的是tpl='login'

```python
{% block js %}
    <script>
    $(function () {
        bindClickBtnSms()
    })

        //发送短信倒计时
        function sendSmsReminder() {
            var $smsBtn = $('#btnSms')

            $smsBtn.prop('disabled', true)

            var time = 60
            var remind = setInterval(function () {
                $smsBtn.val(time + '秒重新发送')
                time = time - 1
                if (time < 1) {
                    clearInterval(remind)
                    $smsBtn.val('点击获取验证码').prop('disabled', false)
                }
            }, 1000)
        }

        // 绑定获取短信验证码的点击操作
        function bindClickBtnSms() {
            $('#btnSms').click(function () {
                //开始置空error-msg内容
                $('.error-msg').empty()

                // 获取用户输入的手机号
                // django 会对由forms生成的字段，加上id_+字段名的id属性
                {#console.log($('#id_mobile_phone').val())#}
                var mobilePhone = $('#id_mobile_phone').val()
                //发送ajax请求
                $.ajax({
                    // 反向生成url，等价于send/sms
                    // 总路由分发时，加了namspace="web"，反向生成时，要加web:
                    url: "{% url 'web:send_sms' %}",
                    type: "GET",
                    data: {mobile_phone: mobilePhone, tpl: 'login'},
                    dataType: "JSON", //将服务器返回的数据反序列化为字典
                    success: function (res) {
                        // ajax请求成功后，返回的值存储在res中
                        {#console.log(res)#}
                        if (res.status) {
                            {#console.log('发送成功，倒计时')#}
                            sendSmsReminder()

                        } else {
                            //错误信息
                            console.log(res) //{status:False,error:{mobile_phone:["错误信息"]}}
                            $.each(res.error, function (key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>

{% endblock %}
```

sendSMSForm中对tpl的值进行判断处理

```python
        exsits = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()

        if tpl == 'login':
            if not exsits:
                raise ValidationError('手机号不存在')
        else:
            if exsits:
                raise ValidationError('手机号已存在')
```



#### 2.3.点击登陆

登陆按钮添加点击事件

```javascript
//点击登陆
function btnClickSubmit() {
    $('#btnSubmit').click(function () {
        $('.error-msg').empty()
        //收集表单中的数据(找到每一个字段)
        {#/$('#regForm').serialize() //所有的字段+csrf token#}
        //数据ajax发送到后台
        $.ajax({
            url: "{% url 'web:login_sms' %}",
            type: "POST",
            data: $('#regForm').serialize(),
            dataType: "JSON",
            success: function (res) {
                {#console.log(res)#}
                if (res.status) {
                    location.href = res.data
                } else {
                    $.each(res.error, function (key, value) {
                        $("#id_" + key).next().text(value[0])
                    })
                }

            }
        })

    })
}
```

视图函数对POST请求进行处理

```python
def login_sms(request):
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request,'web/login_sms.html',{'form':form})
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # user_object = form.cleaned_data['mobile_phone']
        mobile_phone = form.cleaned_data.get('mobile_phone')
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        # 用户信息放入session
        # print(user_object)
        request.session['user_id'] = user_object.id
        request.session['user_name'] = user_object.user_name

        return JsonResponse({'status': True,'data':'/index/'})
    return JsonResponse({'status': False, 'error': form.errors})
```

Form中对字段进行校验

```python
class LoginSMSForm(BootstrapForm, forms.Form):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    code = forms.CharField(label='验证码',widget=forms.TextInput())
    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data.get('mobile_phone')
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        if not user_object:
            raise ValidationError('手机号不存在')
        return user_object

    def clean_code(self):
        code = self.cleaned_data.get('code')
        # mobile_phone = self.cleaned_data['mobile_phone']
        # 通过get方式获取mobile_phone
        user_object = self.cleaned_data.get('mobile_phone')
        if not user_object:
            return code

        conn = get_redis_connection()
        redis_code = conn.get(user_object.obile_phone)
        if not redis_code:
            raise ValidationError('验证码失效或未发送，请重新发送')

        redis_str_code = redis_code.decode('utf-8')
        if code.strip() != redis_str_code:
            raise ValidationError('验证码错误，请重新输入')
        return code
```

### 3.用户名、密码登陆

#### 3.1.pillow模块

指定清华源安装，快一点

`pip3 install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple`

1.创建图片

```python
from PIL import Image

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))

# 在图片查看器中打开
# img.show()

# 保存在本地
with open('code.png', 'wb') as f:
    img.save(f, format='png')
```

2.创建画笔，用于在图片上画任意内容

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
```

 3.画点

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示坐标
# 第二个参数：表示颜色
draw.point([100, 100], fill="red")
draw.point([300, 300], fill=(255, 255, 255))
```

4.画线

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标和结束坐标
# 第二个参数：表示颜色
draw.line((100,100,100,300), fill='red')
draw.line((100,100,300,100), fill=(255, 255, 255))
```

5.画圆

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标和结束坐标（圆要画在其中间）
# 第二个参数：表示开始角度
# 第三个参数：表示结束角度
# 第四个参数：表示颜色
draw.arc((100,100,300,300),0,90,fill="red")
```

6.写文本

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
draw.text([0,0],'python',"red")
```

7.特殊字体文字

```python
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示字体文件路径
# 第二个参数：表示字体大小
font = ImageFont.truetype("kumo.ttf", 28)
# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
# 第四个参数：表示颜色
draw.text([0, 0], 'python', "red", font=font)
```

图片验证码

```python
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def check_code(width=120, height=30, char_length=5, font_file='kumo.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)


if __name__ == '__main__':
    # 1. 直接打开
    # img,code = check_code()
    # img.show()

    # 2. 写入文件
    # img,code = check_code()
    # with open('code.png','wb') as f:
    #     img.save(f,format='png')

    # 3. 写入内存(Python3)
    # from io import BytesIO
    # stream = BytesIO()
    # img.save(stream, 'png')
    # stream.getvalue()

    # 4. 写入内存（Python2）
    # import StringIO
    # stream = StringIO.StringIO()
    # img.save(stream, 'png')
    # stream.getvalue()

    pass
```

字体文件：[点击下载](http://files.cnblogs.com/files/wupeiqi/%E9%AA%8C%E8%AF%81%E7%A0%81%E5%AD%97%E4%BD%93%E6%96%87%E4%BB%B6.zip)

#### 3.2.Session&Cookie

django默认中，是有一个session表的，字段值分别为`session_key`、`session_data`、`expire_date`

![](https://web-image-link-1301132383.cos.ap-nanjing.myqcloud.com/django/session%26cookie.png)

![](https://web-image-link-1301132383.cos.ap-nanjing.myqcloud.com/django/code.png)

#### 3.3.页面显示

新建login路由

```python
    url(r'^login$', account.login, name='login'),
```

新建login视图函数

```python
def login(request):
    form = LoginForm()
    return render(request,'web/login.html',{'form':form})
```

新建login模板

```python
{% extends 'web/layout/basic.html' %}
{% load static %}

{% block title %}用户登陆{% endblock %}

{% block css %}
    <link rel="stylesheet" href="{% static 'web/css/account.css' %}">
{% endblock %}

{% block content %}
    <div class="account">
        <div class="title">用户登陆</div>
        <form id="regForm" method="POST" novalidate>
            {% csrf_token %}
            {% for field in form %}
                {% if field.name == 'code' %}
                    <div class="form-group"><label for="{{ field.id_for_label }}">{{ field.label }}</label>
                        <div class="row">
                            <div class="col-xs-7">
                                {{ field }}
                                <span class="error-msg">{{ field.errors.0 }}</span>
                            </div>
                            <div class="col-xs-5">
                                <img src="{% url 'web:image_code' %}" alt="">
                            </div>
                        </div>
                    </div>
                {% else %}
                    <div class="form-group">
                        <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                        {{ field }}
                        <span class="error-msg">{{ field.errors.0 }}</span>
                    </div>
                {% endif %}
            {% endfor %}
            <div class="row">
                <div class="col-xs-3">
                    <input type="submit" class="btn btn-primary" value="登  陆"/>
                </div>
            </div>
        </form>
    </div>
{% endblock %}



{% block js %}

{% endblock %}
```

更改提交方式为submit，span标签添加`field.errors.0`

新建图片验证码路由

```python
    url(r'^image_code$', account.image_code, name='image_code'),
```

新建图片验证码视图

```python
from utils.image_code import check_code
from io import BytesIO

def image_code(request):
    image_object ,code = check_code()
    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())
```

图片验证码直接写入内存中，然后直接返回给用户

将验证码写入`session`中，并设置过期时间

```python
def image_code(request):
    image_object ,code = check_code()
    request.session['image_code'] = code
    request.session.set_expiry(60)
    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())
```

问：session处理和redis处理对比

生成随机字符串，将这个随机字符串当成key，然后验证码当成value写到redis中，后面用户再来的时候，又要读redis取验证码，这样又得操作cookie，又得操作redis，比较麻烦。

而session，恰好会生成唯一标识，比较简单。

而发短信不用session，是用户自己填写的，手机号就是唯一标识，而不用我们生成唯一标识。



如果使用默认的sqlite数据库，session会存在dajngo-session表中，即使值过期了，字段值还会存在



设置点击事件，点击更换验证码

```javascript
    <script>
        $(function () {
            SwitchImageCode();
        })

        function SwitchImageCode() {
            $('#imageCode').click(function () {
                var oldSrc = $(this).attr('src')
                $(this).attr('src',oldSrc+'?')
            })
        }
    </script>
```



#### 3.4.登陆

account/login.py

```python
'''
用户名密码登陆
'''
def login(request):
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request,'web/login.html',{'form':form})
    form = LoginForm(request,data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username,password)

        # user_object =models.UserInfo.objects.filter(username=username,password=password).first()
        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(password=password).first()
        # 如果去数据库里拿到了
        print(user_object)
        if user_object:
            return redirect('/web/index')
        form.add_error('username','用户名或者密码错误')
    # 校验没通过的话，则会显示错误信息
    return render(request,'web/login.html',{'form':form})
```

forms/account.py

```python
class LoginForm(BootstrapForm, forms.Form):
    username = forms.CharField(label='邮箱或手机号')
    password = forms.CharField(label='密码',widget=forms.PasswordInput(render_value=True))
    code = forms.CharField(label='图片验证码')

    def __init__(self,request,*args,**kwargs):
        # super(LoginForm, self).__init__(*args,**kwargs)
        super().__init__(*args,**kwargs)
        self.request = request

    # 用户验证码的钩子函数
    def clean_code(self):
        # 读取用户输入的验证码
        code = self.cleaned_data['code']

        # 去session中获取自己的验证码
        session_code = self.request.session.get('image_code')
        print(session_code)
        if not session_code:
            raise ValidationError('验证码已过期，请重新获取')

        if code.strip().upper() != session_code.strip().upper():
            raise ValidationError('验证码输入错误')

        return code

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 加密，返回
        return md5(pwd)
```

表单提交的话，在登陆时，如果手机号或者验证码输入错误，提交时密码会置空，解决办法如下：

```python
    password = forms.CharField(label='密码',widget=forms.PasswordInput(render_value=True))
```

#### 3.5.页面联动

index.html

```html
{% extends 'web/layout/basic.html' %}
{% load static %}
{% block title %}首页{% endblock %}
{% block css %}
    <style>
        img {
            width: 100%;
        }
    </style>
{% endblock %}
{% block content %}
    <div>
        <img src="{% static 'web/img/index/index-1.png' %}" alt="">
        <img src="{% static 'web/img/index/index-2.png' %}" alt="">
        <img src="{% static 'web/img/index/index-3.png' %}" alt="">
        <img src="{% static 'web/img/index/index-4.png' %}" alt="">
    </div>
{% endblock %}
```

basic.html

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}{% endblock %}</title>

    <link rel="stylesheet" href="{% static 'web/plugin/bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'web/plugin/font-awesome/css/font-awesome.min.css' %}">

    <style>
        .navbar-default {
            border-radius: 0;
        }
    </style>

    {% block css %}{% endblock %}
</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container">            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false"><span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span></button>
                <a class="navbar-brand" href="{% url 'web:index' %}">Tracer</a></div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <!-- <li class="active"><a href="#">产品功能 <span class="sr-only">(current)</span></a></li> -->
                    <li><a href="#">产品功能</a></li>
                    <li><a href="#">企业方案</a></li>
                    <li><a href="#">帮助文档</a></li>
                    <li><a href="#">价格</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="{% url 'web:login' %}">登陆</a></li>
                    <li><a href="{% url 'web:register' %}">注册</a></li>
                    <li><a href="#">Link</a></li>
                    <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                            aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">管理中心</a></li>
{#                            <li><a href="#">Another action</a></li>#}
{#                            <li><a href="#">Something else here</a></li>#}
                            <li role="separator" class="divider"></li>
                            <li><a href="#">退出</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>

{% block content %}{% endblock %}

<script src="{% static 'web/js/jquery-3.4.1.min.js' %}"></script>
<script src="{% static 'web/plugin/bootstrap/js/bootstrap.js' %}"></script>

{% block js %}{% endblock %}

</body>
</html>
```

保存用户登陆的信息

```python
        if user_object:
            # 登陆成功
            request.session['user_id'] = user_object.id
            # 用户信息保存两周
            request.session.set_expiry(60*60*24*14)
            return redirect('/web/index')
```

#### 3.6.用户登陆状态校验

使用中间件

web/middleware/auth.py

```python
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
```

settings.py中配置

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'web.middleware.auth.AuthMiddleware',
]

```

basic.html进行登陆状态判断

```python
            <ul class="nav navbar-nav navbar-right">
                {% if request.tracer %}
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ request.tracer.username }}
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="#">管理中心</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="{% url 'web:logout' %}">退出</a></li>
                        </ul>
                    </li>
                {% else %}
                    <li><a href="{% url 'web:login' %}">登陆</a></li>
                    <li><a href="{% url 'web:register' %}">注册</a></li>
                {% endif %}
            </ul>
```

加入退出功能

```python
# 用户退出
def logout(request):
    request.session.flush()
    return redirect('/web/index')
```

## Day05.今日概要

### 今日概要

- django写离线脚本
- 探讨业务
- 设计表结构
- 我的表结构
- 功能实现
  - 查看项目列表
  - 创建项目
  - 星标项目

### 1.django离线脚本

理解为什么要用离线脚本，以及什么时候需要使用

```
django-框架
离线-非web运行时
脚本-一个或几个py文件
```

在某个py文件中，对django项目做一些处理

#### 1.1.示例1：使用离线脚本在用户表中插入数据

web/scripts/init_user.py

```python
#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-05 8:46
@func: 离线脚本测试

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
```

查看web_userinfo表，新增了刚刚插入的数据

#### 1.2.示例2：数据库中存储全国的省市县

#### 1.3.示例3：敏感字、词语（10w~20w）

#### 1.3.示例4：saas免费版：1G、5个项目、10人

### 2.探讨业务

#### 2.1.价格策略

| 分类   | 标题       | 价格/年 | 项目个数 | 项目成员 | 每个项目空间 | 单文件限制 | 创建时间 |
| ------ | ---------- | ------- | -------- | -------- | ------------ | ---------- | -------- |
| 免费版 | 个人免费版 | 0       | 5        | 5        | 20M          | 5M         |          |
| 收费版 | VIP        | 199     | 20       | 100      | 50G          | 200M       |          |
| 收费版 | VVIP       | 299     | 50       | 200      | 100G         | 1G         |          |
| 其他   |            |         |          |          |              |            |          |

注意：新用户注册拥有免费版的额度

#### 2.2.用户

| 用户名 | 手机号       | 密码 |
| ------ | ------------ | ---- |
| alex   | 123232323232 | 123  |
| amy    | 123232323233 | 123  |
| bruce  | 123232323234 | 123  |

#### 2.3.交易（关联表）

| ID   | 状态          | 用户 | 价格 | 实际支付 | 开始       | 结束       | 数量（年） | 订单号 |      |
| ---- | ------------- | ---- | ---- | -------- | ---------- | ---------- | ---------- | ------ | ---- |
| 1    | 已支付        | 1    | 1    | 0        | 2020-03-18 | null       | 0          | UY12   |      |
| 2    | 已支付        | 2    | 1    | 0        | 2020-03-18 | null       | 0          | UY13   |      |
| 3    | 已支付        | 3    | 1    | 0        | 2020-03-18 | null       | 0          | UY14   |      |
| 4    | 已支付        | 2    | 2    | 199      | 2020-04-18 | 2021-04-18 | 1          | UY15   |      |
| 5    | 未支付/已支付 | 3    | 3    | 299*2    | 2020-05-18 | 2022-05-18 | 2          | UY16   |      |

`request.tracer = 交易对象`

#### 2.4.创建存储

基于腾讯对象存储COS存储数据

#### 2.5.项目

| ID   | 项目名称 | 描述 | 颜色    | 星标 | 参与人数 | 创建者 | 已使用空间 |      |      |
| ---- | -------- | ---- | ------- | ---- | -------- | ------ | ---------- | ---- | ---- |
| 1    | CRM      | des  | #cccccc | true | 5        | 3      | 5M         |      |      |
| 2    | saas     |      |         |      |          |        |            |      |      |

#### 2.6.项目参与者

| ID   | 项目 | 用户 | 星标 |
| ---- | ---- | ---- | ---- |
| 1    | 1    | 1    | true |
| 2    | 2    | 2    |      |

### 3.任务

#### 3.1.创建相应表结构

models.py

```python
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,db_index=True)
    email = models.EmailField(verbose_name='邮箱',max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)

class PricePolicy(models.Model):
    # 价格策略
    category_choices = (
        (1,'免费版'),
        (2,'收费版'),
        (3,'其他'),
    )

    category = models.SmallIntegerField(verbose_name='收费类型',default=2,choices=category_choices)
    title = models.CharField(verbose_name='标题',max_length=32)
    price = models.PositiveIntegerField(verbose_name='价格',null=True,blank=True)

    project_num = models.PositiveIntegerField(verbose_name='项目数')
    project_member = models.PositiveIntegerField(verbose_name='项目成员数')
    project_space = models.PositiveIntegerField(verbose_name='单项目空间')
    per_file_size = models.PositiveIntegerField(verbose_name='单文件大小（M）')

    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

class Transaction(models.Model):
    '''交易记录'''
    status_choice = (
        (1,'未支付'),
        (2,'已支付'),
    )

    status = models.SmallIntegerField(verbose_name='状态',choices=status_choice)

    order = models.CharField(verbose_name='订单号',max_length=64,unique=True) # 唯一索引

    user = models.ForeignKey(verbose_name='用户',to='UserInfo')
    price_policy = models.ForeignKey(verbose_name='价格策略',to='PricePolicy')

    count = models.IntegerField(verbose_name='数量（年）',help_text='0表示无限制')

    price = models.IntegerField(verbose_name='实际支付价格')

    start_datetime = models.DateTimeField(verbose_name='开始时间',null=True,blank=True)
    end_datetime = models.DateTimeField(verbose_name='结束时间',null=True,blank=True)

    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

class Project(models.Model):
    '''项目表'''
    COLOR_CHOICES = (
        (1,'#A02128'),
        (2,'#D15B8F'),
        (3,'#DD7907'),
        (4,'#D2B773'),
        (5,'#28713E'),
        (6,'#154889'),
        (7,'#8F4E35'),
    )
    name = models.CharField(verbose_name='项目表',max_length=32)
    color = models.SmallIntegerField(verbose_name='颜色',choices=COLOR_CHOICES,default=1)
    desc = models.CharField(verbose_name='项目描述',max_length=255,null=True,blank=True)
    use_space = models.BigIntegerField(verbose_name='项目已使用空间',default=0)
    star = models.BooleanField(verbose_name='星标',default=False)

    # bucket = models.CharField(verbose_name='腾讯对象存储桶',default=1)
    # region = models.CharField(verbose_name='腾讯对象存储桶区域',max_length=32)

    join_count = models.SmallIntegerField(verbose_name='参与人数',default=1)
    creator = models.ForeignKey(verbose_name='创建者',to='UserInfo')
    create_datetime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    # 查询，可以省事儿
    # 增加、删除、修改：无法完成
    # project_user = models.ManyToManyField(to='UserInfo',through='ProjectUser',through_fields=('projects','user'))

class ProjectUser(models.Model):
    '''项目参与者'''
    user = models.ForeignKey(verbose_name='参与者',to='UserInfo',related_name='projects')
    projects = models.ForeignKey(verbose_name='项目',to='Project')

    invitee = models.ForeignKey(verbose_name='邀请者',to='UserInfo',related_name='invites',null=True,blank=True)

    star = models.BooleanField(verbose_name='星标',default=True)

    create_time = models.DateTimeField(verbose_name='加入时间',auto_now_add=True)

```

反向关联表

```python
obj = UserInfo.objects.filter(id=1)
obj.projectuser_set.all()
# 一张表有一个以上的ForeignKey时，需要加related_name以供反向关联
obj.projects.all()
```

#### 3.2.离线脚本

- 创建价格策略【免费版】

| 分类   | 标题       | 价格/年 | 项目个数 | 项目成员 | 每个项目空间 | 单文件限制 | 创建时间 |
| ------ | ---------- | ------- | -------- | -------- | ------------ | ---------- | -------- |
| 免费版 | 个人免费版 | 0       | 3        | 2        | 20M          | 5M         |          |

price字段允许为空的，models中的字段需要加上`null=True,blank=True`

#### 3.3.用户注册【改】

- 之前：注册成功，只是新建用户
- 现在：
  - 新建用户
  - 新建交易记录【免费版】

views/account.py

```python
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    # print(request.POST)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证通过，写入数据库，密码要是密文
        instance = form.save()
        policy_object = models.PricePolicy.objects.filter(category=1,title='个人免费版').first()
        #创建交易记录
        models.Transaction.objects.create(
            status=2,
            order=str(uuid.uuid4()),
            user=instance,
            price_policy=policy_object,
            count=0,
            price=0,
            start_datetime=datetime.datetime.now()
        )
        # data = form.cleaned_data
        # data.pop('code')
        # data.pop('confirm_password')
        # instance = models.UserInfo.objects.create(**data)
        return JsonResponse({'status': True,'data':'/web/login/'})
    else:
        # print(form.errors)
        return JsonResponse({'status': False, 'error': form.errors})
    return JsonResponse({})
```

#### 3.4.添加项目

##### 3.4.1.项目列表母版+样式

manage.html

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}{% endblock %}</title>

    <link rel="stylesheet" href="{% static 'web/plugin/bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'web/plugin/font-awesome/css/font-awesome.min.css' %}">
    <link rel="stylesheet" href="{% static 'web/css/manage.css' %}">


    {% block css %}{% endblock %}
</head>

<body>
<nav class="navbar navbar-av">
    <div class="container-fluid">            <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false"><span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span></button>
            <a class="navbar-brand" href="{% url 'web:project_list' %}">Tracer</a></div>
        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">

                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">项目 <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">One more separated link</a></li>
                    </ul>
                </li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">工作台</a></li>
                <li><a href="#">日历</a></li>
                <li><a href="#"><i class="fa fa-bell-o" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-bookmark" aria-hidden="true"></i></a></li>

                {% if request.tracer %}
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                           aria-expanded="false">{{ request.tracer.username }}
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="{% url 'web:index' %}">回到官网</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="{% url 'web:logout' %}">退出</a></li>
                        </ul>
                    </li>
                {% else %}
                    <li><a href="{% url 'web:login' %}">登陆</a></li>
                    <li><a href="{% url 'web:register' %}">注册</a></li>
                {% endif %}
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

{% block content %}{% endblock %}

<script src="{% static 'web/js/jquery-3.4.1.min.js' %}"></script>
<script src="{% static 'web/plugin/bootstrap/js/bootstrap.js' %}"></script>

{% block js %}{% endblock %}

</body>
</html>
```

manage.css

```css
body {
    margin: 0;
    font-weight: 200;
}

@media (min-width: 1500px) {
    .container {
        width: 1400px;
    }
}

.navbar {
    border-radius: 0;
    margin-bottom: 0;
    color: #ffffff;
    height: 52px;
}

@media (min-width: 900px) {
    .navbar-header {
        float: left;
    }
}

.navbar-av {
    background-color: #499ef3;
    border-color: #499ef3;
}

.navbar-av .navbar-brand {
    color: #ffffff;
    margin: 0 15px;
}

.navbar-av .navbar-brand:hover,
.navbar-av .navbar-brand:focus {
    color: #ffffff;
    background-color: #4dabff;
}

.navbar-av .navbar-text {
    color: #ffffff;
}

.navbar-av .navbar-nav {
    margin: 0 -15px;

}

.navbar-av .navbar-nav > li {
    z-index: 1001;

}

.navbar-av .navbar-nav > li > a {
    color: #ffffff;
    background-color: #499ef3;
    padding-left: 13px;
    padding-right: 13px;

}

.navbar-av .navbar-nav > li > a:hover,
.navbar-av .navbar-nav > li > a:focus {
    color: #ffffff;
    background-color: #4dabff;

}

.navbar-av .navbar-nav > .active > a,
.navbar-av .navbar-nav > .active > a:hover,
.navbar-av .navbar-nav > .active > a:focus {
    color: #ffffff;
    background-color: #4dabff;

}

.navbar-av .navbar-nav > .disabled > a,
.navbar-av .navbar-nav > .disabled > a:hover,
.navbar-av .navbar-nav > .disabled > a:focus {
    color: #ffffff;
    background-color: #4dabff;
}

.navbar-av .navbar-toggle {
    border-color: #499ef3;
}

.navbar-av .navbar-toggle:hover,
.navbar-av .navbar-toggle:focus {
    background-color: #4dabff;
}

.navbar-av .navbar-toggle .icon-bar {
    background-color: #ffffff;
}

.navbar-av .navbar-collapse,
.navbar-av .navbar-form {
    border-color: #e7e7e7;
}

.navbar-av .navbar-nav > .open > a,
.navbar-av .navbar-nav > .open > a:hover,
.navbar-av .navbar-nav > .open > a:focus {
    color: #ffffff;
    background-color: #4dabff;
}

@media (max-width: 767px) {
    .navbar-av .navbar-nav .open .dropdown-menu {
        padding: 0;
    }

    .navbar-av .navbar-nav .open .dropdown-menu > li > a {
        color: #ffffff;
        background-color: #499ef3;
    }

    .navbar-av .navbar-nav .open .dropdown-menu > li > a:hover,
    .navbar-av .navbar-nav .open .dropdown-menu > li > a:focus {
        color: #ffffff;
        background-color: #4dabff;
    }

    .navbar-av .navbar-nav .open .dropdown-menu > .active > a,
    .navbar-av .navbar-nav .open .dropdown-menu > .active > a:hover,
    .navbar-av .navbar-nav .open .dropdown-menu > .active > a:focus {
        color: #ffffff;
        background-color: #4dabff;
    }

    .navbar-av .navbar-nav .open .dropdown-menu > .disabled > a,
    .navbar-av .navbar-nav .open .dropdown-menu > .disabled > a:hover,
    .navbar-av .navbar-nav .open .dropdown-menu > .disabled > a:focus {
        color: #ffffff;
        background-color: #4dabff;
    }
}

.navbar-av .navbar-link {
    color: #ffffff;
}

.navbar-av .navbar-link:hover {
    color: #ffffff;
}

.navbar-av .btn-link {
    color: #ffffff;
}

.navbar-av .btn-link:hover,
.navbar-av .btn-link:focus {
    color: #ffffff;
}

.navbar-av .btn-link[disabled]:hover,
fieldset[disabled] .navbar-av .btn-link:hover,
.navbar-av .btn-link[disabled]:focus,
fieldset[disabled] .navbar-av .btn-link:focus {
    color: #ffffff;
}

.navbar-av .navbar-nav > li > .sep{
    padding: 15px 5px;display: inline-block
}

.dropdown-menu>li{
    padding: 0 5px;
    color: black;
}
```

project_list.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .project {
            margin-top: 10px;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid project">
        <a href="#" class="btn btn-primary"><i class="fa fa-plus-circle"></i> 创建项目</a>
    </div>
{% endblock %}
```

- 后台：登陆成功之后才可以访问
- 官网：都可以访问
- 通过 中间件+白名单，对后台管理的权限，进行处理

settings.py

```python
# 无需登陆就可以访问的白名单
WHITE_REGEX_URL_LIST = [
    '/web/register/',
    '/web/send_sms/',
    '/web/login/sms/',
    '/web/login/',
    '/web/image_code/',
    '/web/index/',
]
```

middleware/auth.py

```python
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

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 如果用户已登陆，则在request中赋值，否则设置为0
        user_id = request.session.get('user_id',0)

        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object
        # 白名单，没有登陆都可以访问的url
        '''
            1.获取当前用户访问的url
            2.检查url是否在白名单中，如果在则可以继续访问，否则进行判断是否已登录
        '''
        # print(request.path_info)
        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return
        # 检查用户是否已登陆，已登陆继续往后走，未登陆则返回登陆页面
        if not request.tracer:
            return redirect('web:login')
```

- 当前拥有的价格策略（额度）

auth.py

```python
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
        if not request.tracer:
            return redirect('web:login')

        # 登陆成功后，访问后台管理时，获取当前用户所拥有的额度
        # 方式一：免费额度在交易记录中存储

        # 获取当前用户ID值最大（最近交易记录）
        _object = models.Transaction.objects.filter(user=user_object, status=2).order_by('-id').first()
        # 判断是否已过期
        current_datetime = datetime.datetime.now()
        if _object.end_datetime and _object.end_datetime < current_datetime:
            # 过期
            _object = models.Transaction.objects.filter(user=user_object, status=2, price_policy_category=1).first()
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

```

account.py

```python
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'web/register.html', {'form': form})
    # print(request.POST)
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证通过，写入数据库，密码要是密文
        instance = form.save()
        policy_object = models.PricePolicy.objects.filter(category=1,title='个人免费版').first()

        # 创建交易记录
        # 方式一
        models.Transaction.objects.create(
            status=2,
            order=str(uuid.uuid4()),
            user=instance,
            price_policy=policy_object,
            count=0,
            price=0,
            start_datetime=datetime.datetime.now()
        )

        # 方式二
        # 不用写


        # data = form.cleaned_data
        # data.pop('code')
        # data.pop('confirm_password')
        # instance = models.UserInfo.objects.create(**data)
        return JsonResponse({'status': True,'data':'/web/login/'})
    else:
        # print(form.errors)
        return JsonResponse({'status': False, 'error': form.errors})
    return JsonResponse({})
```



##### 3.4.2.添加

forms/project.py

```python
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

class ProjectModelForms(BootstrapForm, forms.ModelForm):
    # desc = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = models.Project
        fields = ['name', 'color', 'desc']
        widgets = {
            'desc': forms.Textarea
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

```

template/web/project_list.html

```python
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .project {
            margin-top: 10px;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid project">
        <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#addModal"><i
                class="fa fa-plus-circle"></i>
            创建项目</a>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">新建项目</h4>
                </div>
                <div class="modal-body">
                    <form id="addForm">
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                                {{ field }}
                                <span class="error-msg"></span>
                            </div>
                        {% endfor %}
                    </form>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button id="btnSubmit" type="button" class="btn btn-primary">确定</button>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block js %}
    <script>
        $(function () {
            bindSubmit()
        })

        function bindSubmit() {
            $('#btnSubmit').click(function () {
                $.ajax({
                    url: "{% url 'web:project_list' %}",
                    type: "POST",
                    data: $('#addForm').serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        if (res.status) {
                            location.reload()
                            //location.href = location.href
                        } else {
                            $.each(res.error, function (key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}
```

views/project.py

```python
from django.shortcuts import render,HttpResponse,redirect
from web.forms.project import ProjectModelForms
from django.http import JsonResponse

def project_list(request):
    '''项目列表'''
    # print(request.tracer.user)
    # print(request.tracer.price_policy)
    if request.method == 'GET':
        form = ProjectModelForms(request)
        return render(request,'web/project_list.html',{'form':form})
    form = ProjectModelForms(request,data=request.POST)
    if form.is_valid():
        # 验证通过：项目名，颜色，描述，创建者
        form.instance.creator = request.tracer.user
        # 验证通过
        form.save()
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})
```

#### 3.5.展示项目

- 展示
- 我创建的
- 我参与的

##### 3.5.1.数据

1.从数据库中获取两部分数据

​	我创建的所有项目：已星标、未星标

​	我参与的所有项目：已星标、未星标

2.提取已星标

​	列表 = 循环 [我创建的所有项目] + [我参与的所有项目] 把已星标的数据提取

得到三个列表：星标、创建、参与

##### 3.5.2.样式

project_list.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .project {
            margin-top: 10px;
        }

        .panel-body {
            padding: 0;
            display: flex;
            flex-direction: row;
            justify-content: left;
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .panel-body > .item {
            border-radius: 6px;
            width: 228px;
            border: 1px solid #dddddd;
            margin: 20px 10px;

        }

        .panel-body > .item:hover {
            border: 1px solid #f0ad4e;
        }

        .panel-body > .item > .title {
            height: 104px;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            font-size: 15px;
            text-decoration: none;
        }

        .panel-body > .item > .info {
            padding: 10px 10px;

            display: flex;
            justify-content: space-between;

            border-bottom-left-radius: 6px;
            border-bottom-right-radius: 6px;
            color: #8c8c8c;

        }

        .panel-body > .item > .info a {
            text-decoration: none;
        }

        .panel-body > .item > .info .fa-star {
            font-size: 18px;
        }

        .color-radio label {
            margin-left: 0;
            padding-left: 0;
        }

        .color-radio input[type="radio"] {
            display: none;
        }

        .color-radio input[type="radio"] + .cycle {
            display: inline-block;
            height: 25px;
            width: 25px;
            border-radius: 50%;
            border: 2px solid #dddddd;
        }

        .color-radio input[type="radio"]:checked + .cycle {
            border: 2px solid black;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid project">
        <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#addModal"><i
                class="fa fa-plus-circle"></i>
            创建项目</a>
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-star" aria-hidden="true"></i> 星标</div>
            <div class="panel-body">
                {% for item in project_dict.star %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="#">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-list" aria-hidden="true"></i> 我创建的</div>
            <div class="panel-body">
                {% for item in project_dict.my %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="#">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-handshake-o" aria-hidden="true"></i> 我参与的</div>
            <div class="panel-body">
                {% for item in project_dict.join %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="#">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">新建项目</h4>
                </div>
                <div class="modal-body">
                    <form id="addForm">
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                                {{ field }}
                                <span class="error-msg"></span>
                            </div>
                        {% endfor %}
                    </form>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button id="btnSubmit" type="button" class="btn btn-primary">确定</button>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block js %}
    <script>
        $(function () {
            bindSubmit()
        })

        function bindSubmit() {
            $('#btnSubmit').click(function () {
                $.ajax({
                    url: "{% url 'web:project_list' %}",
                    type: "POST",
                    data: $('#addForm').serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        if (res.status) {
                            location.reload()
                            //location.href = location.href
                        } else {
                            $.each(res.error, function (key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}
```



#### 3.6.星标项目(去除星标)

##### 3.6.1.星标

我创建的项目：Project的star设置为True

我参与的项目：ProjectUser的star设置为True

urls.py

```python
from django.conf.urls import url,include
from web.views import account,home,project

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^send_sms/$', account.send_sms, name='send_sms'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^logout/$', account.logout, name='logout'),
    url(r'^image_code/$', account.image_code, name='image_code'),
    url(r'^index/$', home.index, name='index'),

    # 项目管理
    url(r'^project/list$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    # url(r'^project/list$', project.project_list, name='project_list'),

]
```

views/project.py

```python
def project_star(request,project_type,project_id):
    '''星标项目'''
    if project_type == 'my':
        models.Project.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    return HttpResponse('请求错误')
```



##### 3.6.2.移除星标

我创建的项目：Project的star设置为False

我参与的项目：ProjectUser的star设置为False

urls.py

```python
from django.conf.urls import url,include
from web.views import account,home,project

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^send_sms/$', account.send_sms, name='send_sms'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^logout/$', account.logout, name='logout'),
    url(r'^image_code/$', account.image_code, name='image_code'),
    url(r'^index/$', home.index, name='index'),

    # 项目管理
    url(r'^project/list$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

]
```

views/project.py

```python
def project_star(request,project_type,project_id):
    '''星标项目'''
    if project_type == 'my':
        models.Project.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    return HttpResponse('请求错误')

def project_unstar(request,project_type,project_id):
    '''取消星标项目'''
    if project_type == 'my':
        models.Project.objects.filter(id=project_id,creator=request.tracer.user).update(star=False)
        return redirect('web:project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(id=project_id,creator=request.tracer.user).update(star=Fasle)
        return redirect('web:project_list')
    return HttpResponse('请求错误')
```

#### 3.7.颜色

##### 3.7.1.color字段不应用bootstrap样式

forms/bootstrap.py

```python
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
```

##### 3.7.2.生成颜色选择框

forms/project.py

```python
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

```

templates/widgets/color_radio

radio.html

```html
{% with id=widget.attrs.id %}
    <div{% if id %} id="{{ id }}"{% endif %}{% if widget.attrs.class %} class="{{ widget.attrs.class }}"{% endif %}>
        {% for group, options, index in widget.optgroups %}
            {% for option in options %}
                <label {% if option.attrs.id %} for="{{ option.attrs.id }}"{% endif %} >
                    {% include option.template_name with widget=option %}
                </label>
            {% endfor %}
        {% endfor %}
    </div>
{% endwith %}

```

radio_option.html

```html
{% include "widgets/color_radio/input.html" %}
<span class="cycle" style="background-color:{{ option.label }}"></span>
```

input.html

```html
<input type="{{ widget.type }}" name="{{ widget.name }}"{% if widget.value != None %} value="{{ widget.value|stringformat:'s' }}"{% endif %}{% include "widgets/color_radio/attrs.html" %} />

```

attrs.html

```html
{% for name, value in widget.attrs.items %}{% if value is not False %} {{ name }}{% if value is not True %}="{{ value|stringformat:'s' }}"{% endif %}{% endif %}{% endfor %}
```

input.html和attrs.html就是django自带的

project_list.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .project {
            margin-top: 10px;
        }

        .panel-body {
            padding: 0;
            display: flex;
            flex-direction: row;
            justify-content: left;
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .panel-body > .item {
            border-radius: 6px;
            width: 228px;
            border: 1px solid #dddddd;
            margin: 20px 10px;

        }

        .panel-body > .item:hover {
            border: 1px solid #f0ad4e;
        }

        .panel-body > .item > .title {
            height: 104px;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            font-size: 15px;
            text-decoration: none;
        }

        .panel-body > .item > .info {
            padding: 10px 10px;

            display: flex;
            justify-content: space-between;

            border-bottom-left-radius: 6px;
            border-bottom-right-radius: 6px;
            color: #8c8c8c;

        }

        .panel-body > .item > .info a {
            text-decoration: none;
        }

        .panel-body > .item > .info .fa-star {
            font-size: 18px;
        }

        .color-radio label {
            margin-left: 0;
            padding-left: 0;
        }

        .color-radio input[type="radio"] {
            display: none;
        }

        .color-radio input[type="radio"] + .cycle {
            display: inline-block;
            height: 25px;
            width: 25px;
            border-radius: 50%;
            border: 2px solid #dddddd;
        }

        .color-radio input[type="radio"]:checked + .cycle {
            border: 2px solid black;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid project">
        <div style="margin: 10px 0;">
            <a class="btn btn-primary" data-toggle="modal" data-target="#addModal"><i
                    class="fa fa-plus-circle"></i>
                创建项目</a>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-star" aria-hidden="true"></i> 星标</div>
            <div class="panel-body">
                {% for item in project_dict.star %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.value.get_color_display }};">{{ item.value.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_unstar' project_type=item.type project_id=item.value.id %}">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                                </a>
                                <span>{{ item.value.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.value.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-list" aria-hidden="true"></i> 我创建的</div>
            <div class="panel-body">
                {% for item in project_dict.my %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_star' project_type='my' project_id=item.id %}">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-handshake-o" aria-hidden="true"></i> 我参与的</div>
            <div class="panel-body">
                {% for item in project_dict.join %}
                    <div class="item">
                        <a href="" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_star' project_type='join' project_id=item.id %}">
                                <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">新建项目</h4>
                </div>
                <div class="modal-body">
                    <form id="addForm">
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                                {{ field }}
                                <span class="error-msg"></span>
                            </div>
                        {% endfor %}
                    </form>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button id="btnSubmit" type="button" class="btn btn-primary">确定</button>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block js %}
    <script>
        $(function () {
            bindSubmit()
        })

        function bindSubmit() {
            $('#btnSubmit').click(function () {
                $.ajax({
                    url: "{% url 'web:project_list' %}",
                    type: "POST",
                    data: $('#addForm').serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        if (res.status) {
                            location.reload()
                            //location.href = location.href
                        } else {
                            $.each(res.error, function (key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}	
```

#### 3.8.切换菜单

1.数据库中获取：

​	我创建的

​	我参与的

2.循环显示

3.当前页面需要显示/其他页面也需要显示[inclusion_tag]

manage.html

```html
{% load static %}
{% load project %}


<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            {% all_project_list request %}
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">工作台</a></li>
                <li><a href="#">日历</a></li>
                <li><a href="#"><i class="fa fa-bell-o" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-bookmark" aria-hidden="true"></i></a></li>

                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">{{ request.tracer.user.username }}
                        <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="{% url 'web:index' %}">回到官网</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="{% url 'web:logout' %}">退出</a></li>
                    </ul>
                </li>
            </ul>
        </div>
```

web/inclusion/all_project_list.html

```html
<ul class="nav navbar-nav">
    <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
           aria-expanded="false">项目 <span class="caret"></span></a>
        <ul class="dropdown-menu">
            {% if my %}
                <li><i class="fa fa-list" aria-hidden="true"></i> 我创建的项目</li>
                {% for item in my %}
                    <li><a href="#">{{ item.name }}</a></li>
                {% endfor %}

                <li role="separator" class="divider"></li>
            {% endif %}

            {% if join %}
                <li><i class="fa fa-handshake-o" aria-hidden="true"></i> 我参与的项目</li>

                {% for item in join %}
                    <li><a href="#">{{ item.project.name }}</a></li>
                {% endfor %}
                <li role="separator" class="divider"></li>
            {% endif %}
            <li><a href="{% url 'web:project_list' %}">所有项目</a></li>
        </ul>
    </li>
</ul>
```

templatetags/project.py

```python
#!/usr/bin/env python
# encoding: utf-8
'''

@time: 2021-10-07 14:58
@func:

'''

from django.template import Library
from web import models


register = Library()

@register.inclusion_tag('web/inclusion/all_project_list.html')
def all_project_list(request):
    # 1.获取我创建的项目
    my_project_list = models.Project.objects.filter(creator=request.tracer.user)

    # 2.获取我参与的项目
    join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)

    return {'my': my_project_list,'join':join_project_list}
```

#### 3.9.项目管理

##### 3.9.1.url规划

```
/manage/项目ID/dashboard
/manage/项目ID/issues
/manage/项目ID/statistics
/manage/项目ID/file
/manage/项目ID/wiki
/manage/项目ID/setting
```

urls.py

```python
from django.conf.urls import url,include
from web.views import account,home,project,manage

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^send_sms/$', account.send_sms, name='send_sms'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^logout/$', account.logout, name='logout'),
    url(r'^image_code/$', account.image_code, name='image_code'),
    url(r'^index/$', home.index, name='index'),

    # 项目列表
    url(r'^project/list$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_type>\w+)/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

    # 项目管理
    url(r'^manage/(?P<project_id>\d+)/',include([
        url(r'^dashboard/$', manage.dashboard, name='dashboard'),
        url(r'^issues/$', manage.issues, name='issues'),
        url(r'^statistics/$', manage.statistics, name='statistics'),
        url(r'^file/$', manage.file, name='file'),
        url(r'^wiki/$', manage.wiki, name='wiki'),
        url(r'^setting/$', manage.setting, name='setting'),
    ],)),
	# 若写做include([],None,None)，reverse的时候提示找不到视图函数
]
```

views/manage.py

```python
#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render


def dashboard(request, project_id):
    return render(request, 'web/dashboard.html')


def issues(request, project_id):
    return render(request, 'web/issues.html')


def statistics(request, project_id):
    return render(request, 'web/statistics.html')


def file(request, project_id):
    return render(request, 'web/file.html')


def wiki(request, project_id):
    return render(request, 'web/wiki.html')


def setting(request, project_id):
    return render(request, 'web/setting.html')

```

project_list.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .project {
            margin-top: 10px;
        }

        .panel-body {
            padding: 0;
            display: flex;
            flex-direction: row;
            justify-content: left;
            align-items: flex-start;
            flex-wrap: wrap;
        }

        .panel-body > .item {
            border-radius: 6px;
            width: 228px;
            border: 1px solid #dddddd;
            margin: 20px 10px;

        }

        .panel-body > .item:hover {
            border: 1px solid #f0ad4e;
        }

        .panel-body > .item > .title {
            height: 104px;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            font-size: 15px;
            text-decoration: none;
        }

        .panel-body > .item > .info {
            padding: 10px 10px;

            display: flex;
            justify-content: space-between;

            border-bottom-left-radius: 6px;
            border-bottom-right-radius: 6px;
            color: #8c8c8c;

        }

        .panel-body > .item > .info a {
            text-decoration: none;
        }

        .panel-body > .item > .info .fa-star {
            font-size: 18px;
        }

        .color-radio label {
            margin-left: 0;
            padding-left: 0;
        }

        .color-radio input[type="radio"] {
            display: none;
        }

        .color-radio input[type="radio"] + .cycle {
            display: inline-block;
            height: 25px;
            width: 25px;
            border-radius: 50%;
            border: 2px solid #dddddd;
        }

        .color-radio input[type="radio"]:checked + .cycle {
            border: 2px solid black;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid project">
        <div style="margin: 10px 0;">
            <a class="btn btn-primary" data-toggle="modal" data-target="#addModal"><i
                    class="fa fa-plus-circle"></i>
                创建项目</a>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-star" aria-hidden="true"></i> 星标</div>
            <div class="panel-body">
                {% for item in project_dict.star %}
                    <div class="item">
                        <a href="{% url 'dashboard' project_id=item.value.id %}" class="title"
                           style="background-color: {{ item.value.get_color_display }};">{{ item.value.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_unstar' project_type=item.type project_id=item.value.id %}">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                                </a>
                                <span>{{ item.value.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.value.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-list" aria-hidden="true"></i> 我创建的</div>
            <div class="panel-body">
                {% for item in project_dict.my %}
                    <div class="item">
                        <a href="{% url 'dashboard' project_id=item.id %}" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_star' project_type='my' project_id=item.id %}">
                                    <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>

        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-handshake-o" aria-hidden="true"></i> 我参与的</div>
            <div class="panel-body">
                {% for item in project_dict.join %}
                    <div class="item">
                        <a href="{% url 'dashboard' project_id=item.id %}" class="title"
                           style="background-color: {{ item.get_color_display }};">{{ item.name }}</a>
                        <div class="info">
                            <div>
                                <a href="{% url 'web:project_star' project_type='join' project_id=item.id %}">
                                <i class="fa fa-star" aria-hidden="true" style="color: #d5d5d5;"></i>
                                </a>
                                <span>{{ item.creator.username }}</span>
                            </div>
                            <div>
                                <i class="fa fa-user-o" aria-hidden="true"></i>
                                <span>{{ item.join_count }}</span>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="addModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">新建项目</h4>
                </div>
                <div class="modal-body">
                    <form id="addForm">
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                                {{ field }}
                                <span class="error-msg"></span>
                            </div>
                        {% endfor %}
                    </form>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button id="btnSubmit" type="button" class="btn btn-primary">确定</button>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block js %}
    <script>
        $(function () {
            bindSubmit()
        })

        function bindSubmit() {
            $('#btnSubmit').click(function () {
                $.ajax({
                    url: "{% url 'web:project_list' %}",
                    type: "POST",
                    data: $('#addForm').serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        if (res.status) {
                            location.reload()
                            //location.href = location.href
                        } else {
                            $.each(res.error, function (key, value) {
                                $("#id_" + key).next().text(value[0])
                            })
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}
```

##### 3.9.2.进入项目展示菜单

 - 判断是否进入项目
    - 判断url是否以manage开头
    - project_id是我创建的 or 我参与的
- 使用中间件



auth.py

```python
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
            _object = models.Transaction.objects.filter(user=user_object, status=2, price_policy_category=1).first()
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

```



##### 3.9.3.修复页面小bug

inclusion/project_list.html

```html
<li class="dropdown">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
       aria-expanded="false">项目 <span class="caret"></span></a>
    <ul class="dropdown-menu">
        {% if my %}
            <li><i class="fa fa-list" aria-hidden="true"></i> 我创建的项目</li>
            {% for item in my %}
                <li><a href="#">{{ item.name }}</a></li>
            {% endfor %}

            <li role="separator" class="divider"></li>
        {% endif %}

        {% if join %}
            <li><i class="fa fa-handshake-o" aria-hidden="true"></i> 我参与的项目</li>

            {% for item in join %}
                <li><a href="#">{{ item.project.name }}</a></li>
            {% endfor %}
            <li role="separator" class="divider"></li>
        {% endif %}
        <li><a href="{% url 'web:project_list' %}">所有项目</a></li>
    </ul>
</li>

```

manage.html

```html
            <ul class="nav navbar-nav">

                {% all_project_list request %}

                {% if request.tracer.project %}
                    <li><a href="#">概述</a></li>
                    <li><a href="#">wiki</a></li>
                    <li><a href="#">配置</a></li>
                {% endif %}
            </ul>
```

##### 3.9.4.项目菜单默认选中

每个的project_id保持一致

manage.html

```html
                {% if request.tracer.project %}
                    <li><a href="{% url 'web:dashboard' project_id=request.tracer.project.id %}">概述</a></li>
                    <li><a href="{% url 'web:issues' project_id=request.tracer.project.id %}">问题</a></li>
                    <li><a href="{% url 'web:wiki' project_id=request.tracer.project.id %}">wiki</a></li>

                {% endif %}
```



改写上面的

templatetags/project.py

```python
@register.inclusion_tag('web/inclusion/manage_menu_list.html')
def manage_menu_list(request):
    data_list = [
        {'title': '概览','url': reverse('web:dashboard',kwargs={'project_id':request.tracer.project.id})},
        {'title': '问题', 'url': reverse('web:issues', kwargs={'project_id': request.tracer.project.id})},
        {'title': '统计', 'url': reverse('web:statistics', kwargs={'project_id': request.tracer.project.id})},
        {'title': 'wiki', 'url': reverse('web:wiki', kwargs={'project_id': request.tracer.project.id})},
        {'title': '文件', 'url': reverse('web:file', kwargs={'project_id': request.tracer.project.id})},
        {'title': '配置', 'url': reverse('web:setting', kwargs={'project_id': request.tracer.project.id})},
    ]
    for item in data_list:
        if request.path_info.startswith(item['url']):
            item['class'] = 'active'
    return {'data_list':data_list}
```

inclusion/manage_menu_list.html

```html
{#<li><a href="{% url 'web:dashboard' project_id=request.tracer.project.id %}">概述</a></li>#}
{#<li><a href="{% url 'web:issues' project_id=request.tracer.project.id %}">问题</a></li>#}
{#<li><a href="{% url 'web:wiki' project_id=request.tracer.project.id %}">wiki</a></li>#}

{% for item in data_list %}
    <li {% if item.class %} class="{{ item.class }}" {% endif %} > <a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
```

manage.html

```html
                {% if request.tracer.project %}
                    {% manage_menu_list request %}
                {% endif %}
```

#### 内容总结

1.项目实现思路

2.星标/取消星标

3.inclusion_tag实现项目切换

4.项目菜单

- 中间件 process_view
- 默认选中 inclusion_tag
- 路由分发
  - include("xxx.url")
  - include([aa,bb])
- 颜色选择
  - 源码+扩展【实现】

## Day06.今日概要

**wiki**

- 表结构设计
- 快速开发
- 应用markdown组件
- 腾讯COS做上传

### 1.表结构设计

| ID   | 标题 | 内容 | 项目ID | 父ID |
| ---- | ---- | ---- | ------ | ---- |
| 1    |      |      |        | null |
| 2    |      |      |        | 1    |
|      |      |      |        |      |

```python
class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目',to='Project')
    title = models.CharField(verbose_name='标题',max_length=32)
    content = models.TextField(verbose_name='内容')

    # 自关联
    parent = models.ForeignKey(verbose_name='父文章',to='Wiki',null=True,blank=True,related_name='children')
```

### 2.快速开发

#### 2.1.wiki首页展示

将原来的视图函数分离出来，并修改对应的url 

```python
url(r'^wiki/$', wiki.wiki, name='wiki'),
```



wiki.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .panel-default {
            margin-top: 10px;
        }
        .panel-body{
            padding: 0;
        }
        .title-list {
            border-right: 1px solid #dddddd;
            min-height: 500px;
        }
        .content {
            border-left: 1px solid #dddddd;
            min-height: 600px;
            margin-left: -1px;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid">
        <div class="panel panel-default">
            <div class="panel-heading"><i class="fa fa-book" aria-hidden="true"></i>wiki文档</div>
            <div class="panel-body">
                <div class="col-sm-3 title-list">
                    目录
                </div>
                <div class="col-sm-9 content">
                    <div style="text-align: center;margin-top: 50px">
                        <h4>《{{ request.tracer.project.name }}》 wiki文档库</h4>
                        <a href="#">
                            <i class="fa fa-plus-circle"></i> 新建文章
                        </a>
                    </div>
                </div>
            </div>
        </div>

    </div>


{% endblock %}
```

修改下拉框的同步状态

templatetags/prject.py

传入request

```python
@register.inclusion_tag('web/inclusion/all_project_list.html')
def all_project_list(request):
    # 1.获取我创建的项目
    my_project_list = models.Project.objects.filter(creator=request.tracer.user)

    # 2.获取我参与的项目
    join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)

    return {'my': my_project_list,'join':join_project_list,'request':request}
```

all_project_list.html

加入判断

```html
<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
       aria-expanded="false">项目 {% if request.tracer.project %} ({{ request.tracer.project.name }}) {% endif %} <span class="caret"></span></a>
    
```

#### 2.2.添加文章

新增url

```python
        url(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),

```

完善wiki.html

```html
{% extends 'web/layout/manage.html' %}
{% block css %}
    <style>
        .panel-default {
            margin-top: 10px;
        }

        .panel-body {
            padding: 0;
        }

        .title-list {
            border-right: 1px solid #dddddd;
            min-height: 500px;
        }

        .content {
            border-left: 1px solid #dddddd;
            min-height: 600px;
            margin-left: -1px;
        }

        .panel-default .panel-heading {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }
    </style>
{% endblock %}
{% block content %}
    <div class="container-fluid">
        <div class="panel panel-default">
            <div class="panel-heading">
                <div>
                    <i class="fa fa-book" aria-hidden="true"></i> wiki文档
                </div>
                <div class="function">
                    <a href="{% url 'web:wiki_add' project_id=request.tracer.project.id %}" type="button"
                       class="btn btn-success btn-xs">
                        <i class="fa fa-plus-circle" aria-hidden="true"></i> 新建
                    </a>
                </div>
            </div>
            <div class="panel-body">
                <div class="col-sm-3 title-list">
                    目录

                </div>
                <div class="col-sm-9 content">
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                            <div class="form-group">
                                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                                {{ field }}
                                <span class="error-msg">{{ field.errors.0 }}</span>
                            </div>
                        {% endfor %}

                        <button type="submit" class="btn btn-primary">提 交</button>
                    </form>
                </div>
            </div>
        </div>

    </div>


{% endblock %}
```

新增forms/wiki.py

```python
from django import forms
from web.forms.bootstrap import BootstrapForm
from web import models

class WikiModelForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = models.Wiki
        exclude = ['project',]
```



完善wiki_add视图

```python
def wiki_add(request,project_id):
    '''添加文章'''
    if request.method == 'GET':
        form = WikiModelForm()
        return render(request,'web/wiki_add.html',{'form':form})
    form = WikiModelForm(request.POST)
    if form.is_valid():
        form.instance.prject = request.tracer.project
        form.save()
        url = reverse('wiki',kwargs={'prject_id':project_id})
        return redirect(url)
    return render(request, 'web/wiki_add.html', {'form': form})
```

优化models.py，新增`__str__`

```python
class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目',to='Project',null=True,blank=True)
    title = models.CharField(verbose_name='标题',max_length=32)
    content = models.TextField(verbose_name='内容')

    # 自关联
    parent = models.ForeignKey(verbose_name='父文章',to='Wiki',null=True,blank=True,related_name='children')

    def __str__(self):
        return self.title
```

修复bug：其他项目里的文章，也能作为父级出现

forms/wiki.py

```python
class WikiModelForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = models.Wiki
        exclude = ['project',]
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        total_data_list = [("","请选择"),]
        data_list = models.Wiki.objects.filter(project=request.tracer.project).values_list('id','title')
        total_data_list.extend(data_list)

        self.fields['parent'].choices = total_data_list
```

**层级关系**

通过ajax来请求数据，js操作css选择器来生成数据

wiki.html

```javascript
{% block js %}
    <script>
        $(function () {
            initCatalog()
        })

        function initCatalog() {
            $.ajax({
                url: "{% url 'web:wiki_catalog' project_id=request.tracer.project.id %}",
                type: "GET",
                dataType: "JSON",
                success: function (res) {
                    console.log(res)
                    if (res.status) {
                        $.each(res.data, function (index, item) {
                            var li = $("<li>").attr("id", "id_" + item.id).append($("<a>").text(item.title)).append($("<ul>"))

                            // 接收到后端传递的字典格式的数据
                            if (!item.parent_id) {
                                $("#catalog").append(li)
                            } else {
                                $("#id_" + item.parent_id).children("ul").append(li)
                            }

                        })
                    } else {
                        alert('初始化目录失败')
                    }
                }
            })
        }
    </script>
```

多级目录展示部分存在问题

父目录要提前出线：排序 + 字段（深度depth）

| ID   | 标题 | 内容 | 项目ID | 父ID | 深度 |
| ---- | ---- | ---- | ------ | ---- | ---- |
| 1    |      |      |        | null | 1    |
| 2    |      |      |        | 1    | 2    |

models.py

```python
class Wiki(models.Model):
    project = models.ForeignKey(verbose_name='项目',to='Project')
    title = models.CharField(verbose_name='标题',max_length=32)
    content = models.TextField(verbose_name='内容')
    depth = models.IntegerField(verbose_name='深度',default=1)
    # 自关联
    parent = models.ForeignKey(verbose_name='父文章',to='Wiki',null=True,blank=True,related_name='children')

    def __str__(self):
        return self.title
```

form中也要排除depth字段的渲染

```python
    class Meta:
        model = models.Wiki
        exclude = ['project','depth',]
```

views/wiki.py

```python
def wiki_add(request,project_id):
    '''添加文章'''
    if request.method == 'GET':
        form = WikiModelForm(request)
        return render(request,'web/wiki_add.html',{'form':form})
    form = WikiModelForm(request,data=request.POST)
    if form.is_valid():
        # 判断用户是否选择了父文章
        if form.instance.parent:
            form.instance.depth = form.instance.parent.depth + 1
        else:
            form.instance.depth = 1
        form.instance.project = request.tracer.project
        form.save()
        url = reverse('web:wiki',kwargs={'project_id':project_id})
        return redirect(url)
    return render(request, 'web/wiki_add.html', {'form': form})

def wiki_catalog(request,project_id):
    '''wiki目录'''
    # data = models.Wiki.objects.filter(project=request.tracer.project).values_list("id","title","parent_id")
    # return JsonResponse({'status':True,'data':list(data)})
    # vlaues_list输出的是元组格式，而values返回的是字典
    data = models.Wiki.objects.filter(project=request.tracer.project).values("id","title","parent_id").order('depth','id')
    # data = models.Wiki.objects.filter(project=request.tracer.project).values("id","title","parent_id")

    return JsonResponse({'status':True,'data':list(data)})
```



#### 2.3.预览文章



#### 2.4.修改文章



#### 2.5.删除文章









