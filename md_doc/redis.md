[TOC]



[教程来源](https://www.bilibili.com/video/BV1Rv41177Af)

## 1.NoSQL数据库简介

## 2. Redis概述安装

### 2.1. 应用场景

#### 2.1.1.配合关系型数据库做高速缓存

- 高频次，热门访问的数据，降低数据库IO
- 分布式架构，做session共享

#### 2.1.2.多样的数据结构存储持久化数据

- 最新N个数据：通过List实现按自然时间排序的数据
- 排行榜，TopN：利用zset（有序集合）
- 时效性的数据，比如手机验证码：Expire过期
- 计数器、秒杀：原子性，自增方法：INCR、DECR
- 去除大量数据中的重复数据：利用Set集合
- 构建队列：利用list集合
- 发布订阅消息系统：pub/sub模式

### 2.2. Redis安装

#### 2.2.1. 安装版本

[redis官网](https://redis.io) 下载官网最新稳定版本

不考虑windows环境下对redis的支持

#### 2.2.2. 安装步骤

准备工作：下载安装最新版的gcc编译器

安装C语言的编译环境

```shell
yum install centos-release-scl scl-utils-build
yum install -y devtoolset-8-toolchain
scl enable devtoolset-8 bash
```

测试gcc版本

```shell
gcc --version
```

如果没有，安装gcc

```shell
yum install gcc
```

下载redis-6.2.4.tar.gz安装包，放在/opt目录下

解压命令

```shell
tar -zxvf redis-6.2.4.tar.gz
```

解压完成后进入目录

```shell
cd redis-6.2.4
```

在redis-6.2.4目录下执行make编译命令

```shell
make
```

- 如果没有准备好C语言编译环境，make会报错：Jemalloc/jemalloc.h：没有那个文件
- 解决方案：运行`make distclean`，安装好编译环境后，再次执行make编译命令

跳过`make test`命令，执行`make install`安装命令

#### 2.2.3. 安装目录

默认安装在`/usr/local/bin`目录下

查看默认安装目录：

- `redis-benchmark`：性能测试工具，可以在自己本子运行，看看自己本子性能如何
- `redis-check-aof`：修复有问题的AOF文件，rdb和aof后面讲
- `redis-check-dump`：修复有问题的dump.rdb文件
- `redis-sentinel`：redis集群使用
- **`redis-server`**：redis服务器启动命令
- **`redis-cli`**：客户端，操作入口

#### 2.2.4. 前台启动（不推荐）

前台启动，命令行窗口不能关闭，否则服务器停止

```shell
redis-server
```

#### 2.2.5. 后台启动（推荐）

redis目录中，有一个文件`redis.conf`，把它复制到/etc目录下（或自定义目录下）

```shell
cp redis.conf /etc/redis.conf
```

修改redis.conf(128行)文件将里面的daemonize no 改成yes，让服务在后台启动（可以在vi中按`\`搜索）

```shell
vi redis.conf
```

按`\`进行搜索`daemonize`，然后修改

进入/usr/local/bin目录下，指定配置文件启动redis

```shell
redis-server /etc/redis.conf
```

查询启动的redis进程

```shell
ps -ef | grep redis
```

这种启动方式，即使关闭了命令行窗口，redis仍然是启动状态

此时可以通过`redis-cli`命令启动redis客户端来连接redis数据库

```shell
redis-cli
```

多个端口访问：`redis-cli -p 6379`，如果输入了错误的端口号，虽然可以进入redis终端，但在ping的时候，会报错：

```
Error: Protocol error, got "H" as reply type byte
```

redis终端中输入`ping`，返回`PONG`表示是一个正常的连通状态

redis的关闭

- 单实例关闭：`redis-cli shutdown`（未进入redis终端）

- 也可以进入终端后再关闭：`shutdown`，然后输入`exit`退出

- 可以`ps -ef | grep redis`查询进程号

  ```
  root     22661     1  0 16:44 ?        00:00:00 redis-server 127.0.0.1:6379
  root     34556 21819  0 17:15 pts/7    00:00:00 grep --color=auto redis
  ```

  然后`kill -9 22661`杀掉redis进程即可

- 配置密码

  - 搜索`requirepass foobared`，然后修改`foobared`，记得删除`#`号取消注释
  - 连同后，输入`auth 密码`即可

#### 2.2.6. Redis介绍相关知识

- 端口6379从何而来：`Alessia Merz`

- 默认16个数据库，类似数组下标从0开始，初始默认使用0号库
- 统一密码管理，所有库同样密码
- `dbsize`查看当前数据库的key的数量
- `flushdb`清空当前库
- `flushall`通杀全部库

Redis是单线程+多路IO复用技术

多路IO复用是指使用一个线程来检查多个文件描述符（Socket）的就绪状态，比如调用select和poll函数，传入多个文件描述符，如果有一个文件描述符就绪，则返回，否则阻塞直至超时。

得到就绪状态后进行真正的操作，可以在同一个线程里执行，也可以启动线程执行（比如使用线程池）

串行 vs 多线程 + 锁(memcached) + 单线程 + 多路IO复用（Redis）

(与Memcache三点不同：支持多数据类型，支持持久化，单线程 + 多路IO复用)

## 3.常用五大数据类型

[redis常见数据类型操作命令](http://www.redis.cn/commands.html)

### 3.1.Redis键（key）

- `keys *`：查看当前库所有key（匹配：keys *1（匹配以1结尾的key键））
- `exsits key`：判断某个key是否存在
- `type key`：查看你的key是什么类型
- `del key`：删除指定的key数据
- `unlink key`：根据value选择非阻塞删除
  - 仅将keys从keyspace元数据中删除，真正的删除在后续异步操作
- `expire key 10`：为给定的key设置过期时间为10秒
  - `ttl key`：查看还有多少秒过期，-1表示永不过期，-2表示已过期
- `select 1`：切换数据库1
- `dbsize`：查看当前库的key的数量
- `flushdb`：清空当前库
- `flushall`：通杀全部库

### 3.2.Redis字符串（String）

#### 3.2.1.简介

- String是Redis最基本的数据类型，一个key对应一个value

- String类型是二进制安全的，意味着Redis的string可以包含任何数据。比如jpg图片或者序列化的对象（一个文件，只要能转换成字符串，都可以存到Redis中）

- String类型是Redis最基本的数据类型，一个Redis中字符串value最多可以使512M

#### 3.2.2.常用命令

- `set <key> <value>`添加键值对

- `get <key>`查询对应键值

  ```
  127.0.0.1:6379> set k1 v1 [EX seconds|PX milliseconds|EXAT timestamp|PXAT milliseconds-timestamp|KEEPTTL] [NX|XX] [GET]
  
  set k1 v1
  set k1 v2
  get k1 # "v2"，对同一个key设置，会覆盖原来的
  ```
  
  
  
- *NX：当数据库中key不存在时，可以将key-value添加数据库

- *XX：当数据库key存在时，可以将key-value添加数据库，与NX参数互斥

- *EX：key的超时秒数

- `get <key>`：查询对应键值

- `append <key> <value>`：将给定的`<value>`追加到原值的末尾

- `strlen <key> <value>`：获得值的长度

- `setnx <key> <value>`：只有在`key`不存在时，设置`<key>`的值

- `incr <key>`

  - 将`<key>`中存储的数字值增1
  - 只能对数字值操作，如果为空，新增值为1

- `decr <key>`

  - 将key中存储的数字值减1
  - 只能对数字值操作，如果为空，新增值减1

- `incrby/decrby <key> <步长>`：将key中存储的数字值增减，自定义步长

原子性：

- `incr key`：对存储在指定key的数值执行原子的加1操作

  - 起始版本：1.0.0
  - 时间复杂度：O(1)

- 所谓原子操作，是指不会被线程调度机制打断的操作

- 这种操作一旦开始，就一直运行到结束，中间不会有任何`context switch`（切换到另一个线程）

  - 在单线程中，能够在单条指令中完成的操作都可以认为是“原子操作”，因为中断只能发生于指令质检
  - 在多线程中，不能被其它进程（线程）打断的操作就叫原子操作。

- Redis单命令的原子性主要得益于Redis的单线程

- 案例

  ```
  Java中的i++是否是原子操作？
  	不是，先取值，再++，再赋值
  
  i=0，两个线程分别对i进行i++100次，值是多少？
  	2~200
  ```

- `mset <key1> <value1> <key2> <value2>`

  - 同时设置一个或多个key-value对

- `mget <key1> <key2> <key3>`

  - 同时获取一个或多个value

- `msetnx <key1> <value1> <key2> <value3>`

  - 同时设置一个或者多个key-value，当且仅当给定key都不存在

- `getrange <key> <起始位置> <结束位置>`

  - 获得值的范围，类似java中的substring，前包，后包

- `setrange <key> <起始位置> <value>`

  - 用`<value>`覆写`key`所存储的字符串值，从`<起始位置>`开始（索引从0开始）

- `setex <key> 过期时间 <value>`

  - 设置键值的同时，设置过期时间，单位：秒

- `getset <key> <value>`

  - 因新换旧，设置了新值的 同时获得旧值

#### 3.2.3.数据结构

`String`的数据结构为简单动态字符串(Simple Dynamic String，缩写是SDS)。是可以修改的字符串，内部结构实现上类似于Java的ArrayList，采用预分配冗余空间的方式来减少内存的频繁分配。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210705214701371.png)

如图所示，内部为当前字段串实际分配的空间capacity一般要高于字符串实际长度len。当字符串长度小于1M时，扩容都是加倍现有的空间，如果超过1M，扩容时一次只会多扩1M的空间。需注意的是字符串的最大长度为512M。

### 3.3.Redis列表（List）

#### 3.3.1.简介

单值多键

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

它的底层实际是个**双向链表**，对两端的操作性能很高，同构索引下标来操作中间的节点性能会较差。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210705215815358.png)

#### 3.3.2.常用命令

- `lpush/rpush <key> <value1> <value2> <value3>...`
  - 从左边/右边插入一个或多个值
- `lpop/rpop <key>`
  - 从左边/右边吐出一个值。值在键在，值光键亡。
- `rpoplpush <key1> <key2>`
  - 从`<key1>`列表右边吐出一个值，插到`<key2>`列表左边。
- `lrange <key> <start> <stop>`
  - 按照索引下标获得元素（从左到右）
  - `lrange mylist 0 -1`
    - 0：左边第一个
    - -1：右边第一个
    - 表示获取所有
- `index <key> <index>`
  - 按照索引下标获取元素（从左到右）
- `llen <key>`
  - 获得列表长度
- `linsert <key> before/after <value> <newvalue>`
  - 在`<value>`的前面/后面插入`<newvalue>`插入值
- `lrem <key> <n> <value>`
  - 从左边删除n个value（从左到右）
- `lset <key> <index> <value>`
  - 将列表`<key>`下标为`index`的值替换成`value`

#### 3.3.3.数据结构

List的数据结构为快速链表quicklist。

首先在列表元素较少的情况下会使用一块连续的内存存储，这个结构是ziplist，也即是压缩列表。

它将所有的元素紧挨着一起存储，分配的是一块连续的内存。

当数据量比较多的时候才会改成quicklist。

因为普通的链表需要的附加指针空间太大，会比较浪费空间。比如这个列表里存的只是int类型的数据，结构上还需要两个额外的指针prev和next。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210705225559448.png)

