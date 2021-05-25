<template>
  <div class="wrapper">
    <div class="main">
    <h2 class='sector'>
      <section-title>导师推荐</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>

    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in tutorSugBooks" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <div>
              <a :title=item.name>
                <img :src="item.icon" height="280px" width="200px;">
                <div class="book-name">{{ item.name }}</div>
              </a>
            </div>
          </router-link>
        </li>
      </ul>
    </div>


    <h2 class='sector'>
      <section-title>同学推荐</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>

    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in peerSugBooks" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <div>
              <a :title=item.name>
                <img :src="item.icon" height="280px" width="200px;">
                <div class="book-name">{{ item.name }}</div>
              </a>
            </div>
          </router-link>
        </li>
      </ul>
    </div>

    <h2 class='sector'>
      <section-title>精彩点评</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>
      <div class="review">
        <li v-for="item in comments">
          {{item.review}}
          <br>
          <el-row type="flex" justify="end">—— {{item.name}}</el-row>
        </li>
      </div>
    </div>

    <div class="aside">
      <h2 class=''>
        <section-title>热门标签</section-title>
        <span class="link-more">
        <a class="" href="/tag/?view=type&amp;icn=index-sorttags-all"
        >所有热门标签»</a>
      </span>
      </h2>

      <ul class="hot-tags-col5 s" data-dstat-areaid="54" data-dstat-mode="click,expose">
        <ul class="tag_title">
          编程语言
        </ul>
        <ul>
        <router-link v-for="item in tags" :to="{ path : '/tag-detail/' + item.path }" active-class="active" :key="item.id">
        <li class="tag">{{item.name}}</li>
        </router-link>
      </ul>

        <ul class="tag_title">
          数据库（数据和上面一样懒得改了）
        </ul>
        <ul>
          <router-link v-for="item in tags" :to="{ path : '/tag-detail/' + item.path }" active-class="active" :key="item.id">
            <li class="tag">{{item.name}}</li>
          </router-link>
        </ul>

        <ul class="tag_title">
          操作系统
        </ul>
        <ul>
          <router-link v-for="item in tags" :to="{ path : '/tag-detail/' + item.path }" active-class="active" :key="item.id">
            <li class="tag">{{item.name}}</li>
          </router-link>
        </ul>

        <ul class="tag_title">
          计算机组成
        </ul>
        <ul>
          <router-link v-for="item in tags" :to="{ path : '/tag-detail/' + item.path }" active-class="active" :key="item.id">
            <li class="tag">{{ item.name }}</li>
          </router-link>
        </ul>
      </ul>
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
      tags: {}
    }
  },
  computed: {
  },
  methods: {
    fetchTSB(){
      fetchBookList().then(res=>{
        this.tutorSugBooks = res.data || [];
        // console.log(this.tutorSugBooks);
      })
    },
    fetchPSB(){
      fetchBookList().then(res=>{
        this.peerSugBooks = res.data || [];
        // console.log(this.tutorSugBooks);
      })
    },
    fetchReview(){
      fetchReview().then(res=>{
        this.comments = res.data || [];
      })
    },
    fetchTags(){
      fetchTags().then(res=>{
        this.tags = res.data || []
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
  width: 80%;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 120px;
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
  padding: 10px 10px;
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
</style>
