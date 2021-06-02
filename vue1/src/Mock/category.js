const Mock = require('mockjs');
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
                        title: '创作笔记',
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