import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

import 'element-ui/lib/theme-chalk/index.css'
import notLogin from '../views/NotLogin'
import * as path from "path";

Vue.use(VueRouter)


new Vue({
    'el': '#main'
})

const routes = [
    {
        path: '/',
        redirect: '/home',
    },
    {
        path: '/home',
        name: 'home',
        component: () => import('../views/Home.vue'),
        meta: {
            title: '首页',
        }
    },
    {
      path: '/notLogin',
      name: 'notLogin',
      component: () => import('../views/NotLogin.vue'),
      meta: {title: '请先点击右上角登录'}
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/loginRegister.vue'),
        meta: { title: '注册登录'}
    },
    {
        path: '/personalCenter/:username',
        name: 'personalCenter',
        component: () => import('../views/PersonalCenter1.vue'),
        meta: { title: '个人中心', params: 'username'}
    },
    {
        path: '/writeBlog',
        name: 'writeBlog',
        component: () => import('../components/Write1.vue'),
        meta: { title: '创作笔记'}
    },
    {
        path: '/newBook',
        name: 'newBook',
        component: () => import('../views/newBook.vue'),
        meta: { title: '发布新书'}
    },
    {
        path:'/books/:id',
        name: 'books',
        component: () => import('./../views/Book'),
        meta: { title: '书籍详情页' }
    },
    {
        path:'/book-ground',
        name:'book-ground',
        component: () => import ("../views/BookGround"),
        meta:{title: "藏书阁"}
    },
    {
        path:'/log',
        name:'log',
        component: () => import ('./../views/Log'),
        meta: {title: "读书笔记"}
    },
    {
        path: '/discussion',
        name: 'userContent',
        component: () => import ('./../views/UserContent'),
        meta: {title: "争鸣殿——在这里讨论吧！"}
    },
    // {
    //     path: '/discussion',
    //     name: 'discussion',
    //     component: () => import('../views/Discussion.vue'),
    //     meta: {title: "讨论"}
    // },
    {
        path: '/search/:words',
        name: 'search',
        component: () => import('../views/Home.vue'),
        meta: { title: '搜索', params: 'words'}
    },
    {
        path: '/markdown_test',
        name: 'markdown',
        component: () => import('../views/Markdown.vue'),
        meta: { title: 'markdown'}
    },
    {
        path: '/article/:id',
        name: 'article',
        component: () => import('../views/Articles.vue'),
        meta: { title: '文章', params: 'id'}
    }
]

const router = new VueRouter({
    //mode: 'history',
    base: process.env.BASE_URL,
    routes
})
router.beforeResolve(async (to, from, next) => {
    let title = 'MoYun'
    if (to.meta.params){
        title = `${to.meta.title}: ${to.params[to.meta.params] || ''} - ${title}`
    }else {
        title = `${to.meta.title} - ${title}`
    }
    document.title = title
    let token = localStorage.getItem('Authorization')
    if(to.path === '/login' || to.path === '/' || to.path === '/book-ground')
        // alert(token),
        next();
    else{
        if(token === null || token === '')
            next('/login')
        else
            // alert(token)
            next();
    }
    if (to.path !== from.path) {
        store.dispatch('setLoading', true);
    }
    next();
})
router.afterEach((to, from) => {
    // 最多延迟 关闭 loading
    setTimeout(() => {
        store.dispatch('setLoading', false);
    }, 1500)
})
export default router
