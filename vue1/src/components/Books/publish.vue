<template>
  <div class="sales-board">
      <div class="sales-board-intro">
        <h2>Spring Boot实战</h2>
        <p>本书以Spring应用程序开发为中心，全面讲解如何运用Spring Boot提高效率，使应用程序的开发和管理更加轻松有趣。作者行文亲切流畅，以大量示例讲解了Spring Boot在各类情境中的应用，内容涵盖起步依赖、Spring Boot CLI、Groovy、Grails、Actuator。对于Spring Boot开发应用中较为繁琐的内容，附录奉上整理完毕的表格，一目了然，方便读者查阅。</p>
      </div>
      <div class="sales-board-form">
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  购买数量：
              </div>
              <div class="sales-board-line-right">
                <v-counter @on-change="onParamChange('buyNum', $event)"></v-counter>
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  收货地区：
              </div>
              <div class="sales-board-line-right">
                  <v-selection :selections="buyTypes" @on-change="onParamChange('buyType', $event)"></v-selection>
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  购买版本：
              </div>
              <div class="sales-board-line-right">
                  <v-chooser
                  :selections="periodList"
                  @on-change="onParamChange('period', $event)"></v-chooser>
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  附加产品：
              </div>
              <div class="sales-board-line-right">
                  <v-mul-chooser
                  :selections="versionList"
                  @on-change="onParamChange('versions', $event)"></v-mul-chooser>
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">
                  总价：
              </div>
              <div class="sales-board-line-right">
                  {{ price }} 元
              </div>
          </div>
          <div class="sales-board-line">
              <div class="sales-board-line-left">&nbsp;</div>
              <div class="sales-board-line-right">
              </div>
          </div>
      </div>
      <div class="sales-board-des">
        <h2>精彩书评</h2>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;Node.js让JavaScript在服务器端焕发生机，这是一本带着文艺调调的好看的技术书，书中详细阐述了Node.js的方方面面。如果你是前端工程师，这会是你迈向全端工程师的关键一步。
　　——玉伯，支付宝高级技术专家</p>
    <br><br>
　　<p>&nbsp;&nbsp;&nbsp;&nbsp;通过学习Node.js，你可以接触到新的开发模式与协作思想。通过阅读这本书，你可以在软件开发领域获得广泛而又有深度的收获！所以，我很推荐这本书！
　　——庄表伟</p>
<br><br>
　　<p>&nbsp;&nbsp;&nbsp;&nbsp;从未读过这么让人想一翻到底的Node.js技术读物，看完 “内存控制”这一章后，重新写代码的时候，仿佛都能看到V8是如何进行垃圾回收的。如果你还在纠结callback带来的嵌套问题，那么推荐你阅读“异步编程”这一章，保证让你大开眼界。世界上本没有嵌套回调，写的人多了，也便有了。JavaScript已经不仅仅是在浏览器上运行的玩具语言, 它正在通过Node.js进军所有领域。
　　阅读本书，开启你人生的Node节点吧。
　　——Python发烧友，阿里巴巴数据平台技术专家</p>
      </div>
  </div>
</template>

<script>
import VSelection from './../../components/base/selection.vue'
import VCounter from '../../components/base/counter'
import VChooser from '../../components/base/chooser'
import VMulChooser from '../../components/base/multiplyChooser'
import Dialog from '../../components/base/dialog'
// import BankChooser from '../../components/bankChooser'
// import CheckOrder from '../../components/checkOrder'
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
      buyNum: 0,
      buyType: {},
      versions: [],
      period: {},
      price: 0,
      versionList: [
        {
          label: '书签',
          value: 0
        },
        {
          label: '书套',
          value: 1
        },
        {
          label: '钢笔',
          value: 2
        }
      ],
      periodList: [
        {
          label: '中文',
          value: 0
        },
        {
          label: '英文',
          value: 1
        },
        {
          label: '日语',
          value: 2
        }
      ],
      buyTypes: [
        {
          label: '福建',
          value: 0
        },
        {
          label: '上海',
          value: 1
        },
        {
          label: '北京',
          value: 2
        },
        {
          label: '重庆',
          value: 3
        },
        {
          label: '广州',
          value: 4
        },
        {
          label: '湖南',
          value: 5
        },
        {
          label: '新疆',
          value: 6
        },
        {
          label: '吉林',
          value: 7
        },
        {
          label: '四川',
          value: 8
        },
        {
          label: '合肥',
          value: 9
        }
      ],
      isShowPayDialog: false,
      bankId: null,
      orderId: null,
      isShowCheckOrder: false,
      isShowErrDialog: false
    }
  },
  methods: {
    onParamChange (attr, val) {
      console.log(this[attr],val)
      this[attr] = val
      this.getPrice()
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
//     showPayDialog () {
//       this.isShowPayDialog = true
//     },
//     hidePayDialog () {
//       this.isShowPayDialog = false
//     },
//     hideErrDialog () {
//       this.isShowErrDialog = false
//     },
//     hideCheckOrder () {
//       this.isShowCheckOrder = false
//     },
//     onChangeBanks (bankObj) {
//       this.bankId = bankObj.id
//     },
//     confirmBuy () {
//       let buyVersionsArray = _.map(this.versions, (item) => {
//         return item.value
//       })
//       let reqParams = {
//         buyNumber: this.buyNum,
//         buyType: this.buyType.value,
//         period: this.period.value,
//         version: buyVersionsArray.join(','),
//         bankId: this.bankId
//       }
//       this.$http.post('/api/createOrder', reqParams)
//       .then((res) => {
//         this.orderId = res.data.orderId
//         this.isShowCheckOrder = true
//         this.isShowPayDialog = false
//       }, (err) => {
//         this.isShowBuyDialog = false
//         this.isShowErrDialog = true
//       })
//     }
//   },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.buy-dialog-title {
  font-size: 16px;
  font-weight: bold;
}
.buy-dialog-btn {
  margin-top: 20px;
}
.buy-dialog-table {
  width: 100%;
  margin-bottom: 20px;
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
