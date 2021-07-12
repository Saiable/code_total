[TOC]

# Centos7下Apache安装Brat标注工具

# 一、Brat简介

BRAT是一个基于web的文本标注工具，主要用于对文本的结构化标注，用BRAT生成的标注结果能够把无结构化的原始文本结构化，供计算机处理。利用该工具可以标注实体，事件、关系、属性等，只支持在linux下安装，其使用需要webserver，官方给出的教程使用的是Apache2。

*so,安装Brat之前需要先安装Apache。
如果你使用的windows系统，那么在这之前你需要先安装一个linux系统的虚拟机，我安装的虚拟机是Centos7系统的。*

# 二、 配置Apache

## 1.安装Apache

Centos7下Apache的安装包叫httpd，执行以下命令进行安装：

```bash
yum install httpd -y
```

## 2.修改主配置文件httpd.conf

```bash
vim /etc/httpd/conf/httpd.conf
```

添加如下内容：

```xml
<Directory /var/www/html/brat>
    AllowOverride Options Indexes FileInfo Limit
    Require all granted
    AddType application/xhtml+xml .xhtml
    AddType font/ttf .ttf
    # For CGI support
    AddHandler cgi-script .cgi
    # Comment out the line above and uncomment the line below for FastCGI
    AddHandler fastcgi-script fcgi
</Directory>
```

*/var/www/html/brat路径是与后面要安装brat的路径对应！*

## 3.配置userdir模块

使用以下命令：

```bash
vim /etc/httpd/conf.d/userdir.conf
```

找到文件中代码：

```xml
<IfModule mod_userdir.c>
    #
    # UserDir is disabled by default since it can confirm the presence
    # of a username on the system (depending on home directory
    # permissions).
    #
    UserDir disabled

    #
    # To enable requests to /~user/ to serve the user's public_html
    # directory, remove the "UserDir disabled" line above, and uncomment
    # the following line instead:
    #
    #UserDir public_html
</IfModule>
```

修改为：

```xml
<IfModule mod_userdir.c>
    #
    # UserDir is disabled by default since it can confirm the presence
    # of a username on the system (depending on home directory
    # permissions).
    #
    #UserDir disabled

    #
    # To enable requests to /~user/ to serve the user's public_html
    # directory, remove the "UserDir disabled" line above, and uncomment
    # the following line instead:
    #
    #UserDir public_html
    UserDir brat
</IfModule>
```

## 4.开启Apache服务

```bash
systemctl start httpd
```

### a.设置开机自启Apache服务

```bash
systemctl enable httpd
```

### b.顺便记录一下Apache命令大全

*后面每次更改配置文件后，都需要重启apache服务*

```bash
#重新启动Apache
systemctl restart httpd
#停止Apache
systemctl stop httpd
#查看Apache状态
systemctl status httpd
#设置开机不启动Apache
systemctl disable httpd
```

## 5.测试Apache

Apache的存放路径：/var/www/html
进入apache网页的存放路径，进行网页测试:

```bash
cd var/www/html
```

新建一个测试网页：

```bash
vim index.html
```

在文件中添加以下内容：

```html
<html>
<body>
<p>Hello World</p>
</body>
</html>
```

保存后退出，在浏览器能看到`Hello World`界面，表示Apache配置成功！

# 三、安装Brat

## 1.下载Brat

安装v1.3p1版本，下载地址：
https://github.com/nlplab/brat/archive/v1.3_Crunchy_Frog.tar.gz
别用wget直接下载，wget下载下来的压缩包不完整，有错误。老老实实下载下来，传到linux系统中吧。
下载的压缩文件放在Apache文件夹中：/var/www/html/

## 2.解压文件

```bash
tar -xzvf v1.3_Crunchy_Frog.tar.gz
```

## 3.文件夹重命名

重命名一个文件夹，上面配置Apache的时候已经配置到了brat文件夹下了，所以改名为brat：

```bash
mv brat-1.3_Crunchy_Frog brat
```

## 4.对brat目录授权

```bash
sudo chmod 777 -R /var/www/html/brat
```

## 5.安装Brat

### a.进入brat

```bash
cd brat
```

## b.执行命令进行brat安装

中途需要根据提示输入用户名、密码、管理员邮箱

```bash
sh install.sh
```

出现以下提示，即安装成功：

```clike
Assigning owner of the following directories to apache (apache):
    "/var/www/html/brat/work/"
and
    "/var/www/html/brat/data/"
(this requires sudo; please enter your password if prompted)
The installation has finished, you are almost done.

1.) If you are installing brat on a webserver, make sure you have
    followed the steps described in the brat manual to enable CGI:

    http://brat.nlplab.org/installation.html

2.) Please verify that brat is running by accessing your installation
    using a web browser.

You can automatically diagnose some common installation issues using:

    tools/troubleshooting.sh URL_TO_BRAT_INSTALLATION

If there are issues not detected by the above script, please contact the
brat developers and/or file a bug to the brat bug tracker:

    https://github.com/nlplab/brat/issues

3.) Once brat is running, put your data in the data directory. Or use
    the example data placed there by the installation:

    /var/www/html/brat/data

4.) You can find configuration files to place in your data directory in
    the configurations directory, see the manual for further details:

    /var/www/html/brat/configurations

5.) Then, you (and your team?) are ready to start annotating!
```

