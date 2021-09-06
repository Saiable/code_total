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
      from .local_settings import *
  except ImportError as errr:
      print('import error',err)
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

#### 1.local_settings的作用？

```
本地配置信息- 开发- 测试- 运维
```

#### 2.gitignore的作用？

```
git软件，本地进行版本管理的时候，需要忽略的文件	
git init    
git add .    
git commit -m up
码云/github/gitlab	
代码托管
```

#### 3.虚拟环境的作用？

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
  # 短信的配置# 腾讯云短信应用的app_idTENCENT_SMS_APP_ID = 111111# 腾讯云短信的app_keyTENCENT_SMS_APP_KEY = "111111"# 腾讯云短信的签名内容TENCENT_SMS_SIGN = "aaaaaa"# 配置短信模板TENCENT_SMS_TEMPLATE = {	'register' : 832736,	'login' : 840501,	'reset_password' : 1005457}try:	from .local_settings import *except ImportError:	pass
  ```

#### 1.2华为云短信



#### 1.3阿里云短信



### 2.ModelForm生成注册字段

#### 2.1.在model.py创建表

```python
from django.db import models# Create your models here.class UserInfo(models.Model):    username = models.CharField(verbose_name = "用户名", max_length = 32)    # EmailField在数据库中，存储的实际还是字符串，区别在于ModelForm在页面上做展示的时候    email = models.EmailField(verbose_name = "邮箱", max_length = 32)    mobile_phone = models.CharField(verbose_name = "手机号", max_length = 32)    password = models.CharField(verbose_name = "密码", max_length = 32)
```

#### 2.2.settings.py中挂载app01

```python
INSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    # 挂载app01	'app01.apps.App01Config',]
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
# 创建注册功能的路由url(r'^app01/register/', views.register)
```

- saas/app01/views.py中新增

```python
# 引入ModelForm模块from django import formsfrom app01 import models# 自定义注册model类class RegisterModeForm(forms.ModelForm):	class Meta:		model = models.UserInfo		fields = '__all__'# 注册功能对应的视图函数def register(request):	# 生成model字段	form = RegisterModeForm()	# 根据模板，渲染注册功能的model字段	return render(request, 'register.html', {'form':form})
```

#### 2.5.创建模板

- 在app01中创建templates目录（注意不要拼写错误，不能少了s），并创建register.html
- django默认会先从根目录中找模板，然后会根据settings中的app的注册顺序来找

saas/app01/templates/register.html

```html
<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title>注册</title>	</head>	<body>		<h1>注册</h1>		<!-- 对form字段进行循环，然后展示，类似于vue中的v-for -->		{% for field in form%}			<!-- ModelForm的字段有哪些属性？ -->			<!-- .label获取的实际上就是verbose_name -->			<p>{{field.label}} : {{ field }}</p>		{% endfor %}			</body></html
```

#### 2.6.结果

- 执行`python manage.py runserver 8080`，在浏览器中访问`127.0.0.1:8080/app01/register`，效果如下：

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623192323464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### 2.7.ModelForm自定义字段

- 可以在views视图函数中，在自定义的ModelForm类中，重写model中生成的字段，如下，可以利用正则重写手机号规则(Django中不提供手机号的格式校验)

  vies.py

  ```python
  # 导入django中正则的模块from django.core.validators import RegexValidatorfrom django.core.exceptions import ValidationErrorclass RegisterModeForm(forms.ModelForm):	# 变量名要和model中的保持一致	# validator中，可以放一个或多个正则表达式	# RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息	mobile_phone = forms.CharField(label = '手机号', validators = [RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])	class Meta:		model = models.UserInfo		fields = "__all__"
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
  # 验证码# 如果不加widget，默认生成的是input标签code = forms.CharField(label = '验证码')
  ```

#### 2.8.基于bootstrap美化页面

这是使用v3版本，[bootstrap-v3版本下载](https://v3.bootcss.com/getting-started/#download)

也可以直接使用官网提供的cdn，引入方式如下：

```html
<!-- 最新版本的 Bootstrap 核心 CSS 文件 --><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous"><!-- 可选的 Bootstrap 主题文件（一般不用引入） --><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous"><!-- 最新的 Bootstrap 核心 JavaScript 文件 --><script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
```

也可以下载，然后在django本地引入，具体原理查看，[django项目如何引入css文件](https://www.py.cn/kuangjia/django/11612.html)、具体配置见[Django使用本地css/js文件](https://www.cnblogs.com/lizm166/p/9414156.html)

settings.py中的测试代码

```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)# 这里打印的就是项目文件所在的绝对路径BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# print(BASE_DIR) F:\workspace\py_virtualenv\myproject\Scripts\saas# 基于BASE_DIR构建static路径STATIC_ROOT= os.path.join(BASE_DIR,'static')# print(STATIC_ROOT) F:\workspace\py_virtualenv\myproject\Scripts\saas\static# 追加css文件路径STATICFILES_DIRS=[os.path.join(STATIC_ROOT,'css'),]# print(STATICFILES_DIRS) ['F:\\workspace\\py_virtualenv\\myproject\\Scripts\\saas\\static\\css']
```

- 实际配置

  - 根目录下新建`static`，在里面再新建`static`文件夹，放入下载的css文件

  - settinsg.py中，在`STATIC_URL`下面，配置

    ```python
    STATICFILES_DIRS = [    os.path.join(BASE_DIR, 'static/'),]
    ```

    然后再register.html末班中，使用相对路径访问

    ```html
    <link rel="stylesheet" href="../../static/css/bootstrap.min.css">
    ```

  - 启动server，访问`http://127.0.0.1:8080/static/css/bootstrap.min.css`，可以访问到css文件了。

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623221301445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

  - 前台表单样式调用成功

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210624061226608.png)- 

