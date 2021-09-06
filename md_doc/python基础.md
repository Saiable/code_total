[TOC]



### 迭代器

转载：https://www.cnblogs.com/chichung/p/9537969.html

理论性的东西有点枯燥，耐心点看～

1.迭代是什么？

我们知道可以对list,tuple,dict,str等数据类型使用for...in的循环语法，从其中依次取出数据，这个过程叫做遍历，也叫**迭代**。迭代是访问集合元素的一种常用的方式。

2.可迭代对象是什么？

简单来说，可以用for...in循环语句，从其中依次取出数据的对象，就是**可迭代对象**。例如，列表、元组、字典、字符串都是可迭代对象。整数、浮点数、布尔值都是不可迭代的。

3.迭代器是什么？

在可迭代对象进行迭代的时候，即用for...in...循环语法依次取出数据时，过程是怎样的呢？

我们发现，每迭代一次（即在for...in...中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个过程中就应该有一个“人”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。我们把这个能帮助我们进行数据迭代的“人”称为**迭代器(Iterator)**。举个栗子，老师安排一个班的同学每节课上课前进行演讲，按学号顺序进行，A同学这节课演讲，老师就会记住这节课是A同学演讲，那么下节课就是B同学进行演讲...依次类推，在这个例子里，老师就是一个迭代器。

4.怎样获取可迭代对象的迭代器？

我们可以通过**iter()**内置函数取得可迭代对象的迭代器。



```
list = [1,2,3,4,5]  # list是可迭代对象
lterator = iter(list)  # 通过iter()方法取得list的迭代器
print(lterator)

输出：
<list_iterator object at 0x7f35e6537a20>
```



迭代器是获取到了，那么应该怎样用呢？

**next()函数**是通过迭代器获取下一个位置的值。

**注意:** 当我们已经迭代完最后一个数据之后，再次调用next()函数会抛出StopIteration的异常，来告诉我们所有数据都已迭代完成，不用再执行next()函数了。



```
list = [1,2,3,4,5]  # list是可迭代对象
lterator = iter(list)  # 通过iter()方法取得list的迭代器
print(next(lterator))  # 1
print(next(lterator))  # 2
print(next(lterator))  # 3
print(next(lterator))  # 4
print(next(lterator))  # 5
print(next(lterator))

输出：
1
2
3
4
5
Traceback (most recent call last):
  File "/home/chichung/桌面/课堂练习/协程/iter方法取得可迭代对象的迭代器.py", line 8, in <module>
    print(next(lterator))
StopIteration
```



5.判断一个对象是否可迭代

isinstance(object,classinfo)内置函数可以判断一个对象是否是一个已知的类型，类似 type()。

- object -- 实例对象。
- classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。

在这之前，还需要知道collections模块里的Iterable。通俗点讲，凡是**可迭代对象都是这个类的实例对象**。下面来验证一下：



```
import collections

print(isinstance([1, 2, 3], collections.Iterable))
print(isinstance((1,2,3), collections.Iterable))
print(isinstance({"name":"chichung","age":23}, collections.Iterable))
print(isinstance("sex", collections.Iterable))
print(isinstance(123,collections.Iterable))
print(isinstance(True,collections.Iterable))
print(isinstance(1.23,collections.Iterable))

输出：
True
True
True
True
False
False
False
```



6.可迭代对象怎么可以获取迭代器呢？

看完第4点，有些人就感觉很奇怪，例如：[1,2,3]不就是一个列表，一个对象吗？怎么还能拿出一个迭代器来了？

首先，我们从第5点可以知道，**可迭代对象其实都是collections模块里的Iterable类创建出来的实例**的。你写一个列表，以为他不是任何类创建的，只是单纯一个列表？不是的，其实它就是Iterable类创建的实例对象。点进Iterable的类看一下，你会发现新大陆。



```
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):  # 注意点
        while False:
            yield None
```



原来由Iterable创建的对象，是有一个魔方方法**__iter__(self)**的。这个方法就是返回一个迭代器的。所以，由Iterable类创建的实例对象，是可以拿出一个迭代器的。

接下来要说的有点绕......

**之所以Iterable类创建的对象是可迭代对象，是因为Iterable类有这个方法！**不信？我就来编写一个能创建可迭代对象的类。

 



```
import collections

class BecomeIterable:

    def __iter__(self):
        """返回一个空的迭代器"""
        return None

people = BecomeIterable()
print(isinstance(people, collections.Iterable))

输出：
True
```



