[TOC]

### yield

#### 迭代器

转载：https://www.cnblogs.com/chichung/p/9537969.html

理论性的东西有点枯燥，耐心点看～

##### 1.迭代是什么？

我们知道可以对list,tuple,dict,str等数据类型使用for...in的循环语法，从其中依次取出数据，这个过程叫做遍历，也叫**迭代**。迭代是访问集合元素的一种常用的方式。

##### 2.可迭代对象是什么？

简单来说，可以用for...in循环语句，从其中依次取出数据的对象，就是**可迭代对象**。例如，列表、元组、字典、字符串都是可迭代对象。整数、浮点数、布尔值都是不可迭代的。

##### 3.迭代器是什么？

在可迭代对象进行迭代的时候，即用for...in...循环语法依次取出数据时，过程是怎样的呢？

我们发现，每迭代一次（即在for...in...中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个过程中就应该有一个“人”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。我们把这个能帮助我们进行数据迭代的“人”称为**迭代器(Iterator)**。举个栗子，老师安排一个班的同学每节课上课前进行演讲，按学号顺序进行，A同学这节课演讲，老师就会记住这节课是A同学演讲，那么下节课就是B同学进行演讲...依次类推，在这个例子里，老师就是一个迭代器。

##### 4.怎样获取可迭代对象的迭代器？

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



看完觉得奇怪的同学，是不是觉得一个对象能拿出一个迭代器很amazing。好像编的一样，别急，继续看上去，下面有答案。



##### 5.判断一个对象是否可迭代

isinstance(object,classinfo)内置函数可以判断一个对象是否是一个已知的类型，类似 type()。

- object -- 实例对象。
- classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。

在这之前，还需要知道collections模块里的Iterable。通俗点讲，凡是可迭代对象都是这个类的实例对象。下面来验证一下：



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



##### 6.可迭代对象怎么可以获取迭代器呢？

看完第4点，有些人就感觉很奇怪，例如：[1,2,3]不就是一个列表，一个对象吗？怎么还能拿出一个迭代器来了？

首先，我们从第5点可以知道，可迭代对象其实都是collections模块里的Iterable类创建出来的实例的。你写一个列表，以为他不是任何类创建的，只是单纯一个列表？不是的，其实它就是Iterable类创建的实例对象。点进Iterable的类看一下，你会发现新大陆。

[

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



 

骚不骚？什么都没有，就一个魔法方法，创建的对象就是可迭代对象了。



##### 7.迭代器为什么能用next()函数进行迭代？

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

##### 8.创建一个迭代器类

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

#### 生成器

