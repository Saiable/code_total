
@[toc]
## 1.HTML基础

### HTML全称

HTML(Hypertext Markup Language) 超文本标记语言

### 实体

[https://www.w3school.com.cn/html/html_entities.asp](https://www.w3school.com.cn/html/html_entities.asp)

| 显示结果 | 描述   | 实体名称 |
| -------- | ------ | -------- |
|          | 空格   | &nbsp ;  |
| <        | 小于号 | &lt ;    |
| >        | 大于号 | &gt ;    |

### meta标签

- charset 指定网页的字符集

- name 指定的数据的名称

- content 指定的数据的内容

- keywords 表示网站的关键字，可以同时指定多个关键字，用逗号隔开

  ```html
  <meta name="keyword" content="网上购物,网上商城">
  ```

- description 指定网站的描述，网站的描述会显示在搜索引擎的结果中

  ```html
  <meta name="description" content="京东JD.COM-专业的综合网上购物商城"
  ```

- http-equiv 页面重定向到另一个网站

  ```html
  <meta http-equiv="refresh" content="3;url=https://www.baidu.com"
  ```

### 块和行内

- 块元素（block element）
  - 在网页中，一般通过块元素来进行布局
- 行内元素（inline element）
  - 行内元素主要用来包裹文字
  - 一般情况下会在块元素中放行内元素，而不会在行内元素中放块元素
  - 块元素中基本上什么都能放
  - p元素中不能放任何的块元素

### 标签

- em 表示语音语调的一个加重
- strong 表示强调，重要内容
- blockquote 表示一个长引用
- q 表示一个短引用
- br 表示页面中的换行
- div 没有语义，就用来表示一个区块，是用来布局的元素
- span 没有语义

#### 结构语义化标签

- header 表示网页的头部
- main 表示网页中的主体部分，一般只有一个
- footer 表示网页的底部
- nav 表示网页中的导航
- aside 和主体相关的其他内容（侧边栏）
- article 表示一个独立的文章
- section 表示一个独立的区块，上面的标签都不能表示时，用section

### 列表

- 有序列表 ol

- 无序列表 ul

- 定义列表 dl

  - dt 用来表示定义的内容
  - dd 用来对内容进行解释说明

  ```html
  <dl>
      <dt>结构</dt>
      <dd>网页的结构</dd>
      <dd>网页的结构</dd>
  </dl>
  ```

列表之间可以互相嵌套

### 超链接和路径

- ./ 表示当前文件所在的目录

- ../表示当前文件所在的上一级目录

- target 用来指定超链接打开的位置

  - _self 默认值，在当前页面打开超链接
  - _blank 在一个新的窗口中打开超链接

- 锚点

  ```html
  <a href="bottom">去底部</a>
  <p>paragraph</p>
  <a id="bottom" href="#">回到顶部</a>
  ```

- href 可以将超链接的href属性设置为#，这样点击超链接以后，页面不会发生跳转

- id 每一个标签都可以添加id属性，id属性就是元素的唯一标识，同一个页面中不能出现重复的id属性
  跳转到页面指定位置

### 图片标签

#### 图片的属性

img元素属于替换元素（块和行内元素之间，具有两种元素的特点）

- src：指定外部图片的路径（路径规则和超链一样的）
- alt：图片的描述，默认情况下不会显示，如果不写alt属性，则图片不会被搜索引擎识别
- width：图片的宽度（px）
- height：图片的高度（px）；宽度和高度如果只修改了一个，则另一个会等比缩放
  - 注意：一般在pc端，需要多大的图片就做多大的图，在移动端，一般会大图缩小

#### 图片的格式

- jpeg(jpg)
  - 支持的颜色比较丰富，不支持透明效果，不支持动图
  - 一般用来显示照片
- gif
  - 支持的颜色比较少，支持简单透明，支持动图
  - 颜色单一的图片，动图
- png
  - 支持的颜色丰富，支持复杂透明，不支持动图
  - 颜色丰富，复杂透明图片（专为网页而生）
- webp
  - 这种格式是谷歌新推出的专门用来表示网页中的图片的一种格式
  - 它具备其他图片格式的所有优点，而且文件还特别小
  - 缺点：兼容性不好
- base64
  - 将图片使用base64编码，这样可以将图片转换为字符，通过字符的形式来引入图片
  - vue中的loader相关的知识点中，可以根据指定大小来决定，图片是否为base64
  - 一般都是一些需要和网页一起加载的图片，才会使用base64

使用原则

- 效果一样，用文件小的
- 效果不一样，用效果好的

### 内联框架

用于向当前页面中引入一个其他页面

- src：指定要引入的路径
- frameborder：指定内联框架的边框（0：没有，1：有）

```html
<iframe src="https://www.qq.com" width="800" height="600" frameborder="1"></iframe>
```

### 音视频播放

audio标签用来向页面引入一个外部的音频文件，默认不允许用户自己控制播放停止

- controls：是否允许用户控制播放

  ```html
  <audio src="./若草恵%20-%20想い,あふれて.mp3" controls></audio>
  ```

  加上`controls`才会在界面上显示

- autoplay：音频文件是否自动播放

- loop：音乐是否循环播放

  ```html
  <audio src="./若草恵%20-%20想い,あふれて.mp3" controls autoplay loop></audio>
  ```

除了通过src来指定外部文件的路径外，还可以通过source来指定文件

```html
<audio controls>
	<!-- 对不起，您的浏览器不支持播放音频！请升级浏览器！ -->
    <source src="./若草恵%20-%20想い,あふれて.mp3">
    <source src="./若草恵%20-%20想い,あふれて.ogg">
    <!-- 兼容IE8 -->
    <embed src="./若草恵%20-%20想い,あふれて.mp3" type="video/mp3" width="300" height="100">
</audio>
```

使用video标签来向网页引入一个视频，使用方式和audio基本上是一致的

```html
<video controls>
	<source src="./flower.webm">
    <source src="./flower.mp4">
    <embed src="./flower.mp4" type="video/mp4">
</video>
```

一般情况下，不会直接将音频视频放在本地服务器上的，可以用在云服务器上，或者放在视频网站上

## 2.CSS基础

### 选择器

#### 常用选择器：

- 元素选择器
- 类选择器
- id选择器

#### 交集选择器：

```css
div.red{
	color:red;
}
```

#### 并集选择器：

```css
h1, span{
	color:red;
}
```

#### 关系选择器：

- 父元素：直接包含子元素的元素
- 子元素：直接被父元素包含的元素
- 祖先元素：直接或间接包含后代元素的元素
- 后代元素：直接或间接被祖先元素包含的元素
- 兄弟元素：拥有相同父元素的元素

##### 子元素选择器：

```css
div.box > span{
	color:red;
}
```

##### 后代元素选择器：

```css
div.box span{
	color:red;
}
```

##### 兄弟选择器：

```css
p + span{
	color:red;
}
```

##### 选择下面所有的兄弟：

```css
p ~ span{
	color:red;
}
```

#### 属性选择器：

```css
p[title]{
	color:red;
}

[title=abc]{
	color:red;
}

/*以abc开头*/
[title^=abc]{
	color:red;
}

/*以abc结尾*/
[title$=abc]{
	color:red;
}

/*包含abc即可*/
[title*=abc]{
	color:red;
}
```

#### 伪类选择器：

```css
ul > li:first-child{
	color:red;
}

ul > li:last-child{
	color:red;
}

ul > li:nth-child(1){
	color:red;
}

ul > li:nth-child(2n){
	color:red;
}
```

```css
ul > li:first-of-type{
	color:red;
}

ul > li:last-of-type{
	color:red;
}

ul > li:nth-of-type(1){
	color:red;
}

ul > li:nth-of-type(2n){
	color:red;
}
```

##### 否定伪类：

```css
ul > li:not(nth-child(5)){
	color:red;
}
```

#### 超链接伪类：

```css
a:link{
	color:red;
}

a:visited{
	color:red;
}

a:hover{
	color:red;
}

a:active{
	color:red;
}
```

#### 伪元素选择器：

```css
/*表示第一个字母*/
p::first-letter{
	color:red;
}

/*表示第一行*/
p::first-line{
	color:red;
}

/*表示选中的内容*/
p::selection{
	color:red;
}

/*元素的开始*/
p::before{
	color:red;
}

/*元素的结束*/
p::after{
	color:red;
}
```

### 餐厅练习（选择器练习）

[https://flukeout.github.io/](https://flukeout.github.io/)

### 样式的继承

- 我们为一个元素设置的样式，同时也会应用到它到底后台元素上

- 继承是发生在祖先后代之间的

- 继承的设计是为了方便我们的开发，利用继承我们可以将一些通用的样式，统一设置到共同的祖先元素上，这样只需设置一次即可让所有的元素具有该样式



注意：并不是所有的样式都会被继承，比如，背景相关的，布局相关的等，这些样式都不会被继承

### 选择器的权重

- 样式的冲突：当我们通过不同的选择器，选中相同的元素，并且为相同的样式设置不同的值时，此时就发生了样式的冲突
- 发生样式冲突时，应用哪个样式由选择器的权重（优先级）决定
- 选择器的权重
  - 内联样式				1,0,0,0
  - id选择器				0,1,0,0
  - 类和伪类选择器    0,0,1,0
  - 元素选择器            0,0,0,1
  - 通配选择器            0,0,0,0
  - 继承的样式            没有优先级
- 比较优先级时，需要将所有的选择器的优先级进行相加计算，最后优先级越高，则越优先显示（分组选择器是单独计算的）
  - 选择器的累加不会超过其最大数量级，类选择器再高，也不会超过id选择器
  - 如果优先级计算后相同，此时则优先使用靠下的样式
- 可以在某一个样式的后边添加`!important`，则此时该样式会获取到最高的优先级，甚至超过内联样式（开发中慎用）

### 长度单位

- 像素
  - 屏幕（显示器）实际上是由一个一个小点点构成的
  - 不同屏幕的像素大小是不同的，像素越小的屏幕，显示效果越清晰
  - 所有同样的200px在不同的设备下显示效果不一样
- 百分比
  - 也可以降属性值设置为相对于其父元素属性的百分比
  - 设置 百分比可以使子元素跟随父元素的改变而改变
- em
  - em是相对于元素的字体大小来计算的
  - 1em = 1fontsize
  - em会根据字体大小的改变而改变
- rem
  - rem是相对于根元素的字体大小来计算

### 颜色单位

- 在css中可以直接使用颜色名，来设置各种颜色
  - 比如：red、orange、yellow...
  - 但是在css中直接使用颜色是非常的不方便
- RGB值
  - RGB通过三种颜色的不同浓度来调配出不同的颜色
  - 每一种颜色在0~255之间
  - 语法：rgb(红,绿,蓝)
- RGBA：
  - 在RGB基础上增加了不透明度
  - 1表示完全不透明，0表示完全透明，0.5表示半透明（0可以省略）
- 十六进制的RGB值
  - 颜色浓度：00~ff
  - 如果颜色两位两位重复，可以简写：#aabbcc---->#abc
- HLS
  - H（色相：0 ~ 360）
  - S（饱和度，颜色的浓度：0% ~ 100%）
  - L（亮度，颜色的亮度：0% ~ 100%）

## 3.文档流（normal flow）

- 网页是一个多层结构，一层摞着一层
- 通过css可以为每一层设置样式
- 作为用户只能看到最顶上的一层
- 这些层中，最底下的一层称为文档流，文档流是网页的基础
  - 我们所创建的元素默认都是在文档流中进行排列
- 对于元素主要有连个状态：
  - 在文档流中
  - 不在文档流中（脱离文档流）
- 元素在文档流中有什么特点：
  - 块元素
    - 块元素会在页面上独占一行（自上向下垂直排列）
    - 默认宽度是父元素的全部（会把父元素撑满）
    - 默认宽度是被内容撑开（子元素）
  - 行内元素
    - 行内元素不会独占页面的一行，只占自身的大小
    - 行内元素在页面中，自左向右水平排列，如果一行中不能容下所有的行内元素，则元素会换到第二行继续自左向右排列（书写习惯一致）
    - 行内元素的默认宽度和高度都是被内容撑开

#### 盒子模型

- 内容区(content)，元素中的所有子元素和文本内容都是在内容区中排列
  - 内容区的大小，由width和height两个属性来设置
- 边框(border)，边框属于盒子边缘，出了盒子都是盒子的外部
  - 边框的大小会影响到整个盒子的大小
    - 要设置边框，至少要设置三个样式：`border-width`、`border-color`、`border-style	`
- 盒子模型、盒模型、框模型(box-model)
  - css将页面中的所有元素设置为了一个矩形的盒子
  - 每一个盒子都有以下几个组成部分
    - 内容区(content)
    - 内边距(padding)
    - 边框(border)
    - 外边距(margin)

##### 盒子模型-边框

##### 盒子模型-内边距

##### 盒子模型-外边距

##### 盒子模型-水平方向的布局



![在这里插入图片描述](https://img-blog.csdnimg.cn/20210131080503337.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210131081017254.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

```css
//根据以上原理，设置水平居中
width:xxxpx;
margin:0 auto;
```

##### 盒子模型-垂直方向的布局

1.父元素不设置高度，默认情况下，高度被子元素撑开；
2.子元素超过父元素高度，子元素从父元素中溢出；

```css
.outer{
	width:200px;
	height:200px;
}
.inner{
	width:200px;
	height:400px;
}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210131081821683.png)
使用overflow在父元素中处理溢出；

```css
.outer{
	width:200px;
	height:200px;
	overflow:visible;/*visible hidden scroll auto*/
	/*overflow-x overflow-y*/
}
.inner{
	width:200px;
	height:400px;
}
```

##### 盒子模型-外边距的折叠

###### 外边距折叠现象

相邻的、垂直外边距会发生重叠现象
1.相邻（挨着）
2.垂直（margin-bottom  margin-top）

###### 兄弟元素

两者都是正值，取较大值；
一正一负，取两者和；
两者都是负值，取绝对值较大值；

兄弟元素之间的外边距折叠，不需要处理；

###### 父子元素

父子元素间的相邻（上）外边距，子元素会传递给父元素；
现象：给子元素设置一个上外边距后，父元素被挤下来了；
处理方式一：
计算一下，不用子元素的margin-top，用padding-top;
处理方式二：
用border-top，使父子元素不相邻；

##### 行内元素的盒模型

行内元素不支持设置宽度和高度；
行内元素可以设置padding、border、margin，垂直方向不会影响元素的布局；

###### display

用来设置元素显示的类型
inline：行内元素；
block ：块元素；
inline-block：行内块元素；
既可以设置宽高，也不会独占一行；
table：表格；
none：隐藏一个元素；

###### visibility

visible：默认值，正常显示；
hidden：隐藏不显示，但依然占据页面的位置；

#### 浏览器的默认样式

去除浏览器的默认样式
方案一

```css
*{
	margin:0;
	padding:0;
}
```

方案二，reset.css 

```css
html,body,div,span,applet,object,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video {
	margin:0;
	padding:0;
	border:0;
	font-size:100%;
	font:inherit;
	font-weight:normal;
	vertical-align:baseline;
}
/* HTML5 display-role reset for older browsers */
article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section {
	display:block;
}
ol,ul,li {
	list-style:none;
}
blockquote,q {
	quotes:none;
}
blockquote:before,blockquote:after,q:before,q:after {
	content:'';
	content:none;
}
table {
	border-collapse:collapse;
	border-spacing:0;
}
th,td {
	vertical-align:middle;
}
/* custom */
a {
	outline:none;
	color:#16418a;
	text-decoration:none;
	-webkit-backface-visibility:hidden;
}
a:focus {
	outline:none;
}
input:focus,select:focus,textarea:focus {
	outline:-webkit-focus-ring-color auto 0;
}
```



## 高度塌陷和BFC

### 高度塌陷

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201224122324.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### BFC

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021020122491265.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201224952946.png)

### clear

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201225617910.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 解决高度塌陷的最终方案

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201230356810.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201230720429.png)

### 外边距折叠和高度塌陷的合并写法

```css
.clearfix::before,
.clearfix::after {
	content: '';
	display: table;
	clear:both;
}
```



### 定位介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206183628654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 相对定位

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206183536990.png)

#### 偏移量

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206183353936.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 绝对定位

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206183733889.png)

#### 包含块

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206183816473.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 固定定位

![在这里插入图片描述](https://img-blog.csdnimg.cn/202102061839228.png)

### 粘滞定位

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021020618420256.png)

### 绝对定位元素的位置

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206184344327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206185023867.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			.box1{
				width: 500px;
				height: 500px;
				background-color: #bfa;
				position: relative;
			}
			.box2{
				width: 100px;
				height: 100px;
				background-color: orange;
				position: absolute;
				
				margin-left: auto;
				margin-right: auto;
				left: 0;
				right: 0;
				
				margin-top: auto;
				margin-bottom: auto;
				top: 0;
				bottom: 0;
			}
		</style>
	</head>
	<body>
		<div class="box1">
			<div class="box2"></div>
		</div>
	</body>
</html>

```

### 元素的层级

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206185204186.png)



### 字体介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206191407492.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 引入自定义字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206191723870.png)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			@font-face {
				font-family:myfont;
				src: url(FZPTYJW.TTF) format("truetype");
			}
			p{
				color: red;
				font-size: 40px;
				font-family: "myfont";
			}
		</style>
	</head>
	<body>
		<p>今天天气不错，hello</p>
	</body>
</html>


```

### 图标字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206195718297.png)

#### fontawesome使用步骤

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021020620043628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### 通过伪元素来设置图标字体

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206201621163.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

#### iconfont使用步骤

[https://www.iconfont.cn/](https://www.iconfont.cn/)

[资源链接](https://www.iconfont.cn/collections/detail?spm=a313x.7781069.1998910419.dc64b3430&cid=29085)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206204053428.png)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<link rel="stylesheet" type="text/css" href="iconfont.css"/>
	<style type="text/css">
		.iconfont{
			font-size: 40px;
			color: red;
		}
		p::before{
			content: '\e7be';
			font-family: 'iconfont';
			font-size: 50px;
		}
		.icon-xianxingtanghulu{
			font-size: 60px;
		}
	</style>
</head>
<body>
	<span class="iconfont">&#xe7bd;</span>
	<p class="iconfont">hello</p>
	<i class="iconfont icon-xianxingtanghulu"></i>
</body>
</html>
```



## 字体相关样式

### 行高介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206204553921.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 简写属性

```css
font: bold italic 50px/2 微软雅黑, 'Times New Roman', Times, serif;
//不写不等于没有，浏览器会自动渲染默认值；
```

## 文本相关样式

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206205150357.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206205636486.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

## 其他文本样式

### textdecoration

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210156230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### white-space

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210625684.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210206210615303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)



