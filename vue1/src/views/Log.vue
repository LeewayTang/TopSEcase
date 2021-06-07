<template>
<div class="book-note-wrap">
  <div class="main-container">
<!--    <new-info></new-info>-->
    <log-page-main></log-page-main>
  </div>
  <div class="right">
    <div class="square-block" :style="{backgroundImage: 'url('+ bg+ ')'}">
      <div class="header">
      <router-link :to="/personalCenter/ + $store.state.username">
        <img :src="webSiteInfo.avatar" alt="头像" class="circular">
        <div class="user-name">{{ webSiteInfo.username }}</div>
      </router-link>
        <div class="line"/>
        <div class="slogan">{{webSiteInfo.slogan}}</div>
      </div>
    </div>
    <div class="qz">
      <div class="quanzi">
        <div class="title">你可能想follow的人</div>
        <ul v-for="item in sugList">
        <li class="sug-item"><router-link :to="/personalCenter/ + item">{{item}}</router-link></li>
        </ul>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import LogPageMain from "../components/log/main";
import NewInfo from "../components/log/newInfo";
import SectionTitle from "../components/section-title";
import {fetchSuggest} from "../api";


export default {
  name: "Log",
  components: {SectionTitle, NewInfo, LogPageMain},
  data() {
    return {
      webSiteInfo: {},
      bg: require('../assets/images/bg1.jpg'),
      sugList: [],
    }
  },
  created() {
    this.getWebSiteInfo()
    this.getSugList()
  },
  methods:{
    getWebSiteInfo(){
      this.webSiteInfo = this.$store.state.websiteInfo
    },
    getSugList() {
      fetchSuggest().then(res=>{
        this.sugList = res.follow || []
      })
    }
  }
}
</script>

<style scoped>
.line{
  height: 1px;
  width: 80%;
  background-color: lightgrey;
  margin-left: 10%;
  margin-top: 20px;
}
.slogan{
  width: 80%;
  margin-left: 10%;
  margin-right: 20%;
  margin-top: 10%;
}
.book-note-wrap {
  width: 70%;
  padding-top: 20px;
  margin-left: 15%;
  margin-right: 15%;
  display: flex;
  horiz-align: center;
}
.main-container {
  width: 70%;
  height: fit-content;
  background-color: #eff3f6;
}
.right {
  margin-left: 20px;
  flex-grow: 1;
  width: 30%;
}
.circular {
  margin-left: 20px;
  margin-top: 75px;
  width: 85px;
  height: 85px;
  border-radius: 50%;
  border: 3px solid rgba(255,255,255,0.4);
}
.square-block {
  /*width: 400px;*/
  height: 400px;
  /*background: linear-gradient(to bottom, black 30%, grey 30%,whitesmoke 60%,whitesmoke 100%);*/
  margin-bottom: 50px;
  background-size: cover;
  /*border: 1px solid rgba(155,155,155,0.6);*/
}
.header{
  /*position: absolute;*/
  /*width: 400px;*/
  height: 30%;
}
.user-name {
  margin-left: 20px;
  font-weight: bold;
  font-size: 30px;
  color: #0f0f0f;
}
.qz{
  height: fit-content;
  background-color: #dfdfe8;
}
.quanzi {
  height: fit-content;
  background-color: rgba(232,246,255,0.1);
}

.sug-item {
  height: 75px;
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
</style>
