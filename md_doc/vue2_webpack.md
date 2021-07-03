[TOC]

## 前端代码复杂带来的问题

## 前端模块化雏形和CommonJS

```
var a = 10
var b = 20
function sum1(a,b) {
    return a + b
}
//导出
module.exports = {
    a,
    sum1
}
//导入
var {a, sum1} = require("./aa.js")
console.log(a)
sum1(1,3)
```

## ES6模块化的实现

```
var a = 10
var b = 20
function sum1(a,b) {
    return a + b
}
//导出方式一
export {
    a, sum1
}

//导出方式二
export var num1 = 10

//导出函数或者类
export function sum2(a, b) {
    return a + b
}

//export default
const address = '北京市'
export default address
import {a, sum1} from './aa.js'
console.log(a)
console.log(sum1(1,2))

import {num1} from './aa.js'
console.log(num1)

//自定义名称
import random from './aa.js'
console.log(random)//对应export default

//统一全部导入
import * as aa from './aa.js'
console.log(aa.num1)
```

## Webpack

### webpack的安装和介绍

#### 和GRUNT和GULP的对比

下载node.js 查看自己的node版本

```
node -v
//v.12.16.2
npm -v

//全局安装指定版本的webpack
npm install webpack@3.6.0 -g

//局部安装webpack
--save-dev是开发时依赖，项目打包后不需要使用的
cd 对应目录
npm install webpack@3.6.0 --save-dev

//为什么全局安装后，还要局部安装呢？
在终端直接执行webpack命令，使用的是全局安装的webpack
当在package.json中定义了scripts时，其中包含了webpack命令，那么使用的是局部webpack
```

### webpack的基本使用流程[¶](#webpack_2)

目录结构

```
项目文件夹 - dist
          - src
            - main.js
          - index.html
//1.使用commonjs的模块化规范
const {add, mul} = require('./mathUtil.js')

console.log(add(20,30))

//2.使用es6的模块化规范
import {name,age,height} from "./info.js";

console.log(name)
console.log(age)
console.log(height)
```

打包命令 webpack ./src/main.js ./dist/bundle.js

```
F:\workspace\webstorm\01\webpackTest>webpack ./src/main.js ./dist/bundle.js
Hash: 371e0a3a707406bba89e
Version: webpack 3.6.0
Time: 68ms
    Asset     Size  Chunks             Chunk Names
bundle.js  2.77 kB       0  [emitted]  main
   [0] ./src/main.js 70 bytes {0} [built]
   [1] ./src/mathUtil.js 154 bytes {0} [built]
```

### webpack.config.js配置和package.json配置

执行npm init

```
{
  "name": "meetwebpack",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

配置webpack.config.js，直接只用webpack命令进行打包，相当于执行`webpack ./src/man.js ./dist/bundle.js`

```
const path = require('path')

module.exports ={
    entry:'./src/main.js',
    output:{
        // path:'./dist',//应该是动态获取的路径
        path: path.resolve(__dirname,'dist'),
        filename:'bundle.js'
    },
}
```

实际开发使用的配置，不会直接敲`webpack`，而是让其等价于npm形式的命令，需要在package.json中再做一层映射

改文案晋中，在script键中配置。

执行npm命令时，会优先在本地找webpack执行，所以要在本地也安装一个webpack，不使用全局的webpack，（直接在终端运行webpack也是找的全局的

只安装开发时依赖`webpack install webpack@3.6.0 --save-dev`

```
{
  "name": "meetwebpack",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"//在这里配置
  },
  "author": "",
  "license": "ISC"
}
```

在本地安装webpack包，不要使用全局的webpack包

```
npm install webpack@3.6.0 --save-dev
```

### webpack中使用css文件

添加css依赖，只有依赖的文件，才会进行打包

安装loader，https://webpack.docschina.org/loaders/css-loader/

```
npm install --save-dev css-loader@2.0.2` `npm install --save-dev style-loader@0.23.1
```

安装完后，在webpack.config.js中进行配置

```
const path = require('path')

