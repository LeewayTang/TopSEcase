const Mock = require('mockjs');

// 这个好像才是我们抄的文章下面的评论区的数据格式，我现在也不知道怎么改tmd

const banners = [
    'https://s1.ax1x.com/2020/05/14/YDhagx.jpg',
    'https://s1.ax1x.com/2020/05/14/YDhU81.jpg',
    'https://s1.ax1x.com/2020/05/14/YDhBDO.jpg',
    'https://s1.ax1x.com/2020/05/14/YDhoVg.jpg',
    'https://s1.ax1x.com/2020/05/14/YD4FR1.jpg'
]
function getComment(count) {
    let List = [];
    mockComment(count,null).map(item => {
        let count = 1 + ~~(Math.random() * 5)
        List.push({comment: item,reply: mockComment(count,item.id,item.fromUserName)})
    })
    return List;
}
function mockComment(count,id,userName) {
    let List = [];
    for (let i = 0; i < count; i++) {
        List.push(Mock.mock({
            id: '@increment',
            postId: '',
            parentId: '',
            fromUserId: '',
            fromUserName: '@cname',
            fromUserAvatar: 'banners',
            content: '@ctitle(20,50)',
            createTime: +Mock.Random.time('T'),
            toUserId: id,
            toUserName: userName||'@cname',
            'toUserAvatar|+1': banners,
        }))
    }
    return List;
}

export default [
    {
        url: '/comment',
        type: 'get',
        response: () => {
            let count = 1 + ~~(Math.random() * 5)
            return {
                code: 20000,
                data: getComment(count)
            }
        }
    }
]
