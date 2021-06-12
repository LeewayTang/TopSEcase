const Mock = require('mockjs');

// 这个其实也就是book1，不要被名字骗了
export default [
    {
        url: "/books/tag/CS",
        type: "get",
        response: () => {
            return{
                code: 2000,
                data: [
                    {
                        id: 1,
                        img: require("./../assets/images/1.png"),
                        items:[
                            {text:"第一组"},
                            {text:"第二组"},
                            {text:"第三组"},
                        ],
                        title: '深入浅出Vue.js',
                        introduction: '本书从源码层面分析了Vue.js。首先，简要介绍了Vue.js；然后详细讲解了其内部核心技术“变化侦测”，这里带领大家从0到1实现一个简单的“变化侦测”系统；接着详细介绍了虚拟DOM技术，其中包括虚拟DOM的原理及其patching算法；紧接着详细讨论了模板编译技术，其中包括模板解析器的实现原理、优化器的原理以及代码生成器的原理；最后详细介绍了其整体架构以及提供给我们使用的各种API的内部原理，同时还介绍了生命周期、错误处理、指令系统与模板过滤器等功能的原理。',
                        author: '兰陵笑笑生',
                        press: '高等教育出版社',
                        ISBN: '23333333333333333',
                        href:'http://product.dangdang.com/26922892.html',
                        comments:[{
                            username:'刻晴',
                            says: 'Node.js让JavaScript在服务器端焕发生机，这是一本带着文艺调调的好看的技术书，书中详细阐述了Node.js的方方面面。如果你是前端工程师，这会是你迈向全端工程师的关键一步。'
                        },
                            {
                                username: '甘雨',
                                says: '通过学习Node.js，你可以接触到新的开发模式与协作思想。通过阅读这本书，你可以在软件开发领域获得广泛而又有深度的收获！所以，我很推荐这本书！'
                            },
                            {
                                username: '胡桃',
                                says: '从未读过这么让人想一翻到底的Node.js技术读物，看完 “内存控制”这一章后，重新写代码的时候，仿佛都能看到V8是如何进行垃圾回收的。如果你还在纠结callback带来的嵌套问题，那么推荐你阅读“异步编程”这一章，保证让你大开眼界。世界上本没有嵌套回调，写的人多了，也便有了。JavaScript已经不仅仅是在浏览器上运行的玩具语言, 它正在通过Node.js进军所有领域。\n' +
                                    '　　阅读本书，开启你人生的Node节点吧。'
                            }],
                        downloadCount: 1032,
                        viewsCount: 999,
                    },
                    {
                        id: 2,
                        img: require("./../assets/images/2.png"),
                        items:[
                            {text:"第一组"},
                            {text:"第二组"},
                            {text:"第三组"},
                        ],
                        title: 'JavaScript高级程序设计',
                        introduction: '本书是JavaScript 超级畅销书的最新版。ECMAScript 5 和HTML5 在标准之争中双双胜出，使大量专有实现和客户端扩展正式进入规范，同时也为JavaScript 增添了很多适应未来发展的新特性。本书这一版除增加5 章全新内容外，其他章节也有较大幅度的增补和修订，新内容篇幅约占三分之一。全书从JavaScript 语言实现的各个组成部分——语言核心、DOM、BOM、事件模型讲起，深入浅出地探讨了面向对象编程、Ajax 与Comet 服务器端通信，HTML5 表单、媒体、Canvas（包括WebGL）及Web Workers、地理定位、跨文档传递消息、客户端存储（包括IndexedDB）等新API，还介绍了离线应用和与维护、性能、部署相关的最佳开发实践。本书附录展望了未来的API 和ECMAScript Harmony 规范。',
                        author: '罗辑',
                        press: '三体第一出版社',
                        ISBN: '1231241294712393',
                        href:'http://product.dangdang.com/26922892.html',
                        comments:[{
                            username: '叶文洁',
                            says: 'Node.js让JavaScript在服务器端焕发生机，这是一本带着文艺调调的好看的技术书，书中详细阐述了Node.js的方方面面。如果你是前端工程师，这会是你迈向全端工程师的关键一步。'
                        },
                            {
                                username: '叶问',
                                says: '通过学习Node.js，你可以接触到新的开发模式与协作思想。通过阅读这本书，你可以在软件开发领域获得广泛而又有深度的收获！所以，我很推荐这本书！'
                            },
                            {
                                username: '叶子',
                                says: '从未读过这么让人想一翻到底的Node.js技术读物，看完 “内存控制”这一章后，重新写代码的时候，仿佛都能看到V8是如何进行垃圾回收的。如果你还在纠结callback带来的嵌套问题，那么推荐你阅读“异步编程”这一章，保证让你大开眼界。世界上本没有嵌套回调，写的人多了，也便有了。JavaScript已经不仅仅是在浏览器上运行的玩具语言, 它正在通过Node.js进军所有领域。\n' +
                                    '　　阅读本书，开启你人生的Node节点吧。'
                            }],
                        downloadCount: 1024,
                        viewsCount: 888,
                    },
                    {
                        id: 3,
                        img: require("./../assets/images/3.png"),
                        items:[
                            {text:"第一组"},
                            {text:"第二组"},
                            {text:"第三组"},
                        ],
                        title: 'Node.js源码分析',
                        introduction: '本书从源码层面分析了Node.js。首先，简要介绍了Node.js；然后详细讲解了其内部核心技术“变化侦测”，这里带领大家从0到1实现一个简单的“变化侦测”系统；接着详细介绍了虚拟DOM技术，其中包括虚拟DOM的原理及其patching算法；紧接着详细讨论了模板编译技术，其中包括模板解析器的实现原理、优化器的原理以及代码生成器的原理；最后详细介绍了其整体架构以及提供给我们使用的各种API的内部原理，同时还介绍了生命周期、错误处理、指令系统与模板过滤器等功能的原理。',
                        author: 'Elon Musk',
                        press: 'Bitcoin Press',
                        ISBN: '1864129746298437',
                        href:'http://product.dangdang.com/26922892.html',
                        comments:[{
                            username:'ETH',
                            says: '以太坊yyds'
                        },
                            {
                                username: 'Doge',
                                says: '通过投资加密货币，你可以成为新韭菜'
                            },
                            {
                                username: 'SHIB',
                                says: '投资有风险，入场需谨慎'
                            }],
                        downloadCount: 7912,
                        viewsCount: 258,
                    },
                    {
                        id: 4,
                        img: require("./../assets/images/4.png"),
                        items:[
                            {text:"第一组"},
                            {text:"第二组"},
                            {text:"第三组"},
                        ],
                        title: 'Spring Boot实战',
                        introduction: '本书从源码层面分析了Node.js。首先，简要介绍了Node.js；然后详细讲解了其内部核心技术“变化侦测”，这里带领大家从0到1实现一个简单的“变化侦测”系统；接着详细介绍了虚拟DOM技术，其中包括虚拟DOM的原理及其patching算法；紧接着详细讨论了模板编译技术，其中包括模板解析器的实现原理、优化器的原理以及代码生成器的原理；最后详细介绍了其整体架构以及提供给我们使用的各种API的内部原理，同时还介绍了生命周期、错误处理、指令系统与模板过滤器等功能的原理。',
                        author: 'Bill Gates',
                        press: 'MS Press',
                        ISBN: '1352211231237',
                        href:'http://product.dangdang.com/26922892.html',
                        comments:[{
                            username:'Win XP',
                            says: '以太坊yyds'
                        },
                            {
                                username: 'Win7',
                                says: '通过投资加密货币，你可以成为新韭菜'
                            },
                            {
                                username: 'Win 10',
                                says: '上面各位都是垃圾'
                            }],
                        downloadCount: 9102,
                        viewsCount: 6969,
                    }
                ]
            }
        }
    }
]
