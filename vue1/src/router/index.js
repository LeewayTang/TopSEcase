import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import VueElElements from 'vue-el-element'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Book from './../views/Book'
import BookGround from "../views/BookGround";
import book1 from './../components/Books/analysis'
import book2 from './../components/Books/count'
import book3 from './../components/Books/publish'
import book4 from './../components/Books/forecast'
import log from './../views/Log'
import userContent from './../views/UserContent'
import notLogin from '../views/NotLogin'

Vue.use(VueRouter)
Vue.use(VueElElements)
Vue.use(ElementUI)

import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// use
Vue.use(mavonEditor)
new Vue({
    'el': '#main'
})

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('../views/Home.vue'),
        // redirect: '/login',
        meta: {
            title: '首页',
            // hasLogin: false
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
        path: '/personalCenter',
        name: 'personalCenter',
        component: () => import('../views/PersonalCenter.vue'),
        meta: { title: '个人中心'}
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
        path:'/book',
        component:Book,
        redirect:'/book/analysis',
        children:[
            {
                path:'analysis',
                name:'analysis',
                component:book1,
                meta: { title: "book1"}
            },
            {
                path:'count',
                name:'count',
                component:book2,
                meta: { title: "book2"}
            },
            {
                path:'forecast',
                name:'forecast',
                component:book4,
                meta: { title: "book4"}
            },
            {
                path:'publish',
                name:'publish',
                component:book3,
                meta: { title: "book3"}
            }
        ]
    },
    {
        path:'/book-ground',
        name:'book-ground',
        component:BookGround,
        meta:{title: "藏书阁"}
    },
    {
        path:'/log',
        name:'log',
        component: log,
        meta: {title: "读书日志"}
    },
    {
        path: '/userContent',
        name: 'userContent',
        component: userContent,
        meta: {title: "动态"}
    },
    // {
    //     path: '/category/:cate',
    //     name: 'category',
    //     component: () => import('../views/Home.vue'),
    //     meta: { title: '分类', params: 'cate'}
    // },
    {
        path: '/search/:words',
        name: 'search',
        component: () => import('../views/Home.vue'),
        meta: { title: '搜索', params: 'words'}
    },
    // {
    //     path: '/about',
    //     name: 'about',
    //     component: () => import('../views/About.vue'),
    //     meta: { title: '关于'}
    // },
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
        meta: { title: '文章'}
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
        title = `${to.meta.title}:${to.params[to.meta.params] || ''} - ${title}`
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
