const Mock = require('mockjs');

// 藏书阁的侧栏推荐标签
export default [
    {
        url: 'book-ground/tags',
        type: 'get',
        response: () => {
            return {
                code: 2000,
                data: ['CS', 'Java', 'DataBase', 'Operating System', '倚天屠龙', '干将莫邪', '孝允天sb']
            }
        }
    }
]
