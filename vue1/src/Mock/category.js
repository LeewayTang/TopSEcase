const Mock = require('mockjs');

// 这个是首页导航栏的文书房的子目录
export default [
    {
        url: '/category',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: [
                    {
                        id: 1,
                        title: '创作中心',
                        href: '/writeBlog'
                    },
                    {
                        id: 2,
                        title: '发布新书',
                        href: '/newBook',
                    }
                ]
            }
        }
    }
]
