[TOC]

# 04.vue-router基础

#### 箭头函数的使用和this指向[¶](#this)

#### 什么是路由和其中映射[¶](#_1)

路由，就是通过互联的网络把信息从源地址传输到目的地址的活动

路由器提供了两种机制：路由和传送 - 路由是决定数据包从来源到目的地的路径 - 转送将输入端数据转移到合适的输出端

路由中有一个非常重要的概念叫路由表 - 路由表的本质上就是一个映射表，决定了数据包的指向

内容概述 - 认识路由 - vue-router基本使用 - vue-router嵌套路由 - vue-router参数传递 - vue-router导航守卫 - keep-alive

创建vue-cli2项目来演示 选择安装vue-router

#### 前端渲染、后端渲染和前端路由、后端路由[¶](#_2)

后端渲染 - jsp:java server page

##### 后端路由[¶](#_3)

- 后端处理url和页面之间的映射关系

早期的网站开发整个HTML页面是由服务器来渲染的 - 服务器直接生产渲染好对应的HTML页面，返回给客户端进行展示

但是，一个网站，这么多页面服务器如何处理呢？ - 一个页面有自己对应的网址，也就是URL - URL会发送到服务器，服务器会通过正则对该URL进行匹配，并且最后交给一个Controller进行处理 - Controller进行各种处理，最终生成HTML或者数据，返回给前端 - 这就完成了一个IO操作

上面的这种操作，就是后端路由 - 当我们页面中需要请求不同的路径内容时，交给服务器来进行吹了，服务器渲染好整个页面，并且将页面返回给客户端。 - 这种情况下渲染好的页面，不需要单独加载任何的js和css，可以直接交个浏览器展示，这样也利于seo优化。

后端路由的缺点 - 一种情况是整个页面的模板有后端人员来编写和维护的。 - 另一种情况是前端开发人员如果要开发页面，需要通过PHP和Java等语言来编写页面代码。 - 而且通常情况下HTML代码和数据以及对应的逻辑会混在一起，编写和维护都是非常糟糕的事情

##### 前后端分离[¶](#_4)

后端只负责提供数据，不负责任何借阶段的内容

前端渲染 - 在地址栏输入的地址，先是通过ajax请求静态资源服务器，返回API接口，然后向提供API接口的服务器，请求数据，这些数据中包含了大量的js代码

- 浏览器中显示的网页中的大部分内容，都是由前端写的js代码在浏览器中执行，最终渲染出来的网页

##### 前后端分离阶段：[¶](#_5)

- 随着Ajax的出现，有了前后端分离的开发模式
- 后端只提供API来返回数据，前端通过Ajax获取数据，并且可以通过js将数据渲染到页面中
- 这样做最大的优点就是前后端责任的清晰，后端专注于数据上，前端专注于交互和可视化上
- 并且当移动端出现后，后端不需要进行任何处理，依然使用之前的一套API即可
- 目前很多的网站依然采用这种模式开发

#### SPA页面[¶](#spa)

将一套html+css+js资源从静态资源服务器中，请求下来

前端路由中配置映射关系 - url:sai/home 不会再向服务器发送请求，而是根据js中的判断，从本地资源中抽取需要显示的内容

单页面富应用阶段 - 其实SPA最主要的特点就是在前后端分离的基础上加了一层前段路由 - 也就是前段来维护一套路由规则

前段路由的核心是什么呢？ - 改变URL，但是整体页面不进行刷新 - 如何实现呢

#### url的hash和html5的history[¶](#urlhashhtml5history)

