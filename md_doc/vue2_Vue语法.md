[TOC]

# 01.vue语法基础

### Vue初体验[¶](#vue)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="app">
    <h1>{{message}}</h1>
    <h2>{{name}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello',
            name: 'world'
        }
    })
</script>
</body>
</html>
```

### vue列表的展示[¶](#vue_1)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="app">
    <ul>
        <li v-for="item in movies">{{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: '你好啊',
            movies: ['aaaa','bbbb','cccc','dddd']
        }
    })
</script>
</body>
</html>
```

### 计数器[¶](#_1)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="app">
    <h2>当前计数: {{counter}}</h2>
    <button v-on:click="add">+</button>
    //简写
    <button @click="sub">-</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            counter: 0
        },
        methods:{
            add(){
                this.counter++
            },
            sub(){
                this.counter--
            }
        }
    })
</script>
</body>
</html>
```

### mvvm[¶](#mvvm)

### options选项[¶](#options)

- el:
- data:
- method:
- 生命周期函数:

### vue生命周期[¶](#vue_2)

### vue的生命周期函数有哪些[¶](#vue_3)

### 定义vue的template[¶](#vuetemplate)

### mustache语法[¶](#mustache)

### 其他指令使用[¶](#_2)

v-html

v-text

v-pre

v-cloak

### v-bind的基本使用[¶](#v-bind)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="app">
    <img v-bind:src="imgURL" alt="">
<!--    简写-->
    <a :href="hrefURL">百度一下</a>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            imgURL: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/cb8859c31e431fe84c8977705d1bd442.jpg?w=2452&h=920',
            hrefURL: 'https://www.baidu.com'
        }
    })
</script>
</body>
</html>
```

### v-bind动态绑定class（对象语法）[¶](#v-bindclass)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color: red;
        }
    </style>
</head>
<body>

<div id="app">
    <h2 v-bind:class="{active: isActive, line: isLine}">{{message}}</h2>
    <button v-on:click="btnClick">按钮</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isActive: true,
            isLine: true
        },
        methods:{
            btnClick: function () {
                this.isActive = !this.isActive
            }
        }
    })
</script>

</body>
</html>
```

### v-bind动态绑定class（数组语法）[¶](#v-bindclass_1)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color: red;
        }
    </style>
</head>
<body>

<div id="app">
    <h2 v-bind:class="getClass()">{{message}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            active: 'aaa',
            line: 'bbb'
        },
        methods:{
            getClass: function () {
                return [this.active,this.line]
            }
        }
    })
</script>

</body>
</html>
```

### v-on和v-for练习[¶](#v-onv-for)

### v-bind动态绑定style（对象语法）[¶](#v-bindstyle)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color: red;
        }
    </style>
</head>
<body>

<div id="app">
    <h2 v-bind:style="getStyle()">{{message}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            finalColor: 'red',
            finalSize: '100px'
        },
        methods: {
            getStyle: function () {
                return {color : this.finalColor, fontSize : this.finalSize}
            }
        }
    })
</script>

</body>
</html>
```

### v-bind动态绑定style（数组语法）[¶](#v-bindstyle_1)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <h2 v-bind:style="[baseStyle,baseStyle1]">{{message}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            baseStyle: {backgroundColor:'red'},
            baseStyle1: {fontSize:"30px"}
        }
    })
</script>
</body>
</html>
```

### 计算属性的基本使用[¶](#_3)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <h2>{{firstName + ' ' + lastName}}</h2>
    <h2>{{firstName}} {{lastName}}</h2>
    <h2>{{getFullName()}}</h2>
    <h2>{{FullName}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            firstName: 'John',
            lastName: 'Cena'
        },
        methods:{
            getFullName(){
                return this.firstName + ' ' + this.lastName
            }
        },
        computed:{
            FullName:function () {
                return this.firstName + ' ' + this.lastName
            }
        }
    })
</script>
</body>
</html>
```

### 计算属性的复杂操作[¶](#_4)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active {
            color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>总价格是：{{totalPrice}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            books: [
                {id: 100, name: 'Unix编程艺术', price: 119},
                {id: 110, name: '代码大全', price: 105},
                {id: 120, name: '深入理解计算机系统', price: 98},
                {id: 130, name: '现代操作系统', price: 100}
            ]
        },
        computed: {
            totalPrice: function () {
                let result = 0
                for (let i = 0; i < this.books.length; i++) {
                    result += this.books[i].price
                }
                return result

            }
        }

    })
</script>
</body>
</html>
```

