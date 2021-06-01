const Mock = require('mockjs');

// 这个是藏书阁的精彩点评的内容，其实不应该这么简单，应该是从他人的书评那里摘出来
export default [
    {
        url: 'book-ground/review',
        type: 'get',
        response: () => {
            return {
                code: 2000,
                data: [
                    {
                        id: 1,
                        name: '马云',
                        review: '九九六福报'
                    },
                    {
                        id: 2,
                        name: '刘强东',
                        review: '不奋斗的都不是我兄弟'
                    },
                    {
                        id: 3,
                        name: '贾跃亭',
                        review: '让我们一起，为梦想窒息！'
                    }
                ]
            }

        }
    }
]
