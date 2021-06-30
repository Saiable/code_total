[TOC]

[文本教程来源](https://www.runoob.com/jquery/jquery-tutorial.html)

[官网下载](https://jquery.com/download/)

#### 概览

查看jQuery 使用版本，控制台输入：$.fn.jquery

文档就绪事件，这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码，即在 DOM 加载完成后才可以对 DOM 进行操作。
```javascript
$(function(){
 
   // 开始写 jQuery 代码...
 
});
```
#### jQuery 选择器
它基于已经存在的 CSS 选择器，除此之外，它还有一些自定义的选择器。

jQuery 中所有选择器都以美元符号开头：$()。

#### jQuery 事件
jQuery 是为事件处理特别设计的。

常见 DOM 事件：

| **鼠标事件**                                                 | **键盘事件**                                                 | **表单事件**                                              | **文档/窗口事件**                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------- |
| [click](https://www.runoob.com/jquery/event-click.html)      | [keypress](https://www.runoob.com/jquery/event-keypress.html) | [submit](https://www.runoob.com/jquery/event-submit.html) | [load](https://www.runoob.com/jquery/event-load.html)     |
| [dblclick](https://www.runoob.com/jquery/event-dblclick.html) | [keydown](https://www.runoob.com/jquery/event-keydown.html)  | [change](https://www.runoob.com/jquery/event-change.html) | [resize](https://www.runoob.com/jquery/event-resize.html) |
| [mouseenter](https://www.runoob.com/jquery/event-mouseenter.html) | [keyup](https://www.runoob.com/jquery/event-keyup.html)      | [focus](https://www.runoob.com/jquery/event-focus.html)   | [scroll](https://www.runoob.com/jquery/event-scroll.html) |
| [mouseleave](https://www.runoob.com/jquery/event-mouseleave.html) |                                                              | [blur](https://www.runoob.com/jquery/event-blur.html)     | [unload](https://www.runoob.com/jquery/event-unload.html) |
| [hover](https://www.runoob.com/jquery/event-hover.html)      |                                                              |                                                           |                                                           |

在 jQuery 中，大多数 DOM 事件都有一个等效的 jQuery 方法。

#### jQuery 效果

隐藏、显示、切换，滑动，淡入淡出，以及动画

##### jQuery 效果- 隐藏和显示

hide() 和 show()

`$(selector).hide(speed,callback);`

`$(selector).show(speed,callback);`

```javascript
$(document).ready(function(){
  $(".hidebtn").click(function(){
    $("div").hide(1000,"linear",function(){
      alert("Hide() 方法已完成!");
    });
  });
});
```

第二个参数是一个字符串，表示过渡使用哪种缓动函数。（译者注：jQuery自身提供"linear" 和 "swing"，其他可以使用相关的插件）。

jQuery toggle()

`$(selector).toggle(speed,callback);`

##### jQuery 效果 - 淡入淡出

jQuery fadeIn() 用于淡入已隐藏的元素。

jQuery fadeOut() 方法用于淡出可见元素。

jQuery fadeToggle() 方法可以在 fadeIn() 与 fadeOut() 方法之间进行切换。

jQuery fadeTo() 方法允许渐变为给定的不透明度（值介于 0 与 1 之间）。



一、注意大小写，fadeIn()  fadeOut()  fadeToggle()  fadeTo() 大小写不能变。

二、fadeTo() 没有默认参数，必须加上 slow/fast/Time

##### jQuery 效果 - 滑动

jQuery slideDown() 方法用于向下滑动元素。

jQuery slideUp() 方法用于向上滑动元素。

jQuery slideToggle() 方法可以在 slideDown() 与 slideUp() 方法之间进行切换。

##### jQuery 效果- 动画

jQuery animate() 方法允许您创建自定义的动画。

```
默认情况下，所有 HTML 元素都有一个静态位置，且无法移动。
如需对位置进行操作，要记得首先把元素的 CSS position 属性设置为 relative、fixed 或 absolute！
```

生成动画的过程中可同时使用多个属性：

```javascript
$("button").click(function(){
  $("div").animate({
    left:'250px',
    opacity:'0.5',
    height:'150px',
    width:'150px'
  });
});
```

```
可以用 animate() 方法来操作所有 CSS 属性吗？

是的，几乎可以！不过，需要记住一件重要的事情：当使用 animate() 时，必须使用 Camel 标记法书写所有的属性名，比如，必须使用 paddingLeft 而不是 padding-left，使用 marginRight 而不是 margin-right，等等。

同时，色彩动画并不包含在核心 jQuery 库中。

如果需要生成颜色动画，您需要从 jquery.com 下载 颜色动画 插件。
```

也可以定义相对值（该值相对于元素的当前值）。需要在值的前面加上 += 或 -=

您甚至可以把属性的动画值设置为 "show"、"hide" 或 "toggle"：

```javascript
$("button").click(function(){
  $("div").animate({
    height:'toggle'
  });
});
```

默认地，jQuery 提供针对动画的队列功能。

这意味着如果您在彼此之后编写多个 animate() 调用，jQuery 会创建包含这些方法调用的"内部"队列。然后逐一运行这些 animate 调用。

```javascript
$("button").click(function(){
  var div=$("div");
  div.animate({height:'300px',opacity:'0.4'},"slow");
  div.animate({width:'300px',opacity:'0.8'},"slow");
  div.animate({height:'100px',opacity:'0.4'},"slow");
  div.animate({width:'100px',opacity:'0.8'},"slow");
});
```

下面的例子把` <div> `元素往右边移动了 100 像素，然后增加文本的字号：

```javascript
$("button").click(function(){
  var div=$("div");
  div.animate({left:'100px'},"slow");
  div.animate({fontSize:'3em'},"slow");
});
```

##### jQuery 动画实现原理

**队列操作**

jquery中有一个Queue队列的接口，这个模块没有单独拿出来作为一个章节是因为这个是内部专门为动画服务的，Queue队列如同data数据缓存与Deferred异步模型一样，都是jQuery库的内部实现的基础设施

Queue队列

队列是一种特殊的线性表，只允许在表的前端（队头）进行删除操作（出队），在表的后端（队尾）进行出入操作（入队），队列的特点是先进先出，最先插入的元素最先被删除。

为什么要引入队列

```
var a = 1;
setTimeout(function(){
　　a=2;
},0)
alert(a);
```

我们一直习惯于线性的编写代码逻辑，但是在JavaScript编程几乎总是伴随着异步操作：

setTImeout，css3Transition/Animation,ajax,dom的绘制，postmessage，web Database 等等，大量异步操作所带来的回调函数会把我们的算法分解，**对于“异步+回调”的模式，怎么“拉平”异步操作使之跟同步一样，因为异步操作进行流程控制的时候无非避免的要嵌套大量的回调逻辑，所以就会出现 promises 约定了。**

那么 jQuery 引入队列其实从一个角度上可以认为：**允许一系列函数被异步地调用而不会阻塞程序**。

看一个代码段：

```
$("#Aaron").slideUp().fadeIn()
```

这是 jQuery 的一组动画链式序列，它的内部其实就是一组队列 Queue，所以队列和 Deferred 地位类似，是一个内部使用的基础设施。

- 当 slideUp 运行时，fadeIn 被放到 fx 队列中
- 当 slideUp 完成后，从队列中被取出运行

Queue 函数允许直接操作这个链式调用的行为，同时 Queue 可以指定队列名称获得其他能力而不局限于 fx 队列。

jQuery 提供了 2 组队列操作的 API：

```
jQuery.queue/dequeue
jQuery.fn.queue/dequeue
```

但是不同与普通队列定义的是：

- jQuery.queue 和 jQuery.fn.queue 不仅执行出队操作返回队头元素，还会自动执行返回的队头元素
- fn 是扩展在原型上的高级API是提供给实例使用的
- .queue/.dequeue 其内部是调用的 .queue，.dequeue 静态的底层方法实现入列与出列

**动画调度**

对于 jQuery 的动画的设计我们要分 2 个层面理解：

1. 每一个动画效果可以看作一个独立的动画对象，每个对象都实现了针对自己这个动画的生命周期的控制
2. 动画对象与动画对象之间其实是没有直接关系，但是为了做到连续调用就需要引入一套队列机制也就是 Queue 来控制对象之间的转换的控制

动画的源码：

```
animate: function(prop, speed, easing, callback) {
   doAnimation = function() {
      var anim = Animation(this, args, optall);
   };
   this.queue(optall.queue, doAnimation);
}
```

这个代码缩减了，但是我们上面提到的最重要的 2 点这里都涉及到了：通过 queue 调度动画的之间的衔接，Animation 方法执行单个动画的封装。

jQuery 在 queue 的调度上涉及了一个关键的处理：同步与异步代码同时执行，同步收集动画序列，异步调用序列，看看整个调用的流程是这样的：

1. 通过多个 animate 方法形成动画链，那么这个动画链其实都是会加入到 queue 队列里面
2. 在每一次 queue 方法中会把动画数据写到队列中，然后取出队列中的第一个序列通过 dequeue 方法执行
3. 开始执行之前写一个进程锁“inprogress”到 queue 里面，代表这个动画还在执行中，防止同个序列的多个动画重复执行，这个就是异步执行同步收集的处理方案
4. 此时动画开始了，这里注意动画是在异步执行的同步的代码，继续调用下一个 animate
5. 执行同样的 animate 方法逻辑但是此时问题来了，动画可能还在执行可是后续的 animate 还在继续调用，所以这个时候后面的动画代码就需要等待了（进程锁）
6. 队列头是有一把“inprogress”进程锁的，那么这时候动画只需要加入队列，但是可以通过 inprogress 是否存在来判断是否执行
7. 所有的 animate 方法在加入队列都是按照以上的逻辑依次执行，动画执行完毕了就会有一个结束通知，然后从 queue 取出第一个队列继续执行了，如此循环

以上是整个动画的调度一个流程，其实都是利用队列异步的空闲然后执行同步的代码，这样在处理上是没有浪费资源的，而且精确度也是最高的。

##### jQuery 停止动画

jQuery stop() 方法用于停止动画或效果，在它们完成之前。

stop() 方法适用于所有 jQuery 效果函数，包括滑动、淡入淡出和自定义动画。

##### jQuery Callback 方法

##### jQuery - 链(Chaining)

```javascript
$("#p1").css("color","red").slideUp(2000).slideDown(2000);
```

#### jQuery HTML

##### jQuery - 获取内容和属性

##### jQuery - 设置内容和属性

jQuery 中非常重要的部分，就是操作 DOM 的能力。

jQuery 提供一系列与 DOM 相关的方法，这使访问和操作元素和属性变得很容易。

三个简单实用的用于 DOM 操作的 jQuery 方法：

- text() - 设置或返回所选元素的文本内容
- html() - 设置或返回所选元素的内容（包括 HTML 标记）
- val() - 设置或返回表单字段的值

jQuery attr() 方法用于获取属性值。

下面的例子演示如何通过 text()、html() 以及 val() 方法来设置内容：

```javascript
$("#btn1").click(function(){
    $("#test1").text("Hello world!");
});
$("#btn2").click(function(){
    $("#test2").html("<b>Hello world!</b>");
});
$("#btn3").click(function(){
    $("#test3").val("RUNOOB");
});
```

text()、html() 以及 val()，同样拥有回调函数。回调函数有两个参数：被选元素列表中当前元素的下标，以及原始（旧的）值。然后以函数新值返回您希望使用的字符串。

下面的例子演示带有回调函数的 text() 和 html()：

```javascript
$("#btn1").click(function(){
    $("#test1").text(function(i,origText){
        return "旧文本: " + origText + " 新文本: Hello world! (index: " + i + ")"; 
    });
});
 
$("#btn2").click(function(){
    $("#test2").html(function(i,origText){
        return "旧 html: " + origText + " 新 html: Hello <b>world!</b> (index: " + i + ")"; 
    });
});
```

jQuery attr() 方法也用于设置/改变属性值：

```javascript
$("button").click(function(){
  $("#runoob").attr("href","http://www.runoob.com/jquery");
});
```

下面的例子演示如何同时设置 href 和 title 属性：

```javascript
$("button").click(function(){
    $("#runoob").attr({
        "href" : "http://www.runoob.com/jquery",
        "title" : "jQuery 教程"
    });
});
```

jQuery 方法 attr()，也提供回调函数。回调函数有两个参数：被选元素列表中当前元素的下标，以及原始（旧的）值。然后以函数新值返回您希望使用的字符串。

##### jQuery - 添加元素

我们将学习用于添加新内容的四个 jQuery 方法：

- append() - 在被选元素的结尾插入内容
- prepend() - 在被选元素的开头插入内容
- after() - 在被选元素之后插入内容
- before() - 在被选元素之前插入内容

##### jQuery - 删除元素

如需删除元素和内容，一般可使用以下两个 jQuery 方法：

- remove() - 删除被选元素（及其子元素）
- empty() - 从被选元素中删除子元素

jQuery remove() 方法也可接受一个参数，允许您对被删元素进行过滤。

该参数可以是任何 jQuery 选择器的语法。

下面的例子删除 class="italic" 的所有 <p> 元素：

```javascript
$("p").remove(".italic");
```

##### jQuery - 获取并设置 CSS 类

jQuery 拥有若干进行 CSS 操作的方法。我们将学习下面这些：

- addClass() - 向被选元素添加一个或多个类
- removeClass() - 从被选元素删除一个或多个类
- toggleClass() - 对被选元素进行添加/删除类的切换操作
- css() - 设置或返回样式属性

设置多个 CSS 属性，请使用如下语法：

```javascript
$("p").css({"background-color":"yellow","font-size":"200%"});
```

##### jQuery 尺寸

jQuery 提供多个处理尺寸的重要方法：

- width()
- height()
- innerWidth()
- innerHeight()
- outerWidth()
- outerHeight()

![jQuery Dimensions](https://www.runoob.com/images/img_jquerydim.gif)

唯一需要注意的地方，设置了 box-sizing 后，width() 获取的是 css 设置的 width 减去 padding 和 border 的值。

```
.test{width:100px;height:100px;padding:10px;border:10px;box-sizing:border-box;}
```

-  width() 获取为: 60
-  innerWidth() 获取值为: 80
-  outWidth() 获取值为: 100

#### jQuery 遍历

jQuery 遍历，意为"移动"，用于根据其相对于其他元素的关系来"查找"（或选取）HTML 元素。以某项选择开始，并沿着这个选择移动，直到抵达您期望的元素为止。

下图展示了一个家族树。通过 jQuery 遍历，您能够从被选（当前的）元素开始，轻松地在家族树中向上移动（祖先），向下移动（子孙），水平移动（同胞）。这种移动被称为对 DOM 进行遍历。

![jQuery Dimensions](https://www.runoob.com/images/img_travtree.png)

jQuery 提供了多种遍历 DOM 的方法。

遍历方法中最大的种类是树遍历（tree-traversal）。

接下来会讲解如何在 DOM 树中向上、下以及同级移动。

##### jQuery 遍历 - 祖先

祖先是父、祖父或曾祖父等等。

通过 jQuery，您能够向上遍历 DOM 树，以查找元素的祖先。

这些 jQuery 方法很有用，它们用于向上遍历 DOM 树：

- parent()
- parents()
- parentsUntil()

parent() 方法返回被选元素的直接父元素。

该方法只会向上一级对 DOM 树进行遍历。

下面的例子返回每个` <span> `元素的直接父元素：

```javascript
$(document).ready(function(){
  $("span").parent();
});
```

您也可以使用可选参数来过滤对祖先元素的搜索。

下面的例子返回所有` <span>` 元素的所有祖先，并且它是` <ul> `元素：

```javascript
$(document).ready(function(){
  $("span").parents("ul");
});
```

parentsUntil() 方法返回介于两个给定元素之间的所有祖先元素。

下面的例子返回介于` <span> `与 `<div> `元素之间的所有祖先元素：

```javascript
$(document).ready(function(){
  $("span").parentsUntil("div");
});
```

##### jQuery 遍历 - 后代

下面是两个用于向下遍历 DOM 树的 jQuery 方法：

- children()
- find()

返回` <div> `的所有后代：

```javascript
$(document).ready(function(){
  $("div").find("*");
});
```

##### jQuery 遍历 - 同胞(siblings)

