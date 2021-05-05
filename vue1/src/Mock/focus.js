const Mock = require('mockjs');
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
                        title: '我将筛选出日推中的日志内容',
                        img: 'https://z3.ax1x.com/2021/05/05/gKbA74.jpg'
                    },
                    {
                        id: 2,
                        title: '我将筛选出日推中的书帖内容',
                        img: 'https://z3.ax1x.com/2021/05/05/gKbkBF.jpg'
                    },
                    {
                        id: 3,
                        title: '我将筛选出日推中与你相关的内容',
                        img: 'https://z3.ax1x.com/2021/05/05/gKbVAJ.jpg'
                    }
                ]
            }
        }
    }
]