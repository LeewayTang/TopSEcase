<template>
  <div class="book-wrap">
    <div class="book-left">
      <div class="product-board">
        <img :src="productIcon" width="220px;">
        <ul>
          <el-button type='text' class='switch' v-for="item in bookList" @click="bookClick(item.id)" :key="item.id">
            {{ item.name }}
          </el-button>
        </ul>
      </div>
    </div>
    <div class="book-right">
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
    </div>
  </div>
</template>

<script>
import VSelection from "../components/base/selection";
import VCounter from "../components/base/counter";
import VChooser from "../components/base/chooser";
import VMulChooser from "../components/base/multiplyChooser";
import Dialog from "../components/base/dialog";
import _ from "lodash";
import {fetchBookList, fetchBookInfo} from '../api';

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
        id: 1,
        img: '',
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
      },
      bookList: [],
    }
  },
  activated() {
    fetchBookInfo(this.$route.params.id)
  },
  computed: {
    productIcon () {
      return this.bookInfo.img;
    }
  },
  created() {
    // this.fetchBookInfo(this.bookInfo.id);
    this.fetchBookList();
  },
  methods: {
    fetchBookInfo(){
      let id = this.$route.params.id;
      console.log(id);
      fetchBookInfo(id).then(res=>{
        this.bookInfo = res.data;
        console.log("fuck you in fetchBookInfo")
        console.log(this.bookInfo);
      })
    },
    fetchBookList() {
      fetchBookList().then(res => {
        this.bookList = res.data || [];
        console.log(this.bookList);
      })
    },
    bookClick(id) {
      console.log(this.$route.path);
      this.$router.push('/books/' + id);
      console.log(this.$route.params.id);
      this.fetchBookInfo(this.$route.params.id);
      console.log(this.bookInfo);
    }
  },
  mounted() {
    this.fetchBookInfo(this.bookInfo.id)
  },
  // watch: {
  //   '$route'(to, from) {
  //     this.$forceUpdate()
  //   }
  // }
}
</script>

<style>
.book-wrap {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 120px;
}
.book-left {
  float: left;
  width: 220px;
  text-align: center;
}
.book-right {
  float: left;
  width: 940px;
  margin-left: 20px;
}
.product-board {
  background: #fff;
  padding: 20px 0;
}
.product-board ul {
  margin-top: 20px;
}
.product-board li {
  text-align: left;
  padding: 10px 15px;
  cursor: pointer;
}
.product-board li.active,
.product-board li:hover {
  background: #4fc08d;
  color: #fff;
}
.product-board li a {
  display: block;
}
.sales-board {
  background: #fff;
}
.sales-board-form {

}
.sales-board-intro h2 {
  font-size: 20px;
  padding: 20px;
}
.sales-board-intro p {
  background: #f7fcff;
  padding: 10px 20px;
  color: #999;
  line-height: 1.8;
}
.sales-board-form {
  padding: 30px 20px;
  font-size: 14px;
}
.sales-board-line {
  clear: both;
  padding-bottom: 20px;
}
.sales-board-line-left {
  display: inline-block;
  width: 300px;
}
.sales-board-line-right {
  display: inline-block;
  width: 75%;
}
.sales-board-des {
  border-top: 20px solid #f0f2f5;
  padding: 15px 20px;
}
.sales-board-des p {
  line-height: 1.6;
}
.sales-board-des h2 {
  font-size: 20px;
  padding-bottom: 15px;
}
.sales-board-des h3 {
  font-size: 18px;
  font-weight: bold;
  padding: 20px 0 10px 0;
}
.sales-board-des li {
  padding: 5px 0;
}
.sales-board-table {
  width: 100%;
  margin-top: 20px;
}
.sales-board-table th {
  background: #4fc08d;
  color: #fff;
}
.sales-board-table td {
  border: 1px solid #f0f2f5;
  padding: 15px;
}
.switch {
  width: 300px;
  font-size: 20px;
  text-align: left
}

</style>
