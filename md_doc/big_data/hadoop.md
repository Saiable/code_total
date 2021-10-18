



[TOC]

教程来源：https://www.bilibili.com/video/BV1Qp4y1n7EN?p=1

# 第1章、入门

## 1.1.Hadoop是什么

## 1.2.Hadoop发展历史

## 1.3.Hadoop三大发行版本

## 1.4.Hadoop优势

## 1.5.Hadoop组成

### 1.5.1.HDFS概述

### 1.5.2.Yarn架构概述

### 1.5.3.MapReduce架构概述

## 1.6.大数据技术生态体系

## 1.7.推荐系统架构图

# 第2章 Hadoop运行环境搭建（开发重点）

## 2.1.模板虚拟机环境准备

### 2.1.1.安装模板虚拟机

|       IP       | 主机名称  | 内存 | 硬盘 |
| :------------: | :-------: | :--: | :--: |
| 192.168.10.100 | hadoop100 |  4G  | 50G  |

### 2.1.2.VMware

虚拟机 VMware Workstation Pro 15.5.0 及永久激活密钥：https://www.cnblogs.com/zero-vic/p/11584437.html

------

15 虚拟机下载地址：https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.5.0-14665864.exe

16虚拟机下载地址：http://download3.vmware.com/software/wkst/file/VMware-workstation-full-16.1.0-17198959.exe

------

激活密钥许可证VMware Workstation Pro 15 
激活许可证
UY758-0RXEQ-M81WP-8ZM7Z-Y3HDA
VF750-4MX5Q-488DQ-9WZE9-ZY2D6
UU54R-FVD91-488PP-7NNGC-ZFAX6
YC74H-FGF92-081VZ-R5QNG-P6RY4
YC34H-6WWDK-085MQ-JYPNX-NZRA2

激活密钥许可证VMware Workstation Pro 16
激活许可证
ZF3R0-FHED2-M80TY-8QYGC-NPKYF

#### 2.1.2.1.版本

以下是VMware WorkStation Pro 15.5的安装步骤

- 模拟准备物理硬件

![在这里插入图片描述](https://img-blog.csdnimg.cn/7d85d432db81441f9fa84f918b8462cd.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/4cf8b30e0f2a465d99a354f2965b1bf5.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/354790178bbd4dd58ae6e6df147793ff.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/3f1fd0d950184a718e343601196e9a4c.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/b8bd590cefce4d6781f290710b930e37.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/432c2e10017540ca9f31183ded55e14e.png)

这里需要查看下自己的cpu核数，我这里是16核的，后面要新建4台左右的虚拟机，每台处理器的内核总数为，16/4

![在这里插入图片描述](https://img-blog.csdnimg.cn/23379a60450a46a48b744261ca412ad6.png)

![image-20211019065226809](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211019065226809.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/c767324fab17405abebf3be1f33baecb.png)

接下来两步，都是默认下一步

![在这里插入图片描述](https://img-blog.csdnimg.cn/5b5e4566f8c94befab7468aae983689f.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/5577ab8a706941739a5c1f6bbdf8b0e3.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/c1f74d7f25f84e05b90b8a559b8852f8.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/3fc1e57213a74023a50c257e60f0070a.png)

如果虚拟化没有开启，报的是以下错误

![在这里插入图片描述](https://img-blog.csdnimg.cn/84dd88112ccc4c29a0e7fdd92ebc9f9d.png)

Win10直接可以在任务管理器中的【性能】面看查看，Win7则需要进入bios中查看



### 2.1.3.CentOS

系统的安装得分两步，第一步得配置一台电脑，选CPU、内存、磁盘、网卡等硬件

第二步才是安装系统

### 2.1.4.远程终端工具安装



## 2.2.克隆虚拟机



## 2.3.在hadoop102安装JDK



## 2.4.在hadoop102安装Hadoop



## 2.5.Hadoop目录结构

# 第三章、MapReduce



# 第四章、Hadoop源码解析



# 第五章、生产调优手册



# 第六章、Yarn