### 计算属性setter和setter[¶](#settersetter)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active {
            color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>{{fullName}}</h2>
    <h2>{{fullName2}}</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            firstName: 'John',
            lastName: 'Cena'
        },
        computed: {
          fullName: {
              set: function (newValue) {
                const names = newValue.split(' ')
                this.firstName = names[0]
                this.lastName = names[1]
              },
              get: function () {
                return this.firstName + ' ' + this.lastName
               }
          },
          //简写
          fullName2:function () {
              return this.firstName + ' ' + this.lastName
          }
        }
    })
</script>

</body>
</html>
```

### 计算属性和methods的对比[¶](#methods)

computed只会调用一次

### 块级作用域[¶](#_5)

块级作用域 JS中使用var来声明一个对象时，变量的作用域主要是和函数的定义有关

针对于其他块定义来说，是没有作用域的，比如if/for等，这在开发中往往会引起一些问题

```
// if 和 for 里面没有块级作用域
var btns = document.getElementsByTagName("button")
for (var i = 0;i < btns.length;i++){
    btns[i].addEventListener('click',function () {
        console.log('第'+i+'个按钮被点击')//第4个按钮被点击
    })
}
```

使用闭包，因为函数是一个作用域

```
// if 和 for 里面没有块级作用域
var btns = document.getElementsByTagName("button")
for (var i = 0;i < btns.length;i++){
    (function (i) {
        btns[i].addEventListener('click',function () {
            console.log('第'+i+'个按钮被点击')//第4个按钮被点击
        })
    })(i)
}
```

ES6中的写法

```
const btns = document.getElementsByTagName("button")
for (let i = 0;i < btns.length;i++){
        btns[i].addEventListener('click',function () {
            console.log('第'+i+'个按钮被点击')
        })
}
```

### const的使用和注意点[¶](#const)

在es6的开发中，优先使用const

一旦给const修饰的标识符被赋值后，不能修改

```
const name = 'xiaoming'
name = 'abc'
console.log(name)
```

在使用const定义标识符，必须进行赋值

```
const name;
```

const指向对象时不能修改，但是可以改变对象内部的属性

```
const obj = {
    name: 'xiaoing',
    age: 10,
    height: 1.88
}
obj.name = 'xiaohong'
obj.age = 11
obj.height = 1.89

console.log(obj);//{ name: 'xiaohong', age: 11, height: 1.89 }
```

### ES6对象字面量增强写法[¶](#es6)

属性的增强写法

```
const name = "xiaoming"
const age = 18
const height = 1.88
//es5的写法
const obj = {
    name: name,
    age: age,
    height: height
}

console.log(obj);//{ name: 'xiaoming', age: 18, height: 1.88 }

//es6的写法，属性增强写法
const obj2 = {
    name,
    age,
    height
}
console.log(obj2);//{ name: 'xiaoming', age: 18, height: 1.88 }
```

函数属性的增强写法

```
//es5的写法
const obj = {
    eat: function () {
        console.log('eat1')
    }
}
obj.eat()//eat1


//es6写法
const obj2 = {
    eat() {
        console.log('eat2');
    }
}
obj2.eat()//eat2
```

### v-on的基本使用和语法糖[¶](#v-on)

在前端开发中，我们经常需要和用户交互

这个时候就必须监听用户发生的事件，比如点击、拖拽等

在Vue中如何使用事件监听呢？ v-on指令，缩写 @

可以将事件指向一个在methods中的函数

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active {
            color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <h2>{{counter}}</h2>
    <button @click="increament">+</button>
    <button @click="decrement">-</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            counter: 0
        },
        methods: {
            increament () {
                return this.counter++
            },
            decrement () {
                return this.counter--
            }
        }
    })
</script>


<script src="js/vue.js"></script>
</body>
</html>
```

### v-on的参数传递[¶](#v-on_1)

当通过methods中定义方法，以供@click调用时，需要注意参数问题

