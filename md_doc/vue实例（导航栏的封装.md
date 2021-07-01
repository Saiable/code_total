[TOC]

# 01.导航栏的封装

### TabBar 基本结构的搭建[¶](#tabbar)

#### 实现思路[¶](#_1)

1.如果在下方有一个单独的TabBar组件，如何封装

- 自定义TabBar组件，在App中使用
- 让TabBar处于底部，并且设置相关样式

2.TabBar中显示的内容由外部决定 - 定义插槽 - flex布局平分TabBar

3.自定义TabBaritem，可以传入图片和文字 - 自定义TabBarItem,并且定义两个插槽：图片、文字 - 给两个插槽外层包装div，用于设置样式 - 填充插槽，实现底部TabBar效果

4.传入高亮图片 - 定义另一个插槽，插入active-icon的数据 - 定义一个变量isActive，通过v-show来决定是否显示对象的icon

5.TabBarItem绑定路由数据 - 安装路由：npm install vue-router --save - 完成router/index.js的内容，以及创建对应的组件 - main.js中注册router - App中加入组件

6.点击item跳转到对应路由，并且动态决定isActive - 监听item的点击，通过this.route.replace()替换路由路径 - 通过this.route.path.indexOf(this.link) !== -1 来判断是否是active

7.动态计算active样式 - 封装新的计算属性：this.isActive ? {'color':'red"'}:{}

```
vue init webpack TabBar
```

#### tabbar TabBar和TabBarItem组件的封装[¶](#tabbar-tabbartabbaritem)

App.vue

```
<template>
  <div id="app">
  <tab-bar>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/home.svg" alt="">
      <div slot="item-text">首页</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/menu.svg" alt="">
      <div slot="item-text">分类</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/shopping.svg" alt="">
      <div slot="item-text">购物车</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/profile.svg" alt="">
      <div slot="item-text">我的</div>
    </tab-bar-item>
  </tab-bar>
  </div>
</template>

<script>
  import TabBar from "./components/tabbar/TabBar";
  import TabBarItem from "./components/tabbar/TabBarItem";
  export default {
    name: 'App',
    components: {
      TabBarItem,
      TabBar
    }
  }
</script>

<style>
  @import "./assets/css/base.css";

</style>
```

TabBar.vue

```
<template>
  <div id="tab-bar">
    <slot></slot>
  </div>
</template>

<script>
    export default {
        name: "TabBar"
    }
</script>

<style scoped>
  #tab-bar {
    display: flex;
    background-color: #f6f6f6;

    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;

    box-shadow: 0px -3px 1px rgba(100,100,100,0.1);
  }
</style>
```

TabBarItem.vue

```
<template>
  <div class="tab-bar-item">
    <slot name="item-icon"></slot>
    <slot name="item-text"></slot>
  </div>
</template>

<script>
    export default {
        name: "TabBarItem"
    }
</script>

<style scoped>
  .tab-bar-item {
    flex: 1;
    text-align: center;
    height: 49px;
    font-size: 14px;
  }
  .tab-bar-item img{
    width: 24px;
    height: 24px;
    margin-top: 3px;
    vertical-align: middle;
    margin-bottom: 2px;
  }
</style>
```

#### 给TabBarItem传入active图片[¶](#tabbaritemactive)

TabBarItem.vue

```
<template>
  <div class="tab-bar-item">
    <div v-if="!isActive">
      <slot name="item-icon"></slot>
    </div>

    <div v-else>
      <slot name="item-icon-active"></slot>
    </div>

    <div :class="{active: isActive}">
      <slot name="item-text"></slot>
    </div>
  </div>
</template>

<script>
    export default {
        name: "TabBarItem",
        data() {
          return {
            isActive: true
          }
        }
    }
</script>

<style scoped>
  .tab-bar-item {
    flex: 1;
    text-align: center;
    height: 49px;
    font-size: 14px;
  }
  .tab-bar-item img{
    width: 24px;
    height: 24px;
    margin-top: 3px;
    vertical-align: middle;
    margin-bottom: 2px;
  }

  .active {
    color: green;
  }
</style>
```

