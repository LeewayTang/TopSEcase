const Mock = require('mockjs');

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