## 6. 安装完成后，更改data和work目录的用户组和权限

```bash
chgrp -R apache data work
chmod -R g+rwx data work
```

至此，就可以在浏览器进行测试一下了，默认的url是IP/brat/,example:127.0.0.1/brat/。

## 7.添加用户

实现标注时，可以多个用户登录进行标注。
编辑文档：

```bash
vim /var/www/html/brat/config.py 
```

修改对应的行，增加用户名和密码：

```python
USER_PASSWORD = {
'admn': 'admin',
'test': 'test',
# (add USERNAME:PASSWORD pairs below this line.)
}
```

## 8.设置支持中文

编辑配置文件：

```bash
vim /var/www/html/brat/server/src/projectconfig.py
```

找到n = re.sub(r’[^a-zA-Z0-9_-]’, ‘*’, n)这一行，大概在162行，修改为：
re.sub(u’[^a-zA-Z\u4e00-\u9fa5<>,0-9*-]’, ‘_’, n)
如下:

```python
def normalize_to_storage_form(t):
    """
    Given a label, returns a form of the term that can be used for
    disk storage. For example, space can be replaced with underscores
    to allow use with space-separated formats.
    """
    if t not in normalize_to_storage_form.__cache:
        # conservative implementation: replace any space with
        # underscore, replace unicode accented characters with
        # non-accented equivalents, remove others, and finally replace
        # all characters not in [a-zA-Z0-9_-] with underscores.
 
        import re
        import unicodedata
 
        n = t.replace(" ", "_")
        if isinstance(n, unicode):
            ascii = unicodedata.normalize('NFKD', n).encode('ascii', 'ignore')
        #n  = re.sub(r'[^a-zA-Z0-9_-]', '_', n)
        n  = re.sub(u'[^a-zA-Z\u4e00-\u9fa5<>,0-9_-]', '_', n)
 
        normalize_to_storage_form.__cache[t] = n
 
    return normalize_to_storage_form.__cache[t]
normalize_to_storage_form.__cache = {}
```

注意，修改的时候加`tab`键，不要敲空格

用下面的正则规则：`n = re.sub(u'[^a-zA-Z\u4e00-\u9fa5< >\u2014-\uff1b< >\x00-\xff< >,0-9_-]', '_', n)`

## 9.标注示例

现在就可以真正的使用Brat进行标注了。

### a.新建项目文件夹并进入此文件夹

首先进入brat文件夹的data目录中新建project文件夹：

```bash
cd /var/www/html/brat/data
mkdir project
cd project
```

### b.设置项目目录权限

```bash
sudo chmod 777 -R /var/www/html/brat/data/project/
```

### c.新建文件

新建一个配置文件annotation.conf

```bash
vim annotation.conf
```

在文件中插入以下内容：

```clike
[entities]
# Definition of entities.
#Format is a simple list with one type per line.
时间
地点
人名
组织名
公司名
产品名
[attributes]
Category Arg:Disease, Value:SpecificDisease|Modifier|DiseaseClass|CompositeMention
[relations]
[events]
```

再新建一个配置文件visual.conf，以配置不同的类别用不同的颜色显示。

```bash
vim visual.conf
```

在文件中插入以下内容：

```clike
[labels]
时间 | 时间
地点 | 地点
人名 | 人名
组织名 | 组织名
公司名 | 公司名
产品名 | 产品名
[drawing]
时间 bgColor:yellow
地点 bgColor:blue, fgColor:white
人名 bgColor:deepskyblue
组织名 bgColor:green, fgColor:white
公司名 bgColor:purple, fgColor:white
产品名 bgColor:pink
Category glyph:[spec]|[mod]|[cls]|[comp]
```

新建一个配置文件visual.conf，以配置不同的类别用不同的颜色显示。

接下来，新建一个待标注的文本文件example.txt:

```bash
vim example.txt
```

在文件中放入你想标注的文字，标注文本建议控制在500字符内：

```clike
今年海钓比赛在厦门市与金门之间的海域举行。
```

新建一个标注的空文件example.ann，对example.txt标注的结果存储在example.ann中。

```bash
vim example.ann
```

### d.开始标注

在浏览器输入：http://127.0.0.1/brat/
首先登录，例如登录我们添加的test用户

打开example.ann可以看到文件中新增了标注的内容：

```clike
T1      地点 7 10       厦门市
T2      地点 11 13      金门
```

到此就标注完成了。
若要进行NER命名实体识别等模型训练时，再写个程序把ann文件转化为BIO标注的文件即可。