URL的hash - URL的hash也就是锚点(#)，本质上是改变window.location的href属性 - 我们可以直接通过赋值location.hash来改变href，但是页面不刷新 - vue-router会监听location.hash

HTML5的history模式：pushState - history.pushState({},'','home') 把这些url压入到栈结构中（入栈） - history.back() 移除掉栈顶(出栈) - history.replaceState() 不能再点击返回按钮了 - history.go() -1(相当于出栈 .back()) -2（出栈2个） 2（入栈2个）....

#### vue-route安装和配置方式[¶](#vue-route)

#### 路由映射配置和呈现出来[¶](#_6)

目前前端流行的三大框架，都是有自己的路由实现 - Angular的ngRouter - React的ReactRouter - Vue的VueRouter

当然，我们的重点是vue-router - vue-router是Vue.js官方的路由插件，它和vue.js是深度集成的，适合用于构建单页面富应用 - 我们可以访问其官方网站进行学习：https://router.vuejs.org/zh/

vue-router是基于路由和组件的 - 路由用于设定访问路径，将路径和组件映射起来 - 在vue-router的单页面应用中，页面的路径的改变就是组件的切换

安装和使用vue-router

因为我们已经学历了webpack，后续开发中，我们主要是通过工程化的方式进行开发的，这里通过vuecli2来学习vue-router - 所以在后续，我们直接使用npm来安装路由即可 - 步骤一：安装vue-router `npm install vue-router@3.0.1 --save` - 步骤二：在模块化工程使用它（因为它是一个插件，所以可以通过Vue.use()来安装路由功能）

```
第一步：导入路由对象，并且调用Vue.use(VueRouter)
第二步：创建路由实例，并且传入路由映射配置
第三步：在VUe实例中挂载创建的路由实例
```

使用vue-router步骤

```
第一步：创建路由组件
第二步：配置路由映射：组件和路径映射关系
第三部：使用路由：通过<router-linK>和<router-view>
import Vue from 'vue'
import App from './App'
import router from './router'//如果参数是一个文件夹，则会自动找index.js的文件的
//
vue.config.productionTip = false

new Vue({
 el: "#app",
 router,//简写
 render: h => h(App) 
})
```

创建router/index.js

```
//配置路由相关的信息
import VueRouter from 'vue-router'
import Vue from 'vue'
import Home from '../componets/Home'
import About from '../componets/About'
//1.通过Vue.use(插件)安装插件
Vue.use(VueRouter)

//2.创建路由对象
const routes = [
 {
  path: '/home',
  components: Home
 },
 {
  path: '/about',
  components: About
 }
]

const router =  new VueRouter({
 //配置路由和组件之间的映射关系
 routers: [
  routes
 ]
})
//3.将routers对象传入到Vue实例中
exports default router
```

app.vue

```
<template>
 <div id = "app">
  <router-link to = "/home">首页</router-link>
  <router-link to = "/about">关于</router-link>//最终会被渲染成<a>标签
  <router-view></router-view>//相当于是个占位符，放在下面就会在下面显示
 </div>
</template>

<script>
 export default = {
  name: "App"
 }
</script>
```

components/About.vue

```
<template>
 <div>
  <h2>我是关于</h2>
  <div>我是关于内容</div>
 </div>
</template>

<script>
 exports default = {
  name: "About"
 }
</script>

<style scoped>

</style>
```

components/Home.vue

```
<template>
 <div>
  <h2>我是首页</h2>
  <div>我是首页内容</div>
 </div>
</template>

<script>
 export default = {
  name: 'Home'
 }
</script>

<style scoped>

</style>
```

#### 路由的默认值和修改为history模式[¶](#history)

路由的默认值

```
//新增一个路由
{
 path: '',
 //redirect
 redirect:'/home'
}
```

将默认的hash模式，改为html5的history模式，去除掉"#"

```
const router = new VueRouter({
 routes,
 mode: 'history'
})
```

#### router-link的其他属性补充[¶](#router-link)

不使用router-link默认渲染出的a标签，tag属性

设置不能返回,replace属性

```
<template>
 <div id="app">
  <h2>我是App组件</h2>
  <router-link to='/home' tag='button'>首页</router-link>
  <router-link to='/about' tag='button replace'>关于</router-link>
 </div>
</template>
```

点击后，会自动新增一个类名.router-link-active

可以设置active-class属性,更改上面的类名，如果需要统一修改，需要在路由的index.js里面配置

```
const router = new VueRouter({
 routes,
 mode: 'history',
 linkActiveClass: 'active'
})
```

#### 通过代码实现路由跳转[¶](#_7)

App.vue

```
<template>
 <div id="app">
 <h2>我是网站的标题</h2>
 <button @click="linkToHome">首页</button>
 <button @click="linkToAbout">关于</button>
 <router-view></router-view>
 </div>
</template>

<script>
 export default = {
  name: "App",
  methods: {
   linkToHome() {
    this.$router.push('/home')
   },
   linkToAbout() {
    this.$router.push('about')
   }
  }
 }
</script>
```

#### vue-router动态路由的使用[¶](#vue-router)

在某些情况下，一个页面的path路径可能是不确定的，比如我们进入用户界面时，希望是如下的路径： - user/aaa或user/bbb - 除了有前面的/user之外，后面还跟上了用户的id - 这种path和components的匹配关系，我们称之为动态路由（也是路由传递的一种方式）

```
{
 path: '/user/:id',
 component: User
}
<div>
 <h2>{{$route.params.id}}</h2>
</div>
<router-link to="/user/123">用户</router-link>
```

User.vue

```
<template>
 <div>
  <h2>我是用户界面</h2>
  <p>我是用户的相关信息，嘿嘿嘿</p >
  <h2>{{$route.}}</h2>
 </div>
</template>

<script>
 export default ={
  name: 'User',
  computed: {
   userid() {
    //当前哪个路由处于活跃状态，就是哪个路由
    return this.$route.params.userid//拿到的是path后面配置的
   }
  }
 }
</script>

<style scoped>

</style>
```

index.js

```
import User from '../components/User'


const routes = {
 ...

 {
  path: '/user/:userid',
  component: User
 }
 ...
}
```

App.vue

```
<tempalte>
 <div id="app">
  <router-link to="/user/zhangsan">用户</router-link>
  //真实开发中，zhangsan是动态获取的
  <router-link v-bind:to="/user"+userid>用户</router-link>
 </div>
</template>

<script>
 export default = {
  name: 'App',
  data() {
   return {
    userid: 'lisi'
   }
  }
 }
</script>
```

$router是整个大的路由活跃对象 $route是当前活跃的路由对象

#### 打包文件的解析[¶](#_8)

/dist/static/js/app*.js - 当前应用开发的所有业务代码

/dist/static/js/vendor*.js - 引用的第三方的代码

/dist/static/js/manifest*.js - 为我们打包的代码做底层支撑的（**webpack_require**)

