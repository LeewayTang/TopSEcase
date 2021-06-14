<template>
  <div class="book-wrap">
    <div class="book-left">
<!--      <el-card>-->
        <img :src="productIcon" class="image" width="220px" :alt="this.bookInfo.title">
<!--      </el-card>-->
    </div>
    <div class="book-right">
      <div class="sales-board">
        <el-card>
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
              <el-row type="flex" justify="end">
                <el-button type="primary">获取电子书</el-button>
              </el-row>
            </div>
          </div>
        </el-card>
        <el-card>
          <h1>精彩书评</h1>
          <div class="sales-board-des">
            <li v-for="item in bookInfo.comments">
              {{item.says}}
              <br>
              <el-row type="flex" justify="end">—— {{item.username}}</el-row>
            </li>
          </div>
        </el-card>
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
      bookInfo:{},
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
    this.fetchBookInfo();
  },
  methods: {
    fetchBookInfo(){
      let self = this;
      let id = self.$route.params.id;
      console.log(id);
      self.$axios({
        url: '/api/book/getIdBook/',
        method: 'post',
        data:{
          id: id,
        }
      }).then(res =>{
        switch (res.data.status){
          case -1:
            self.$Notice.open({
              title: '查无此书'
            });
            self.$router.push({
              path: '/home',
            });
            break;
          case 1:
            self.bookInfo = res.data.data[0];
            break;
        }
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

.sales-board-intro h2 {
  font-size: 20px;
  padding: 20px;
}
.sales-board-intro p {
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
.el-card {
  margin-bottom: 20px;
}
/*.image {*/
/*  padding-right: 30px;*/
/*}*/
</style>
