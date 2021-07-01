<template>
  <div class="tab-bar-item" @click="itemClick">
    <div v-if="!isActive">
      <slot name="slot-img"></slot>
    </div>

    <div v-else>
      <slot name="slot-img-active"></slot>
    </div>

    <div :style="colorChange">
      <slot name="slot-text"></slot>
    </div>
  </div>
</template>

<script>
    export default {
        name: "TabBarItem",
        props: {
          path: String,
          color: {
            type: String,
            default: 'green'
          }
        },
        methods: {
          itemClick() {
            // console.log(this.$route.matched[0].path,this.path)
            if(this.$route.matched[0].path != this.path) {
              this.$router.replace(this.path)
            }
            // this.$router.replace(this.path)

          }
        },
        computed: {
          isActive() {
            return this.$route.path.indexOf(this.path) != -1
          },
          colorChange() {
            return this.isActive ? {color: this.color} : {}
          }
        }
    }
</script>

<style scoped>
  .tab-bar-item {
    flex: 1;
    text-align: center;
    font-size: 14px;
    height: 49px;
  }
  .tab-bar-item img{
    width: 24px;
    height: 24px;
    vertical-align: middle;
    margin-top: 3px;
    margin-bottom: 2px;
  }
</style>
