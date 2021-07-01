<template>
  <div class="goods">
    <good-list-item v-for="item in goods" :goods-item="item"></good-list-item>
  </div>
</template>

<script>
    import GoodListItem from "@/components/content/goods/GoodListItem";
    export default {
        name: "GoodsList",
        props: {
          goods: {
            type: Array,
            default() {
              return []
            }
          }
        },
        components: {
          GoodListItem
        }
    }
</script>

<style scoped>
  .goods {
    /*width: 100%;*/
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }
</style>
