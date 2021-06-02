const Mock = require('mockjs');

// 这个是文章的数据内容
export default [
    {
        url: '/content-list',
        type: 'get',
        response:()=> {
            return{
                code: 20000,
                data:[
                    {
                        id: 1,
                        name: 'essay1',
                        type: 'essay',
                        title: '刚发布！Python 一二线城市月薪 15K 起！12 月再夺语言榜首',
                        content: '',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'CSDNedu',
                        category: '',
                        date: '39分钟前',
                        read: '518',
                        comment: '1'
                    },
                    {
                        id:2,
                        name: 'essay2',
                        type: 'essay',
                        title: 'Docker最全教程——从理论到实战（七）',
                        content:
                            '本篇教程持续编写了3个星期左右并且一直在完善、补充具体的细节和实践，预计全部完成还需要1到2个月的时间。整个教程完成之后，我们将会出书（目前已联系出版社）。在这个过程中，...  ',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'dotNET跨平台',
                        category: '云计算/大数据',
                        date: '12月09日',
                        read: '8145',
                        comment: '14'
                    },
                    {
                        id:3,
                        name: 'essay3',
                        type: 'essay',
                        title: '源码:Spark SQL 分区特性第一弹',
                        content:
                            '头条号上说过近期分享Spark SQL系列文章，前面在头条号上分享了Dataset API的基本操作和复杂操作，不知道下面大家有没有自己测试一下。今天主要是分享Spark...',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'Spark高级玩法',
                        category: '云计算/大数据',
                        date: '12月09日',
                        read: '3187',
                        comment: '2'
                    },
                    {
                        id:4,
                        name: 'essay4',
                        type: 'essay',
                        title: '刚发布！Python 一二线城市月薪 15K 起！12 月再夺语言榜首',
                        content: '',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'CSDNedu',
                        category: '',
                        date: '39分钟前',
                        read: '518',
                        comment: '1'
                    },
                    {
                        id:5,
                        name: 'essay5',
                        type: 'essay',
                        title: 'Docker最全教程——从理论到实战（七）',
                        content:
                            '本篇教程持续编写了3个星期左右并且一直在完善、补充具体的细节和实践，预计全部完成还需要1到2个月的时间。整个教程完成之后，我们将会出书（目前已联系出版社）。在这个过程中，...  ',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'dotNET跨平台',
                        category: '云计算/大数据',
                        date: '12月09日',
                        read: '8145',
                        comment: '14'
                    },
                    {
                        id:6,
                        name: 'essay6',
                        type: 'essay',
                        title: '源码:Spark SQL 分区特性第一弹',
                        content:
                            '头条号上说过近期分享Spark SQL系列文章，前面在头条号上分享了Dataset API的基本操作和复杂操作，不知道下面大家有没有自己测试一下。今天主要是分享Spark...',
                        // imgUrl: require('../../assets/images/headImgDefault.png'),
                        forum: 'Spark高级玩法',
                        category: '云计算/大数据',
                        date: '12月09日',
                        read: '3187',
                        comment: '2'
                    }
                ]
            }
        }
    }
]
