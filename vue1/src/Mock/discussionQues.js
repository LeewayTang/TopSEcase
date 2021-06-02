const Mock = require('mockjs');

// 这个是评论区的数据，既展示在争鸣殿里（部分），又展示在争鸣殿点击跳转到的具体讨论的地方。
export default [{
  url: '/discussionQues',
  type: 'get',
  response: () => {
      return{
          code: 2000,
          data: [
              {
              id: 1,
              question: '你期末想及格吗？',
              content: 'sdlf;dfjs oians sfd',
              ownerName: '刻晴',
              Avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX1Ued78e4N2yBMIZLPMtS03do7rBnkhHIiA&usqp=CAU',
              time: Date.now(),
              tags: ['Software Engineer', 'lyx', 'Vue'],
              reply: '1'
          },
              {
                  id: 2,
                  question: '生存还是毁灭？',
                  content: '噢我的上帝啊',
                  ownerName: 'Hamlet',
                  Avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX1Ued78e4N2yBMIZLPMtS03do7rBnkhHIiA&usqp=CAU',
                  time: Date.now(),
                  tags: ['life', 'Shakespeare', 'Opera'],
                  reply: '66'
              },
              {
                  id: 3,
                  question: '爱是六月飞霜吗？',
                  content: '我偏要勉强',
                  ownerName: '欧阳锋',
                  Avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX1Ued78e4N2yBMIZLPMtS03do7rBnkhHIiA&usqp=CAU',
                  time: Date.now(),
                  tags: ['金庸', '射雕', '武侠'],
                  reply: '99'
              },
          ]
      }
  }
}]