- 完善register.html中的登录界面代码

  ```html
  		<div class="account">			<h1>注册</h1>			<form>				{% for field in form%}				<div class="form-group">					<label for="{{field.id_for_label}}">{{field.label}}</label>					<!-- <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email"> -->					{{ field }}				</div>				{% endfor %}				<button type="submit" class="btn btn-default">注册</button>			</form>		</div>
  ```

  此时`field`的字段是没有`form-control`的类名的，要借助ModelForm中的`attrs`，重写字段时，给每个字段加上类名

  ```python
  confirm_password = forms.CharField(label = '重复密码', widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : '请重复输入密码'}))
  ```

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210624063221205.png)

  重写`RegisterModelForm`的初始化方法，批量给字段添加`form-control`类属性以及`placeholder`属性

  ```python
  def __init__(self, *args,**kwargs):    super().__init__(*args, **kwargs)    for name, field in self.fields.items():        field.widget.attrs['class'] = 'form-control'        field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
  ```

  自定义字段顺序

  ```python
  # fields = "__all__"fields = ['username','email','password','confirm_password','mobile_phone','code']
  ```

  完善register模板样式

  ```html
  <div class="account">	<h1 style="text-align: center;">注册</h1>	<form>		{% for field in form%}			{%if field.name == 'code'%}				<div class="form-group">					<label for="{{field.id_for_label}}">{{field.label}}</label>					<div class="clearfix">						<div class="col-md-6" style="padding-left: 0;">{{ field }}</div>						<div class="col-md-6">							<button type="button" class="btn btn-default" value="点击获取验证码">点击获取验证码</button>						</div>					</div>				</div>			{%else%}				<div class="form-group">					<label for="{{field.id_for_label}}">{{field.label}}</label>					{{ field }}				</div>			{%endif%}		{% endfor %}		<button type="submit" class="btn btn-primary">注册</button>	</form></div>
  ```

### 3.注册实现思路

- 点击获取验证
  - 获取手机号
  - 向后台发送ajax
  - 向手机发送验证码
  - 验证码失效处理

