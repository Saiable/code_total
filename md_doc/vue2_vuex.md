[TOC]

[TOC]

## VueX

### VueX概念和作用

官方解释：VueX是一个转为Vue.js应用程序开发的状态管理模式 - 它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化 - VueX也集成到Vue的官方调试工具devtools.extension，并提供了诸如零配置的time-travel调试、状态快照导入导出等高级调试功能

状态管理是什么 - 可以简单的将其看成多个组件共享的变量，全部存储在一个对象里面 - 然后，将这个对象放在顶层的Vue实例中，让其他组件可以使用 - 那么，多个组件是不是可以共享这个对象中的所有变量属性了呢？

虽然我们可以自己封装一个对象，但是不能保证它里面所有的属性都是响应式的，VueX就是为了提供这样一个在多个组件共享状态的插件

管理什么状态呢？ - 用户的登陆状态、用户名称、头像、地理位置等等 - 商品的收藏、购车车中的物品等等 - 这些的状态信息都是响应式的，我们都可以放在同一的地方，对它进行保存和管理，而且它们还是响应式的

### Vue-X单界面到多界面状态管理

单页面状态管理

![img](https://web-image-link-1301132383.cos.ap-nanjing.myqcloud.com/vue/vuex01.png)

State: - 就是状态，可以理解成data中的属性

View: - 视图层，可以针对State的变化，显示不同的信息

Actions: - 主要是用户的各种操作：点击、输入等，会导致状态的改变

安装VueX

```
npm install vuex@3.0.1 --save
```

在/src文件夹下，新建/store文件，放vuex的代码

```
/store/index.js
import Vue from 'vue'
import Vuex from 'vuex'

//1.安装插件
Vue.use(Vuex)

//2.创建对象
const store = new Vuex.Store({
  state: {
    counter: 1000
  },
  mutations: {

  },
  actions: {

  },
  getters: {

  },
  modules: {

  }
})

//3.导出store独享
export default store
App.vue
<template>
  <div id="app">
    <h2>{{message}}</h2>
    <h2>{{$store.state.counter}}</h2>
    <button @click="counter++">+</button>
    <button @click="counter--">-</button>
    <hello-vuex></hello-vuex>
  </div>
</template>

<script>
  import HelloVuex from "./components/HelloVuex";
export default {
  name: 'App',
  components: {
    HelloVuex
  },
  data() {
    return  {
      message: '我是App组件',
      counter: 0
    }
  }
}
</script>

<style>

</style>
```

### 多界面状态管理

Vue已经帮我们做好了单个界面的状态管理，但是如果是多个界面呢？

- 多个视图都依赖同一个状态
- 不同界面的Actions都想修改同一个状态（Home.vue需要修改，Profile.vue也需要修改)

也就是说对于某些状态（½/3）来说，只属于一个视图，但是也有一些状态（a/b/c）属于多个视图想要共同维护的

- ½/3放在自己的房间中管理，没问题
- 但是a/b/c希望交给一个人统一进行管理
- Vuex就是这样的管理工具

全局单例模式

- 将共享的状态抽取出来，进行统一管理
- 之后每个视图，按照**规定好的**规则，进行访问和修改操作
- 这就是Vuex背后的思想