App.vue

```
<template>
  <div id="app">
  <tab-bar>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/home.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/home_activate.svg" alt="">
      <div slot="item-text">首页</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/menu.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/menu_activate.svg" alt="">
      <div slot="item-text">分类</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/shopping.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/shopping_activate.svg" alt="">
      <div slot="item-text">购物车</div>
    </tab-bar-item>
    <tab-bar-item>
      <img slot="item-icon" src="./assets/img/tabbar/profile.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/profile_activate.svg" alt="">
      <div slot="item-text">我的</div>
    </tab-bar-item>
  </tab-bar>
  </div>
</template>

<script>
  import TabBar from "./components/tabbar/TabBar";
  import TabBarItem from "./components/tabbar/TabBarItem";
  export default {
    name: 'App',
    components: {
      TabBarItem,
      TabBar
    }
  }
</script>

<style>
  @import "./assets/css/base.css";

</style>
```

#### TabBarItem和路由结合效果[¶](#tabbaritem)

TabBarItem.vue

```
<template>
  <div class="tab-bar-item" @click="itemClick">
    <div v-if="!isActive">
      <slot name="item-icon"></slot>
    </div>

    <div v-else>
      <slot name="item-icon-active"></slot>
    </div>

    <div :class="{active: isActive}">
      <slot name="item-text"></slot>
    </div>
  </div>
</template>

<script>
    export default {
        name: "TabBarItem",
        props: {
          path: String
        },
        data() {
          return {
            isActive: true
          }
        },
        methods: {
            itemClick() {
              this.$router.replace(this.path)
            }
        }
    }
</script>

<style scoped>
  .tab-bar-item {
    flex: 1;
    text-align: center;
    height: 49px;
    font-size: 14px;
  }
  .tab-bar-item img{
    width: 24px;
    height: 24px;
    margin-top: 3px;
    vertical-align: middle;
    margin-bottom: 2px;
  }

  .active {
    color: green;
  }
</style>
```

App.vue

```
<template>
  <div id="app">
    <router-view></router-view>
  <tab-bar>
    <tab-bar-item path="/home">
      <img slot="item-icon" src="./assets/img/tabbar/home.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/home_activate.svg" alt="">
      <div slot="item-text">首页</div>
    </tab-bar-item>
    <tab-bar-item path="/category">
      <img slot="item-icon" src="./assets/img/tabbar/category.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/category_activate.svg" alt="">
      <div slot="item-text">分类</div>
    </tab-bar-item>
    <tab-bar-item path="/cart">
      <img slot="item-icon" src="./assets/img/tabbar/shopping.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/shopping_activate.svg" alt="">
      <div slot="item-text">购物车</div>
    </tab-bar-item>
    <tab-bar-item path="/profile">
      <img slot="item-icon" src="./assets/img/tabbar/profile.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/profile_activate.svg" alt="">
      <div slot="item-text">我的</div>
    </tab-bar-item>
  </tab-bar>
  </div>
</template>

<script>
  import TabBar from "./components/tabbar/TabBar";
  import TabBarItem from "./components/tabbar/TabBarItem";
  export default {
    name: 'App',
    components: {
      TabBarItem,
      TabBar
    }
  }
</script>

<style>
  @import "./assets/css/base.css";

</style>
```

问题：连续点击会报错 - 解决方案：

```
        methods: {
            itemClick() {

              // this.$router.replace(this.path)
              // this.$router.replace(this.path).catch(err => err)
              //同路由跳转时会报错，可以先捕获错误，并用console.table打印出来
              // this.$router.replace(this.path).catch(err => {console.table(err)})
              // console.log(this.$route)
              // console.log(this.$route.matched[0].path)
              //这里的this.$route.matched[0].path保存的是点击之前，path的值，this.path实际是即将要跳转的path的值
              if(this.$route.matched[0].path != this.path){
                this.$router.replace(this.path)
              }
            }
        }
```

