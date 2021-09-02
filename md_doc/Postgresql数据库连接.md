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

### 5.常用API

https://www.yiibai.com/postgresql/postgresql_python.html

**S.N. API & 描述**
1	psycopg2.connect(database="testdb", user="postgres", password="cohondob", host="127.0.0.1", port="5432") 
　　这个API打开一个连接到PostgreSQL数据库。如果成功打开数据库时，它返回一个连接对象。 
2	connection.cursor()
　　该程序创建一个光标将用于整个数据库使用Python编程。 
3	cursor.execute(sql [, optional parameters])
　　此例程执行SQL语句。可被参数化的SQL语句（即占位符，而不是SQL文字）。 psycopg2的模块支持占位符用％s标志 
　　例如：cursor.execute("insert into people values (%s, %s)", (who, age))
4	curosr.executemany(sql, seq_of_parameters)
　　该程序执行SQL命令对所有参数序列或序列中的sql映射。 
5	curosr.callproc(procname[, parameters])
　　这个程序执行的存储数据库程序给定的名称。该程序预计为每一个参数，参数的顺序必须包含一个条目。
6	cursor.rowcount
　　这个只读属性，它返回数据库中的行的总数已修改，插入或删除最后 execute*().
7	connection.commit()
　　此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用commit()是不可见的，从其他的数据库连接。
8	connection.rollback()
　　此方法会回滚任何更改数据库自上次调用commit（）方法。
9	connection.close()
　　此方法关闭数据库连接。请注意，这并不自动调用commit（）。如果你只是关闭数据库连接而不调用commit（）方法首先，那么所有更改将会丢失！ 
10	cursor.fetchone()
　　这种方法提取的查询结果集的下一行，返回一个序列，或者无当没有更多的数据是可用的。
11	cursor.fetchmany([size=cursor.arraysize])
　　这个例程中取出下一个组的查询结果的行数，返回一个列表。当没有找到记录，返回空列表。该方法试图获取尽可能多的行所显示的大小参数。
12	cursor.fetchall()
　　这个例程获取所有查询结果（剩余）行，返回一个列表。空行时则返回空列表。

#### 每条完整的sql执行步骤

1. 建立连接获得 connect 对象
2. 获得游标对象，一个游标对象可以对数据库进行执行操作，非线程安全，多个应用会在同一个连接种创建多个光标；
3. 书写sql语句
4. 调用execute()方法执行sql
5. 抓取数据（可选操作）
6. 提交事物
7. 关闭连接

```python

import os
import sys
import psycopg2

def connectPostgreSQL():
    conn = psycopg2.connect(database="komablog", user="postgres", password="123123", host="127.0.0.1", port="5432")
    print('connect successful!')
    cursor=conn.cursor()
    cursor.execute('''
        create table public.member(
            id integer not null primary key,
            name varchar(32) not null,
            password varchar(32) not null,
            singal varchar(128)
        )
    ''')
    conn.commit()
    conn.close()
    print('table public.member is created!')

def insertOperate():
    conn = psycopg2.connect(database="komablog", user="postgres", password="123123", host="127.0.0.1", port="5432")
    cursor=conn.cursor()
    cursor.execute("insert into public.member(id,name,password,singal)\
    values(1,'member0','password0','signal0')")
    cursor.execute("insert into public.member(id,name,password,singal)\
    values(2,'member1','password1','signal1')")
    cursor.execute("insert into public.member(id,name,password,singal)\
    values(3,'member2','password2','signal2')")
    cursor.execute("insert into public.member(id,name,password,singal)\
    values(4,'member3','password3','signal3')")
    conn.commit()
    conn.close()

    print('insert records into public.memmber successfully')

def selectOperate():
    conn = psycopg2.connect(database="komablog", user="postgres", password="123123", host="127.0.0.1", port="5432")
    cursor=conn.cursor()
    cursor.execute("select id,name,password,singal from public.member where id>2")
    rows=cursor.fetchall()
    print(rows)
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    conn.close()

def updateOperate():
    conn = psycopg2.connect(database="komablog", user="postgres", password="123123", host="127.0.0.1", port="5432")
    cursor=conn.cursor()
    cursor.execute("update public.member set name='update ...' where id=2")
    conn.commit()
    print("Total number of rows updated :", cursor.rowcount)

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    conn.close()

def deleteOperate():
    conn = psycopg2.connect(database="komablog", user="postgres", password="123123", host="127.0.0.1", port="5432")
    cursor=conn.cursor()

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')

    print('begin delete')
    cursor.execute("delete from public.member where id=2")
    conn.commit()
    print('end delete')
    print("Total number of rows deleted :", cursor.rowcount)

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    conn.close()

if __name__=='__main__':
    #connectPostgreSQL()
    #insertOperate()
    #selectOperate()
    #updateOperate()
    deleteOperate()
```

#### python操作psql功能封装

