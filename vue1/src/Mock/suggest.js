const Mock = require('mockjs');
export default [
    {
        url: '/suggest',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: ['Cynic', 'Leeway', 'MJX', 'YMY']
            }
        }
    }
    ]
