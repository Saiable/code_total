[TOC]



### 迭代器

转载：https://www.cnblogs.com/chichung/p/9537969.html

理论性的东西有点枯燥，耐心点看～

#### 1.迭代是什么？

我们知道可以对list,tuple,dict,str等数据类型使用for...in的循环语法，从其中依次取出数据，这个过程叫做遍历，也叫**迭代**。迭代是访问集合元素的一种常用的方式。

#### 2.可迭代对象是什么？

简单来说，可以用for...in循环语句，从其中依次取出数据的对象，就是**可迭代对象**。例如，列表、元组、字典、字符串都是可迭代对象。整数、浮点数、布尔值都是不可迭代的。

#### 3.迭代器是什么？

在可迭代对象进行迭代的时候，即用for...in...循环语法依次取出数据时，过程是怎样的呢？

我们发现，每迭代一次（即在for...in...中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。那么，在这个过程中就应该有一个“人”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。我们把这个能帮助我们进行数据迭代的“人”称为**迭代器(Iterator)**。举个栗子，老师安排一个班的同学每节课上课前进行演讲，按学号顺序进行，A同学这节课演讲，老师就会记住这节课是A同学演讲，那么下节课就是B同学进行演讲...依次类推，在这个例子里，老师就是一个迭代器。

#### 4.怎样获取可迭代对象的迭代器？

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



#### 5.判断一个对象是否可迭代

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



#### 6.可迭代对象怎么可以获取迭代器呢？

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

#### 7.迭代器为什么能用next()函数进行迭代？

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

#### 8.创建一个迭代器类

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

#### 1.生成器是什么？

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

#### 2.yield接受传参

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



### 装饰器

装饰器(Decorators)是 Python 的一个重要部分。简单地说：他们是修改其他函数的功能的函数。他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。大多数初学者不知道在哪儿使用它们，所以我将要分享下，哪些区域里装饰器可以让你的代码更简洁。 首先，让我们讨论下如何写你自己的装饰器。

这可能是最难掌握的概念之一。我们会每次只讨论一个步骤，这样你能完全理解它。

#### 1.一切皆对象

首先我们来理解下 Python 中的函数:

def hi(name="yasoob"):    return "hi " + name  print(hi()) # output: 'hi yasoob'  # 我们甚至可以将一个函数赋值给一个变量，比如 greet = hi # 我们这里没有在使用小括号，因为我们并不是在调用hi函数 # 而是在将它放在greet变量里头。我们尝试运行下这个  print(greet()) # output: 'hi yasoob'  # 如果我们删掉旧的hi函数，看看会发生什么！ del hi print(hi()) #outputs: NameError  print(greet()) #outputs: 'hi yasoob'

#### 在函数中定义函数

刚才那些就是函数的基本知识了。我们来让你的知识更进一步。在 Python 中我们可以在一个函数中定义另一个函数：

def hi(name="yasoob"):    print("now you are inside the hi() function")     def greet():        return "now you are in the greet() function"     def welcome():        return "now you are in the welcome() function"     print(greet())    print(welcome())    print("now you are back in the hi() function")  hi() #output:now you are inside the hi() function #       now you are in the greet() function #       now you are in the welcome() function #       now you are back in the hi() function  # 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。 # 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：  greet() #outputs: NameError: name 'greet' is not defined

那现在我们知道了可以在函数中定义另外的函数。也就是说：我们可以创建嵌套的函数。现在你需要再多学一点，就是函数也能返回函数。

#### 从函数中返回函数

其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

def hi(name="yasoob"):    def greet():        return "now you are in the greet() function"     def welcome():        return "now you are in the welcome() function"     if name == "yasoob":        return greet    else:        return welcome  a = hi() print(a) #outputs: <function greet at 0x7f2143c01500>  #上面清晰地展示了`a`现在指向到hi()函数中的greet()函数 #现在试试这个  print(a()) #outputs: now you are in the greet() function

再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。 你明白了吗？让我再稍微多解释点细节。

当我们写下 **a = hi()**，hi() 会被执行，而由于 name 参数默认是 yasoob，所以函数 greet 被返回了。如果我们把语句改为 **a = hi(name = "ali")**，那么 welcome 函数将被返回。我们还可以打印出 **hi()()**，这会输出 **now you are in the greet() function**。

#### 将函数作为参数传给另一个函数

def hi():    return "hi yasoob!"  def doSomethingBeforeHi(func):    print("I am doing some boring work before executing hi()")    print(func())  doSomethingBeforeHi(hi) #outputs:I am doing some boring work before executing hi() #        hi yasoob!

现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。装饰器让你在一个函数的前后去执行代码。

#### 你的第一个装饰器

在上一个例子里，其实我们已经创建了一个装饰器！现在我们修改下上一个装饰器，并编写一个稍微更有用点的程序：

def a_new_decorator(a_func):     def wrapTheFunction():        print("I am doing some boring work before executing a_func()")         a_func()         print("I am doing some boring work after executing a_func()")     return wrapTheFunction  def a_function_requiring_decoration():    print("I am the function which needs some decoration to remove my foul smell")  a_function_requiring_decoration() #outputs: "I am the function which needs some decoration to remove my foul smell"  a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration) #now a_function_requiring_decoration is wrapped by wrapTheFunction()  a_function_requiring_decoration() #outputs:I am doing some boring work before executing a_func() #        I am the function which needs some decoration to remove my foul smell #        I am doing some boring work after executing a_func()

