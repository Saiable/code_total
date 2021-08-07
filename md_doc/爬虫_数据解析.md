[TOC]

[菜鸟教程](https://www.runoob.com/xpath/xpath-intro.html)

### 跳过某个序号的标签进行匹配

![](https://img-blog.csdnimg.cn/20200705223831654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1J5YW5fbGVlOTQxMA==,size_16,color_FFFFFF,t_70)

比如这里想跳过第一个`<tr>`标签，可以用到position>1。

```python
XXX.xpath("//tr[position()>1]/td[1]/input/@value").extract()
```

### XPath查找没有id或类的元素

https://qa.1r1g.com/sf/ask/168289131/

很简单:

```
//tr[not(@id) and not(@class)]
```

这会给你所有`tr`缺乏这两种元素`id`和`class`属性.如果您希望所有`tr`元素都缺少其中一个,请使用`or`而不是`and`:

```
//tr[not(@id) or not(@class)]
```

当以这种方式使用属性和元素时,如果属性或元素具有值,则将其视为是真的.如果它丢失则将其视为错误.

