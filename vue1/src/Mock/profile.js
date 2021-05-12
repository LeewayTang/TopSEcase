const Mock = require('mockjs');
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
                        href: '/personalCenter'
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