1.如果该方法不需要额外参数，那么方法后的()可以不添加。但是需要注意：如果方法本身有一个参数，那么会默认将原生事件event参数传递进去。

2.如果需要同时传入某个参数，同时需要event时，可以通过$event传入事件。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
<!--    事件调用的方法中没有参数-->
    <button @click="btnClick1()">btn0</button>
<!--    省略括号-->
    <button @click="btnClick1">btn1</button>
    <br/>
<!--    正常传参输出-->
    <button @click="btnClick2(123)">btn2</button>
<!--    需要传入一个参数，此时省略了括号，但是方法本身是需要传入一个参数的，此时，vue会默认将浏览器产生的event事件对象传入到方法中-->
    <button @click="btnClick2">btn3</button>
<!--    此时输出打印的是一个MouseEvent对象-->
<!--    如果加了括号，但是没有传递参数，则会返回undefined-->
    <button @click="btnClick2()">btn4</button>
<br/>
<!--    定义方法时，我们需要event对象，同时又需要其他参数的时候，应该这样写-->
<!--    在调用方法时，如何手动的获取到浏览器参数的event对象呢   $event-->
    <button @click="btnClick3(123, $event)">btn5</button>
    <button>btn6</button>
    <button>btn5</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
        },
        methods : {
            btnClick1 () {
                console.log('我没有参数');
            },
            btnClick2 (event) {//有单个参数时，一般取名为event
                console.log(event)
            },
            btnClick3 (abc, event){
                console.log(abc, event)//没有加$之前，此时默认的将event对象传入第一个形参
            }
        }
    })
</script>


<script src="js/vue.js"></script>
</body>
</html>
```

拓展：如果函数需要参数，但是没有传入，那么函数的形参为undefined

```
function test (aa) {
    console.log(aa);
}
test()//undefined
```

### v-on修饰符的使用[¶](#v-on_2)

vue提供了修饰符来帮助我们方便的处理一些事情：

- .stop 调用event.stopPropagation()
- .prevent 调用event.preventDefault()
- .{keyCode | keyAlias} 只当事件是从特定键触发时才触发回调
- .native 监听组件根元素的原生事件
- .once 只触发一次回调

.stop修饰符的使用

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <div @click = "divClick">
        aaaaa
        <button @click.stop="btnClick">click</button>
    </div>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
        },
        methods:{
            divClick () {
                console.log("divClick");
            },
            btnClick () {
                console.log("btnClick");
            }
        }
    })
</script>


<script src="js/vue.js"></script>
</body>
</html>
```

.prevent修饰符的使用

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <form action="baidu">
<!--        此时点击提交，将会阻止页面的默认提交动作，进行打印-->
        <input type="submit" value="提交" @click.prevent = subClick>
    </form>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
        },
        methods:{
            subClick () {
                console.log('subClick');
            }
        }
    })
</script>

<script src="js/vue.js"></script>
</body>
</html>
```

监听键盘的点击 @keyup @enter @keydown

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <input type="text" @keyup="keyUp">
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
        },
        methods : {
            keyUp () {
                console.log('keyUp')
            }
        }
    })
</script>
<script src="js/vue.js"></script>
</body>
</html>
```

.once 修饰符的使用

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
<!--    只会输出打印一次-->
    <button @click.once = "btnOnce">提交</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
        },
        methods : {
            btnOnce () {
                console.log('btnOnce')
            }
        }
    })
</script>
<script src="js/vue.js"></script>
</body>
</html>
```

### v-if[¶](#v-if)

v-if 如果是false，最后渲染是通过注释代码来隐藏的

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <div v-if="show()">
        {{message}}
    </div>
    <div v-if="isShow">
        {{message}}
    </div>
</div>

<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isShow : false
        },
        methods : {
            show () {
                return false
            }
        }
    })
</script>
</body>
</html>
```

v-else

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js"></script>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <div v-if="isShow">
        {{message}}
    </div>
    <div v-else>
        v-else显示我
    </div>
</div>

<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isShow : false//如果用methods的函数来传参的话，v-else则不会生效
        }
    })
</script>
</body>
</html>
```

v-else-if的使用

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <h2 v-if="score >=90">优秀</h2>
    <h2 v-else-if="score >= 80">良好</h2>
    <h2 v-else-if="60">及格</h2>
    <h2 v-else>不及格</h2>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            score : 88,
        }
    })
</script>
</body>
</html>
```

