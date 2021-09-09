[TOC]

### 模板的创建

- 在每个app下创建templates文件夹
- 再创建同app名的文件夹
- 再创建模板，自定义名称，格式为`html`
- 路径例子：`templates/web/register.html`

### 模板语法

**注意尖括号和百分号之间不能有空格**，组成部分如下：

```html
{% extends 'web/layout/basic.html' %}

{% load static %}

{% block title %}用户注册{% endblock %}

{% block css %}
    <link rel="stylesheet" href="{% static 'css/account.css' %}">
{% endblock %}

{% block content %}

{% endblock %}

{% block js %}

{% endblock %}
```

### 调用模板

```python
def register(request):
    return render(request,'web/register.html')
```

注意render的路径，前面没有斜杠。

