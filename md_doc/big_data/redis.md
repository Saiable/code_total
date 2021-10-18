[TOC]



## 2. Redis概述安装

### 2.1. 应用场景

### 2.2. Redis安装

#### 2.1.1. 安装版本

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

修改redis.conf(128行)文件将里面的daemonize no 改成yes，让服务在后台启动

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

再输入`ping`，返回`PONG`表示是一个正常的连通状态

redis的关闭

- 单实例关闭：redis-cli shutdown

#### 2.2.6. Redis介绍相关知识