上述情况，一般推荐使用computed

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    {{result}}
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            score: 80
        },
        computed: {
            result() {
                let showMessage = ""
                if (this.score >= 90) {
                    showMessage = "优秀"
                } else if (this.score >= 80) {
                    showMessage = "良好"
                } else if (this.score >= 60) {
                    showMessage = "及格"
                } else {
                    showMessage = "不及格"
                }
                return showMessage
            }
        }
    })
</script>
</body>
</html>
```

### 登陆切换的小案例[¶](#_6)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>

    <span v-if="isUser">
        <label for="username">用户账号</label>
        <input type="text" id="username" placeholder="用户账号">
    </span>
    <span v-else>
        <label for="email">用户邮箱</label>
        <input type="text" id="email" placeholder="用户邮箱">
    </span>
    <button @click="isUser = !isUser">切换</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isUser: true,
        }
    })
</script>
</body>
</html>
```

### 登陆切换的input复用问题[¶](#input)

需要给不同的input指定不同的key，告诉vue不需要复用input

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>

    <span v-if="isUser">
        <label for="username">用户账号</label>
        <input type="text" id="username" placeholder="用户账号" key = "username">
    </span>
    <span v-else>
        <label for="email">用户邮箱</label>
        <input type="text" id="email" placeholder="用户邮箱" key = "email">
    </span>
    <button @click="isUser = !isUser">切换</button>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isUser: true,
        }
    })
</script>
</body>
</html>
```

### v-show的使用以及和v-if的区别[¶](#v-showv-if)

v-if：当条件为false时，包含v-if指令的元素，根本就不会存在于dom中（被注释了）

v-show：当条件为false时，v-show只是给我们元素添加一个行内样式：display:none

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <div v-show="!isShow">{{message}}</div>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            isShow : true
        }
    })
</script>
</body>
</html>
```

开发中如何选择呢？

当需要显示和隐藏之间切换很频繁时，用v-show；次数很少时，用v-if

### v-for遍历数组和对象[¶](#v-for)

1.在遍历的过程中，没有使用索引值

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
        <li v-for="item in names">{{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            names : ['1','2','3','4']
        }
    })
</script>
</body>
</html>
```

2.在遍历过程中，使用索引值

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
        <li v-for="(item,index) in names">{{index + 1}}.{{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            names : ['1','2','3','4']
        }
    })
</script>
</body>
</html>
```

3.在遍历对象的过程中，如果只是获取一个值，那么获取的是value

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
        <li v-for="item in person">{{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            person : {
                name : 'xiaoming',
                age : 18,
                height : 1.8
            }
        }
    })
</script>
</body>
</html>
```

4.获取key和value的语法

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
<!--        <li v-for="item in person">{{item}}</li>-->
        <li v-for="(key, value) in person">{{key}} - {{value}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            person : {
                name : 'xiaoming',
                age : 18,
                height : 1.88
            }
        }
    })
</script>
</body>
</html>
```

### v-for绑定和非绑定的区别[¶](#v-for_1)

在使用v-for的时候，最好给对应的元素或者组件添加一个:key属性

为什么需要？

这个和vue的虚拟dom的diff算法有关系

我们需要使用key来给每个节点做一个唯一标识，diff算法就可以正确识别此节点，就可以找到正确的位置区插入新的节点

总结：key的作用主要是为了高效的更新虚拟dom

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
        <li v-for="item in letters" :key="item">{{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            letters : ['a','b','c','d','e']
        }
    })
</script>
</body>
</html>
```

### 数组中哪些方法是响应式的[¶](#_7)

push()

pop() 删除数组中的最后一个元素

shift() 删除数组中的第一个元素

unshift() 在数组最前面添加元素

splice()

sort()

reverse()

### 购物车作业的回顾和实现[¶](#_8)

v-for中，点击切换颜色

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .active{
            color :red;
        }
    </style>

</head>
<body>
<div id="app">
    <h2>{{message}}</h2>
    <ul>
        <li v-for="(item,index) in books" :class="{active: currentIndex === index}" @click = liClick(index)>{{index + 1}} - {{item}}</li>
    </ul>
</div>

<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        //用于挂载需要管理的元素
        el: '#app',
        //定义数据
        data: {
            message: 'hello world',
            books :['人民的名义','论持久战','天上最亮的星星','黑洞','Java语言精粹'],
            active : "active",
            currentIndex : 0
        },
        methods : {
            liClick (index) {
                this.currentIndex = index//不能写成this.index ，这个的值是undefined
            }
        }
    })
</script>
</body>
</html>
```