### 一、transition属性介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022119352793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221193706747.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221193810113.png)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			*{
				margin:0;
				padding:0;
			}
			.box1{
				width: 400px;
				height: 400px;
				background-color: #BBFFAA;
			}
			.box1 div{
				width: 50px;
				height: 50px;
			}
			.box2{
				
				background-color: skyblue;
				/* transition-property: width,height; */
				transition-property: all;
				transition-duration: 2s;
				/* transition-timing-function: ease; */
				transition-timing-function: steps(2,starts);
			}
			.box3{
				background-color: orange;
				transition-property: all;
				transition-duration: 2s;
				transition-timing-function: cubic-bezier(.19,1.24,.82,-0.58);
			}
			.box1:hover div{
				/* width: 100px;
				height: 100px; */
				margin-left: 350px;
			}
		</style>
	</head>
	<body>
		<div class="box1">
			<div class="box2"></div>
			<div class="box3"></div>
		</div>
	</body>
</html>

```

### 二、米兔练习

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			.box{
				width: 96px;
				height: 194px;
				background-image: url("mitu.png");
				background-position: 0,0;
				transition: 0.8s steps(4);
			}
			.box:hover{
				background-position: -378px 0;
			}
		</style>
	</head>
	<body>
	<div class="box"></div>
	</body>
</html>

```

