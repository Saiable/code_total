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

### 模板中生成字段

- for

  ```
  {% for field in form %}
  
  {% endfor %}
  ```

- if

  ```html
  {% if field.name == 'code' %}
  
  {% else %}
  
  {% endif %}
  ```

- form表单中，{% csrf_token %}的作用

  - 前端会生成如下标签

    ```html
    <input type='hidden' name='csrfmiddlewaretoken' value='vuvuGklRunDBMJTlpeOlg3qjG8x2nMzotE647gzi0r0tNcvkATzQSFgi0E0hw3n0' />
                
    ```

  - 作用

    ```html
    <form>
    
    {% csrf_token %}
    
    </form>
    
    在django中我们需要在templates的form中加入{%csrf_token%}这串内容，
    
    它的作用是当我们get表单页面时，服务器返回页面的同时也会向前端返回一串随机字符，post提交时服务器会验证这串字符来确保用户是在服务端返回的表单页面中提交的数据，
    
    防止有人通过例如jquery脚本向某个url不断提交数据，是一种数据提交的验证机制。
    ```

    


### 模板中调用form字段

- field.name

  - 定义form字段的变量名
  - 可以在模板文件中，进行条件判断，来决定展示不同的页面内容，类似v-if

- field.label

  - 在models，或modelModel中，定义字段时，写的label的值

  - 如下，field.label的值就是`用户名`

    ```python
    username=  models.CharField(lable='用户名',max_length=32)
    ```

- field.id_for_label

  ```html
  <label for="{{ field.id_for_label }}">{{ field.label }}</label>
  ```

  - 生成的是

    ```html
    <label for="id_username">用户名</label>
    ```

  - 会生成以id开头，加下变量名的属性值。

