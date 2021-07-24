[TOC]

[教程来源](https://www.bilibili.com/video/BV1a7411z75u?from=search&seid=6695941388107712803)

### 1.Socket概念

#### 1.1.Tcp/Ip

当今的网络世界，基本上是使用TCP/IP协议进行通信的。

#### 1.2.引入Socket

类比于快递收发，对应到软件开发上，

收发信息的`程序进程`就像`收件人和发件人`；

收发的信息`信息`就像快递传输的`物品`；

具体信息的传输路径（中间经过哪些路由器）和传输的方法（使用什么协议）就像快递公司的运输流程；

同样的，我们编写发出信息的程序和接受信息的程序，并不需要知道，信息传输的所有细节，比如中间经过哪些路由器，路由器之间又是如何进行传输的。

这个过程，可以用下图来表示：

![在这里插入图片描述](https://img-blog.csdnimg.cn/0f9e4e7e819a4e2d9227766420a5ca4b.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 2.Python Socket代码示例

ts.py

```python
```

tc.py

```python
```

#### 2.1.发送接受缓冲，消息格式定义

上面的例子中，我们发送的消息就是要传递的内容，格式是字符串。

实际上，我们在企业开发中的程序通讯，消息往往是有格式定义的。消息的格式定义可以归入OS网络模型的`表示层`。

比如，定义的消息，包括`消息头`和`消息体`。

消息头存放消息的格式数据，比如`消息的长度、类型、状态等等`，而消息体存放具体的传送数据。

对于使用TCP协议传输信息的程序来说，格式定义一定要明确规定`消息的边界`。

因为TCP协议传输的是`字节流（bytes stream）`，如果消息中没有指定边界或者长度，接收方就不知道一个完整的消息，从字节流哪里开始，到哪里结束。

指定消息的边界，有两种方式：

- 用特殊字符作为作为消息的结尾符号
  - 可以用消息内容中不可能出现的字符串（比如FFFFFF），作为消息的结尾字符。
- 在消息开头某个位置，直接指定消息长度

UDP协议通常不需要指定消息边界，因为UDP是数据协议，应用程序从socket接收到的必定是发送方发送的完整的消息（:notice-info）



![在这里插入图片描述](https://img-blog.csdnimg.cn/cbd594c146974b35834bac6aba6c905c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### 2.2.支持多个客户端

上面的服务器代码，只能和一个客户端进行通信。

如果我们同时运行多个客户端，就会发现后面的客户端不能和服务端连接成功。为什么呢？

### 3.消息格式定义