[TOC]

# 一、什么是PostgreSql？

PostgreSQL 是一个自由的对象-关系数据库服务器(数据库管理系统)，是从伯克利写的 POSTGRES 软件包发展而来的。经过十几年的发展， PostgreSQL 是世界上可以获得的最先进的开放源码的数据库系统， 它提供了多版本并发控制，支持几乎所有SQL语句（包括子查询，事务和用户定义类型和函数），并且可以获得非常广阔范围的（开发）语言绑定 （包括C,C++,Java,perl,python,php,nodejs,ruby）。

## 知识点

- 面向关系的数据库
- Oracle
- MySql
- SQLServer
- PostgreSql
- NoSql
- MongoDB
- Redis

### 数据库排名

https://db-engines.com/en/ranking

## 官方网站

https://www.postgresql.org/

## 技术准备

- SQL语言基础

## 使用环境及安装

（参照官网）https://www.postgresql.org/download/linux/redhat/

- Ubuntu Server 16 LTS
- PostgreSql 9.5.x

```
$ sudo apt-get install postgresql
$ psql --version
```

- Centos 7
- PostgreSql 13

```shell
# Install the repository RPM:
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Install PostgreSQL:
sudo yum install -y postgresql13-server

# Optionally initialize the database and enable automatic start:
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb
sudo systemctl enable postgresql-13
sudo systemctl start postgresql-13
```



# 二、初来乍到数据库

## 知识点

- psql的基础
- 数据库简单操作
- 写个SQL

## 实战演习

```
# 切换postgres用户，加 - 是为了解决报权限错误
$ sudo su - postgres

# 查看数据库版本
$ psql --version

# 查看数据库情况
$ psql -l

# 创建数据库
$ createdb komablog

$ psql -l

# 进入到komablog数据库
$ psql komablog

> help
> \h
> \?
> \l
> \q

$ psql komablog
> select now();
> select version();
> \q

# 删除数据库
$ dropdb komablog
$ psql -l
```

# 三、操作数据表

## 知识点

- create table
- drop table
- psql使用

## 实战演习

```
$ sudo su - postgres
$ createdb komablog
$ psql -l
$ psql komablog

# 创建posts表
> create table posts (title varchar(255), content text);

# 查看所有表
> \dt

# 查看指定posts表
> \d posts

# 修改表名
> alter table posts rename to komaposts;
> \dt

# 删除表
> drop table komaposts;
> \dt
> \q

# 指定编辑器，编写sql语句
$ vi db.sql # 或者nano db.sql
...
create table posts (title varchar(255), content text);
...

# 进入到数据库
$ psql komablog

# 运行sql
> \i db.sql
> \dt
```

# 四、字段类型

## 知识点

- PostgreSql的基础数据类型

## PostgreSql的基础数据类型

- 数值型：
- integer(int)
- real
- serial
- 文字型：
- char
- varchar
- text
- 布尔型：
- boolean
- 日期型：
- date
- time
- timestamp
- 特色类型：
- Array
- 网络地址型(inet)
- JSON型
- XML型

参考网站：

https://www.postgresql.org/docs/9.5/static/datatype.html

# 五、添加表约束

## 知识点

- 表子段的约束条件

## 实战演习

**db.sql**

```
create table posts (
    id serial primary key,
    title varchar(255) not null,
    content text check(length(content) > 8),
    is_draft boolean default TRUE,
    is_del boolean default FALSE,
    created_date timestamp default 'now'
);

-- 说明
/*
约束条件：

not null:不能为空
unique:在所有数据中值必须唯一
check:字段设置条件
default:字段默认值
primary key(not null, unique):主键，不能为空，且不能重复
*/
```

# 六、INSERT语句

## 知识点

- insert into [tablename] (field, ...) values (value, ...)

## 实战演习

```
$ psql komablog
> \dt
> \d posts
```

### SQL部分

