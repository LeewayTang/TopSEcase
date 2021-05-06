<template>
<div class="book-note-wrap">
  <div class="main-container">
  <new-info></new-info>
  <log-page-main></log-page-main>
  </div>
  <div class="right">
    <div class="header-block">
      <div class="header">
      <router-link to="/personalCenter">
        <img src="../assets/images/助教也是人.png" alt="头像" class="circular">
        <div class="user-name">用户名</div>
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
  width: 1200px;
}
.right {
  margin-left: 100px;
  flex-grow: 1;
}
.circular {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 3px solid rgba(255,255,255,0.4);
}
.header-block {
  margin-bottom: 50px;
}
.user-name {
  font-weight: bolder;
  font-size: 30px;
  color: #0f0f0f;
  margin-top: 20px;
}

</style>