#### vue-router懒加载[¶](#vue-router_1)

- 当打包构建应用时，js包会变得非常大，影响页面加载。
- 如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就更加高效了

```
const routes = [
    {
        path: '/home',
        component: () => import('../components/Home')
    },
    {
        path: '/about',
        component: () => import('../components/About')
    }
]
```

懒加载的方式

方式一：结合Vue的异步组件和Webpack的代码分析

```
const Home = resolve => {require.ensure(['../components/Home.vue'],() => {resolve(require('../components/Home.vue'))})}
```

方式二：AMD写法

```
const About = resolve => require(['../components/About.vue'], resolve)
```

方式三：在ES6中，我们可以有更加简单的方法来组织Vue异步组件和Webpack的代码分割

```
const Hoem = () => import('../components/Home.vue')
```

#### 路由的嵌套使用[¶](#_9)

嵌套路由是一个很常见的功能 - 比如在home页面中，我们希望通过/home/news和/home/message访问一些内容 - 一个路径映射一个组件，访问这两个路径也会分别渲染链各个组件

实现嵌套路由有两个步骤： - 创建对应的子组件，并且在路由映射中配置对应的子路由 - 在组件内部使用标签

```
{
    path: '/home',
    component: Home,
    children: [
        {
            path: 'news',
            component: HomeNews
        }
    ]   
}
```

Home.vue

```
<template>
    <div id = "app">
        <router-link to="/home/news">新闻</router-link>
        <router-link to="/home/message">消息</router-link>
        <router-view></router-view>
    </div>

</template>
```

#### vue-router参数传递（一）[¶](#vue-router_2)

传递参数主要有两种类型：params和query

params的类型： - 配置路由格式：/router/:id - 传递的方式：在path后面跟上对应的值 - 传递后形成的路径：/router/123,/router/abc

query的类型： - 配置路由格式：/router，也就是普通配置 - 传递的方式：对象中使用query的key作为传递方式 - 传递后形成的路径：/router?id=123,/router?id=abc

```
<router-link :to="{path:'/profile',query: {name: 'why',age:18,height:1.88}">档案</router-link>
```

Profile.vue

```
//取query的值
<template>
    <div>
        <h2>{{$route.query}}</h2>
        <h2>{{$route.query.name}}</h2>
        <h2>{{$route.query.age}}</h2>
        <h2>{{$route.query.height}}</h2>
    </div>
</template>
```

#### vue-router参数传递（二）[¶](#vue-router_3)

不使用router-link

```
profileClick() {
    this.$router.push({
        path:'/profile',
        query: {
            name:'aa',
            age:18,
            height:1.78
        }    
    })

}
```

#### vue-router中的router和route的由来[¶](#vue-routerrouterroute)

Vue.use(VueRouter) - 会执行插件VueRouter的install方法

为什么能够用`<router-link>`和`<router-view>`

-在install.js中注册了全局组件

```
//注册的时候用驼峰命名法，实际使用可以用小写，并用-连接(<router-link>、<router-view>)
Vue.component('RouterView',View)
Vue.component('RouterView',View)
```

