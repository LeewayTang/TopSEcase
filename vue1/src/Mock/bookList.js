const Mock = require('mockjs');

// 这个是书的列表，和book1、2、3等对应，我觉得可以分开建表？俺也不太了解
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
                        path: '/books/1',
                        icon: require("./../assets/images/1.png"),
                        active: true
                    },
                    {
                        id: 2,
                        name: 'JavaScript高级程序设计',
                        path: '/books/2',
                        icon: require("./../assets/images/2.png"),
                        active: false
                    },
                    {
                        id: 3,
                        name: 'Node.js源码分析',
                        path: '/books/3',
                        icon: require("./../assets/images/3.png"),
                        active: false
                    },
                    {
                        id: 4,
                        name: 'Spring Boot实战',
                        path: '/books/4',
                        icon: require("./../assets/images/4.png"),
                        active: false
                    },
                ]
            }
        }

    }
]
