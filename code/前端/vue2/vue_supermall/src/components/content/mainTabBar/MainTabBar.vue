<template>
    <tab-bar>
      <tab-bar-item path="/home" color="#FF6699">
        <img slot="slot-img" src="~assets/img/tabbar/home.svg" alt="">
        <img slot="slot-img-active" src="~assets/img/tabbar/home_activate_pink.svg" alt="">
        <div slot="slot-text" >首页</div>
      </tab-bar-item>
<!--      <tab-bar-item path="/category" color="darkblue">-->
      <tab-bar-item path="/category" color="#FF6699">
        <img slot="slot-img" src="~assets/img/tabbar/category.svg" alt="">
        <img slot="slot-img-active" src="~assets/img/tabbar/category_activate_pink.svg" alt="">
        <div slot="slot-text" >分类</div>
      </tab-bar-item>
      <tab-bar-item path="/cart" color="#FF6699">
        <img slot="slot-img" src="~assets/img/tabbar/shopping.svg" alt="">
        <img slot="slot-img-active" src="~assets/img/tabbar/shopping_activate_pink.svg" alt="">
        <div slot="slot-text" >购物车</div>
      </tab-bar-item>
      <tab-bar-item path="/profile" color="#FF6699">
        <img slot="slot-img" src="~assets/img/tabbar/profile.svg" alt="">
        <img slot="slot-img-active" src="~assets/img/tabbar/profile_activate_pink.svg" alt="">
        <div slot="slot-text" >我的</div>
      </tab-bar-item>
    </tab-bar>

</template>

<script>
    import TabBar from "components/common/tabbar/TabBar.vue";
    import TabBarItem from "components/common/tabbar/TabBarItem.vue";
    export default {
        name: "MainTabBar",
        components: {
          TabBar,
          TabBarItem
        }
    }
</script>

<style scoped>

</style>