### 三、动画属性介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221221650932.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221223127487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221223220780.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221223301202.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210221223725998.png)

### 四、奔跑的少年

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222221120834.png)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			.box1{
				width: 91px;
				height: 91px;
				margin: 0 auto;
				background-image: url(sprite01.jpg);
				animation: run 1s steps(6) infinite;
			}
			/* 创建关键帧 */
			@keyframes run{
				from{background-position: 0,0;}
				to{background-position: -551px;}
			}
		</style>
	</head>
	<body>
		<div class="box1"></div>
	</body>
</html>

```

### 五、关键帧

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			.box1 {
				height: 500px;
				margin: 50 auto;
				overflow: hidden;
				border-bottom: 10px solid black;
			}

			.box2 {
				width: 100px;
				height: 100px;
				border-radius: 50%;
				background-color: #BBFFAA;
				animation: ball 2s forwards ease-in alternate;

			}

			/* 创建小球落下的动画 */
			@keyframes ball {
				from {
					margin-top: 0;
				}

				20%,
				60%,
				to {
					margin-top: 400px;
					animation-timing-function: ease-in;
				}

				40% {
					margin-top: 100px;
				}

				80% {
					margin-top: 200px;
				}
			}
		</style>
	</head>
	<body>
		<div class="box1">
			<div class="box2"></div>
		</div>
	</body>
</html>

```



