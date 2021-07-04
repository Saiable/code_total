## 前置知识

### JavaScript this 关键字

参考：https://www.runoob.com/js/js-this.html

面向对象语言中 this 表示当前对象的一个引用。

但在 JavaScript 中 this 不是固定不变的，它会随着执行环境的改变而改变。

- 在方法中，this 表示该方法所属的对象。
- 如果单独使用，this 表示全局对象。
- 在函数中，this 表示全局对象。
- 在函数中，在严格模式下，this 是未定义的(undefined)。
- 在事件中，this 表示接收事件的元素。
- 类似 call() 和 apply() 方法可以将 this 引用到任何对象。

#### 方法中的 this

在对象方法中， this 指向调用它所在方法的对象。

在上面一个实例中，this 表示 person 对象。

fullName 方法所属的对象就是 person。

#### 单独使用 this

单独使用 this，则它指向全局(Global)对象。

在浏览器中，window 就是该全局对象为 [**object Window**]

#### 函数中使用 this（默认）

在函数中，函数的所属者默认绑定到 this 上。

在浏览器中，window 就是该全局对象为 [**object Window**]:

```javascript
function myFunction() {
  return this;
}
```

#### 事件中的 this

在 HTML 事件句柄中，this 指向了接收事件的 HTML 元素：

```javascript
<button onclick="this.style.display='none'">
点我后我就消失了
</button>
```

#### 对象方法中绑定

下面实例中，this 是 person 对象，person 对象是函数的所有者：

```javascript
var person = {
  firstName  : "John",
  lastName   : "Doe",
  id         : 5566,
  myFunction : function() {
    return this;
  }
};
```

#### 显式函数绑定

在 JavaScript 中函数也是对象，对象则有方法，**apply** 和 **call** 就是函数对象的方法。这两个方法异常强大，他们允许切换函数执行的上下文环境（context），即 this 绑定的对象。

在下面实例中，当我们使用 person2 作为参数来调用 person1.fullName 方法时, **this** 将指向 person2, 即便它是 person1 的方法：

```javascript
var person1 = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
var person2 = {
  firstName:"John",
  lastName: "Doe",
}
person1.fullName.call(person2);  // 返回 "John Doe"
```

### JavaScript 中 call()、apply()、bind() 的用法

```javascript
var name='小王',age=17
var obj={
    name:'小张',
    objAge:this.age,
    myFun:function() {
        console.log(this.name+"年龄"+this.age)//小张年龄undefined
        console.log(this)//{name: "小张", objAge: 17, myFun: ƒ}
    }
}
console.log(obj.objAge) //17
obj.myFun()
```

```javascript
var fav='盲僧'
function show() {
    console.log(this.fav)//盲僧
}
```

比较一下这两者 this 的差别，第一个打印里面的 this 指向 obj，第二个全局声明的 shows() 函数 this 是 window ；

#### call()、apply()、bind() 都是用来重定义 this 这个对象的！

```javascript
var name='小王',age=17
var obj={
    name:'小张',
    objAge:this.age,
    myFun:function() {
        console.log(this.name+"年龄"+this.age)
        // console.log(this)
    }
}
var db = {
    name:'德玛',
    age:99
}

obj.myFun()//小张年龄undefined
obj.myFun.call(db)//德玛年龄99
obj.myFun.apply(db)//德玛年龄99
obj.myFun.bind(db)()//德玛年龄99
```

以上出了 bind 方法后面多了个 () 外 ，结果返回都一致！

由此得出结论，bind 返回的是一个新的函数，你必须调用它才会被执行。

### JavaScript constructor 属性