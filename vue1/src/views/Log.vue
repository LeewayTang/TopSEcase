<template>
<div class="book-note-wrap">
  <div class="main-container">
  <new-info></new-info>
  <log-page-main></log-page-main>
  </div>
  <div class="right">
    <div class="square-block">
      <div class="header">
      <router-link to="/personalCenter">
        <img src="../assets/images/助教也是人.png" alt="头像" class="circular">
        <div class="user-name">用户名</div>
        <div class="follow-and-followed">
          <div class="follow">99 关注</div> |
          <div class="followed">99 被关注</div>
        </div>
      </router-link>
      </div>
    </div>
    <div class="quanzi">
      <section-title>
        我的圈子
      </section-title>
    </div>
  </div>
</div>
</template>

<script>
import LogPageMain from "../components/log/main";
import NewInfo from "../components/log/newInfo";
import SectionTitle from "../components/section-title";
export default {
name: "Log",
  components: {SectionTitle, NewInfo, LogPageMain}
}
</script>

<style scoped>
.book-note-wrap {
  margin-top: 120px;
  display: flex;
}
.main-container {
  width: 1000px;
}
.right {
  margin-left: 20px;
  flex-grow: 1;
}
.circular {
  margin-left: 20px;
  margin-top: 155px;
  width: 85px;
  height: 85px;
  border-radius: 50%;
  border: 3px solid rgba(255,255,255,0.4);
}
.square-block {
  width: 400px;
  height: 400px;
  background: linear-gradient(to bottom, grey 0%, grey 50%,whitesmoke 50%,whitesmoke 100%);
  margin-bottom: 50px;
}
.user-name {
  margin-left: 20px;
  font-weight: bolder;
  font-size: 30px;
  color: #0f0f0f;
  margin-top: 10px;
}
.follow-and-followed {
  margin-left: 20px;
  margin-top: 10px;
}
.follow {
  display: inline-block;
}
.followed {
  display: inline-block;
}
</style>
