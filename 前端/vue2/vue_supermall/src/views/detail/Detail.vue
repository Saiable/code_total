<template>
    <div id="detail">
      <detail-nav-bar class="detail-nav" @titleClick="titleClick" ref="nav"></detail-nav-bar>
      <scroll class="content" ref="scroll" :probe-type="3" @scroll="contentScroll">
        <detail-swiper :top-images="topImages"></detail-swiper>
        <detail-base-info :goods="goods"></detail-base-info>
        <detail-shop-info :shop-info="shop"></detail-shop-info>
        <detail-goods-info :goods-info="detailInfo" @goodsInfoImgLoad="imageLoad"></detail-goods-info>
        <detail-goods-params ref="params" :goodsParams="paramInfo"></detail-goods-params>
        <detail-comment-info ref="comment" :commentInfo="commentInfo"></detail-comment-info>
        <goods-list ref="recommend" :goods="recommends"></goods-list>
      </scroll>
      <detail-bottom-bar></detail-bottom-bar>

      <back-top @click.native="backClick" v-show="isShowBackTop"></back-top>
    </div>
</template>

<script>
    import DetailNavBar from "@/views/detail/childComponents/DetailNavBar";
    import DetailSwiper from "@/views/detail/childComponents/DetailSwiper";
    import DetailBaseInfo from "@/views/detail/childComponents/DetailBaseInfo";
    import DetailShopInfo from "@/views/detail/childComponents/DetailShopInfo";
    import DetailGoodsInfo from "@/views/detail/childComponents/DetailGoodsInfo";
    import DetailGoodsParams from "@/views/detail/childComponents/DetailGoodsParams";
    import DetailCommentInfo from "@/views/detail/childComponents/DetailCommentInfo";
    import DetailBottomBar from "@/views/detail/childComponents/DetailBottomBar";
    import GoodsList from "@/components/content/goods/GoodsList";

    import{getDetail,Goods,Shop,GoodsParam,getRecommend} from "@/network/detail";

    import Scroll from "@/components/common/scroll/Scroll";
    import {debounce} from "@/common/utils";
    import {itemListenerMixin,backTopMixin} from "@/common/mixin"
    export default {
        name: "Detail",
        data(){
          return {
            iid: null,
            topImages:[],
            goods: {},
            shop: {},
            detailInfo: {},
            paramInfo: {},
            commentInfo: {},
            recommends: [],
            themeTopYs: [],
            getThemeTopY: null,
            currentIndex: 0
          }
        },
        mixins: [itemListenerMixin,backTopMixin],
        created() {
          //1. 保存传入的id
          this.iid = this.$route.params.iid

          //2. 根据iid请求详情数据
          getDetail(this.iid).then(res => {
            // console.log(res);
            //1. 获取顶部轮播图数据
            const data = res.result
            this.topImages = data.itemInfo.topImages
            // console.log(this.topImages)

            //2.获取商品信息
            this.goods = new Goods(data.itemInfo,data.columns,data.shopInfo.services)

            //3.创建店铺信息的对象
            this.shop = new Shop(data.shopInfo)

            //4.保存商品详情的数据
            this.detailInfo = data.detailInfo

            //5.获取参数信息
            this.paramInfo = new GoodsParam(data.itemParams.info, data.itemParams.rule)

            //6.取出评论信息
            if(data.rate.cRate !== 0) {
              this.commentInfo = data.rate.list[0]
            }

            this.$nextTick(() => {

            })
          })

          //3.请求推荐数据
          getRecommend().then(res => {
            // console.log(res)
            this.recommends = res.data.list
          })

          //4.给该函数赋值
          this.getThemeTopY = debounce(() => {

            this.themeTopYs = []
            this.themeTopYs.push(0)
            this.themeTopYs.push(this.$refs.params.$el.offsetTop-44)
            this.themeTopYs.push(this.$refs.comment.$el.offsetTop-44)
            this.themeTopYs.push(this.$refs.recommend.$el.offsetTop-44)
            this.themeTopYs.push(Number.MAX_VALUE)
            // console.log(this.themeTopYs)
          }, 100)
        },
        mounted() {

        },
        updated() {

        },
      destroyed() {
          this.$bus.$off('itemImageLoad', this.itemImageListener)
        },
      components: {
          DetailNavBar,
          DetailSwiper,
          DetailBaseInfo,
          DetailShopInfo,
          Scroll,
          DetailGoodsInfo,
          DetailGoodsParams,
          DetailCommentInfo,
          GoodsList,
          DetailBottomBar
        },
        methods: {

          imageLoad() {
            this.$refs.scroll.refresh()
            this.getThemeTopY()
          },
          titleClick(index) {
            // console.log(index);
            this.$refs.scroll.scrollTo(0, -this.themeTopYs[index], 100)
          },
          contentScroll(position) {
            // console.log(position);
            //1.获取y值
            const positionY = -position.y
            //2.positionY的值进行对比
            //  [0, 6738, 8154, 8244]
            let length = this.themeTopYs.length
            for(let i = 0; i < length-1; i++){
              // console.log(i)
              // if(positionY > this.themeTopYs[i] && positionY < this.themeTopYs[i+1] ){
              //   console.log(i);
              // if ((this.currentIndex !== i) && ((i < length -1 && positionY >= this.themeTopYs[i] && positionY < this.themeTopYs[i+1]) || (i === length - 1 && positionY >= this.themeTopYs[i]))){
              //   // console.log(i);
              //   this.currentIndex = i
              //   // console.log(this.currentIndex)
              //   this.$refs.nav.currentIndex = this.currentIndex
              // }

              if (this.currentIndex != i && (positionY > this.themeTopYs[i]) && positionY < this.themeTopYs[i+1]) {
                  this.currentIndex = i
                  // console.log(this.currentIndex)
                  this.$refs.nav.currentIndex = this.currentIndex
              }

              //显示是否回到顶部
              this.isShowBackTop = (-position.y) > 1000

            }
          }
        }
    }
</script>

<style scoped>
  #detail{
    position: relative;
    z-index: 9;
    background-color: #ffffff;
    height: 100vh;
  }
  .detail-nav{
    position: relative;
    z-index: 9;
    background-color: #ffffff;
  }
  .content {
    height: calc(100% - 44px);
  }
</style>
