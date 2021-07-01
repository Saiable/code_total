[TOC]

# 03.vue-cli基础

### vuecli-脚手架的介绍和安装[¶](#vuecli-)

安装Vue脚手架 `npm install -g @vue/cli@3.2.1`脚手架3的安装方式，可以在3的基础上搭2的模板

查看vue的版本

```
vue --version
```

拉取2的模板

```
npm install -g @vue/cli-init@3.2.0
```

Vue-Cli2初始化项目

```
vue init webpack my-project
```

#### vuecli-CLI2初始化项目过程[¶](#vuecli-cli2)

```
vue init webpack vuecli2test
?project name(vuecli2test)
?project description(A Vue.js project)vuecli2test
?Author(Administrator<24**91@qq.com>)myemail@test.com//这里默认值是读取git的配置
 Runtime + Compiler:recommand for most users
>Runtime-only:about 6KB lighter min+gzip, but template(or any Vue-specific HTML) are ONLY allowed in .vue files -render functions are required elsewhere//实际选择第二个，但这里是个测试，就选择第一个了
?Install vue-router?(Y/N)n//暂时选择n
?Use EsLint to lint your code?(Y/N)n//强制代码规范
?Set up unit tests(Y/N)n//不使用单元测试
?Setup e2e tests with Nightwatch?(Y/N)n//Nightwatch可以结合selenium，一般是测试来写测试脚本的
?Should we run `npm install` for you after the project has benn created?(recommended)(Use arrow keys)
>Yes,use NPM
 Yes,use Yarn
 No,I will handle that myself//选择NPM
```

#### vuecli-CLI2的目录结构解析[¶](#vuecli-cli2_1)

package.json

```
  "scripts": {
    "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
    "start": "npm run dev",
    "build": "node build/build.js"
  },
```

config/

```
定义了一些配置的基础变量
```

src/

```
以后实际写代码的地方
```

static/

```
放静态资源的地方
```

.babelrc

```
如果安装的有babel-preset-env、babel-preset-stage-2
则需要单独在.babelrc中配置
```

.editconfig

```
对代码风格进行统一
```

.eslintignore

```
某某些代码进行格式忽略检测
```

index.html

```
模板文件
```

#### 安装CLI错误和ESLint规范[¶](#clieslint)

安装不成功

```
如果是通过cmd命令安装的，最好以管理员身份执行
删除 Users/Adminstrator/AppData/Romaning/npm-cache 或者npm clean cache -force
```

Eslint会对所有的代码进行规范检测

build/index.js 中可以配置eslint是否开启

#### runtime-compiler和runtime-only[¶](#runtime-compilerruntime-only)

两者的区别，只在main.js文件 runtiem-compiler/main.js

```

```

runtime-only/main.js

```

```

Vue程序运行过程

```
vm.options:template--->[parse]--->ast--->[compiler]--->vm.option:render
                          (abstract syntax tree)          (function)       
                                                               |
                                                               |[render] 
                                                               V
                                                           virtual dom
                                                               |
                                                               |[update(diff and patch)] 
                                                               V
                                                               UI
```

runtime-compiler

```
template -> ast -> render ->vdom -> UI
```

runtime-only:性能更高，代码更少

```
render -> vdom -> UI
```

render函数

```
const cpn = {
    template: `<div>{{message}}</div>`
    data() {
        return {
            message: '我是一个组件'
        }   
    }   
}
//也可以导入一个组件，然后给createElement调用
import App from './App'

render: function (createElement) {
    //1.createElement('标签名称',{标签属性},['标签内容'])
    return createElement('h2',
        {class:box},
        ['hello world',createElement('button',['按钮'])])//会用h2替换掉挂载的app

    //2.传入组件对象
    return createElement(cpn)
    //传入导入的组件对象
    return createElement(App)
}
```

runtime-only → src/main.js

```
import Vue from './vue'
import App from './App'

Vue.config.productionTip = false

new Vue({
    el: "#data",
    render: function (h) {
        return h(App)
    }
})
```

即使App包含template，但实际拿到的时候，已经没有template了

```
console.log(App)
//object中有render()函数
```

