<template>
  <div class="book-note-wrap">
    <div class="main-container">
      <new-info></new-info>
      <log-page-main></log-page-main>
    </div>
    <div class="right">
      <div class="s-block">
        <div class="title">圈内同学</div>
        <div class="sug-list">
          <li class="sug-item"><router-link to="/">cynic</router-link></li>
          <li class="sug-item"><router-link to="/">leeway</router-link></li>
          <li class="sug-item"><router-link to="/">Michalel</router-link></li>
          <li class="sug-item"><router-link to="/">Yogurt</router-link></li>
        </div>
      </div>
      <div class="quanzi">
        <div class="title">优秀圈子</div>
        <li class="sug-item"><router-link to="/">cynic</router-link></li>
        <li class="sug-item"><router-link to="/">leeway</router-link></li>
        <li class="sug-item"><router-link to="/">MichaleJacksonXXX</router-link></li>
        <li class="sug-item"><router-link to="/">YogurtMakesYoungsters</router-link></li>
      </div>
    </div>
  </div>
</template>

<script>
import LogPageMain from "../components/log/main";
import NewInfo from "../components/log/newInfo";
import SectionTitle from "../components/section-title";
export default {
  name: "UserContent",
  components: {SectionTitle, NewInfo, LogPageMain}
}
</script>

<style scoped>
.book-note-wrap {
  width: 70%;
  margin-top: 120px;
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
  background-color: rgba(232,246,255,0.1);
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

</style>