### 一、变形介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222222811666.png)
设置水平居中
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222223235422.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 二、平移案例

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			body{
				background-color: #CCCCCC;
			}
			.box1{
				width: 250px;
				height: 400px;
				background-color: white;
				margin:20px auto;
				transition: all .3s;
			}
			.box1:hover{
				transform: translate(-2px, -3px);
				box-shadow: 2px 2px 10px rgba(0,0,0,.3);
			}
		</style>
	</head>
	<body>
		<div class="box1">
		</div>
	</body>
</html>

```

### 三、z轴平移

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222224706487.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222224806422.png)

### 四、旋转介绍

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			html{
				/* perspective: 800px; */
			}
			body{
				border:1px solid red;
			}
			.box1{
				width: 200px;
				height: 200px;
				background-color: #BBFFAA;
				margin: 50px auto;
				transition: 2s;
			}
			body:hover .box1{
				/* transform: rotateY(180deg) translateY(100px); */
				transform: rotateY(180deg);
				/* 是否显示元素的背面 */
				backface-visibility: hidden;
			}
		</style>
	</head>
	<body>
		<div class="box1">
			<img src="./54.布局作业/01/img/0102.webp" >
		</div>
	</body>
</html>

```

### 五、旋转练习--钟表

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style type="text/css">
			* {
				margin: 0;
				padding: 0;
			}
			.block{
				width: 500px;
				height: 500px;
				margin: 0 auto;
				margin-top: 100px;
				border-radius: 50%;
				border: 10px solid black;
				position: relative;
			}
			.block > div{
				position: absolute;
				top: 0;
				left:0;
				bottom: 0;
				right:0;
				margin: auto;
			}
			/* 设置时针 */
			.hour-wrapper{
				height: 70%;
				width: 70%;
				animation: run 7200s linear infinite;
			}
			.min-wrapper{
				height: 80%;
				width: 80%;
				animation: run 600s steps(60) infinite;
			}
			.sec-wrapper{
				height: 90%;
				width: 90%;
				animation: run 10s steps(60) infinite;
			}
			.hour{
				height: 50%;
				width: 6px;
				background-color: black;
				margin: 0 auto;
			}
			.min{
				height: 50%;
				width: 4px;
				background-color: black;
				margin: 0 auto;
			}
			.sec{
				height: 50%;
				width: 2px;
				background-color: black;
				margin: 0 auto;
			}
			/* 旋转的关键帧 */
			@keyframes run {
				from {
					transform: rotateZ(0);
				}
				to {
					transform: rotateZ(360deg);
				}
			}
		</style>
	</head>
	<body>
		<!-- 创建表容器 -->
		<div class="block">
			<!-- 创建时针 -->
			<div class="hour-wrapper">
				<div class="hour"></div>
			</div>
			<!-- 创建分针 -->
			<div class="min-wrapper">
				<div class="min"></div>
			</div>
			<!-- 创建秒针 -->
			<div class="sec-wrapper">
				<div class="sec"></div>
			</div>
		</div>
	</body>