#### 3.1.windows安装redis

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
      import redisconn = redis.Redis(host='127.0.0.1',port='6379',password='foobared',encoding='utf-8')# 设置k1的值为v1，过期时间为10秒conn.set('k1','v1',ex=10)value = conn.get('k1')print(value)
      ```

    - 上面的python操作redis示例，是以直接创建连接的方式实现，每次操作redis如果重新连接一次，效率会比较低，建议使用redis连接池来替换【推荐】，例如：

      ```python
      import redis#创建redis连接池（默认连接池最大连接数 2**31=2147483648）pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='foobared',encoding='utf-8',max_connections=1000)#去连接池中获取一个连接conn = redis.Redis(connection_pool = pool)#设置键值，且超时时间为10秒（写入redis时，会自动转换为字符串）conn.set('k1','v1',ex=10)#根据键获取值，如果值存在，获取到的是字符串类型；不存在则返回Nonevalue = conn.get('k1')print(value)
      ```

      ```python
      # 在django中使用import redisfrom django.shortcuts import HttpResponse#创建redis连接池（默认连接池最大连接数 2**31=2147483648）pool = redis.ConnectionPool(host='127.0.0.1',port=6379,password='foobared',encoding='utf-8',max_connections=1000)def index(request):    #去连接池中获取一个连接    conn = redis.Redis(connection_pool = pool)    #设置键值，且超时时间为10秒（写入redis时，会自动转换为字符串）    conn.set('k1','v1',ex=10)    #根据键获取值，如果值存在，获取到的是字符串类型；不存在则返回None    value = conn.get('k1')    print(value)        return HttpResponse('ok')
      ```

      这种方式可以实现在django中操作redis，但是，这种形式有点非主流，一般不这么干，而是采用一种更简洁的方式。

    - django连接redis，django-redis

      - 在django中`方便的`使用redis

        ```python
        不方便：redis模块+连接池方便：django-redis
        ```

      - 安装`django-redis`

        ```python
        pip install django-redis
        ```

      - local_settings.py配置：

        ```python
        # django-redis的配置CACHES = {	"default": {		"BACKEND": "django_redis.cache.RedisCache",		"LOCATION": "redis://127.0.0.1:6379", # 安装redis的主机的IP和端口		"OPTIONS": {			"CLIENT_CLASS": "django_redis.client.DefaultClient",			"CONNECTION_POOL_KWARGS": {				"max_connections": 1000,				"encoding": "utf-8"			},			"PASSWORD": "foorbared" # redis密码，放在local_settings.py中		}	},}
        ```

        ```python
        # 链接到数据库from django.shortcuts import HttpResponsefrom django_redis import get_redis_connectiondef index(request):    #去连接池中获取一个连接    conn = get_redis_connection("defalut") # 默认读取defalut的配置，也可以读取其他的，比如master的配置，在settings.py中配置好即可    # 后期读写分离的时候可以用到        conn.set('k1','v1',ex=10)    value = conn.get('k1')    print(value)        return HttpResponse('ok')
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

- 在`settinsg.py`最后一行中注册

  ```python
  INSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',	'app01.apps.App01Config',	'web.apps.WebConfig',]
  ```

- 删除web/views.py，创建views文件夹，创建web/views/account.py文件

- 创建web/templates文件夹

  - 不同app的templates目录，一般还会创建和app名称相同的文件夹，然后再放模板文件，即web/templates/web/register.html
  - 模板和静态文件的查找顺序是，现在项目的根目录查找，然后按照app在配置文件中的配置顺序查找

