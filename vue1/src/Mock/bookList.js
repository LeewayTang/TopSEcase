const Mock = require('mockjs');

export default [
    {
        url: '/book-list',
        type: 'get',
        response: () => {
            return {
                code: 2000,
                data: [
                    {
                        id: 1,
                        name: '深入浅出Vue.js',
                        path: 'count',
                        active: false
                    },
                    {
                        id: 2,
                        name: 'JavaScript高级程序设计',
                        path: 'forecast',
                        active: false
                    },
                    {
                        id: 3,
                        name: 'Node.js源码分析',
                        path: 'analysis',
                        active: false
                    },
                    {
                        id: 4,
                        name: 'Spring Boot实战',
                        path: 'publish',
                        active: false
                    },
                ]
            }
        }

    }
]
