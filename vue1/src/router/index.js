import Vue from 'vue'
import Router from 'vue-router'
import loginRegister from '../components/loginRegister.vue'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'login',
    component: loginRegister
  }
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
