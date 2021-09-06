<template>
  <div id="home">
    <nav-bar class="home-nav"><div slot="center">购物街</div></nav-bar>
    <tab-control :titles="['流行','新款','精选']" @tabClick="tabClick" ref="tabControl1" class="tab-control" v-show="isTabFixed"></tab-control>
    <scroll class="content" ref="scroll" :probe-type="3" @scroll="contentScroll" :pull-up-load="true" @pullingUp="loadMore">
      <home-swiper :banners="banners" @swiperImageLoad="swiperImageLoad"></home-swiper>
      <home-recomend-view :recommends="recommends"></home-recomend-view>
      <feature-view></feature-view>
      <tab-control :titles="['流行','新款','精选']" @tabClick="tabClick" ref="tabControl2"></tab-control>
      <goods-list :goods="showGoods"></goods-list>
    </scroll>

    <back-top @click.native="backClick" v-show="isShowBackTop"></back-top>
<!--    <div class="temp"></div>-->
  </div>
</template>

<script>
  import NavBar from "components/common/navBar/NavBar";
  import TabControl from "@/components/common/tabControl/TabControl";
  import Scroll from '@/components/common/scroll/Scroll';
  import GoodsList from "@/components/content/goods/GoodsList";

  import HomeSwiper from "views/home/childrenComponents/HomeSwiper";
  import HomeRecomendView from "@/views/home/childrenComponents/HomeRecomendView";
  import FeatureView from "@/views/home/childrenComponents/FeatureView";

  import {getHomeMultidata, getHomeGoods} from 'network/home';
  import {debounce} from "@/common/utils";
  import {itemListenerMixin,backTopMixin} from "@/common/mixin";

  export default {
        name: "Home",
        components: {
          Scroll,
          NavBar,
          TabControl,
          HomeSwiper,
          HomeRecomendView,
          FeatureView,
          GoodsList
        },
        data() {
          return{
            banners: [],
            recommends: [],
            goods: {
              'pop': {page: 0, list: []},
              'new': {page: 0, list: []},
              'sell': {page: 0, list: []}
            },
            currentType: 'pop',
            tabOffsetTop: 0,
            isTabFixed: false,
            saveY: 0
          }
        },
        mixins: [itemListenerMixin,backTopMixin],
        computed: {
          showGoods() {
            return this.goods[this.currentType].list
          }
        },
        destroyed() {
          console.log('des')
        },
        activated() {
          // this.$refs.scroll.scrollTo(0,this.saveY,0)
          // this.$refs.scroll.scrollTo(0,this.saveY,0)
          // this.$refs.scroll.refresh()
          // console.log('activated')
          this.$refs.scroll.refresh()
          this.$refs.scroll.scrollTo(0,this.saveY,0)
        },
        deactivated() {
          // this.saveY = this.$refs.scroll.getScrollY()
          // console.log('deactivated')
          //1.保存Y值
          this.saveY = this.$refs.scroll.getScrollY()

          //2.取消全局事件的监听
          this.$bus.$off('itemImageLoad', this.itemImageListener)
        },
        created() {
          //1. 请求多个数据
          this.getHomeMultidata()

          //2.请求goods数据
          this.getHomeGoods('pop')
          this.getHomeGoods('new')
          this.getHomeGoods('sell')
        },
        mounted() {
        },
        methods: {
          /**
           * 事件监听相关的方法
           */
          swiperImageLoad() {
            //获取tabControl的offsetTop
            //所有组件都有一个$el属性，用于获取元素的
            // console.log(this.$refs.tabControl.$el.offsetTop)
            this.tabOffsetTop = this.$refs.tabControl2.$el.offsetTop
          },
          loadMore() {
            // console.log('bb');
            this.getHomeGoods(this.currentType)
          },
          tabClick(index) {
            // console.log(index)
            switch (index) {
              case 0:
                this.currentType = 'pop'
                break
              case 1:
                this.currentType = 'new'
                break
              case 2:
                this.currentType = 'sell'
                break

            // this.currentType = Object.keys(this.goods)[index]
            }

            this.$refs.tabControl1.currentIndex = index
            this.$refs.tabControl2.currentIndex = index
          },

          contentScroll(position) {
            //1.判断BackTop是否显示
            // console.log(position)
            // position < 1000
            this.isShowBackTop = (-position.y) > 1000

            //2.决定tabControl是否吸顶
            this.isTabFixed = (-position.y) > this.tabOffsetTop
          },

          // loadMore(){
          //   // console.log('aa')
          //   this.getHomeGoods(this.currentType)
          //   this.$refs.scroll.scroll.refresh()
          // },
          /**
           * 网络请求相关的方法
           */
          getHomeMultidata() {
            getHomeMultidata().then(res => {
              // console.log(res)
              this.banners = res.data.banner.list
              this.recommends = res.data.recommend.list
            })
          },
          getHomeGoods(type) {
            const page = this.goods[type].page + 1
            getHomeGoods(type,page).then(res => {
              // console.log(res)
              this.goods[type].list.push(...res.data.list)
              this.goods[type].page += 1

              this.$refs.scroll.finishPullUp()
            })
          }
        }

    }
</script>

<style scoped>
  #home{
    /*padding-top: 44px;*/
    height: 100vh;

    position: relative;
  }
  .home-nav {
    background-color: var(--color-tint);
    color: white;

    /*position: fixed;*/
    /*top: 0;*/
    /*left: 0;*/
    /*right: 0;*/
    /*z-index: 9;*/
  }

  /*.temp {*/
  /*  height: 900px;*/
  /*}*/
  /*.tab-control{*/
  /*  position: sticky;*/
  /*  top: 44px;*/
  /*  background-color: #ffffff;*/
  /*}*/

  .content{
    /*height: calc(100% - 93px);*/
    /*overflow: hidden;*/
    /*margin-top: 44px;*/


    /*height: 300px;*/
    overflow: hidden;
    position: absolute;
    top: 44px;
    bottom: 49px;
    left: 0;
    right: 0;
  }

  /*.fixed{*/
  /*  position: fixed;*/
  /*  left: 0;*/
  /*  right: 0;*/
  /*  top: 44px;*/
  /*}*/
  .tab-control{
    position: relative;
    z-index: 9;
    background-color: white;
  }
</style>
