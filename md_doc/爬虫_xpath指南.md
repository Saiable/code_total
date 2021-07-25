[TOC]

[菜鸟教程](https://www.runoob.com/xpath/xpath-intro.html)

### 跳过某个序号的标签进行匹配

![](https://img-blog.csdnimg.cn/20200705223831654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1J5YW5fbGVlOTQxMA==,size_16,color_FFFFFF,t_70)

比如这里想跳过第一个`<tr>`标签，可以用到position>1。

```python
XXX.xpath("//tr[position()>1]/td[1]/input/@value").extract()
```