redis将链表和ziplist结合起来组成了quicklist。也就是将多个ziplist使用双向指针串起来使用。这样既满足了快速的插入删除性能，又不会出现太大的空间冗余。

### 3.4.Redis集合（Set）

#### 3.4.1.简介

Redis set对外提供的功能与list类似是一个列表的功能，特殊之处在于set是可以**自动排重**的，当你需要存储一个列表数据，又不希望出现重复数据时，set是一个很好的选择，并且set提供了判断某个成员是否在一个set集合内的重要接口，这个也是list所不能提供的。

Redis的Set是String类型的无序集合。它底层其实是一个value为null的hash表，所以添加，删除，查找的复杂度都是O(1)。

一个算法，随着数据的增加，执行时间的长短，如果是O(1)，数据增加，查找数据的时间不变。

#### 3.4.2.常用命令

- `sadd <key> <value1> <value2>...`
  - 将一个或多个member元素加入到集合key中，已经存在的member元素将被忽略
- `smembers <key>`
  - 取出该集合的所有值
- `sismember <key> <value>`
  - 判断集合`<key>`是否含有该`<value>`值，有1，没有0
- `scard <key>`
  - 返回该集合的元素个数
- `srem <key> <value1> <value2>`...
  - 删除集合中的某个元素
- `spop <key>`
  - 随机从该集合中吐出一个值