![img](https://web-image-link-1301132383.cos.ap-nanjing.myqcloud.com/vue/vuex02.png)

不建议直接在`Components`中修改`State`，通过`Components` `Dispatch`到`Actions`中，然后通过`Actions` `Commit`到`Mutations`中，再通过`Mutations` `Mutate`到`State`，再从`State` `Render`到`Components`里

上述过程可以通过`Devtolols`工具来实现

### vuex - devtools和mutations

devtools for chrome下载

通过mutations来修改state

index.js

```
import Vue from 'vue'
import Vuex from 'vuex'

//1.安装插件
Vue.use(Vuex)

//2.创建对象
const store = new Vuex.Store({
  state: {
    counter: 1000
  },
  mutations: {
    //方法
    increment(state) {
      state.counter++
    },
    decrement(state){
      state.counter--
    }
  },
  actions: {

  },
  getters: {

  },
  modules: {

  }
})

//3.导出store独享
export default store
```

### state单一状态树的理解

Vuex里几个比较核心的概念

- State
- Getters
- Mutations
- Action
- Module

Single Source Truth

### getters使用详解

类似于computed计算属性

```
getters: {
    powerCounter(state) {
        return state.counter * state.counter
    },
    //获取年龄大于20岁的学生
    more20stu(state) {
        return state.students.filter(s => s.age > 20)
    },
    //获取年龄大于20岁学生的个数
    more20stuLength(state,getters) {
        return getters.more20stu.length
    },
    //传参
    moreAgeStu(state) {
        return function(age) {
            return state.students.filter(s => s.age > age)
        }
    }

}
```

### mutation的携带参数

index.js

```
mutataion: {
     incrementCount(state,count){
        state.counter += count
     }
}
```

App.vue

```
<template>
  <div id="app">
    <h2>{{message}}</h2>
    <h2>{{$store.state.counter}}</h2>
    <button @click="addition">+</button>
    <button @click="substraction">-</button>
    <button @click="addCount(5)">+5</button>
    <hello-vuex></hello-vuex>
    <h2>{{$store.state.student}}</h2>
    <button @click="addStu">add</button>
  </div>
</template>

<script>
  import HelloVuex from "./components/HelloVuex";
export default {
  name: 'App',
  components: {
    HelloVuex
  },
  data() {
    return  {
      message: '我是App组件',
      counter: 0
    }
  },
  methods: {
    addition() {
      this.$store.commit('increment')
    },
    substraction() {
      this.$store.commit('decrement')
    },
    addCount(number) {
      this.$store.commit('add', number)
    },
    addStu() {
      const stu = {name:'bbb',age:22}
      this.$store.commit('addStudent',stu)
    }
  }
}
</script>

<style>

</style>
```

index.js

```
import Vue from 'vue'
import Vuex from 'vuex'

//1.安装插件
Vue.use(Vuex)

//2.创建对象
const store = new Vuex.Store({
  state: {
    counter: 1000,
    student: [
      {name:'aa',age:11}
    ]
  },
  mutations: {
    //方法
    increment(state) {
      state.counter++
    },
    decrement(state){
      state.counter--
    },
    add(state, number){
      state.counter += number
    },
    //如果有多个参数需要传递的时候，放在对象里面
    addStudent(state, stu) {
      state.student.push(stu)
    }
  },
  actions: {

  },
  getters: {

  },
  modules: {

  }
})

//3.导出store独享
export default store
```

- 参数被称为是mutation的载荷（payload）
- 如果参数不是一个，我们通常会以对象的形式传递，也就是payload是一个对象

### mutation的提交风格

- 通过commit进行提交是一种普通的方式
- Vue还提供了另外一种风格，它是一个包含type属性的对象

```
vue this.$store.commit({ type: 'changeCount', count: 100 })
```

- Mutation中的处理方式是将整个commit的对象，作为payload使用

```
javascript changeCount(state,payload) { state.count = pyaload.count }
```

\#### Vuex的响应式原理

```
updateInfo(state) {
    state.info.name='aaa'
    state.info['address'] = 'bbb'
    Vue.set(state.info, 'address','bbb')

    delete state.info.age
    Vue.delete(state.info,'age')
}
```

### vuex-数据的响应式原理

### mutation的类型常量

store/mutations-types.js

```
export const INCREMENT = 'increament'
```

index.js

```
import {
    INCREMENT
} from './mutations-types.js'


mutations: {
    [INCREMENT](state) {
        state.counter++
    }
}
```

### vuex-actions的使用详解

- mutation中不建议进行异步操作, devtools不能进行很好的跟踪
- 但是某些情况，我们确实希望在Vuex中进行一些异步操作，比如网络请求
- action类似于mutation，是用来代替mutation进行异步操作的

一：

index.js

```
actions: {
    aUpdateInfo(context,payload) {
        setTimeout(() => {
            context.commit('updateinfo')
        },1000)
    }
}
```

App.vue

```
updateInfo() {
    this.$store.dispatch('aupdateInfo','我是payload')
}
```

二：

index.js

```
actions: {
    aUpdateInfo(context,payload){
        setTimeout(() => {
            context.commit('updateInfo')
            console.log(payload.message)
            payload.success()
        },1000)
    }
}
```

App.vue

```
updateInfo(){
    this.$store.dispatch('aUpdateInfo',{
        message:'我是携带的信息',
        success: () => {
            console.log('里面已经完成了')
        }
    })
}
```

三：

index.js

```
aUpdateInfo(context,payload) {
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            context.commit('updateInfo')
            console.log(payload)
            resolve('1111')
        },1000)
    })
}
```

App.vue

```
updateInfoe() {
    this.$store
    .dispatch('aUpdateInfo','我是携带的信息')
    .then(res => {
        console.log('里面完成了提交')
        console.log(res)
    })
}
```

### vuex-modules详解

```
moudules: {
 a:{
  state: {},
  mutations: {}
  actions: {}
  getters: {}
 },
 b: {

 }
}
```

index.js

```
const moudleA = {
 state:{
  name: 'zhagnsan'
 },
 mutation:{
  updateName(state,payload){
   state.name = payload
  }
 },
 actions:{
  aUpdateName(context) {
   console.log(context)
            setTimeout(() => {
                context.commit('updateName','wangwu')
            }, 1000)
  }
 },
 getters:{
  fullname(state){
   return state.name + '111'
  },
  fullname2(state, getters) {
   return getters.fullname + '222'
  },
  fullname3(state,getters,rootState){
   return getters.fullname2 + rootState.counter
  }
 }
}

const store = new Vuex.Store({
 state:{
  counter:1000
 },
 mutation:{},
 actions:{},
 getters:{}

 moudules:{
  a: mouduleA
 }

})
```

App.vue

```
<template>
 <h2>{{$store.state.a.name}}</h2>
 <button @click="updateName">modify</button>
 <h2>{{$store.getters.fullname}}</h2>
 <h2>{{$store.getters.fullname2}}</h2>
 <h2>{{$store.getters.fullname3}}</h2>
 <button @click="asyncUpateName">异步修改名字</button>
</template>

<script>
 updateName() {
  this.$store.commit('updateName','lisi')
 },
 asyncUpdateName() {
  this.$store.dispatch('aUpdateName')
 }

</script>
```

### vuex-store文件将的目录组织

可以把context写成{state,commit,rootState}

这属于ES6对象解构的写法

- 当我们的Vuex帮助我们管理过多的内容时，好的项目结构可以让我们的代码更清晰

store

- index.js
- actions.js
- mutations.js
- modules
  - cart.js
  - product.js