迭代器就是重复地做一些事情，可以简单的理解为循环，在python中实现了__iter__方法的对象是可迭代的，实现了next()方法的对象是迭代器，这样说起来有点拗口，实际上要想让一个迭代器工作，至少要实现__iter__方法和next方法。很多时候使用迭代器完成的工作使用列表也可以完成，但是如果有很多值列表就会占用太多的内存，而且使用迭代器也让我们的程序更加通用、优雅、pythonic。

7.迭代器为什么能用next()函数进行迭代？

我们知道，可以用iter()函数，在可迭代对象中获取迭代器。例如：iterator = iter([1,2,3])

这样一看，迭代器也就是一个对象而已啊，为什么他可以用next()函数，一下子出来一个值，一下子又出来一个值。

其实是这样的，**iter()函数能调用可迭代对象的魔方方法__iter__()，从而返回一个迭代器。怎么返回的呢？__iter__()方法是使用collections模块里的Iterator类来创建一个迭代器对象。**

接下来看下Iterator的一部分源代码：



```
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self
```



是不是茅塞顿开了？和第6点的解释原理一样。这里就不详细解释了。稍微**注意下魔方方法__next__()的最后一句，如果超出迭代方位就抛出StopIteration异常。**

还有一点需要注意，迭代器的源代码也有__iter__()魔方方法，所以，**Iterator也是一个可迭代对象呀！！！**

所以，如果你喜欢在迭代器里面再取出迭代器也是可以的，但是好像有点无聊......目前还不知道有什么应用到......

8.创建一个迭代器类

理论讲完了额...不懂的还是要多看几遍。下面开始应用～

如果我们编写一段代码，想把结果一个一个迭代出来，这时候就需要编写迭代器类了。

```
class MyIterator():
    def __init__(self):
        self.list = []
        self.position = 0

    def add_name(self,name):
        self.list.append(name)

    def __iter__(self):
        return self  # 返回一个迭代器

    def __next__(self):
        if self.position < len(self.list):
            item = self.list[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


people = MyIterator()  # people对象既是一个迭代器，也是一个可迭代对象
people.add_name("张三")
people.add_name("李四")
people.add_name("王五")

# 把people当做一个迭代器来看时
print(next(people))
print(next(people))
print(next(people))

# 把humen当做一个可迭代对象来看时
humen = MyIterator()  # 因为迭代器只能用一次，再用会抛出错误，所以需要再创建
humen.add_name("张三")
humen.add_name("李四")
humen.add_name("王五")
iterator = iter(humen)  # iter()方法获取可迭代对象的迭代器
print(next(iterator))
print(next(iterator))
print(next(iterator))输出：张三李四王五张三李四王五
```

注意看注释，如果原理都懂，这其实是一个很简单的例子。

### 生成器

1.生成器是什么？

先说一种比较简单的生成器，通过例子慢慢来体会什么是生成器。



```
# 列表生成式
L = [x for x in range(5)]
print(L)

#简单的生成器
G = (x for x in range(5))  # G就是一个生成器，也是一个迭代器，迭代器也是可迭代对象，所以这个G也可以说是可迭代对象
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

输出：
[0, 1, 2, 3, 4]
0
1
2
3
4
```



把列表生成器的[]改为()就变成一个简单的生成器。由上面的例子，我们大概可以知道，生成器就是一个迭代器，把数据一个一个拿出来，可以减少内存的负担。

那么，yield又是一个什么东西呢？为什么说他优雅呢？

当我们写的代码输出的结果，想一个一个出来。有两种常用的方法：

方法1.我们可以创建一个迭代器类，然后把代码写进类里，用类来创建一个可迭代对象，然后用next()函数一个一个把结果迭代出来。

方法2.我们可以用代码函数的合适位置加上yield，这时候这个函数就变成一个生成器了，不需要再创建一个迭代器类，不需要再写__iter__，__next__方法了。这样一来不是很方便，很优雅吗？哈哈哈哈～

口说无凭，下面我们2个方法都做一下，让你们体会一下：

我们做一个斐波那契的数列生成器。斐波那契数列的第一个数是0，第二个数是1，第三个数是第一、二个数相加，第四个数是第二、三个数相加......

方法1：



```
class FeiboIterator():
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
            num = self.a
            self.a,self.b = self.b,self.a+self.b
            return num


iterator = FeiboIterator()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

输出：0
1
2
3
5
8
13
```



是不是很麻烦？又要初始化，又要写__iter__和__next__魔方方法。

方法2：



```
def feibo():
    a = 0
    b = 1
    while True:
        yield a  # 假如yield后面紧接着一个数据，就会把数据返回，作为next()函数或者for ...in...迭代出的下一个值
        a,b = b,a+b


generator = feibo()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

输出：
0
1
1
2
3
5
8
13
```