</html>

```

### 六、3d旋转

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			html{
				perspective: 800px;
			}
			.cube{
				width: 200px;
				height: 200px;
				margin: 100px auto;
				transform-style: preserve-3d;
				transform: rotateX(45deg) rotateZ(45deg);
				animation: rotate 20s infinite linear;
			}
			.cube > div{
				width: 200px;
				height: 200px;
				opacity: 0.8;
				position: absolute;
				/* 设置3d变形效果 */

			}
			img{
				vertical-align: top;
			}
			.box1{
				transform: rotateY(90deg) translateZ(100px);
			}
			.box2{
				transform: rotateY(-90deg) translateZ(100px);
			}
			.box3{
				transform: rotateX(90deg) translateZ(100px);
			}
			.box4{
				transform: rotateX(-90deg) translateZ(100px);
			}
			.box5{
				transform: rotateY(180deg) translateZ(100px);
			}
			.box6{
				transform: rotateY(0deg) translateZ(100px);
			}
			@keyframes rotate{
				from{
					transform: rotateX(0) rotateZ(0);
				}
				to{
					transform: rotateX(1turn) rotateZ(1turn);
				}
			}
		</style>
	</head>
	<body>
		<!-- 创建一个外部容器 -->
		<div class="cube">
			<!-- 引入图片 -->
			<div class="box1"><img src="../img/laopo01.png" alt=""></div>
			<div class="box2"><img src="../img/laopo02.png" alt=""></div>
			<div class="box3"><img src="../img/laopo03.png" alt=""></div>
			<div class="box4"><img src="../img/laopo04.png" alt=""></div>
			<div class="box5"><img src="../img/laopo05.png" alt=""></div>
			<div class="box6"><img src="../img/laopo06.png" alt=""></div>
			
		</div>
	</body>
</html>

```



