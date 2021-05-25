const Mock = require('mockjs');

export default [
    {
        url: 'book-ground/tags',
        type: 'get',
        response: () => {
            return {
                code: 2000,
                data: [
                    {
                        id: 1,
                        name: 'Java',
                        path: 'Java'
                    },
                    {
                        id: 2,
                        name: 'Python',
                        path: 'Python'
                    },
                    {
                        id: 3,
                        name: 'C++',
                        path: 'Cpp'
                    },
                    {
                        id: 4,
                        name: 'PHP',
                        path: 'PHP'
                    },
                    {
                        id: 5,
                        name: 'C#',
                        path: 'CSharp'
                    }
                ]
            }
        }
    }
]
