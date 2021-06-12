const Mock = require('mockjs');

//这个是用户的信息，但是我感觉东西还是太少了，应该还得有这个用户下面的的笔记、讨论等等内容，没搞明白
//而且还有一个问题是我们得要能看到其他人的主页内容。
export default [
    {
        url: '/site0',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: {
                    avatar: require('../assets/images/E2n0ya2UUAA2odS.jpg'),
                    username: '未登录',
                    title:'没有名分',
                    quanzi:[{name: '没有圈子', dialogVisible: false}],
                    slogan: 'Who am I?',
                    name: 'MoYun'
                }
            }
        }
    },
    // 站点信息
    {
        url: '/site1',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: {
                    avatar: require('../assets/images/rzdf.jpg'),
                    username: '没有共产党就没有新中国',
                    title:'导师',
                    quanzi:[{name: 'BUAA', dialogVisible: false}, {name:'Software Engineer', dialogVisible: false}],
                    slogan: '银鞍照白马，飒沓如流星。',
                    name: 'MoYun',
                }
            }
        }
    },
    {
        url: '/Cynic',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: {
                    avatar: require('../assets/images/gg.jpg'),
                    username: 'cynic',
                    title:'学生',
                    quanzi:[{name: 'BUAA', dialogVisible: false}, {name:'Software Engineer', dialogVisible: false}],
                    slogan: '那年十八，母校舞会，站着如喽罗。',
                    name: 'MoYun',
                }
            }
        }
    },

    // 这个没有用！！！
    // 站点社交信息
    {
        url: '/social',
        type: 'get',
        response: () => {
            return {
                code: 20000,
                data: [
                    {
                        id: 1,
                        title: 'QQ',
                        icon: 'iconqq',
                        color: '#1AB6FF ',
                        href: 'http://wpa.qq.com/msgrd?v=3&uin=1224971566&site=qq&menu=yes'
                    },
                    {
                        id: 2,
                        title: 'Gitee',
                        icon: 'icongitee',
                        color: '#d81e06',
                        href: 'https://gitee.com/fengziy'
                    },
                    {
                        id: 3,
                        title: 'GitHub',
                        icon: 'icongithub',
                        color: '',
                        href: 'https://github.com/fengziye'
                    },
                    {
                        id: 4,
                        title: 'CSDN',
                        icon: 'iconcsdn',
                        color: 'red',
                        href: 'https://blog.csdn.net/feng_zi_ye'
                    }
                ]
            }
        }
    }
]
