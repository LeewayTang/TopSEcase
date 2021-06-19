<template>
  <div class="wrapper">
    <div class="main">

      <el-card>
      <div class='sector'>
      <section-title>导师推荐</section-title>
      <span class="link-more">
        <router-link :to="{path: '/books/tag/tutor'}"
        > 更多»</router-link>
      </span>
    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in tutorSugBooks" :to="{ path : '/books/' + item.id}" tag="li" active-class="active"
                       :key="item.id" class="link-to">
            <div>
              <a :title=item.title>
                <img :src="item.img" height="280px" width="200px;">
                <div class="book-name">{{ item.title }}</div>
              </a>
            </div>
          </router-link>
        </li>
      </ul>
    </div>
    </div>
      </el-card>

      <el-card>
        <div class='sector'>
          <section-title>同学推荐</section-title>
          <span class="link-more">
        <router-link :to="{path: '/books/tag/student'}"
        > 更多»</router-link>
      </span>
          <div class="book-bubble">
            <ul class="books">
              <li>
                <router-link v-for="item in peerSugBooks" :to="{ path : '/books/' + item.id }" tag="li" active-class="active"
                             :key="item.id" class="link-to">
                  <div>
                    <a :title=item.title>
                      <img :src="item.img" height="280px" width="200px;">
                      <div class="book-name">{{ item.title }}</div>
                    </a>
                  </div>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </el-card>

<!--    <el-card>-->
<!--      <div class='sector'>-->
<!--        <section-title>精彩点评</section-title>-->
<!--        <span class="link-more">-->
<!--        <a class="" href="/latest?icn=index-latestbook-all"-->
<!--        > 更多»</a>-->
<!--      </span>-->
<!--      </div>-->
<!--      <div class="review">-->
<!--        <li v-for="item in comments">-->
<!--          {{item.review}}-->
<!--          <br>-->
<!--          <el-row type="flex" justify="end">—— {{item.name}}</el-row>-->
<!--        </li>-->
<!--      </div>-->
<!--    </el-card>-->
    </div>


    <div class="aside">
      <el-card>
      <h2 class=''>
        <section-title>热门标签</section-title>
        <span class="link-more">
        </span>
      </h2>
      <ul class="hot-tags-col5 s" data-dstat-areaid="54" data-dstat-mode="click,expose">
        <ul>
        <router-link v-for="item in tags" :to="{ path : '/books/tag/' + item.tag }" active-class="active" :key="item.tag">
        <el-tag class="tag">{{item.tag}}</el-tag>
        </router-link>
      </ul>
      </ul>
      </el-card>
    </div>

  </div>
</template>

<script>
import SectionTitle from "../components/section-title";
import {fetchTags, fetchBookList, fetchReview} from "../api";
export default {
  components: {SectionTitle},
  data () {
    return {
      tutorSugBooks: [],
      peerSugBooks: [],
      comments: [],
      tags: {},
      tagTitle: ['编程语言', '数据库', '操作系统', '计算机组成']
    }
  },
  computed: {
  },
  methods: {
    fetchTSB(){
      let self = this;
      self.$axios({
        url: '/api/search/searchBook/',
        method: 'post',
        data:{
          tag: 'tutor',
          number: 4
        }
      }).then(res => {
        this.tutorSugBooks = res.data.data || [];
      }).catch(err =>{
        console.log(err);
      })
    },
    fetchPSB(){
      let self = this;
      self.$axios({
        url: '/api/search/searchBook/',
        method: 'post',
        data:{
          tag: 'student',
          number: 4
        }
      }).then(res => {
        this.peerSugBooks = res.data.data || [];
      }).catch(err =>{
        console.log(err);
      })
    },
    fetchReview(){
      fetchReview().then(res=>{
        this.comments = res.data || [];
      })
    },
    fetchTags(){
      let self = this;
      self.$axios({
        url: '/api/book/getTag',
        method: 'get'
      }).then(res => {
        this.tags = res.data.data;
      }).catch(err => {
        console.log(err)
      })
    }
    // fetchPSB() {
    //   fetchPSB().then(res => {
    //     this.bookList = res.data || [];
    //     // console.log(this.bookList);
    //   })
    // }
  },
  created() {
    this.fetchTSB();
    this.fetchPSB();
    this.fetchTags();
    this.fetchReview();
    console.log("Fetch finish");
  },
}
</script>

<style scoped>
.wrapper {
  width: 90%;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 20px;
  display: flex;
}
.link-more {
  padding-left: 20px;
  display: inline-block;
}
.link-to {
  width: 200px;
}
.book-bubble {
  margin-top: 20px;
}
.books li {
  float: left;
  margin-right: 30px;
}
.book-name {
  margin-top: 20px;
  font-size: 20px;
  text-align: center;
}
.sector {
  width: 950px;
}
.main {
  width: 950px;
}
.aside {
  /*margin-top: 50px;*/
  margin-left: 10px;
  flex-grow: 1;
}
.tag {
  font-size: 20px;
  display: inline;
  margin-right: 10px;
  margin-top: 10px;
  background-color: #eef1f3;
  color: #354b44;
}
.tag:hover {
  color: #e7051e;
}
.more_tag {
  color: #3b4151;
}
.tag_title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 20px;
  padding-top: 20px;
  padding-bottom: 10px;
  color: #000000;
}
.el-card {
  margin-bottom: 20px;
}
</style>