```
> insert into posts (title, content) values ('', '');
ERROR:  new row for relation "posts" violates check constraint "posts_content_check"
DETAIL:  Failing row contains (1, , , t, f, 2021-08-28 08:15:57.275567).


> insert into posts (title, content) values (NULL, '');
ERROR:  null value in column "title" of relation "posts" violates not-null constraint
DETAIL:  Failing row contains (2, null, , t, f, 2021-08-28 08:15:57.275567).


> insert into posts (title, content) values ('title1', 'content11');
INSERT 0 1


> select * from posts;
 id | title  |  content  | is_draft | is_del |        created_date        
----+--------+-----------+----------+--------+----------------------------
  3 | title1 | content11 | t        | f      | 2021-08-28 08:15:57.275567


> insert into posts (title, content) values ('title2', 'content22');
INSERT 0 1


> insert into posts (title, content) values ('title3', 'content33');
INSERT 0 1


> select * from posts;
 id | title  |  content  | is_draft | is_del |        created_date        
----+--------+-----------+----------+--------+----------------------------
  3 | title1 | content11 | t        | f      | 2021-08-28 08:15:57.275567
  4 | title2 | content22 | t        | f      | 2021-08-28 08:15:57.275567
  5 | title3 | content33 | t        | f      | 2021-08-28 08:15:57.275567
(3 rows)


```

# 七、SELECT语句

## 知识点

- select 基本使用

## 实战演习

**init.sql**

```
create table users (
    id serial primary key,
    player varchar(255) not null,
    score real,
    team varchar(255)
);

insert into users (player, score, team) values
('库里', 28.3, '勇士'),
('哈登', 30.2, '火箭'),
('阿杜', 25.6, '勇士'),
('阿詹', 27.8, '骑士'),
('神龟', 31.3, '雷霆'),
('白边', 19.8, '热火');
```

**SQL实战**

```
$ psql komablog
> \i init.sql
> \dt
> \d users
> select * from users;
> \x
> select * from users;
> \x
> select * from users;
> select player, score from users;
```

# 八、WHERE语句

## 知识点

- where语句的使用

使用where语句来设定select,update,delete语句数据抽出的条件。

## 实战演习

```
> select * from users;
> select * from users where score > 20;
> select * from users where score < 30;
> select * from users where score > 20 and score < 30;
> select * from users where team = '勇士';
> select * from users where team != '勇士';
# 抽出以“阿”开头的字段，百分号可以对应多个
> select * from users where player like '阿%';
# 下划线表示只对应一个
> select * from users where player like '阿_';
```

# 九、数据抽出选项

## 知识点

select语句在抽出数据时，可以对语句设置更多的选项，已得到想要的数据。

- order by
- limit
- offset

## 实战演习

```
# 升序
> select * from users order by score asc;

# 降序
> select * from users order by score desc;

> select * from users order by team;

# 先按team，再按score排序
> select * from users order by team, score;
> select * from users order by team, score desc;
> select * from users order by team desc, score desc;

# 通过偏移量来控制分页
> select * from users order by score desc limit 3;
> select * from users order by score desc limit 3 offset 1;
> select * from users order by score desc limit 3 offset 2;
> select * from users order by score desc limit 3 offset 3;
```

# 十、统计抽出数据

## 知识点

- distinct
- sum
- max/min
- group by/having

## 实战演习

```
# 去重
> select distinct team from users;

# 求和
> select sum(score) from users;

> select max(score) from users;
> select min(score) from users;

# 取出当前表得分最大的用户信息
> select * from users where score = (select max(score) from users);
> select * from users where score = (select min(score) from users);

# 按球队分组，然后取出球队和最大得分
> select team, max(score) from users group by team;

> select team, max(score) from users group by team having max(score) >= 25;
> select team, max(score) from users group by team having max(score) >= 25 order by max(score);
```

# 十一、方便的函数

## 知识点

- length
  - 长度
- concat
  - 连接两个字符串
- alias
  - 别名
- substring
  - 切割字符串
- random
  - 返回随机数

参考网站：

https://www.postgresql.org/docs/9.5/static/functions.html

## 实战演习

```
> select player, length(player) from users;
> select player, concat(player, '/', team) from users;
> select player, concat(player, '/', team) as "球员信息" from users;
> select substring(team, 1, 1) as "球队首文字" from users;
> select concat('我', substring(team, 1, 1)) as "球队首文字" from users;
> select random();
> select * from users order by random();
> select * from users order by random() limit 1;
```

