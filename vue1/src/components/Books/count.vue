<template>
  <div class="sales-board">
      <div class="sales-board-intro">
        <h1>{{this.bookInfo.title}}</h1>
        <p>{{this.bookInfo.introduction}}</p>
      </div>
      <div class="sales-board-form">
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  作者：{{ this.bookInfo.author }} ｜ {{ this.bookInfo.press }}
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  ISBN：{{ this.bookInfo.ISBN }}
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  <a :href="this.bookInfo.href">购买链接🔗</a>
              </div>
          </div>
          <div class="sales-board-line">
            <el-row type="flex" justify="end">
              <el-button type="primary">获取电子书</el-button>
            </el-row>
          </div>
      </div>
    <h1>精彩书评</h1>
      <div class="sales-board-des">
        <li v-for="item in bookInfo.comments">
          {{item.says}}
          <br>
          <el-row type="flex" justify="end">—— {{item.username}}</el-row>
        </li>
      </div>
  </div>
</template>

<script>
import VSelection from './../../components/base/selection.vue'
import VCounter from '../../components/base/counter'
import VChooser from '../../components/base/chooser'
import VMulChooser from '../../components/base/multiplyChooser'
import Dialog from '../../components/base/dialog'

import _ from 'lodash'
export default {
  components: {
    VSelection,
    VCounter,
    VChooser,
    VMulChooser,
    MyDialog: Dialog,
  },
  data () {
    return {
      bookInfo:{
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
          }]
      }
    }
  },
  methods: {
    onParamChange (attr, val) {
      console.log(this[attr],val)
      this[attr] = val
      this.getPrice()
    },
    getPrice () {
      let buyVersionsArray = _.map(this.versions, (item) => {
        return item.value
      })
      let reqParams = {
        buyNumber: this.buyNum,
        buyType: this.buyType.value,
        period: this.period.value,
        version: buyVersionsArray.join(',')
      }
      this.$http.post('/api/getPrice', reqParams)
      .then((res) => {
        this.price = res.data.amount
      })
    }
  },
  mounted () {
    this.buyNum = 1
    this.buyType = this.buyTypes[0]
    this.versions = [this.versionList[0]]
    this.period = this.periodList[0]
    this.getPrice()
    console.log("初始完毕")
  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sales-board-line-left{
  width:fit-content;
}
.buy-dialog-table td,
.buy-dialog-table th{
  border: 1px solid #e3e3e3;
  text-align: center;
  padding: 5px 0;
}
.buy-dialog-table th {
  background: #4fc08d;
  color: #fff;
  border: 1px solid #4fc08d;
}
</style>
