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
                    avatar:'data:image/jpeg;base64,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',
                    username: '未登录',
                    title:'没有名分',
                    quanzi:[{name: '没有圈子'}],
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
                    username: 'Cheems',
                    title:'游客',
                    quanzi:'BUAA',
                    slogan: 'I do not wish to be horny any more.',
                    name: 'MoYun'
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