module.exports ={
    entry:'./src/main.js',
    output:{
        // path:'./dist',//应该是动态获取的路径
        path: path.resolve(__dirname,'dist'),
        filename:'bundle.js'
    },
    //在这里进行配置
    module:{
        rules:[
            {
                test: /\.css$/,
                //css-loader只负责将文件加载   @2.0.2
                //style-loader负责将样式添加到dom中   @0.23.1
                //使用多个loader时，是从右向左
                use: ['style-loader', 'css-loader']
            }
        ]
    }
}
```

在`main.js`引入css文件，最后在index.html中引入bundle.js

### webpack-less文件的处理

在入口文件main.js中，添加less的依赖

```
//依赖less文件
require('./css/special.less')
```

再安装less-loader

```
npm install --save-dev less-loader@4.1.0 less
```

配置webpack.config.js

```
const path = require('path')

module.exports ={
    entry:'./src/main.js',
    output:{
        // path:'./dist',//应该是动态获取的路径
        path: path.resolve(__dirname,'dist'),
        filename:'bundle.js'
    },
    module:{
        rules:[
            {
                test: /\.css$/,
                //css-loader只负责将文件加载   @2.0.2
                //style-loader负责将样式添加到dom中   @0.23.1
                //使用多个loader时，是从右向左
                use: ['style-loader', 'css-loader']
            },
            //配置Less-loader   @4.1.0
            {
                test: /\.less$/,
                loader: [ // compiles Less to CSS
                    "style-loader",
                    "css-loader",
                    "less-loader",
                ]
            }
        ]
    },

}
```

### webpack-图片文件的处理

安装url-loader

```
npm install url-loader@1.1.2 --save-dev
```

配置webpack.config.js

```
const path = require('path')

module.exports ={
    entry:'./src/main.js',
    output:{
        // path:'./dist',//应该是动态获取的路径
        path: path.resolve(__dirname,'dist'),
        filename:'bundle.js'
    },
    module:{
        rules:[
            {
                test: /\.css$/,
                //css-loader只负责将文件加载   @2.0.2
                //style-loader负责将样式添加到dom中   @0.23.1
                //使用多个loader时，是从右向左
                use: ['style-loader', 'css-loader']
            },
            //配置Less-loader
            {
                test: /\.less$/,
                loader: [ // compiles Less to CSS
                    "style-loader",
                    "css-loader",
                    "less-loader",
                ]
            },
            //配置url-loader
            {
                test: /\.(png|jpg|gif|jpeg)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 8192,
                        },
                    },
                ],
            }
        ]
    },
}
```

当加载的图片小于limit的时候，会将图片变异成base64，这种情况下不需要单独的文件夹进行处理

```
npm install file-loader@3.0.1 --save-dev
```

当加载的图片大于limit的时候，需要使用file-loader模块进行加载 @3.0.1，这种情况下需要处理下文件夹及命名，否则图片文件会默认打包在dist文件夹下

需要在entry下添加publicPath字段，所有涉及url的东西，都会拼接一个publicPath的字段值

```
    output:{
        // path:'./dist',//应该是动态获取的路径
        path: path.resolve(__dirname,'dist'),
        filename:'bundle.js',
        //添加publicPath字段
        publicPath: 'dist/'
    },
```

图片命名

处理图片打包后所在的文件夹及文件名

```
            //配置url-loader
            {
                test: /\.(png|jpg|gif|jpeg)$/i,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            //当加载的图片小于limit的时候，会将图片变异成base64
                            //当加载的图片大于limit的时候，需要使用file-loader模块进行加载  @3.0.1
                            limit: 15000,
                            //设置图片所在文件夹及文件名
                            name: 'img/[name].[hash:8].[ext]'
                        },

                    },
                ],
            }
