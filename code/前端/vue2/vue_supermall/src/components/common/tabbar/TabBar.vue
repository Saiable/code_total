<template>
  <div class="tab-bar">
    <slot></slot>
  </div>
</template>

<script>
    export default {
        name: "TabBar",
    }
</script>

<style scoped>
  .tab-bar{
    display: flex;
    background-color: #e9e9e9;

    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;

    box-shadow: 0px -3px 1px rgba(100,100,100,0.1);
  }
</style>