- `srandmember <key> <n>`
  - 随机从该集合中取出n个值，不会从集合中删除
- `smove <source> <destiantion> value`
  - 把集合中的一个值从一个集合移动到另一个集合
- `sinter <key1> <key2>`
  - 返回两个集合的交集元素
- `sunion <key1> <key2>`
  - 返回两个集合的并集元素
- `sdiff <key1> <key2>`
  - 返回两个集合的差集元素（key1中的，不包含key2中的）

#### 3.4.3.数据结构

Set数据结构是dict字典，字典使用哈希表实现的。

Java中的HashSet的内部实现使用的是HashMap，只不过所有的value都指向同一个对象。

Redis的set结构也是一样，它的内部结构也使用hash结构，所有的value都指向同一个内部值。

### 3.5.Redis哈希（Hash）

#### 3.5.1.简介

Redis hash是一个键值对集合

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

类似Java里面的`Map<StringObject>`

用户ID为查找的key，存储的value用户对象包含姓名，年龄，生日等信息，如果用普通的key/value结构来存储

主要有以下2中存储方式：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210706221754154.png)

方法一：每次修改用户的某个属性，需要先反序列化，改好后再序列化回去，开销较大

方法二：用户ID数据冗余

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210706223305385.png)

方法三：通过key（用户ID）+field（属性标签）就可以操作对应属性数据了，既不需要重复存储数据，也不会带来序列化和并发修改控制的问题

