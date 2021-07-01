[TOC]

# 文件系统

## 文件系统[¶](#_1)

### Buffer（缓冲区）[¶](#buffer)

#### Buffer介绍[¶](#buffer_1)

Buffer的结构和数组很像，操作的方法和数组类似

数组中不能存储二进制文件，而buffer就是专门存储二进制数据

```
buffer中的每一个元素范围是从00~ff，即0~255，即00000000~11111111

计算机中一个0或者一个1，称之为1位(bit)，8bit = 1byte(字节)

1024byte=1kb,1024byte=1mb,1024mb=1gb,1024gb=1tb

buffer中的一个元素，占用一个字节

buffer的大小，一旦确定，将不会修改

Buffer.from(str) 将一个字符串转换成buffer
Buffer.alloc(size) 创建一个指定大小的buffer
Buffer.allocUnsafe(size) 创建一个指定大小的buffer，但是可能包含敏感数据
buf.toString() 将缓冲区的字符串转换成字符串

作为服务器无非就干两件事，一个是接受用户发过来的请求，二是返回给用户的响应；
    用户发的请求，都是二进制数据；用户发的请求服务器会存储到buffer里面；
    同理，在给用户发送数据的时候，需要先将数据转化成二进制数据，也是存储在buffer里面；
```

使用buffer不需要引入模块，直接使用即可

```
/*
*buffer
* */

var str = "Hello World";
//将一个字符串保存到buffer中
var buf = Buffer.from(str);
//在buffer中存储的都是二进制数据，但是在显示时，是以十六进制显示
console.log(buf)// <Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64>  Unicode编码
console.log(buf.length) // 11 占用内存的大小
console.log(str.length) // 11 字符串的长度
console.log("--------------")

var str2 = "hello 世界";
var buf2 = Buffer.from(str2);
console.log(buf2.length)//12 占用内存的大小
console.log(str2.length)//8 字符串的长度

//创建指定大小的buffer
//var buf3 = new Buffer(10)//10byte
//console.log(buf3.length)//(node:11692) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
//buffer所有的构造函数不推荐使用 Node.js中文网：http://nodejs.cn/api/
//创建一个10字节的buffer
var buf4 = Buffer.alloc(10);
console.log(buf4.length)//10
console.log(buf4)//<Buffer 00 00 00 00 00 00 00 00 00 00>
//通过索引，来给buffer赋值
buf4[0] = 88;
buf4[1] = 255;
buf4[2] = 0xaa;
//buf4[10] =15;//buffer的大小，一旦确定，将不会修改// <Buffer 58 ff aa 00 00 00 00 00 00 00>
buf4[3] = 255;
console.log(buf4);
//只要数字在控制台或者页面中输出，一定是10进制
console.log(buf4[2])//170
console.log(buf4[2].toString(16))//aa

for(var i = 0; i < buf4.length;i++){
    console.log(buf4[i]);//以10进制遍历输出
}
console.log("--------------")
//Buffer.allocUnsafe(size) 创建一个指定大小的buffer，但是buffer中可能含有敏感数据

var buf5 = Buffer.allocUnsafe(10);
console.log(buf5);//分配空间的时间，没有清除内存空间，相对而言性能更好一点，因为只分配空间，不清除数据，但不推荐使用
```

#### Buffer中的其他方法[¶](#buffer_2)

实际 使用时，可参照：[Node.js中文文档](http://nodejs.cn/api/buffer.html)

### 文件系统(Files System)[¶](#files-system)

文件系统，简单来说就是通过Node来操作系统中的文件

使用文件系统，需要先引入fs模块，直接引入不需要下载

```
var fs = require("fs");
手动操作的步骤：
    1.打开文件
        fs.openSync(path,flags[,mode]);
            -path 要打开文件的路径
            -flags 打开文件要操作的类型
                r 只读的
                w 可写的
            -mode 设置文件的操作权限，一般不传
            返回值：该方法会返回一个文件的描述符作为结果，我们可以该描述符来对文件进行各种操作
    2.向文件中写入内容
        fs.writeSync(fd,string[,position[,encoding]]);
            -fd 文件的描述符，需要传递要写入的文件描述符
            -string 要写入的内容
            -position 写入的起始位置
    3.关闭文件并保存
        fs.closeSync(fd)
            -fd 要关闭文件的描述符
// 同步方式
var fs = require("fs");
var fd = fs.openSync("hello.txt1","w");
fs.writeSync(fd,"今天天气真不错呀~~",2);
fs.closeSync(fd);
```