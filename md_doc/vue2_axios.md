[TOC]
# 07.axios基础

#### 网络请求模块的选择-axios[¶](#-axios)

在前段开发中，我们一种常见的网络请求方式就是JSONP

- 使用JSONP最主要的原因，往往是为了解决跨域访问的问题

JSONP的原理是什么呢？

- JSONP的核心在于通过`<script>`标签的src来帮助我们请求数据
- 原因是我们的项目部署在domain1.com服务器上时，是不能直接访问domain2.com服务器上的资料的
- 这个时候，我们利用`<script>`标签的src帮助我们去服务器请求到数据，将数据当做一个javascript函数来执行，并且执行的过程中传入我们需要的json
- 所以，封装jsonp的核心就在于我们监听window上的jsonp进行回调的名称

##### 为什么选择AXIOS？[¶](#axios)

- 在浏览器中发送XMLHttpRequest请求
- 在node.js中发送http请求
- 支持Promise API
- 拦截请求和相应
- 转换请求和相应数据
- 等等

#### axios框架的基本使用[¶](#axios_1)

- 支持多种请求方式
- axios(config)
- axios.request(url, config)
- axios.get(url[,config])
- axios.delete(url[,config])
- axios.head(url[,config])
- axios.post(url[,data[,config]])
- axios.put(url[,data[,config]])
- axios.patch(url[,data[,config]])

安装axios：`npm install axios@0.18.0 --save`

基本使用

```
axios({
  url:'http://152.136.185.210:7878/api/m5/home/multidata',
  method:'get'
}).then(res => {
  console.log(res)
})
axios({
    url:'http://152.136.185.210:7878/home/data',
    params: {
        type: 'pop',
        page: 1
    }
}).then(res => {
    console.log(res)
})
```

#### axios发送并发请求[¶](#axios_2)

```
axios.all([axios(), axios()]).then(results => {

})
axios.all([axios({
    url: 'http://152.136.185.210:7878/api/m5/home/multidata'
}),axios({
    url:'http://152.136.185.210:7878/home/data',
    params: {
        type: 'pop',
        page: 1
})]).then(results => {
    console.log(results)
    console.log(results[0])
})
axios.all([axios({
    url: 'http://152.136.185.210:7878/api/m5/home/multidata'
}),axios({
    url:'http://152.136.185.210:7878/home/data',
    params: {
        type: 'pop',
        page: 1
})]).then(axios.spread((res1, res2) => {
    console.log(res1)
    console.log(res2)
}))
```

#### axios的配置信息相关[¶](#axios_3)

在上面的示例中，我们的BaseUrl是固定的

- 事实上，在开发中可能很多参数都是固定的
- 这个时候我们可以进行一些抽取，也可以利用axios的全局配置

```
axios.defaults.baseURL = '123.207.32.32:8080'
axios.defaults.headers.post['Content-Type']='application/x-www-form-urlencoded'
```

常见的配置选项

- 请求地址
- 请求类型
- 请根路径
- 请求前的数据处理
- 请求后的数据处理
- 自定义的请求头
- URL查询对象
- 查询对象序列化函数
- request body
- 超时设置s
- 跨域是否带Token
- 自定义请求处理
- 身份验证信息
- 响应式的数据格式json/blob/document/arrarybuffer/text/stream

#### axios的实例和模块封装[¶](#axios_4)

```
const instance1 = axios.create({
    baseURL: 'http://152.136.185.210:7878'
    timeout: 5000
})

instance1({
    url: '/home/multidata'
}).then(res => {
    console.log(res)
})

instance1({
    url: '/home/data',
    params: {
        type: 'pop',
        page: 1
    }
})

const instance2 = axios.create({
    baseURL: 'http://111.111.11.1:1111'
    timeout: 1111
})
```

/network/request.js

```
import axios from 'axios'

export function request(config) {
    //1.创建axios的实例
    const instance = axios.create({
        baseURL: 'http://111.111.11.1:1111',
        timeout: 1111
    })

    // 发送真正的网络请求
    instance(config, success, failure)
        .then(res =>{
            success(res)
        })
        .catch(error =>){
            failure(err)
        }
}
```

main.js

```
import {request} from './network/request'

request({
    url: '/home/multidata'
},res => {
    console.log(res)
},err => {
    console.log(err)
})
```

另一种写法：对象的写法

request.js

```
instance(config.baseConfig)
    .then(res => {
        config.success(res)
    })
    .catch(err => {
        config.faulure(err)
    })
```

main.js

```
request({
    baseConfig: {

    },
    success: function(res) {

    },
    failure: function(err) {

    }
})
```

第三种写法：Promise

request.js

```
export function request(config) {
    return new Promise((resolve, reject) => {
        const instance = axios.create({
            baseURL: 'http://111.111.11.1:1111',
            timeout: 1111
        })

        instance(config)
            .then(res => {
                resolve(res)
            })
            .catch(err => {
                reject(err)
            })
    })
}
```

main.js

```
request({
    url:'/home/multidata'
}).then(res => {
    console.log(res)
}).catch(err => {
    console.log(err)
})
```

第四种写法:instance本身返回的就是Promise

request.js

```
export function request(config) {
    return new Promise((resolve, reject) => {
        const instance = axios.create({
            baseURL: 'http://111.111.11.1:1111',
            timeout: 1111
        })

        return instance(config)
    })
}
```

#### axios的拦截器的使用[¶](#axios_5)

- axios提供了拦截器，用于我们每次在发送请求或者得到相应的请求后，进行对应的处理
- 如何使用拦截器呢

```
//配置请求和响应拦截
instance.interceptors.request.use(config => {
    console.log('来到了request拦截success中')
    return config
},err => {
    console.log('来到了request拦截failure中')
    return err
})
instance.interceptors.reponse.use(response => {
    console.log('来到了response拦截success中')
    return response.data
},err => {
    console.log('来到了response拦截failure中')
    return err
})
```