#### 3.5.2.常用命令

- `hset <key> <field> <value>`
  - 给`<key>`集合中的`<field>`键赋值`<value>`
- `hget <key> <field> `
  - 从`<key>集合<field>取出<value>`
- `hmset <key> <field1> <value1> <field2> <value2> ...`
  - 批量设置hash的值
- `hexists <key> <field>`
  - 查看哈希表key中，给定域field是否存在
- `hkeys <key>`
  - 列出该hash集合的所有field
- `hvals <key>`
  - 列出该hash集合的所有value
- `hincrby <key> <field> <increment>` 
  - 为哈希表key中的域filed的值加上增量1（-1）
- `hset <key> <field> <value>`
  - 将哈希表key中的域field的值设置为value，当且仅当域field不存在

#### 3.5.3.数据结构

Hash类型对应的数据结构是两种，ziplist（压缩列表），hashtable（哈希表），当field-value长度较短且个数较少时，使用ziplist，否则使用hashtable

### 3.6.Redis有序集合Zset（set）

#### 3.6.1.简介

#### 3.6.2.常用命令

#### 3.6.3.数据结构

#### 3.6.4.跳跃表（跳表）

## 4.Redis配置文件介绍

## 5.Redis的发布和订阅

### 5.1.什么是发布和订阅

### 5.2.Redis的发布和订阅

### 5.3.发布订阅命令行实现