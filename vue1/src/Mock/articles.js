const Mock = require('mockjs');

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
            'fromUserAvatar|+1': banners,
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
        url: '/article/0',
        type: 'get',
        response: () => {
            let count = 1 + ~~(Math.random() * 5)
            return {
                code: 20000,
                data: {
                    username: 'cynic',
                    avatar: require('../assets/images/gg.jpg'),
                    header: '这个是标题',
                    content: '# 几个页面的数据样例\n' +
                    '\n' +
                    '## 首页日推\n' +
                    '\n' +
                    '```json\n' +
                    '{\n' +
                    '    id: 0,\n' +
                    '    isTop: true,\n' +
                    '    banner: banners[0],\n' +
                    '    isHot: true,\n' +
                    '    pubTime: +Mock.Random.date(\'T\'),\n' +
                    '    title: \'看一遍闭着眼都会安装Lua了\',\n' +
                    '    summary: \'Lua 是一种轻量小巧的脚本语言，能为应用程序提供灵活的扩展和定制功能。\',\n' +
                    '    content: \'\',\n' +
                    '    viewsCount: 4045,\n' +
                    '    commentsCount: 99\n' +
                    '}\n' +
                    '```\n' +
                    '\n' +
                    '## 发现笔记\n' +
                    '\n' +
                    '```json\n' +
                    '{\n' +
                    '  name: \'essay1\',\n' +
                    '  type: \'essay\',\n' +
                    ' \ttitle: \'刚发布！Python 一二线城市月薪 15K 起！12 月再夺语言榜首\',\n' +
                    '  content: \'\',\n' +
                    '  // imgUrl: require(\'../../assets/images/headImgDefault.png\'),\n' +
                    '  forum: \'CSDNedu\',\n' +
                    '  category: \'\',\n' +
                    '  date: \'39分钟前\',\n' +
                    '  read: \'518\',\n' +
                    '  comment: \'1\'\n' +
                    '}\n' +
                    '```\n' +
                    '\n' +
                    '## 用户资料\n' +
                    '\n' +
                    '```json\n' +
                    '{\n' +
                    '  avatar:\'https://z3.ax1x.com/2021/05/12/g0JPxS.jpg\',\n' +
                    '\tusername: \'未登录\',\n' +
                    '\ttitle:\'没有名分\',\n' +
                    '\tquanzi:\'没有圈子\',\n' +
                    '\tslogan: \'Who am I?\',\n' +
                    '\tname: \'MoYun\'\n' +
                    '}\n' +
                    '```\n' +
                    '\n',
                    comments: getComment(count)
                }
            }
        }
    }
    ]
