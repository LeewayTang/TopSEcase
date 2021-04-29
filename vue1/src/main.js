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

Vue.use(vcolorpicker)
Vue.use(ViewUI);
Vue.config.productionTip = false
Vue.prototype.$axios= axios
Vue.config.productionTip = false
Vue.filter('parseTime', (v) => parseTime(v,'{y}-{m}-{d}'))
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
