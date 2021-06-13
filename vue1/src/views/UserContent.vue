<template>
  <div class="book-note-wrap">
    <div class="main-container">
      <div class="body">
        <div class="body-left">
          <div class="content" v-for="item in articles">
            <el-card>
              <post :post="item" :key="item.id"></post>
            </el-card>
          </div>
        </div>
      </div>
    </div>
    <div class="right">
      <el-card>
        <div class="title">圈内同学</div>
        <div class="sug-list" v-for="item in sugPeer">
          <li class="sug-item"><router-link :to="/personalCenter/ + item.username">{{ item.username }}</router-link></li>
        </div>
      </el-card>
      <div>
<!--        <router-link to="/discussion">test</router-link>-->
      </div>
    </div>
  </div>
</template>

<script>
import LogPageMain from "../components/log/main";
import NewInfo from "../components/log/newInfo";
import SectionTitle from "../components/section-title";
import ForumList from "../components/forum/forumList"
import ForumPageMain from "../components/forum/main";
import Discussion from "./Discussion";
import {fetchSuggest} from "../api";
import post from '../components/post'

export default {
  name: "UserContent",
  components: {ForumPageMain, ForumList, SectionTitle, NewInfo, LogPageMain, post},
  data() {
    return {
      sugPeer: [],
      sugQuanzi: [],
      articles: [],
      Quanzi: [],
    }
  },
  methods: {
    getSugList() {
      let self = this
      self.$axios({
        url: '/api/user/getUserQuanzi/',
        method: 'post',
        data: {
          token: sessionStorage.getItem('Authorization'),
        },
      }).then(res =>{
        switch (res.data.status){
          case -1:
            self.$Notice.open({
              title: '请登录',
            });
            self.$router.push({
              path: '/login'
            });
            break;
          case 1:
            self.Quanzi = res.data.data.quanzi || [];
            self.$axios({
              url: '/api/search/searchQuanzi/',
              method: 'post',
              data: {
                qz: self.Quanzi[0].name,
              }
            }).then(res =>{
              switch (res.data.status){
                case -1:
                  self.$Notice.open({
                    title: '请登录',
                  });
                  self.$router.push({
                    path: '/login'
                  });
                  break;
                case 1:
                  self.sugPeer = res.data.user || [];
                  console.log(self.sugPeer)
                  break;
              }
            }).catch(err =>{
              console.log(err);
            })
            break;
        }
      }).catch(err =>{
        console.log(err);
      })
    },
    getArticles() {
      this.$axios(
          {
            url: '/api/discuss/getAllDiscuss/',
            method: 'get'
          }
      ).then(res => {
        // console.log(res)
        this.articles = res.data.data || []
        // console.log(this.articles)
        // console.log('get articles ok')
      }).catch(err => {
        console.log(err)
      })
    },
  },
  mounted() {
    this.getSugList();
    this.getArticles();
  }
}
</script>

<style scoped>
.book-note-wrap {
  width: 70%;
  padding-top: 20px;
  margin-left: auto;
  margin-right: auto;
  display: flex;
}
.main-container {
  width: 70%;
}
.right {
  width: 30%;
  margin-left: 20px;
  flex-grow: 1;
}

.s-block {
  background-color: rgba(232, 246, 255, 0.1);
  /*width: 30%;*/
  height: fit-content;
  margin-bottom: 50px;
  /*border: 1px solid gainsboro;*/
}

.quanzi {
  height: fit-content;
  /*width: 30%;*/
  background-color: rgba(232,246,255,0.1);
}
.sug-item {
  height: 75px;
  /*width: 30%;*/
  /*padding-bottom: 30px;*/
  padding-left: 30px;
  box-sizing: border-box;
  border: 1px solid #EEF0F6;
  vertical-align: middle;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.title{
  background-color: white;
  height: 20%;
  padding: 20px;
  font-weight: bold;
  color: #3bb4f2;
}
.el-card {
  margin-bottom: 10px;
}

</style>