那么，App.vue文件中的template是谁来处理的呢？

```
之前安装的vue-tempalte-compiler
```

#### VueCLI3创建项目和目录[¶](#vuecli3)

npm run build的解析过程

```
                              npm run build          
                                    |
                                    |
          ________________________入口文件________________________
         |                   (build/build.js)                   |
         |                                                      |        
         |                                                      |                           
         |                                                      |   
         V                                                      V       
   config/index.js                                    build/webpack.prod.conf       --->      build/utils.js                     
该文件包含了一些配置信息                                            |                                   |                     
         |                                                      |                                   |                    
         |                                                      |                                   V                    
         V                                                      V                            1.计算资源存放的路径
     生产环境参数              build/vue-loader.js  <--- build/webpack.base.conf               2.生成css-loader用于加载.vue文件中的样式               
config/prod.env.js                    |                         |                            3.生成style-loader用于加载不在.vue文件中的样式
         |                            |                         |                    
         |                            V                         V                     
         V                        导出一些Vue     定义了入口、出口、编译规则、插件相关配置
NODE_ENV:"production"             配置相关选项   上面两个文件合并，其实就是我们单独使用webpack  
                                                          打包编译需要的文件                                                                
```

npm run dev的解析过程

```
                                                                npm run dev
                                                                    |
                                                                    V
                                                                  入口文件  
                                                                    |
                                                                    V
   config/index.js                   <---               build/webpack.dev.config      --->       build/utils.js
 该文件包含了一些配置信息                                               |                                 |
           |                                                        |                                 V                   
           V                                                        V                         1.计算资源的存放路径         
       生产环境参数        build/vue-loader.js      <---     build/webpack.base.conf            2.生成cssLoaders用于加载.vue文件中的样式
   config/prod.env.js             |                                 |                         3.生成styleLoaders用于加载不在.vue文件中的样式
           |                      V                                 V
           V                  导入一些Vue            定义了入口、出口、编译规则、插件相关配置
   NODE_ENV:"production"      配置相关选项         上面两个文件合并，其实就是我们单独用webpack打包
                                                               编译需要的文件
```

#### VueCLI3创建项目和目录结构[¶](#vuecli3_1)

修改配置:webpack.base.conf.js

```
resolve: {
    extensions:['.js','.vue','.json'],
    alias:{
        '@': resolve('src'),
        'pages':resolve('src/pages'),
        'common':resolve('src/common'),
        'components':resolve('src/components')，
        'network':resolve('src/network')
    }
}
```

vue-cli3与2有很大区别 - vue-cli3 是基于webpack4打造，vue-cli2 还是webpack3 - vue-cli3 的设计原则是“0配置”，移除了配置文件根目录下的，buidl和config目录 - vue-cli3 提供了vue ui命令，提供了可视化配置，更加人性化 - 移除了static文件夹，新增了public 文件夹，并且index.html移动到了public中

vue-cli2初始化项目

```
vue init webpack my-project
```

vue-cli3初始化项目

```
vue create my-project
```

main.js

```
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')//el的本质都是挂载，和之前只是写法不同
```

package.json

```
{
  "name": "my-porject",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build"
  },
  "dependencies": {
    "core-js": "^3.6.5",
    "vue": "^2.6.11"
  },
  "devDependencies": {
    "@vue/cli-plugin-babel": "^4.5.0",
    "@vue/cli-service": "^4.5.0",
    "vue-template-compiler": "^2.6.11"
  }
}
//配置更少了，通过vue/cli-service来管理了
```

public/

```
相当于cli2中的static目录
```

src/

```
源代码，以后就在这里写
```

.browserslistrc

```
浏览器相关支持情况
```

.gitignore

```
git忽略的文件
```

babel.config.js

```
ES语法转化
```

postcss.config.js

```
css相关转换
```

#### vuecli配置文件的查看和修改[¶](#vuecli)

- `vue ui` UI可以查看配置
- node_modules/@vue/cli-service/lib/Service.js

```
模块这边也可以看配置位置
```

- 在根目录创建vue.config.js

```
modules.exports = {
    //最后会将vuecli-service那边的配置文件合并
}
```
