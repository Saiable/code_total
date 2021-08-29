[TOC]

### 1. 修改PostgreSQL数据库默认用户postgres的密码

PostgreSQL数据库创建一个postgres用户作为数据库的管理员，密码随机，所以需要修改密码，方式如下：

步骤一：登录PostgreSQL

```
sudo -u postgres psql
```

步骤二：修改登录PostgreSQL密码

```
ALTER USER postgres WITH PASSWORD 'postgres';
```

**注：**

- 密码postgres要用引号引起来
- 命令最后有分号

步骤三：退出PostgreSQL客户端

```
\q
```

### 2. 修改linux系统postgres用户的密码

PostgreSQL会创建一个默认的linux用户postgres，修改该用户密码的方法如下：

步骤一：删除用户postgres的密码

```
sudo passwd -d postgres
```

步骤二：设置用户postgres的密码

```
sudo -u postgres passwd
```

系统提示输入新的密码

```
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

###  3.修改配置文件

在Centos下，默认的数据目录在 /var/lib/pgsql/版本号/data 下 ，配置的参数文件就在此目录下。

### 4.直接通过ssh连接服务器，就进到psql数据库了。