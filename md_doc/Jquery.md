[TOC]

[文本教程](https://www.runoob.com/jquery/jquery-tutorial.html)

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

#### jQuery 效果- 隐藏和显示

隐藏、显示、切换，滑动，淡入淡出，以及动画

##### hide() 和 show()

`$(selector).hide(speed,callback);`

`$(selector).show(speed,callback);`

