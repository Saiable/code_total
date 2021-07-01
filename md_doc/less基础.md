[TOC]

# Less基础语法

## 一、less基础语法[¶](#less)

```
@a:100px;
// 变量，在变量中可以存储一个任意值
// 变量作为类名使用，或者一部分值使用时，需要加大括号
@b:box;
.@{b}{
    color: red;
}

.p1{
    width: 100px;
    height: 200px/2;
    // 数值可以进行计算
    >.box1{
        border: 1px solid red;;
    }
    //& 表示外层的父元素
    &:hover{
        color:blue;
    }
}
.p2{
    width: 100px;
    height: 200px;
    color: red;
}
// 对当前选择器扩展指定选择器的样式
.p3:extend(.p2){
    background-color: cornflowerblue;
}
.p4:extend(.p1>.box1){
    color: red;
}
.p5{
    // 直接对指定的样式进行引用，这里就相当于复制
    // mix混合
    .p4();
}
//使用类选择器时可以在选择器后面添加一个括号，这时我们就创建了一个mix，专门给别人引用的
.p6(){
    color: red;
}
.p7{
    .p6;
}

//混合函数 在混合函数中可以直接设置变量
.test1(@w){
    width: @w;
    height:200px;
    border: 1px solid red;
}
.div1{
    .test1(200px);
}
.test2(@w:100px,@h:200px,@bgc:red){
    width: @w;
    height:@h;
    border: 1px solid @bgc;
}
.div2{
    // 按顺序传参
    .test2(200px);
}
```

## 二、对应css文件[¶](#css)

```
.box {
  color: red;
}
.p1 {
  width: 100px;
  height: 100px;
}
.p1 > .box1,
.p4 {
  border: 1px solid red;
}
.p2,
.p3 {
  width: 100px;
  height: 200px;
  color: red;
}
.p3 {
  background-color: cornflowerblue;
}
.p4 {
  color: red;
}
.p5 {
  color: red;
}
.p7 {
  color: red;
}
.div1 {
  width: 200px;
  height: 200px;
  border: 1px solid red;
}
.div2 {
  width: 200px;
  height: 200px;
  border: 1px solid red;
}
```