- 购物车案例-界面搭建
- 过滤器的使用
- 购物车案例-改变购买数量
- 高阶函数

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        [v-cloak] {
            display: none !important;
        }

        table{
            border: 1px solid #e9e9e9;
            border-spacing: 0;
            border-collapse: collapse;
        }

        th, td{
            border: 1px solid #e9e9e9;
            padding: 8px 16px;
            text-align: center;
        }
        th{
            font-weight: 600;
            background-color: grey;
            color: white;
        }
    </style>

</head>
<body>
    <div id="app" v-cloak>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th>名称</th>
                    <th>发布时间</th>
                    <th>价格</th>
                    <th>数量</th>
                    <th>操作</th>
                </tr>

            </thead>
            <tbody>
                <tr v-for="(item,index) in books">
                    <td>{{item.id}}</td>
                    <td>{{item.name}}</td>
                    <td>{{item.publishTime}}</td>
                    <td>{{item.price | getPrice}}</td>
                    <td>
                        <button @click="decre(idnex)" :disabled="item.count <= 1">-</button>
                        {{item.count}}
                        <button @click="incre(index)">+</button>
                    </td>
                    <td>
                        <button @click="rmData(index)">移除</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <h2>总价格：{{totalPrice | getPrice}}</h2>
    </div>
    <script src="js/vue.js"></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                books: [
                    {id:1,name:'aa',publishTime:'1990-01',price:40,count:1},
                    {id:1,name:'bb',publishTime:'1990-01',price:40,count:1},
                    {id:1,name:'cc',publishTime:'1990-01',price:40,count:1},
                    {id:1,name:'dd',publishTime:'1990-01',price:40,count:1},
                ]
            },
            filters : {
                getPrice(price) {
                    return "￥" + price.toFixed(2)
                }
            },
            computed: {
                totalPrice() {
                    return this.books.reduce(function (preValue, book) {
                        return preValue + book.count * book.price
                    },0)
                }
            },
            methods: {
                decre(index) {
                    this.books[index].count--
                },
                incre(index) {
                    this.books[index].count++
                },
                rmData(index) {
                    this.books.splice(index,1)
                }
            }
        })
    </script>
</body>
</html>
```

### v-model[¶](#v-model)

- 使用及原理
- 结合radio使用
- 结合checkbox类型
- 结合select类型
- input中值的绑定
- v-model修饰符

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<div id="app">
    使用及原理
    <input type="text" v-model="message">
    <h2>{{message}}</h2>
    <input type="text" :value="message" @input="message = $event.target.value">

    结合radio使用
    <label for="">
        <input type="radio" name="sex" id="male" value="男" v-model="sex">男
    </label>
    <label for="">
        <input type="radio" name="sex" id="female" value="女" v-model="sex">女
    </label>
    <h2>您选择的性别是{{sex}}</h2>

    结合checkbox类型
    <label for="">
        <input type="checkbox" v-model="fruits" value="苹果">苹果
        <input type="checkbox" v-model="fruits" value="香蕉">香蕉
        <input type="checkbox" v-model="fruits" value="梨子">梨子
    </label>
    <h2>您选择的水果是{{fruits}}</h2>

    结合select类型
    <label for="">
        <select name="" id="" v-model="fruits2" multiple>
            <option value="苹果">苹果</option>
            <option value="香蕉">香蕉</option>
            <option value="梨子">梨子</option>
        </select>
    </label>
    <h2>您选择的水果是{{fruits2}}</h2>

    input中值的绑定
    <label v-for="item in sports">
        <input type="checkbox" :value="item" name="sex" v-model="sport">{{item}}
    </label>

    <h2>您选择的是{{sport}}</h2>

    v-model修饰符

    懒加载
    <input type="text" v-model.lazy="test">
    {{test}}
    限制输入类型
    <input type="text" v-model.number="test1">
    {{test1}}
    去除空行
    <input type="text" v-model.trim="test2">
    {{test2}}
</div>
<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data : {
            message: 'helloworld',
            sex:'男',
            fruits:[],
            fruits2:[],
            sports: ['篮球','羽毛球','乒乓球'],
            sport:[],
            test:'',
            test1: 0,
            test2:'',
        }
    })
</script>
</body>
</html>
```