### 一、弹性容器的样式

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223234313434.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223234544914.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224195243588.png)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210223235135676.png)

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			ul{
				width: 800px;
				border: 10px solid red;
				/*设置ul为弹性容器 */
				display: flex;
				/* 设置排列的方向 */
				/* flex-direction: row; */
				/* 设置弹性元素是否自动换行 */
				/* flex-wrap: wrap; */
				/* 简写属性 */
				/* flex-flow: column nowrap; */
				
				/* 如何分主轴上的空白空间
					flex-start:沿着主轴的起边排列；
					flex-end:沿着主轴的终边排列；
					center:居中排列；
					space-around:空白分布到元素两侧；
					space-between:空白分布元素中间；
					space-evenly:空白分布在元素的单侧；
				 */
				/* justify-content: space-evenly;
					针对主轴上的布局
				 */
				
				/* 
				 stretch  默认值，让元素的长度相同（行与行之间的高度）
				 flex-start  沿着辅轴的起边对齐
				 flex-end  沿着辅轴的终边对齐
				 center   居中对齐
				 baseline  基线对齐
				 */
				align-items: stretch;
				
				/* 
				辅轴中间的空白对齐方式； 
				 */
				align-content: flex-end;
				
				
			}
			li{
				width:200px;
				height: 100px;
				background-color: #bfa;
				font-size: 50px;
				text-align: center;
				line-height: 100px;
				list-style: none;
				/* 设置缩减系数 */
				flex-shrink: 0;
			}
			li:nth-child(1){
				align-self: stretch;
				/* 用来覆盖当前元素的align-items */
			}
			li:nth-child(2){
				background-color: pink;
			}
			li:nth-child(3){
				background-color: orange;
			}
		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>
	</body>
</html>

```

### 二、弹性元素的样式

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			ul{
				width: 800px;
				border: 10px solid red;
				/*设置ul为弹性容器 */
				display: flex;
				
				
				
			}
			li{
				width:200px;
				height: 100px;
				background-color: #bfa;
				font-size: 50px;
				text-align: center;
				line-height: 100px;
				list-style: none;
				/* 弹性增长系数 */
				/* flex-grow: 1; */
				/* 
				 设置的缩减系数
					计算的方式比较复杂，是根缩减系数和大小决定
				 */
				flex-shrink: 1;
				
				/* 
				元素基础长度
					如果主轴是横向的，则指定的是元素的宽度
					如果主轴是纵向的，则指定的是元素的高度
					默认值，auto表示参考的是元素自身的宽度或者高度
				 */
				flex-basis: 100px;
				
				/* flex可以设置弹性元素的样式 
					flex 增长 缩减 基础
					initial :0 1 auto;
					auto :1 1 auto;
					none : 0 0 auto;弹性元素没有弹性
				*/
				flex:1 1 auto; 
				
			}
			li:nth-child(1){
				/* 决定元素的排列顺序 */
				order: 3;
			}
			li:nth-child(2){
				background-color: pink;
				/* flex-grow: 2; */
			}
			li:nth-child(3){
				background-color: orange;
				/* flex-grow: 3; */
			}
		</style>
	</head>
	<body>
		<ul>
			<li>1</li>
			<li>2</li>
			<li>3</li>
		</ul>
	</body>
</html>

```

### 三、淘宝手机导航练习

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224205602502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<style>
		.nav{
			width: 100%
		}
		/* 设置每一行的容器 */
		.nav-inner{
			/* 设置为弹性容器 */
			display: flex;
			justify-content: space-around;
		}
		.item{
			/* flex:auto; */
			width: 18%;
			text-align: center;
		}
		.item img{
			width: 100%;
		}
		.item a{
			color: #333;
			text-decoration: none;
			font-size: 16px;
		}
			
	</style>
