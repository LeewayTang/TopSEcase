const Mock = require('mockjs');


export default [{
    url: '/studentList',
    type: 'get',
    response: () => {
        return {
            data: [
                {
                    avatar: require('../assets/images/E2n0ya2UUAA2odS.jpg'),
                    username: 'Cynic',
                    trueName: '宋永欣',
                    id: '19231061',
                    title:'学生',
                    quanzi:[{name: '没有圈子', dialogVisible: false}],
                    slogan: '欲说还休，却道天凉好个秋',
                },
                {
                    avatar: require('../assets/images/E3MlNB0VEAoTyYl.png'),
                    username: 'MJX',
                    trueName: '闵家旭',
                    id: '19231181',
                    title:'学生',
                    quanzi:[{name: '没有圈子', dialogVisible: false}],
                    slogan: '寄！',
                }
            ]
        }
    }
}]