你看明白了吗？我们刚刚应用了之前学习到的原理。这正是 python 中装饰器做的事情！它们封装一个函数，并且用这样或者那样的方式来修改它的行为。现在你也许疑惑，我们在代码里并没有使用 **@** 符号？那只是一个简短的方式来生成一个被装饰的函数。这里是我们如何使用 **@** 来运行之前的代码：

@a_new_decorator def a_function_requiring_decoration():    """Hey you! Decorate me!"""    print("I am the function which needs some decoration to "          "remove my foul smell")  a_function_requiring_decoration() #outputs: I am doing some boring work before executing a_func() #         I am the function which needs some decoration to remove my foul smell #         I am doing some boring work after executing a_func()  #the @a_new_decorator is just a short way of saying: a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

希望你现在对 Python 装饰器的工作原理有一个基本的理解。如果我们运行如下代码会存在一个问题：

```
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
```

这并不是我们想要的！Ouput输出应该是"a_function_requiring_decoration"。这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。我们修改上一个例子来使用functools.wraps：

from functools import wraps  def a_new_decorator(a_func):    @wraps(a_func)    def wrapTheFunction():        print("I am doing some boring work before executing a_func()")        a_func()        print("I am doing some boring work after executing a_func()")    return wrapTheFunction  @a_new_decorator def a_function_requiring_decoration():    """Hey yo! Decorate me!"""    print("I am the function which needs some decoration to "          "remove my foul smell")  print(a_function_requiring_decoration.__name__) # Output: a_function_requiring_decoration

现在好多了。我们接下来学习装饰器的一些常用场景。

蓝本规范:

from functools import wraps def decorator_name(f):    @wraps(f)    def decorated(*args, **kwargs):        if not can_run:            return "Function will not run"        return f(*args, **kwargs)    return decorated  @decorator_name def func():    return("Function is running")  can_run = True print(func()) # Output: Function is running  can_run = False print(func()) # Output: Function will not run

**注意：****@wraps**接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

------

#### 使用场景

现在我们来看一下装饰器在哪些地方特别耀眼，以及使用它可以让一些事情管理起来变得更简单。

##### 授权(Authorization)

装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：

from functools import wraps  def requires_auth(f):    @wraps(f)    def decorated(*args, **kwargs):        auth = request.authorization        if not auth or not check_auth(auth.username, auth.password):            authenticate()        return f(*args, **kwargs)    return decorated

##### 日志(Logging)

日志是装饰器运用的另一个亮点。这是个例子：

from functools import wraps  def logit(func):    @wraps(func)    def with_logging(*args, **kwargs):        print(func.__name__ + " was called")        return func(*args, **kwargs)    return with_logging  @logit def addition_func(x):   """Do some math."""   return x + x   result = addition_func(4) # Output: addition_func was called

我敢肯定你已经在思考装饰器的一个其他聪明用法了。

------

#### 带参数的装饰器

来想想这个问题，难道@wraps不也是个装饰器吗？但是，它接收一个参数，就像任何普通的函数能做的那样。那么，为什么我们不也那样做呢？ 这是因为，当你使用@my_decorator语法时，你是在应用一个以单个函数作为参数的一个包裹函数。记住，Python里每个东西都是一个对象，而且这包括函数！记住了这些，我们可以编写一下能返回一个包裹函数的函数。

#### 在函数中嵌入装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

from functools import wraps  def logit(logfile='out.log'):    def logging_decorator(func):        @wraps(func)        def wrapped_function(*args, **kwargs):            log_string = func.__name__ + " was called"            print(log_string)            # 打开logfile，并写入内容            with open(logfile, 'a') as opened_file:                # 现在将日志打到指定的logfile                opened_file.write(log_string + '\n')            return func(*args, **kwargs)        return wrapped_function    return logging_decorator  @logit() def myfunc1():    pass  myfunc1() # Output: myfunc1 was called # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串  @logit(logfile='func2.log') def myfunc2():    pass  myfunc2() # Output: myfunc2 was called # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

------

#### 装饰器类

现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建logit。

from functools import wraps  class logit(object):    def __init__(self, logfile='out.log'):        self.logfile = logfile     def __call__(self, func):        @wraps(func)        def wrapped_function(*args, **kwargs):            log_string = func.__name__ + " was called"            print(log_string)            # 打开logfile并写入            with open(self.logfile, 'a') as opened_file:                # 现在将日志打到指定的文件                opened_file.write(log_string + '\n')            # 现在，发送一个通知            self.notify()            return func(*args, **kwargs)        return wrapped_function     def notify(self):        # logit只打日志，不做别的        pass

这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

```
@logit()
def myfunc1():
    pass
```

现在，我们给 logit 创建子类，来添加 email 的功能(虽然 email 这个话题不会在这里展开)。

class email_logit(logit):    '''    一个logit的实现版本，可以在函数调用时发送email给管理员    '''    def __init__(self, email='admin@myproject.com', *args, **kwargs):        self.email = email        super(email_logit, self).__init__(*args, **kwargs)     def notify(self):        # 发送一封email到self.email        # 这里就不做实现了        pass

从现在起，@email_logit 将会和 @logit 产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。

> 原文地址：https://eastlakeside.gitbooks.io/interpy-zh/content/decorators/