- 创建母版目录web/templates/layout/basic.html

  basic.html

  ```html
  {% load static %}<!DOCTYPE html><html>	<head>		<meta charset="utf-8">		<title>{% block title%}{% endblock %}</title>		<link rel="stylesheet" href="{% static 'plugin/bootstrap-3.4.1-dist/css/bootstrap.min.css' %}">		<link rel="stylesheet" href="{% static 'plugin/fontawesome-free-5.11.2-web/css/fontawesome.min.css' %}">		<style>			.navbar-default{				border-radius: 0;			}		</style>		{% block css %}{% endblock %}	</head>	<body>				<nav class="navbar navbar-default">		  <div class="container">		    <!-- Brand and toggle get grouped for better mobile display -->		    <div class="navbar-header">		      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">		        <span class="sr-only">Toggle navigation</span>		        <span class="icon-bar"></span>		        <span class="icon-bar"></span>		        <span class="icon-bar"></span>		      </button>		      <a class="navbar-brand" href="#">Tracer</a>		    </div>				    <!-- Collect the nav links, forms, and other content for toggling -->		    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">		      <ul class="nav navbar-nav">		        <!-- <li class="active"><a href="#">产品功能 <span class="sr-only">(current)</span></a></li> -->		        <li><a href="#">产品功能</a></li>		        <li><a href="#">企业方案</a></li>		        <li><a href="#">帮助文档</a></li>		        <li><a href="#">价格</a></li>		      		      </ul>		      		      <ul class="nav navbar-nav navbar-right">		        <li><a href="#">Link</a></li>		        <li class="dropdown">		          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>		          <ul class="dropdown-menu">		            <li><a href="#">Action</a></li>		            <li><a href="#">Another action</a></li>		            <li><a href="#">Something else here</a></li>		            <li role="separator" class="divider"></li>		            <li><a href="#">Separated link</a></li>		          </ul>		        </li>		      </ul>		    </div><!-- /.navbar-collapse -->		  </div><!-- /.container-fluid -->		</nav>		{% block content %}{% endblock %}				<script src="{% static 'js/jquery-3.6.0.min.js'%}"></script>		<script src="{% static 'plugin/bootstrap-3.4.1-dist/js/bootstrap.min.js'%}"></script>		{% block js %}{% endblock %}	</body></html>
  ```

  

##### 1.1.2.路由分发

- 做路由匹配的时候，最前面不需要加`/`符号

- 总路由saas/urls.py

  ```python
  from django.conf.urls import url,includefrom django.contrib import adminurlpatterns = [    url(r'^admin/', admin.site.urls),    url(r'^app01/', include('app01.urls',namespace='app01')),    url(r'^', include('web.urls',namespace='web')),]
  ```

  app01/urls.py

  ```python
  from django.conf.urls import urlfrom django.contrib import adminfrom app01 import viewsurlpatterns = [    url(r'^send/sms/', views.send_sms),    url(r'^register/', views.register, name='register'),]
  ```

  web/urls.py

  ```python
  from django.conf.urls import url,includefrom web.views import accounturlpatterns = [    url(r'^register/', account.register, name='register'),]
  ```

##### 1.1.3.register.html

- account.css

  ```css
  .account {	width: 400px;	margin-top: 30px;	margin-left: auto;	margin-right: auto;	border: 1px solid #f0f0f0;	padding: 10px 30px 30px 30px;	-webkit-box-shadow: 5px 10px 10px rgba(0, 0, 0, .05);	box-shadow: 5px 10px 10px rgba(0, 0, 0, .05);}.account .title {	font-size: 25px;	font-weight: bold;	text-align: center;}.account .form-group {	margin-bottom: 20px;}
  ```

  register.html

  ```python
  {% extends 'layout/basic.html' %}{% load static %}{% block title %}用户注册{% endblock%}{% block css%}	<link rel="stylesheet" href="{% static 'css/account.css' %}">{% endblock %}{% block content %}    <div class="account">        <div class="title">用户注册</div>        <form id="regForm" method="POST" novalidate>            {% csrf_token %}            {% for field in form %}                {% if field.name == 'code' %}                    <div class="form-group">                        <label for="{{ field.id_for_label }}">{{ field.label }}</label>                        <div class="row">                            <div class="col-xs-7">                                {{ field }}                                <span class="error-msg"></span>                            </div>                            <div class="col-xs-5">                                <input id="btnSms" type="button" class="btn btn-default" value="点击获取验证码">                            </div>                        </div>                    </div>                {% else %}                    <div class="form-group">                        <label for="{{ field.id_for_label }}">{{ field.label }}</label>                        {{ field }}                        <span class="error-msg"></span>                    </div>                {% endif %}            {% endfor %}            <div class="row">                <div class="col-xs-3">                    <input id="btnSubmit" type="button" class="btn btn-primary" value="注  册"/>                </div>            </div>        </form>    </div>{% endblock %}{% block js %}{% endblock%}
  ```

