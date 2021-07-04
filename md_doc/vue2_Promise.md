[TOC]

## Promise

### Promise的介绍和基本使用

Promise到底是什么 - Promise是一种异步解决方案

那么，什么时候会处理异步事件呢？ - 一种很常见的场景就是异步请求 - 我们封装一个网络请求的函数，因为不能立即拿到结果，所以不能简单的3+5=8一样将结果返回 - 所以往往我们会传入另外一个参数，在数据请求成功时，将数据通过传入的参数回调出去 - 如果只是一个简单的网络请求，那么这种方案不会给我们带来很大麻烦

但是，当网络请求非常复杂的时候时，就会出现回调地狱，这样的代码难看而且不容易维护

- 如何做呢，就是使用Promise

### Promise的三种状态和另外处理方式

- pending:等待状态，比如正在进行网络请求，或者定时器没有到时间
- fulfill:满足状态，当我们主动回调了resolve时，就处于该状态，并且回调.then()
- reject:拒绝状态，当我们主动回调了reject时，就处于该状态，并且回调.catch()

```
new Promis((resolve, reject) => {
    setTimeout(function() {
      //resolve('hello world')
        reject('Error Data')
    },1000)
}).then(data => {
        console.log(data)
},error =>{
        console.log(error)
}
)
```

### Promise的链式调用

我们在看Promise的流程图时，发现无论是then还是catch都可以返回一个Promise对象。

所以，我们的代码其实是可以通过链式调用的：

这里我们直接通过Promise包装了一下新的数据，将Promise对象返回了 - Promise.resolve():将数据包装成Promise对象，并且在内部回调resolve()函数 - Promise.reject():将数据包装成Promise对象，并且在内部回调reject()函数

```
//链式调用的代码
new Promise((resolve, reject) => {
    setTimeout(function() {
      resolve('hello world')
    },1000)
}).then(data => {
    console.log(data)//hello world
    return Promise.resolve(data + '111')
}).then(data => {
    console.log(data)//hello world111
    return Promise.resolve(data + '222')
}).then(data => {
    console.log(data)//hello world111222
    return Promise.reject(data + 'error')
}).then(data => {
    console.log(data)//这里没有输出，这部分代码不会执行
    return Promise.resolve(data + '333')
}).then(data => {
    console.log(data)//hello world111222error
    return Promise.resolve(data + '444')
}).then(data => {
    console.log(data)//hello world111222error444
})
```

### Promised的all方法使用

```
Promise.all([
    //Promise1
    //Promise2
]).then(results => {//等待两个Promise都执行完，才会调用then
    console.log(results)//以数组的形式，打印两个Promise返回的结果
})
```
