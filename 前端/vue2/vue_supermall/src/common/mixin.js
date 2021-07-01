import {debounce} from "@/common/utils";
import BackTop from "@/components/content/backtop/BackTop";

export const itemListenerMixin = {
  data() {
    return {
      itemImageListener: null
    }
  },
  mounted() {
    const refresh = debounce(this.$refs.scroll && this.$refs.scroll.refresh, 200)
    this.itemImageListener = () => {
      refresh()
    }
    this.$bus.$on('itemImageLoad', this.itemImageListener)
    // console.log('mixin');
  }
}

export const backTopMixin = {
  data() {
    return {
      isShowBackTop: false

    }
  },
  methods: {
    backClick() {
      // console.log('aa')
      // this.$refs.scroll.scroll.scrollTo(0,0,500)
      this.$refs.scroll.scrollTo(0,0)
    },
    components: {
      BackTop
    }
  }

}
