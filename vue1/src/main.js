import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/style.less'
import './assets/font/iconfont.css'
require('./Mock')
import {parseTime} from './utils'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import vcolorpicker from 'vcolorpicker'
import axios from 'axios'
import 'github-markdown-css/github-markdown.css'
import qs from "qs"
import 'github-markdown-css/github-markdown.css'
import hljs from 'highlight.js'
import Element from 'element-ui'
// 如果开启了typescript 需要额外安装 npm install @types/highlight.js
// 通过 import * as hljs from 'highlight.js' 引入
Vue.directive('highlight', function (el) {
  const blocks = el.querySelectorAll('pre code')
  blocks.forEach(block => {
    hljs.highlightBlock(block)
  })
})
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import VueCropper from 'vue-cropper'
// use
Vue.use(mavonEditor)
Vue.prototype.$qs = qs
Vue.use(vcolorpicker)
Vue.use(ViewUI)
Vue.use(VueCropper)
Vue.use(Element)
Vue.config.productionTip = false
Vue.prototype.$axios= axios
Vue.config.productionTip = false
// Vue.forceUpdate()
Vue.filter('parseTime', (v) => parseTime(v,'{y}-{m}-{d}'))
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
