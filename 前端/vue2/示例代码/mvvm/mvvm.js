// mvvm.js
class MVVM {
    constructor(options) {
      this.$el = options.el
      this.$data = options.data
      // 如果有要编译的模板 =>编译
      if(this.$el) {
        // 将文本+元素模板进行编译
        new Compile(this.$el, this)
      }
    }
  }