```

### webpack-ES6转ES5的babel

如果希望ES6的语法转为ES5，那么就需要使用babel `npm install --save-dev babel-loader@7.1.5 babel-core@6.26.3 babel-preset-es2015@6.24.1`

配置webpack.config.js

```
{
    test: /\.m?js$/,
    exclude: /(node_modules|bower_components)/,
    use: {
        loader: 'babel-loader',
        options: {
            // presets: ['@babel/preset-env']
            presets: ['es2015']
        }
    }
}
```

### webpack-使用vue的配置

安装vue，注意不要加开发时依赖

[vue的github](https://github.com/vuejs/vue)

```
npm install vue@2.5.21 -save
```

runtime-only:代码中，不能有任何的template

runtime-compiler:可以有template

需要在webpack.config.js的ouput同级配置下resolve字段，指定vue的版本，否则默认情况使用的是vue.runtime.js

```
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    }
```

最后在main.js中导入vue进行使用

```
import Vue from 'vue'
new Vue({
    el: "#app",
    data: {
        message: 'hello webpack'
    }
})
```

### 创建Vue时template和el的关系

实际开发中，index.html是不写的，而是写在vue实例中了

template和el同时存在的时候，最后vue在编译的时候，会将template的值替换掉index.html中的div标签

最后注意，template最外层是需要用一个div来包裹的

```
import Vue from 'vue'
new Vue({
    el: "#app",
    data: {
        message: 'hello webpack',
        name:'aa'
    },
    template: `
        <div>
            <div>{{message}}</div>
            <button>click me</button>
            <div>{{name}}</div>
        </div>
    `
})
```

### Vue的终极使用方案

vue/app.js

```
export default {
    template: `
        <div>
            <div>{{message}}</div>
            <button @click="btnClick">click me</button>
            <div>{{name}}</div>
        </div>
    `,
    data() {
        return {
            message: 'hello webpack',
            name:'aa'
        }
    },
    methods: {
        btnClick(){
            console.log('hello')
        }
    }
}
```

main.js

```
import Vue from 'vue'
import App from '../vue/app.js'//default导入，就不需要使用大括号了
new Vue({
    el: "#app",
    template: "<App/>",//去找有没有App组件
    components: {
        App
    }

})
```

但这里还存在一个问题，就是模板和js没有分离

创建vue/App.vue

```
//这里放模板
<template>
    <div>
        <div class="title">{{message}}</div>
        <button @click="btnClick">click me</button>
        <div>{{name}}</div>
    </div>
</template>

//这里放脚本
<script>
    export default {
        name: "App",
        data() {
            return {
                message: 'hello webpack',
                name:'aa'
            }
        },
        methods: {
            btnClick(){
                console.log('hello')
            }
        }
    }
</script>

//这里放样式
<style scoped>
.title {
    color: blue;
}
</style>
```

main.js

```
import Vue from 'vue'
// import App from '../vue/app.js'//default导入，就不需要使用大括号了
import App from '../vue/App.vue'
new Vue({
    el: "#app",
    template: "<App/>",//去找有没有App组件
    components: {
        App
    }

})
```

安装vue对应的loader

```
npm install vue-loader@15.4.2 vue-template-compiler@2.5.21 --save-dev
```

vue-loader中从14的版本开始，要想使用还要额外下载一个插件

所以可以安装13的版本

```
npm install vue-loader@13 vue-template-compiler@2.5.21 --save-dev
```

也可以直接修改package.json中的版本为13.0.，webstrom会提示重新安装的

在webpack.config.js中配置

```
    {
        test: /\.vue$/,
        use: ['vue-loader']
    }
```

导入时如何省略后缀名文件

在resolve中配置extensions

```
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['.js','.css','.vue']
    }
```



### Plugin

#### webpack-横幅Plugin的使用

```
//版权声明，BannerPlugin是webpack自带的，直接导入即可，然后再moudle中添加字段
const webpack = require("webpack")

    plugins: [
        new webpack.BannerPlugin('最终版权归aaa所有')
    ]
```

#### webpack-HtmlWebpackPlugin的使用[¶](#webpack-htmlwebpackplugin)

需求：

- 将index.html文件也同时打包到dist文件夹中

HtmlWebpackPlugin作用：

- 自动生成一个index.html文件（可以指定模板来生成）
- 将打包的js文件，自动通过script标签插入到body中

安装：

```
npm install html-webpack-plugin@3.2.0 --save-dev
```

使用：

修改webpack.config.js文件中plugin部分的内容如下：

- tempalte表示根据哪个文件来生成index.html
- 另外，还需要删除之前在output中添加的publicPath属性，否则插入的script标签中的src会有问题

webpack.config.js

```
const HtmlWebpackPlugin = require("html-webpack-plugin")

    plugins: [
        new webpack.BannerPlugin('最终版权归aaa所有'),
        new HtmlWebpackPlugin({
            template: "index.html"
        })
    ]