# 十二、更新和删除

## 知识点

- update [table] set [field=newvalue,...] where ...
- delete from [table] where ...

## 实战演习

```
> update users set score = 29.1 where player = '阿詹';
> update users set score = score + 1 where team = '勇士';
> update users set score = score + 100 where team IN ('勇士', '骑士');
> delete from users where score > 30;
```

# 十三、变更表结构

## 知识点

- alter table [tablename] ...
- create index ...
- drop index ...

## 实战演习

```
> \d users;
> alter table users add fullname varchar(255);
> \d users;
> alter table users drop fullname;
> \d users;
> alter table users rename player to nba_player;
> \d users;
> alter table users alter nba_player type varchar(100);
> \d users;
> create index nba_player_index on users(nba_player);
> \d users;
> drop index nba_player_index;
> \d users;
```

# 十四、操作多个表

## 知识点

- 表结合查询的基础知识

## 实战演习

### renew.sql

```
create table users (
    id serial primary key,
    player varchar(255) not null,
    score real,
    team varchar(255)
);
insert into users (player, score, team) values
('库里', 28.3, '勇士'),
('哈登', 30.2, '火箭'),
('阿杜', 25.6, '勇士'),
('阿詹', 27.8, '骑士'),
('神龟', 31.3, '雷霆'),
('白边', 19.8, '热火');

create table twitters (
    id serial primary key,
    user_id integer,
    content varchar(255) not null
);
insert into twitters (user_id, content) values
(1, '今天又是大胜,克莱打的真好!'),
(2, '今晚我得了60分,哈哈!'),
(3, '获胜咱不怕,缺谁谁尴尬.'),
(4, '明年我也可能转会西部'),
(5, '我都双20+了，怎么球队就是不胜呢?'),
(1, '明年听说有条大鱼要来,谁呀?');
```

### SQL实行

```
$ dropdb komablog;
$ createdb komablog;
$ psql komablog;
> \i renew.sql
> select * from users;
> select * from twitters;
> select users.player, twitters.content from users, twitters where users.id = twitters.user_id;
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id;
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1;
```

# 十五、使用视图

## 视图概念

视图（View）是从一个或多个表导出的对象。视图与表不同，视图是一个虚表，即视图所对应的数据不进行实际存储，数据库中只存储视图的定义，在对视图的数据进行操作时，系统根据视图的定义去操作与视图相关联的基本表。

## 小马解释

视图就是一个SELECT语句，把业务系统中常用的SELECT语句简化成一个类似于表的对象，便于简单读取和开发。

## 知识点

- 使用数据库视图(view)
- create view ...
- drop view ...

## 实战演习

```
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1;
> create view curry_twitters as select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1;
> \dv
> \d curry_twitters
> select * from curry_twitters;
> drop view curry_twitters;
> \dv
```

## 实战建议

在自己项目中，为了提高数据查询速度，可在表中加入索引index。同时对于经常需要查询的语句，可以提前建立视图view，方便于编码和管理。

# 十六、使用事务

数据库事务(Database Transaction) ，是指作为单个逻辑工作单元执行的一系列操作，要么完全地执行，要么完全地不执行。 事务处理可以确保除非事务性单元内的所有操作都成功完成，否则不会永久更新面向数据的资源。通过将一组相关操作组合为一个要么全部成功要么全部失败的单元，可以简化错误恢复并使应用程序更加可靠。一个逻辑工作单元要成为事务，必须满足所谓的ACID（原子性、一致性、隔离性和持久性）属性。事务是数据库运行中的逻辑工作单位，由DBMS中的事务管理子系统负责事务的处理。

## 知识点

- PostgreSql数据库事务使用
- begin
- commit
- rollback

## 实战演习

```
> select * from users;
> begin;
> update users set score = 50 where player = '库里';
> update users set score = 60 where player = '哈登';
> commit;
> select * from users;
> begin;
> update users set score = 0 where player = '库里';
> update users set score = 0 where player = '哈登';
> rollback;
> select * from users;
```



# 教程来源如下

## 课程文件

https://gitee.com/komavideo/LearnPostgreSql

## 小马视频频道

http://komavideo.com

