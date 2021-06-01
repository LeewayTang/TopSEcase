const Mock = require('mockjs');

// 这个是首页的三个图标显示的内容
export default [
    {
        url: '/focus/list',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: [
                    {
                        id: 1,
                        name: 'Articles',
                        title: '我将筛选出日推中的日志内容',
                        img: 'https://z3.ax1x.com/2021/05/06/gQgii8.jpg'
                    },
                    {
                        id: 2,
                        name: 'Books',
                        title: '我将筛选出日推中的书帖内容',
                        img: 'https://z3.ax1x.com/2021/05/06/gQgkRg.jpg'
                    },
                    {
                        id: 3,
                        name: 'Relative',
                        title: '我将筛选出日推中与你相关的内容',
                        img: 'https://z3.ax1x.com/2021/05/06/gQgFJS.jpg'
                    }
                ]
            }
        }
    }
]
