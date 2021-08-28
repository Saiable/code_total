[TOC]

### `if __name__ == '__main__'`

python解释器在执行一些代码时，有一些内建、隐含的变量，`__name__`就是其中之一，其意义是`模块名称`。

如果该模块是被引用，那么`__name__`的值会是此模块的名称。

如果该模块是直接被执行，那么`__name__`的值是`__main__`。

`__name__`在模块被直接执行时与被引用时是不同的。



问：当一个模块被引用时，如何不执行该模块的语句？

答：依靠判断`__name__`是否等于`__main__`。当一个模块被直接执行时，其`__name__`必然等于`__main__`；当一个模块被引用时，其`__name__必然等于文件名`

### `__all__`

#### 1.提供了哪些是公开接口的约定

python可以在模块级别暴露接口

不像Ruby或者Java，python没有语言原生的可见性控制，而是靠一套需要大家自觉遵守的“约定”下工作。

比如下划线开头的，应该对外部不可见。

同样，`__all__`也是对于模块公开接口的一种约定，比起下划线，`__all__`提供了暴露接口用的“白名单”。

一些不以下划线开头的变量（比如从其他地方`import`到当前模块的成员）可以同样被排除出去。

```python
import os,sys

__all__ = ["my_func"] # 排除了os和sys


def my_func():
    pass
```

#### 2.控制`from xx import *`的行为

代码中当然是不提倡用`from xx import *`的写法的。

如果一个模块`spam`没有定义`__all__`，执行`from spam import *`的时候，会将`spam`中非下划线开头的成员，都导入到当前命名空间中。

这样就有可能弄脏当前名称空间，如果显示声明了`__all__`，`import *`就只会导入`__all__`列出的成员。

如果`__all__`定义有误，列出的成员不存在，还会明确的抛出异常，而不是默默忽略。

#### 3.为lint工具提供辅助

编写一个库的时候，经常会在`__init__.py`中暴露整个包的API，而这些API的实现可能是在包中的其他模块中定义的。如果我们仅仅这样写：

```python
from foobar import Spam, Egg
```

一些代码检查工具，如`pyflakes`就会报错，认为`Spam`和`Egg`是`import`了又没被使用的变量。当然一个可行的方法是把这个警告压掉：

```python
from foobar import Spam, Egg # noqa
```

但是更好的方法是显示定义`__all__`，这样代码检查工具会理解这层意思，就不再报`unused variables`的警告：

```python
from foobar import Spam, Egg

__all__ = [
    "Spam",
    "Egg",
]
```

需要注意的是大部分情况下，`__all__`都是一个`list`，而不是`tuple`或者其他序列类型。如果写了其他类型的`__all__`，如无例外`pyflaskes`等lint工具会无法识别出。

#### 4.定义`__all__`需要注意的地方

- `__all__`应该是list。

- 不应该动态生成`__all__`，比如使用列表解析式。`__all__`的作用就是定义公开接口，如果不以字面量的形式写出来，就失去意义了。

- 即使有了`__all__`也不应该在非临时代码中使用`from xx import *`语法，或者用元编程手段模拟`Ruby`的自动`import`

  - python不像Ruby，没有`Module`这种成员，模块就是命名空间隔离的执行者。如果打破了这一层，而且引入诸多动态因素，生产环境跑的代码就充满了不确定性，调试也会非常困难。

- 按照PEP8建议的风格，`__all__`应该写在所有`import`语句下面，和函数、常量等模块成员定义的上面。

- 如果一个模块需要暴露的接口改动频繁，`__all__`可以这样定义：

  ```python
  __all__ = [
      "foo",
      "bar",
      "egg",
  ]
  ```

- 最后多出来的逗号在python中是允许的，也是符合PEP8风格的。这样修改一个接口的暴露，就只修改一行，方便版本控制的时候看`diff`。

### `__init__.py`

#### 1.标识该目录是一个Python的模块包（module package）

如果使用python相关IDE来进行开发，那么目录中存在该文件，该目录就会被识别是`module package`

#### 2.简化模块导入操作

##### 2.1.`__init__.py是如何工作的`

如果目录中包含了`__init__.py`时，当用`import`导入该目录时，会执行`__init__.py`里面的代码。

##### 2.2.控制模块导入

在执行import的时候，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。



综上，我们可以在`__init__.py`指定默认需要导入的模块

##### 2.3.偷懒的导包方式

要用`__all__`来约束`from mypackage import *`的导包行为

`__all__`关联了一个模块列表，当执行`from mypackage import *`时，就会导入列表中的模块。

#### 3.配置模块的初始化操作

该文件就是一个正常的python代码文件，可以将初始化代码放在该文件中。

### 闭包

定义：函数定义和函数表达式位于另一个函数的函数体内（嵌套函数）。

意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得该函数无论在何处调用，优先使用自己外层包裹的作用域。

使用场景：装饰器

### 软件开发原则

#### 开放-封闭原则

- 封闭：已实现的功能代码不应该被修改
- 开放：对现有功能的扩展开放

不能再原有代码里新增，不能更改原有代码调用方式，

更改函数名指向但不能直接调用原函数 ===>嵌套函数



### `*args、**kwargs`

*args用发送一个非键值对的可变数量的参数列表，给一个函数

```python
def test(f_arg,*argv):
    print('first normal arg:',f_arg)
    for arg in argv:
        print('another arg through *argv:',arg)

test('aaa','bbb','cccc','dddd')

# first normal arg: aaa
# another arg through *argv: bbb
# another arg through *argv: cccc
# another arg through *argv: dddd
```

**kwargs允许将不定长度的键值对，作为参数传递给一个参数。

如果想要在一个函数里处理带名字的参数，应该使用**kwargs。

```python
def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0}--{1}--".format(key,value))

greet_me(name='aaa')
```