```

#### webpack-UglifyjsWebpackPlugin的使用

需求：

- 在项目发布之前，对打包的js文件进行压缩
- 这里使用第三方插件uglifyjs-webpack-plugin，并且指定版本号为1.1.1，与CLI2保持一致

安装： `npm install uglifyjs-webpack-plugin@1.1.1 --save-dev`

使用：

- 修改webpack.config.js文件

查看打包后的bundle.js文件，是已经被压缩过了的

#### webpack-dev-server搭建本地服务器

webpack提供了一个可选的本地开发服务器，其基于node.js搭建，内部使用express框架，可以实现浏览器自动刷新

安装： `npm install --save-dev webpack-dev-server@2.9.1`

使用：

devserver也是作为webpack的一个选项，选项本身可以进行如下设置：

- contentBase:为哪一个文件提供本地服务，默认是根文件夹，我们这里要填写./dist
- port:端口号
- inline:页面实时刷新
- historyApiFallback:在SPA页面中，依赖HTML5的history模式 webpack.config.js文件配置修改如下：

```
devServer: {
    contentBase: './dist',
    inline: true
}
```

配置package.json

```
"script":{
    ...
    "dev": "webpack-dev-server --open"
}
```

我们可以再配置另外一个scripts： --open表示直接打开浏览器

#### 配置文件的分离

开发阶段，不建议使用丑化代码的功能，只有在发布的时候才需要

这里要形成一个概念，开发时依赖的配置，和发布时依赖的配置

创建文件夹和文件 - build/base.config.js

这里放开发和发布时都需要的配置，先复制原来的完整的配置，然后先注释掉丑化代码和devServer的配置

```
const path = require("path")
const webpack = require("webpack")
const HtmlWebpackPlugin = require("html-webpack-plugin")
const unglifyJsPlugin = require("uglifyjs-webpack-plugin")

module.exports = {
    entry: "./src/main.js",
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
        // publicPath: 'dist/'
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader','css-loader']
            },
            {
                test: /\.less$/,
                loader: [ // compiles Less to CSS
                    "style-loader",
                    "css-loader",
                    "less-loader",
                ]
            },
            {
                test: /\.(png|jpg|gif|jpeg)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 1,
                            name: 'img/[name].[hash:8].[ext]'
                        }
                    }
                ]
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        // presets: ['@babel/preset-env']
                        presets: ['es2015']
                    }
                }
            },
            {
                test: /\.vue$/,
                use: ['vue-loader']
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['.js','.css','.vue']
    },
    plugins: [
        new webpack.BannerPlugin('最终版权归aaa所有'),
        new HtmlWebpackPlugin({
            template: "index.html"
        })
    ]
}
```

- build/prod.config.js

这里放发布时依赖的配置

```
const unglifyJsPlugin = require("uglifyjs-webpack-plugin")

module.exports = {
     plugins: [
        new unglifyJsPlugin()
    ]
}
```

- build/dev.config.js

这里放开发时依赖的配置

```
module.exports = {
    devServer: {
        contentBase: './dist',
        inline: true
    }
}
```

还需要安装webpack-merge来处理配置文件的合并 `npm install webpack-merge@4.1.5`prod.config.js的合并

```
const unglifyJsPlugin = require("uglifyjs-webpack-plugin")
const webpackMerge = require("webpack-merge")
const baseConfig = require("./base.config.js")

module.exports = webpackMerge(baseConfig,{
    plugins: [
        new unglifyJsPlugin()
    ]
})
```

dev.config.js的合并

```
const webpackMerge = require("webpack-merge")
const baseConfig = require("./base.config.js")

module.exports = webpackMerge(baseConfig,    {
    devServer: {
        contentBase: './dist',
        inline: true
    }
})
```

然后删除webpack.config.js文件，同时配置scripts，指定配置文件:

```
  "scripts": {
    ...
    "build": "webpack --config ./build/prod.config.js",
    "dev": "webpack-dev-server --open --config ./build/dev.config.js"
  }
```

这里执行`npm run build`，虽然打包成功了，但打包的位置不对，打包到build目录下了，需要改下输出文件夹的路径

```
    output: {
        path: path.resolve(__dirname, '../dist'),
        filename: 'bundle.js'
        // publicPath: 'dist/'
    },
```

再测试下`npm run dev`

## Vite