#### TabBarItem的颜色动态控制[¶](#tabbaritem_1)

TabBarItem.vue

```
<template>
  <div class="tab-bar-item" @click="itemClick">
    <div v-if="!isActive">
      <slot name="item-icon"></slot>
    </div>

    <div v-else>
      <slot name="item-icon-active"></slot>
    </div>

<!--    <div :class="{active: isActive}">-->
<!--      <slot name="item-text"></slot>-->
<!--    </div>-->

    <div :style="activeStyle">
      <slot name="item-text"></slot>
    </div>
  </div>
</template>

<script>
    export default {
        name: "TabBarItem",
        props: {
          path: String,
          activeColor: {
            type: String,
            default: 'green'
          }
        },
        data() {
          return {
            // isActive: true
          }
        },
        computed: {
          isActive() {
            // console.log(this.$route.path,this.path)
            // console.log(this.$route.matched[0].path)  一开始的时候，没有激活的路由对象，如果用matched的话会报undefined错误
            return this.$route.path.indexOf(this.path) != -1
          },
          activeStyle() {
            return this.isActive ? {color: this.activeColor} : {}
          }
        },
        methods: {
            itemClick() {

              // this.$router.replace(this.path)
              // this.$router.replace(this.path).catch(err => err)
              //同路由跳转时会报错，可以先捕获错误，并用console.table打印出来
              // this.$router.replace(this.path).catch(err => {console.table(err)})
              // console.log(this.$route)
              // console.log(this.$route.matched[0].path)
              //这里的this.$route.matched[0].path保存的是点击之前，path的值，this.path实际是即将要跳转的path的值
              if(this.$route.matched[0].path != this.path){
                this.$router.replace(this.path)
              }
            }
        }
    }
</script>

<style scoped>
  .tab-bar-item {
    flex: 1;
    text-align: center;
    height: 49px;
    font-size: 14px;
  }
  .tab-bar-item img{
    width: 24px;
    height: 24px;
    margin-top: 3px;
    vertical-align: middle;
    margin-bottom: 2px;
  }
</style>
```

App.vue

```
<template>
  <div id="app">
    <router-view></router-view>
  <tab-bar>
<!--    <tab-bar-item path="/home" active-color="pink">-->
    <tab-bar-item path="/home">
      <img slot="item-icon" src="./assets/img/tabbar/home.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/home_activate.svg" alt="">
      <div slot="item-text">首页</div>
    </tab-bar-item>
    <tab-bar-item path="/category">
      <img slot="item-icon" src="./assets/img/tabbar/category.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/category_activate.svg" alt="">
      <div slot="item-text">分类</div>
    </tab-bar-item>
    <tab-bar-item path="/cart">
      <img slot="item-icon" src="./assets/img/tabbar/shopping.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/shopping_activate.svg" alt="">
      <div slot="item-text">购物车</div>
    </tab-bar-item>
    <tab-bar-item path="/profile">
      <img slot="item-icon" src="./assets/img/tabbar/profile.svg" alt="">
      <img slot="item-icon-active" src="./assets/img/tabbar/profile_activate.svg" alt="">
      <div slot="item-text">我的</div>
    </tab-bar-item>
  </tab-bar>
  </div>
</template>

<script>
  import TabBar from "./components/tabbar/TabBar";
  import TabBarItem from "./components/tabbar/TabBarItem";
  export default {
    name: 'App',
    components: {
      TabBarItem,
      TabBar
    }
  }
</script>

<style>
  @import "./assets/css/base.css";

</style>
```

#### 文件路径的引用[¶](#_2)

webpack.base.config.js

```
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      '@': resolve('src'),
      'asserts': resolve('src/asserts'),
      'components': resolve('src/components'),
      'views': resolve('src/views')
    }
  },
```

如果是import里的路径引用，则可以直接用别名，

如果是html里的src路径引用，则需要加波浪号`~`