</head>
<body>
	<!-- 创建一个外部容器 -->
	<nav class="nav">
		<div class="nav-inner">
			<div class="item"><a href="#"><img src="taobaoImage/01.png" alt=""><span>天猫</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/02.png" alt=""><span>今日爆款</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/03.png" alt=""><span>天猫国际</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/04.png" alt=""><span>饿了么</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/05.png" alt=""><span>天猫超市</span></a></div>

		</div>
		<div class="nav-inner">
			<div class="item"><a href="#"><img src="taobaoImage/06.png" alt=""><span>充值中心</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/07.png" alt=""><span>机票酒店</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/08.png" alt=""><span>金币庄园</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/09.png" alt=""><span>阿里拍卖</span></a></div>
			<div class="item"><a href="#"><img src="taobaoImage/10.png" alt=""><span>淘宝吃货</span></a></div>
			
		</div>
	</nav>
</body>
</html>
```



### 一、像素、视口介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224210946994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224211542822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224214927283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210224220210413.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022422055355.png)

### 二、手机页面练习

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title></title>
	<link rel="stylesheet" type="text/css" href="css/style.css"/>
	<link rel="stylesheet" href="77.图标字体/fa/css/all.css">
</head>
<body>
	<!-- 创建头部容器 -->
	<header class="top-bar">
		<div class="menu-btn"><a href="#"><i class="fas fa-stream"></i></a></div>
		<h1 class="logo"><a href="#">爱学习</a></h1>
		<div class="search-btn"><a href="#"><i class="fas fa-search"></i></a></div>
	</header>
	<!-- 创建banner -->
	<div class="banner"><a href="#"><img src="mobileprac/banner.png" ></a></div>
	<!-- 菜单 -->
	<nav class="menu">
		<a href="#" class="course"><i class="fas fa-book"></i>我的课程</a>
		<a href="#" class="star"><i class="fas fa-cut"></i>明星讲师</a>
		<a href="#" class="sub"><i class="fas fa-globe"></i>我的订阅</a>
		<a href="#" class="download"><i class="fas fa-envelope"></i>我的下载</a>
	</nav>
	<!-- 课程列表 -->
	<div class="course-list">
		<!-- 列表标题 -->
		<div class="title">
			<h2>最新课程</h2>
			<a href="#" class="more">更多+</a>
		</div>
		<!-- 列表容器 -->
		<div class="item-list">
			<div class="item">
				<!-- 封面 -->
				<div class="cover"><img src="mobileprac/pic01.jpg" alt=""></div>
				<!-- 小标题 -->
				<h3 class="course-title">摄影课程</h3>
				<!-- 用户信息 -->
				<div class="user-info">
					<div class="avatar"><img src="mobileprac/user-image.jpg" alt=""></div>
					<div class="nickname">令狐冲</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>
```

```css
// 使用的是less
*{
	margin: 0;
	padding: 0;
}
@total-width:750;
.w{
	width: 693/40rem;
	margin: 0 auto;
}
html{
	// 设置rem比值
	font-size: 100vw/@total-width * 40;
	background-color: #eff0f4;
}
a{
	text-decoration: none;
}
// 设置头部
.top-bar:extend(.w){
	display: flex;
	height: 175/40rem;
	line-height: 175/40rem;
	// 设置对齐方式
	justify-content: space-between;
	// 设置辅轴的对齐方式
	align-items: center;
	a{
		color: #24253d;
		font-size: 50/40rem;
		i{
			color: #999;
			font-size: 40/40rem;
		}
	}
}
// 设置banner
.banner:extend(.w){
	overflow: hidden;
	img{
		width: 100%;
	}
}
// 设置中间菜单
.menu:extend(.w){
	// 确定元素的高度
	height: 329/40rem;
	
	// 设置弹性元素
	display: flex;
	// 设置框的大小
	// 设置换行
	flex-flow:row wrap; 
	justify-content: space-between;
	align-content: space-around;
	a{
		width: 327/40rem;
		height: 104/40rem;
		line-height: 104/40rem;
		color: white;
		border-radius: 10/40rem;
		i{
			margin: 0 20/40rem 0 38/40rem;
		}
	}

	.course{
		background-color: #f97053;
	}
	.star{
		background-color: #cd6efe;
	}
	.sub{
		background-color: #fe4479;
	}
	.download{
		background-color: #1bc4fb;
	}
}

// 设置课程列表
.course-list:extend(.w){
	height: 394/40rem;
	display: flex;
	flex-flow: column;
	justify-content: space-between;
	margin-bottom: 46px/40rem;
	.title{
		display: flex;
		justify-content: space-between;
		align-items: center;
		h2{
			font-size: 33/40rem;
			color: #24253D;
			border-left: 2/40rem solid #3a84ff;
			padding-left: 4/40rem;
		}
		a{
			font-size: 28/40rem;
			color: #656565;
		}
	}
}

// 设置item
.item{
	width: 320/40rem;
	height: 350/40rem;
	background-color: #fff;
	box-shadow: 0 0 10px/40rem rgba(0,0,0,.3);
	overflow: hidden;
	border-radius: 10/40rem;
	padding: 0 22/40rem;
	display: flex;
	flex-flow: column;
	justify-content: space-evenly;
	.cover{
		overflow: hidden;
		// padding-top: 15/40rem;
	}
	img{
		width: 100%;
		vertical-align: top;
	}
	.course-title{
		font-size: 32/40rem;
		color: #24253D;
	}
	.user-info{
		display: flex;
		align-items: center;
	}
	.avatar{
		width: 42/40rem;
		height: 42/40rem;
		border-radius: 50%;
		overflow: hidden;
	}
	.nickname{
		font-size: 24/40rem;
		color: #969693;
	}
}
```



