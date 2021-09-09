[TOC]



### 静态资源文件夹创建

同模板文件夹创建方式：

- 在每个app下创建static文件夹

- 再创建同app名的文件夹

- 再放入需要的css、js等文件（夹）

- 路径例子：`static/web/css/account.css`

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/b6480094aed444cdbb398db583c0e258.png)

### 模板中，静态资源的导入

html文件开始加上`{% load static %}`

引入方式如下：

`<link rel="stylesheet" href="{% static 'web/css/account.css' %}">`

注意路径前一开始不需要加斜杠