### 组件化[¶](#_9)

#### 组件化的实现和使用步骤[¶](#_10)

#### 组件化的基本使用过程[¶](#_11)

#### 全局组件和局部组件[¶](#_12)

#### 父组件和子组件的区分[¶](#_13)

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="app">
        <mycpn2></mycpn2>
    </div>

    <script src="../js/vue.js"></script>
    <script>
        const cpnC1 = Vue.extend({
            template:`
                <div>
                    <h2>cpnC1</h2>
                </div>
            `
        })

        const cpnC2 = Vue.extend({
            template:`
                <div>
                    <h2>cpnC2</h2>
                    <mycpn1></mycpn1>
                </div>

            `,
            components:{
                mycpn1: cpnC1
            }
        })


        const app = new Vue({
            el:"#app",
            data:{

            },
            components: {
                mycpn2: cpnC2
            }
        })
    </script>
</body>
</html>
```

#### 注册组件的语法糖写法[¶](#_14)

#### 组件模板抽离的写法[¶](#_15)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <cpn></cpn>
</div>
<!--第一种写法-->
<script type="text/x-template" id="cpn">
    <div>
        <h2>
            hello world
            hello world
        </h2>
    </div>
</script>

<!--第二种写法-->
<template id="cpn2">
    <div>
        <h2>
            hello world2
            hello world2
        </h2>
    </div>
</template>

<script src="../js/vue.js"></script>
<script>
    Vue.component('cpn',{
        template: '#cpn2'
    })

    const app = new Vue({
        el:"#app"
    })
</script>
</body>
</html>
```

#### 为什么组件data必须是函数[¶](#data)

组件中不可以直接访问Vue示例中data里面的数据，而且即使可以访问，也不应该将所有数据放在Vue示例中，否则会非常臃肿。

组件自己的数据存放在哪里呢？

```
组件对象也有一个data属性（也可以有methods等属性）
只是这个data属性必须是一个函数
而且这个函数返回一个对象，对象内部保存着数据
```

如果直接返回一个对象，则会出现不同的组件实例，指向相同的问题

#### 父子组件通信-父传子props[¶](#-props)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <cpn></cpn>
    <cpn :cmovies="movies" :cmessage="message"></cpn>
</div>
<template id="cpn">
<div>
    <ul v-for="item in cmovies">
        <li>{{item}}</li>
    </ul>
    <h2>{{cmessage}}</h2>
</div>
</template>

<script src="../js/vue.js"></script>
<script>
    const cpn = {
        template:'#cpn',
        // props:['cmovies','cmessage']
        props:{
            cmovies:{
                type:Array,
                required: false,
                default() {
                    return []
                }
            },
            cmessage:{
                type:String,
                default:'isDefault'
            }
        }
    }

    const app = new Vue({
        el: "#app",
        data:{
            movies:['aa','bb','cc'],
            message:'hello world'
        },
        components:{
            cpn//这里用到了对象字面量的增强写法，以及注册子组件的语法糖
        }
    })
</script>
</body>
</html>
```

#### 父子组件通信-props驼峰标识[¶](#-props_1)

在props中变量名如果是驼峰的话，在使用的时候,html中要用“-”连接，并转为小写

#### 父子组件通信-子传父（自定义事件）[¶](#-)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="app">
    <cpn @item-click="cpnClick"></cpn>
<!--    这里没有浏览器产生的事件对象的，所以没有传参的话，会自动将item传进去-->
</div>
<template id="cpn">
    <div>
        <button v-for="item in categories"
                @click="btnClick(item)">
            {{item.name}}</button>
    </div>
</template>

<script src="../js/vue.js"></script>
<script>
    const cpn = {
        template:'#cpn',
        data() {
            return {
                categories : [
                    {id :1,name:'aa'},
                    {id :2,name:'bb'}
                ]
            }
        },
        methods:{
            btnClick(item) {
                //发射事件
                this.$emit('item-click',item)
            }
        }
    }

    const app = new Vue({
        el: "#app",
        components:{
            cpn
        },
        methods: {
            cpnClick(item){
                console.log('cpnClick',item)
            }
        }
    })
</script>
</body>
</html>
```