### 一、媒体查询介绍

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210227074630439.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MjczNzI3,size_16,color_FFFFFF,t_70)

### 二、语法

```html
		<style type="text/css">
			@media only screen and (min-width:500px) and (max-width:700px) {
				body{
					background-color: #bfa;
				}
			}
		</style>
```

### 三、练习：响应式导航条

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<link rel="stylesheet" type="text/css" href="../54.布局作业/01/reset.css" />
		<link rel="stylesheet" type="text/css" href="../77.图标字体/fa/css/all.css" />
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<!-- 
		 响应式设计的网页：
			移动端优先；
			渐进增强；
		 -->
		<div class="topbar-wrapper">
			<!-- 外部容器 -->
			<div class="top-bar">
				<!-- 左侧的菜单栏 -->
				<div class="left-menu">
					<!-- 创建菜单图标 -->
					<ul class="menu-icon">
						<li></li>
						<li></li>
						<li></li>
					</ul>
					<!-- 创建菜单 -->
					<ul class="nav">
						<li><a href="#">手机</a></li>
						<li><a href="#">美容仪器</a></li>
						<li><a href="#">配件</a></li>
						<li><a href="#">服务支撑</a></li>
						<li><a href="#">企业网站</a></li>
						<li>
							<a href=""><i class="fas fa-search"></i></a>
							<span>搜索 Meitu.com</span>
						</li>
					</ul>
				</div>
				<!-- logo -->
				<h1 class="logo">
					<a href="#">美图手机</a>
				</h1>
				<!-- 用户信息 -->
				<div class="user-info">
					<a href="#">
						<i class="fa fa-user"></i>
					</a>
				</div>
			</div>
		</div>
	</body>
</html>

```

```css
a{
	text-decoration: none;
	color: #fff;
	&:hover{
		color: rgb(197,196,196);
	}
}
.topbar-wrapper{
	background-color: #000000;
}
// 导航条外部容器
.top-bar{
	max-width: 1200px;
	margin: 0 auto;
	height: 48px;
	background-color: #000000;
	padding: 0 14px;
	display: flex;
	align-items: center;
	justify-content: space-between;
}

.left-menu{
	// position: relative;
	&:hover{
		.nav{
			display: block;
		}
	}
	.nav{
		display: none;
		position: absolute;
		top: 48px;
		background-color: #000;
		left:0;
		right:0;
		bottom: 0;
		padding-top: 60px;
		li{
			width: 80%;
			margin: 0 auto;
			border-bottom: 1px solid #4e4e4e;
			a{
				display: block;
				line-height: 44px;
				font-size: 14px;
			}
			&:last-child a{
				display: inline-block;
				margin-right: 6px;
			}
			span{
				color: #fff;
				font-size: 14px;
			}
		}
	}
	.menu-icon{
		// background-color: #bfa;
		width: 18px;
		height: 48px;
		position: relative;
		li{
			width: 18px;
			height: 1px;
			background-color: #fff;
			position: absolute;
			// 修改变形原点
			transform-origin: left center;
			transition: all 0.5s;
		}
		li:nth-child(1){
			top: 18px;
		}
		li:nth-child(2){
			top: 24px;
		}
		li:nth-child(3){
			top: 30px;
		}
		&:hover{
			li:nth-child(1){
				// 向下旋转
				transform: rotateZ(40deg);
			
			}
			li:nth-child(2){
				opacity: 0;
			}
			li:nth-child(3){
				transform: rotateZ(-40deg);
			}

		}
	}
}
// 设置logo
.logo{
	a{
		display: block;
		width: 122px;
		height: 32px;
		background-image: url(images/dff63979.sprites-index@2x.png);
		background-size: 400px 400px;
		text-indent: -9999px;
	}
}
// 设置媒体查询
@media only screen {
	// 断点768px
	@media (min-width: 768px){
		.left-menu{
			order: 2;
			// 显示菜单
			flex: auto;
			.nav{
				display: flex;
				position: static;
				padding: 0;
				justify-content: space-around;
				li{
					width: auto;
					border-bottom: none;
					margin: 0;
					a{
						line-height: 48px;
						
					}
					span{
						display: none;
					}
				}
			}
			// 隐藏菜单图标
			.menu-icon{
				display: none;
			}
			
		}
		.logo{
			order: 1;
		}
		.user-info{
			order: 3;
		}
	}
}
```