<template>
  <div class="wrapper" ref="wrapper">
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
    import BScroll from 'better-scroll'
    export default {
        name: "Scroll",
        data() {
          return {
            scroll: null
          }
        },
        props: {
          probeType:{
            type: Number,
            default: 0
          },
          pullUpLoad: {
            type: Boolean,
            default: false
          }
        },
        methods: {
          scrollTo(x, y, time=300) {
            this.scroll && this.scroll.scrollTo(x,y,time)
          },
          finishPullUp(){
            this.scroll.finishPullUp()
          },
          refresh() {
            // console.log('111')
            this.scroll && this.scroll.refresh()
          },
          finishPullUp() {
            this.scroll && this.scroll.finishPullUp()
          },
          getScrollY() {
            return this.scroll?this.scroll.y:0
          }
        },
        mounted() {
          this.scroll = new BScroll(this.$refs.wrapper, {
            click: true,
            probeType: this.probeType,
            pullUpLoad: this.pullUpLoad
          })

          //监听滚动的位置
          if(this.probeType === 2 || this.probeType === 3) {
            this.scroll.on('scroll', (position) => {
              // console.log(position)
              this.$emit('scroll',position)
            })
          }

          // //监听上拉事件
          // this.scroll.on('pullingUp', () => {
          //   // console.log('up')
          //   this.$emit('pullingUp')
          // })

          // 3.监听scroll滚动到底部
          if(this.pullUpLoad) {
            this.scroll.on('pullingUp',() => {
              // console.log('aa');
              this.$emit('pullingUp')
            })
          }
        }
    }
</script>

<style scoped>

</style>