看！只有6行代码，是不是很elegant？关于这个程序是怎么运行的？yield是怎么运作的？我们等下就讲，现在需要注意几点：

1.上面代码的红色字那里！**假如yield后面紧接着一个数据，就会把数据返回，作为next()函数或者for ...in...迭代出的下一个值。**

2.假如函数中有yield，就不再是函数。而是一个能返回生成器的函数！注意！是返回，这个函数并不是一个生成器。**（修正：这句话发现有错误，这个函数也是一个生成器）**

3.拿到函数的生成器后，可以和迭代器一样，用next()函数获得下一个值。

好了，该来理解一下yield是怎么运作的了！

1.第一次唤醒生成器时，是从函数的起始位置开始，直到遇到yield，就会暂停函数，挂起函数。
2.第二次唤醒生成器时，是从yield断点处开始，直到又遇到yield。
3.当生成器已经没有yield，再使用next，则抛StopIteration异常。

然后，我们来理一下上面用yield写的代码。

第一次用next()唤醒生成器时，从函数的开头开始运行，遇到yield a，返回a，然后暂停函数，并记住函数是运行到这个位置的。

第二次唤醒生成器，从yield a断点处开始，然后a,b开始赋值，while True循环又遇见yield a，返回a，然后暂停函数，并记住函数是运行到这个位置的。

下面唤醒多少次都是这个道理，但是由于这个函数是死循环，所以不会没有yield，也就不会抛出StopIteration异常。

2.yield接受传参

其实yield还能接受值，用send方法进行传入。代码体会一下：



```
def gg():
    i = 1
    while True:
        recv = yield i
        print("接收到一个值：",recv)
        i += 1

generator = gg()

print(next(generator))
print(generator.send("456"))
print(generator.send("789"))

输出：
1
接收到一个值： 456
2
接收到一个值： 789
3
```



实现过程和上面的例子一样。

要懂得的是，**yield = a，会返回a。**

**b = yield，会把yield接收的值赋值给b。**

### 导包

不同模块（文件夹）下的文件互相引用

```python
import os, sys
# 获得父级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把父级路径添加到环境变量中
sys.path.append(BASE_DIR)
```



### `if __name__ == '__main__'`

python解释器在执行一些代码时，有一些内建、隐含的变量，`__name__`就是其中之一，其意义是`模块名称`。

如果该模块是被引用，那么`__name__`的值会是此模块的名称。

如果该模块是直接被执行，那么`__name__`的值是`__main__`。

`__name__`在模块被直接执行时与被引用时是不同的。



问：当一个模块被引用时，如何不执行该模块的语句？

答：依靠判断`__name__`是否等于`__main__`。当一个模块被直接执行时，其`__name__`必然等于`__main__`；当一个模块被引用时，其`__name__必然等于文件名`

### `__all__`

1.提供了哪些是公开接口的约定

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

2.控制`from xx import *`的行为

代码中当然是不提倡用`from xx import *`的写法的。

如果一个模块`spam`没有定义`__all__`，执行`from spam import *`的时候，会将`spam`中非下划线开头的成员，都导入到当前命名空间中。

这样就有可能弄脏当前名称空间，如果显示声明了`__all__`，`import *`就只会导入`__all__`列出的成员。

如果`__all__`定义有误，列出的成员不存在，还会明确的抛出异常，而不是默默忽略。

3.为lint工具提供辅助

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

4.定义`__all__`需要注意的地方

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

1.标识该目录是一个Python的模块包（module package）

如果使用python相关IDE来进行开发，那么目录中存在该文件，该目录就会被识别是`module package`

2.简化模块导入操作

2.1.`__init__.py是如何工作的`

如果目录中包含了`__init__.py`时，当用`import`导入该目录时，会执行`__init__.py`里面的代码。

2.2.控制模块导入

在执行import的时候，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。



综上，我们可以在`__init__.py`指定默认需要导入的模块

2.3.偷懒的导包方式

要用`__all__`来约束`from mypackage import *`的导包行为

`__all__`关联了一个模块列表，当执行`from mypackage import *`时，就会导入列表中的模块。

3.配置模块的初始化操作

该文件就是一个正常的python代码文件，可以将初始化代码放在该文件中。

### 闭包

定义：函数定义和函数表达式位于另一个函数的函数体内（嵌套函数）。

意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得该函数无论在何处调用，优先使用自己外层包裹的作用域。

使用场景：装饰器

### 软件开发原则

开放-封闭原则

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