所有的组件继承自Vue类的原型

```
Vue.prototype.test = function() {
 console.log('test')
}

Vue.prototype.$router = 'hahaha'

Object.defineProperty(obj,'age',18) //该方法是vue响应式的核心
```

route和router是有区别的

- router为VueRouter实例，想要导航到不同URL，则使用router.push方法
- $route为当前router跳转对象里面可以获取name、path、query、params等

使用熟练后，再去看看vue源码

#### vue-router全局导航守卫[¶](#vue-router_4)

需要对来回跳转的过程进行监听

我们来考虑一个需求：在一个SPA应用中，如何改变网页的标题呢？

- 网页标题是通过`<title>`显示的，但是SPA只有一个固定的HTML，切换不同的页面时，标题并不会改变
- 但是我们可以通过js来修改title的内容.window.document.title='new tilte'
- 那么在vue项目中，在哪里修改？什么时候修改比较合适呢

1.利用created()、mounted()、updated()、destoryed()生命周期函数

请了解一下vue的源码以及生命周期函数

```
created() {
 document.title = 'new title'
}
```

问题：需要改很多次

优化：每次跳转都是路由的跳转，监听路由的跳转，然后修改标题就可以了

那么怎么监听呢？使用全局导航守卫

```
router.beforeEach()//参数是有三个参数的函数

router.beforEach(function(to,from,next){})//可以写成箭头函数

router.beforeEach((to, from, next) => {
 //从from跳转到to，类型是Route类型，就是定义的一个一个路由
 document.title = to.meta.title
 //如果是嵌套路由的话，可能会有点问题
 //需要修改成
 document.title = to.matched[0].meta.title
 //可以打印下to对象，查看一下
 console.log(to)

 //必须调用next，目的仅仅是为了调用next，以重写系统自带的
 //调用该方法后，才能进入下一个钩子
 next()

})
```

index.js

```
在路由对象中定义
{
 path: '/About'
 component: About,
 meta: {
  title: '关于'
 }
}
```

#### 导航守卫的补充[¶](#_10)

补充一：如果是后置钩子，也就是afterEach，不需要主动调用next()函数

index.js

```
router.afterEach((to, from) => {

})
```

补充二：上面我们使用的导航守卫，被称之为全局守卫，还有 - 路由独享的守卫 - 组件内的守卫

可以通过官方网站来学习，需要使用的时候看官网的api

#### vue-router keep-alive及其他问题[¶](#vue-router-keep-alive)

router-view也是一个组件，如果直接被包在keep-alive里面，所有路径匹配到的视图组件都会被缓存

keep-alive是Vue内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染

我们不希望每次切换的时候，都会创建一个新的组件，就可以使用keep-alive

```
//之前的写法
<router-view></router-view>

//现在有keep-alive的写法
<keep-alive>
 <router-view></router-view>//或者<router-view/>
</keep-alive>
```

大部分的时候，都不需要重新创建组件

路由嵌套缺省值可能会引起一些问题 在Home.vue中修改 解决方案一： 不直接写缺省值，而是在父路径的created()第一次创建时，push一下自路径，但仍然不行，切换回来路由传的还是父路径

解决方案二： activated(){} 页面处于活跃状态时，执行该函数 deactivated(){} 页面不处于活跃状态时，执行该函数

这两个函数，只有组件被keep-alive包裹时才是有效的

```
activated() {
 //先给一个默认值
 this.$router.push(this.path)
},
deactivated() {
 //离开之前，获取一下
 this.path = this.$route.path
 //但实际上，跳转之后，这里已经变成了跳转之后的path，所以仍然不行
 console.log(this.$route.path)
}
```

解决方案三：使用组件内导航守卫

```
beforeRouteLeave(to, from, next) {
 console.log(this.$route.path)
 this.path = this.$route.path

 next()
}
```

#### vue-router keep-alive属性介绍[¶](#vue-router-keep-alive_1)

需求：有一个单独的组件，需要频繁的创建和销毁

keep-alive是Vue内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染 - 它们有两个非常重要的属性 - include 字符串或正则表达式，只有匹配的组件才会被缓存 - exclude 字符串或正则表达式，任何匹配的组件都不会被缓存

router-view也是一个组件，如果直接被包在keep-alive里面，所有路径匹配到的视图都会被缓存

APP.vue

```
<keep-alive exclude='Profile,User'>//这里写子组件的name属性，这里逗号不要加空格
 <router-view/>
</keep-alive>
```

可以通过created()来验证