- 新建web/forms文件夹，后面用到的Forms，都统一放在该目录

  该目录下，新建account.py

  ```python
  # 引入ModelForm模块from django import formsfrom app01 import modelsfrom django.core.validators import RegexValidatorfrom django.core.exceptions import ValidationError# 自定义注册model类class RegisterModeForm(forms.ModelForm):	# 变量名要和model中的保持一致	# validator中，可以放一个或多个正则表达式	# RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息	mobile_phone = forms.CharField(label = '手机号', validators = [RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])		#重写密码字段	password = forms.CharField(label = '密码', widget = forms.PasswordInput())		# 重复密码	confirm_password = forms.CharField(label = '重复密码', widget = forms.PasswordInput())		# 验证码	code = forms.CharField(label = '验证码')		class Meta:		model = models.UserInfo		# fields = "__all__"		fields = ['username','email','password','confirm_password','mobile_phone','code']	def __init__(self, *args,**kwargs):		super().__init__(*args, **kwargs)		for name, field in self.fields.items():			field.widget.attrs['class'] = 'form-control'			field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
  ```

  views/account.py

  ```python
  """用户账户相关的功能：注册、短信、登录、注销"""
  from django.shortcuts import render
  from web.forms.account import RegisterModeForm
  def register(request):	
      form = RegisterModeForm()	
      return render(request,'register.html',{'form': form})
  ```

- 把web的models.py按照app01的方式，重新生成一遍

  web/models.py

  ```python
  from django.db import models# Create your models here.
  class UserInfo(models.Model):	
      username = models.CharField(verbose_name = "用户名", max_length = 32)		# EmailField在数据库中，存储的实际还是字符串，区别在于ModelForm在页面上做展示的时候	
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

```js
{% block js %}    <script>        // 页面加载完成后执行        $(function() {            bindClickBtnSms()        })        // 绑定获取短信验证码的点击操作        function bindClickBtnSms() {            $('#btnSms').click(function () {                // 获取用户输入的手机号                // django 会对由forms生成的字段，加上id_+字段名的id属性                console.log($('#id_mobile_phone').val())            })        }    </script>{% endblock%}
```

##### 1.2.3.发送ajax

```javascript
//发送ajax请求$.ajax({	// 反向生成url，等价于send/sms	// 总路由分发时，加了namspace="web"，反向生成时，要加web:	url: "{% url 'web:send_sms' %}",	type: 'GET',	data: {mobilePhone:mobilePhone, tpl:'register'},	success: function(res) {		// ajax请求成功后，返回的值存储在res中		console.log(res)	}})
```

##### 1.2.4.手机号校验

- 不能为空
- 格式正确
- 没有注册过

form中如果要拿到视图函数中的request值，可以重写`__init__`方法

```python
def __init__(self, request, *args, **kwargs):    super().__init__(*args, **kwargs)    self.request = request
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
	mobile_phone = forms.CharField(label='手机号',validators=[RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])

	def __init__(self, request, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.request = request


	# 手机号校验的钩子函数
	def clean_mobile_phone(self):
		moblie_phone = self.cleaned_data('mobile_phone')

		# 判断短信模板是否有问题
		tpl = self.request.GET.get('tpl')
		template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
		if not template_id:
			raise ValidationError('模板错误')

		# 检查数据库中，是否有手机号
		# django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。
		exsits = models.UserInfo.objects.filter(moblie_phone=moblie_phone).exists()
		if exsits:
			raise ValidationError('手机号已存在')
		return moblie_phone

# 自定义注册model类
class RegisterModeForm(forms.ModelForm):
	# 变量名要和model中的保持一致
	# validator中，可以放一个或多个正则表达式
	# RegexValidator是一个对象，接收两个参数：1.正则表达式2.正则未通过时的报错信息
	mobile_phone = forms.CharField(label = '手机号', validators = [RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')])
	
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

##### 1.2.5.发送成功与失败处理

- 失败，显示错误信息
- 成功，显示倒计时

#### 1.3.点击注册







