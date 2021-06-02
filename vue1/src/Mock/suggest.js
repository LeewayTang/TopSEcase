const Mock = require('mockjs');

// 笔记坊、争鸣殿的侧栏推荐内容
export default [
    {
        url: '/suggest',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                follow: ['Cynic', 'Leeway', 'MJX', 'YMY'],
                peer: ['MJX', 'YMY', 'Leeway', 'Cynic'],
                quanzi: ['Software Engineering', 'Computing Science', 'Machine Learning', 'Computing Math']
            }
        }
    }
    ]
