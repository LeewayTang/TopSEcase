const Mock = require('mockjs');
<<<<<<< HEAD
<<<<<<< HEAD
=======

// 这个是笔记坊里一个个笔记的数据，同时也是文书房创作笔记markdown编辑器写出来的东西
>>>>>>> parent of deea024 (Revert "对Mock加上了说明性注释")
=======

// 这个是笔记坊里一个个笔记的数据，文书房创作笔记markdown编辑器写出来的东西
>>>>>>> parent of 7fade73 (Revert "更新")
export default [
    {
        url: '/article/0',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: '# 几个页面的数据样例\n' +
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
                    '\n'
            }
        }
    }
    ]