#### 父子组件通信-结合双向绑定[¶](#-_1)

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<div id="app">
<cpn  :number1="num1" :number2="num2"  @input1emit="input1receive" @input2emit="input2receive"></cpn>
</div>
<template id="cpn">
    <div>
        <h2>props:{{number1}}</h2>
        <h2>data:{{dnumber1}}</h2>
        <input type="text" :value="dnumber1"  @input="input1change">

        <h2>props:{{number2}}</h2>
        <h2>data:{{dnumber2}}</h2>
        <input type="text" :value="dnumber2" @input="input2change">
    </div>
</template>
<script src="js/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            num1: 1,
            num2: 0
        },
        methods: {
          input1receive(value) {
              this.num1 = parseFloat(value)
          },
          input2receive(value){
              this.num2 = parseFloat(value)
          }
        },
        components: {
            cpn : {
                template: "#cpn",
                props: {
                    number1: {
                        type: Number
                    },
                    number2: {
                        type: Number
                    }
                },
                data() {
                    return {
                        dnumber1: this.number1,
                        dnumber2: this.number2
                    }
                },
                methods: {
                    input1change(event) {
                        this.dnumber1 = event.target.value
                        this.$emit('input1emit', this.dnumber1)
                        this.dnumber2 = this.dnumber1 * 100
                        this.$emit('input2emit', this.dnumber2)
                    },
                    input2change(event) {
                        this.dnumber2 = event.target.value
                        this.$emit('input2emit', this.dnumber2)
                        this.dnumber1 = this.dnumber2 / 100
                        this.$emit('input1emit', this.dnumber1)
                    }
                }
            }
        }
    })
</script>
</body>
</html>
```

#### 父子间通信-watch[¶](#-watch)

#### 父访问子-children-refs[¶](#-children-refs)

#### 子访问父-parent-root[¶](#-parent-root)

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<div id="app">
<cpn1></cpn1>
</div>

<template id="cpn1">
    <div>
        <h2>我是cpn1组件</h2>
        <cpn2></cpn2>
    </div>
</template>

<template id="cpn2">
    <div>
        <h2>我是cpn2组件</h2>
        <button @click="btnClick">click me</button>
    </div>
</template>
<script src="../js/vue.js"></script>
<script>
    const app = new Vue({
        el: "#app",
        data: {
            message: "hello world"
        },
        components: {
            cpn1: {
                template: "#cpn1",
                data() {
                    return {
                        name: {
                            type: String,
                            default: '我是name'
                        }
                    }
                },
                components: {
                    cpn2: {
                        template: "#cpn2",
                        methods: {
                            btnClick() {
                                console.log(this.$parent)
                                console.log(this.$parent.name.default)
                                console.log(this.$root)
                            }
                        }
                    }
                }
            }
        }
    })
</script>
</body>
</html>
```

#### slot插槽的基本使用[¶](#slot)

#### 具名插槽[¶](#_16)

#### 编译作用域[¶](#_17)

#### 作用域插槽的使用[¶](#_18)

父组件替换插槽的标签，但是内容由子组件提供

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="app">
        <h2>{{message}}</h2>
        <cpn1></cpn1>
        <cpn1>
            <template slot-scope="slot">
                <span>{{slot.data.join(' - ')}}</span>
            </template>
        </cpn1>
    </div>
    <template id="cpn1">
        <div>
            <slot :data="Language">
                <ul>
                    <li v-for="item in Language">{{item}}</li>
                </ul>
            </slot>
        </div>
    </template>
    <script src="js/vue.js"></script>
    <script>
        const app = new Vue({
            //用于挂载需要管理的元素
            el: '#app',
            //定义数据
            data: {
                message: 'hello world',
            },
            components: {
                cpn1: {
                    template: "#cpn1",
                    data() {
                        return {
                            Language: ['c','c++','java']
                        }
                    }
                }
            }
        })
    </script>
</body>
</html>
```