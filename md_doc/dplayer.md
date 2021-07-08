`main.js`

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(store).use(router).mount('#app')
import VueDPlayer from 'vue-dplayer';
import 'vue-dplayer/dist/vue-dplayer.css';

Vue.use(VueDPlayer);
```

`Home.vue`

```javascript
//参考dplayer的官方文档：http://dplayer.js.org/guide.html#options。参照options章节，填写参数进行自定义播放器。

<template>
  <div class='home'>
    <d-player ref="player" :options="options"></d-player>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        options: {
          theme: '#b7daff',  // 风格颜色，例如播放条，音量条的颜色
          loop: false,  // 是否自动循环
          lang: 'zh-cn',  // 语言，'en', 'zh-cn', 'zh-tw'
          screenshot: true,  // 是否允许截图（按钮），点击可以自动将截图下载到本地
          hotkey: true,  // 是否支持热键，调节音量，播放，暂停等
          preload: 'auto',  // 自动预加载
          volume: 0.7,  // 初始化音量
          logo: '../assets/logo.png',  // 在视频左脚上打一个logo
          video: {
            url: '../assets/1625722243.mp4', // 播放视频的路径
            quality: [  // 设置多个质量的视频
              {
                name: 'HD',
                url: '../assets/1625722243.mp4',
                type: 'auto',  // 'auto', 'hls', 'flv', 'dash', 'webtorrent', 'normal' 或 其他自定义类型
              },
              {
                name: 'SD',
                url: '../assets/1625722243.mp4',
                type: 'auto',
              }
            ],
            defaultQuality: 0,  // 默认是HD
            pic: '../assets/logo.png',  // 视频封面图片
            thumbnails: '../assets/logo.png'  // 进度条上的缩略图,需要通过dplayer-thumbnails来生成
          },
          subtitle: {
            url: 'http://www.baidu.com',
            fontSize: '20px',
            bottom: '40px',
          },
          danmaku: {   // 弹幕
            id: '9E2E3368B56CDBB4',
            api: 'https://api.prprpr.me/dplayer/',
            token: 'tokendemo',
            maximum: 1000,
            addition: ['https://api.prprpr.me/dplayer/v3/bilibili?aid=4157142'],
            user: 'DIYgod',
            bottom: '15%',
            unlimited: true
          },
          contextmenu: [  // 右键菜单
            {
              text: 'custom1',
              link: 'https://www.bilibili.com'
            },
            {
              text: 'custom2',
              click: (player) => {
                console.log(player);
              }
            }
          ],
          highlight: [  // 进度条时间点高亮
            {
              text: '10M',
              time: 600,
            },
            {
              text: '20M',
              time: 1200,
            },
          ],
        }
      }
    }
  }
</script>
<style scoped>
  .home {
    width: 1000px;
    margin: 0 auto;
    text-align: center;
  }
</style>
```

