<template>
  <div class="book-wrap">
    <div class="book-left">
<!--      <el-card>-->
      <img :src="productIcon" class="image" width="220px" :alt="this.bookInfo.title">
      <el-button round @click="bookDialogVisible = true">
        修改封面
      </el-button>
<!--      </el-card>-->
    </div>
    <el-dialog title="编辑" :visible.sync="bookDialogVisible" :before-close="handleClose">
      <span>
        <el-row>
          <input
              ref="filElem"
              type="file"
              id="uploads"
              accept="image/png, image/jpeg, image/gif, image/jpg"
              @change="uploadImg($event,1)"
              class="el-button hide"
              style="font-size: 15px; margin-bottom:15px; margin-left: 0px"
          />
        </el-row>
        <el-row class="footerBtn" align="center">
          <el-button type="primary " size="medium" round @click="uploadBookImg">确认</el-button>
          <el-button type="info" size="medium" round @click="handleClose">取消</el-button>
        </el-row>
      </span>
    </el-dialog>
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
                作者 | {{ this.bookInfo.author }} ：出版社 ｜ {{ this.bookInfo.press }}
              </div>
            </div>
            <div class="sales-board-line">
              <div class="sales-board-line-left">
                ISBN：{{ this.bookInfo.ISBN }}
              </div>
            </div>
            <div class="sales-board-line">
              <el-row type="flex" justify="end">
                <el-button @click.stop="showCommentEditor=true">评论</el-button>
                <el-button type="primary" @click="handleGetBook">获取电子书</el-button>
              </el-row>

            </div>
          </div>
        </el-card>
        <div v-if="showCommentEditor" @click.stop="">
          <mavon-editor v-model="myComment" :toolbars="{
              bold: true, // 粗体
              italic: true,// 斜体
              header: true,// 标题
              quote: true, // 引用
              code: true, // code
              table: true, // 表格
              imagelink: true, // 图片链接
              fullscreen: true, // 全屏编辑
              subfield: true, // 单双栏模式
              preview: true, // 预览
            }"></mavon-editor>
          <el-button type="success" @click="submitReply">提交</el-button>
        </div>
        <el-card>
          <h1>精彩书评</h1>
          <div class="sales-board-des">
            <li>
              {{bookInfo.review}}
              <br>
<!--              <el-row type="flex" justify="end">—— {{item.username}}</el-row>-->
            </li>
          </div>
        </el-card>
        <div class="comments">
          <comment v-for="item in comments" :comment="item">
          </comment>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VSelection from "../components/base/selection";
import VCounter from "../components/base/counter";
import VChooser from "../components/base/chooser";
import comment from '../components/comment';
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
    comment,
    VMulChooser,
    MyDialog: Dialog,
  },
  data () {
    return {
      bookInfo:{},
      bookList: [],
      bookDialogVisible: false,
      showCommentEditor: false,
      myComment: '',
      comments: [],
      file: [],
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
    this.getComment();
  },
  methods: {
    getComment(){
      let self = this;
      console.log("id : " + self.$route.params.id)
      self.$axios({
        url: '/api/book/getIdComment/',
        method: 'post',
        data:{
          id: self.$route.params.id,
        }
      }).then(res => {
        self.comments = res.data.data || [];
      }).catch(err => {
        console.log(err);
      })
    },
    handleGetBook(){
      let url = window.location.href.split('#')[0];
      window.location.href = url + 'media/' + this.bookInfo.file
    },
    uploadImg(e, num) {
      const file = e.target.files[0];
      if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
        this.$message.error("图片类型必须是.gif,jpeg,jpg,png,bmp中的一种");
        return false;
      }
      this.file = e.target.files;
      console.log(this.file)
    },
    handleClose(v) {
      this.bookDialogVisible = false;
    },
    submitReply(){
      let self = this
      self.$axios({
        url: '/api/book/setComment/',
        method: 'post',
        data: {
          id: self.$route.params.id,
          content: self.myComment,
          token: sessionStorage.getItem('Authorization'),
          toUsername: '',
        }
      }).then(res => {
        switch (res.data.status){
          case -3:
            self.$Notice.open({
              title: '游客禁止发布评论',
            });
            break;
          case 1:
            self.$Notice.open({
              title: '评论成功'
            })
            window.location.reload();
            break;
        }
      }).catch(err => {
        console.log(err);
      })
    },
    uploadBookImg(){
      let self = this;
      if(self.file === '' || self.file === null){
        self.$message({
          type: 'error',
          message: '输入不能为空'
        })
      }else{
        let formData = new FormData();
        formData.append('file', self.file[0]);
        console.log(self.file);
        formData.append('token', sessionStorage.getItem('Authorization'));
        formData.append('id', this.$route.params.id)
        self.$axios.post('/api/upload/uploadBookImg/', formData,{
          headers:{
            "Content-Type": "multipart/form-data"
          }
        }).then(res => {
          switch (res.data.status){
            case -1:
              self.$message({
                type: 'error',
                message: '游客禁止改封面'
              });
              break;
            case 1:
              self.$message({
                type: 'success',
                message: '修改成功'
              });
              window.location.reload();
              break;

          }
        })
      }
    },
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
    },
    close(){
      this.showCommentEditor = false
    },
  },
  mounted() {
    this.fetchBookInfo(this.bookInfo.id)
  },
  watch:{
    showCommentEditor(value) {
      if (value) {
        document.body.addEventListener('click', this.close)
      } else {
        document.body.removeEventListener('click', this.close)
      }
    }
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
  border-top: 20px solid #FFFFFF;
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
