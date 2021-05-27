const Mock = require('mockjs');
export default [{
  url: '/discussionQues',
  type: 'get',
  response: () => {
      return{
          code: 2000,
          data: {
              question: '你期末想及格吗？',
              ownerName: '刻晴',
              Avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX1Ued78e4N2yBMIZLPMtS03do7rBnkhHIiA&usqp=CAU',
              time: Date.now(),
              tags: ['Software Engineer', 'lyx', 'Vue']
          }
      }
  }
}]
