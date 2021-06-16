const Mock = require('mockjs');
import store from '../store/index'
// 这个是首页头像下面的子目录的内容
export default [
    {
        url: '/profile',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: [
                    {
                        id: 1,
                        title: '个人资料',
                        href: '/personalCenter/' + store.state.username
                    },
                    {
                        id: 2,
                        title: '退出',
                        href: '/',
                    }
                ]
            }
        }
    }
]
