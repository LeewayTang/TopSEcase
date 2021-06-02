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
import VSelection from "../base/selection";
import VCounter from "../base/counter";
import VChooser from "../base/chooser";
import VMulChooser from "../base/multiplyChooser";
import Dialog from "../base/dialog";
import _ from "lodash";
import {fetchBookInfo} from '../../api';

export default {
  name: "books",
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
          {text:""},
          {text:""},
          {text:""},
        ],
        title: '',
        introduction: '',
        author: '',
        press: '',
        ISBN: '',
        href:'',
        comments:[{
          username:'',
          says: ''
        },
          {
            username: '',
            says: ''
          },
          {
            username: '',
            says: ''
          }]
      }
    }
  },
  created() {
    this.fetchBookInfo();
  },
  methods: {
    fetchBookInfo(){
      fetchBookInfo().then(res=>{
        this.bookInfo = res.book1.data
        console.log(this.bookInfo);
      })
    }
  },
  mounted () {
    fetchBookInfo();
    console.log("初始完毕")
  }

}

</script>

<style scoped>
.sales-board-line-left{
  width:50%;
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
