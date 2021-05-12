<template>
  <div class="book-note-wrap">
    <div class="main-container">
      <new-info></new-info>
      <log-page-main></log-page-main>
    </div>
    <div class="right">
      <div class="s-block">
        <section-title>发现同学</section-title>
        <div class="sug-list">
          <li class="sug-item"><router-link to="/">cynic</router-link></li>
          <li class="sug-item"><router-link to="/">leeway</router-link></li>
          <li class="sug-item"><router-link to="/">MichaleJacksonXXX</router-link></li>
          <li class="sug-item"><router-link to="/">YogurtMakesYoungsters</router-link></li>
        </div>
      </div>
      <div class="quanzi">
        <section-title>
          圈子推荐
        </section-title>
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
  width: 1400px;
  margin-top: 120px;
  margin-left: auto;
  margin-right: auto;
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
.s-block {
  width: 400px;
  height: 400px;
  margin-bottom: 50px;
}

.quanzi {
  height: 600px;
  width: 400px;
  background-color: #dfdfe8;
}
.sug-item {
  height: 75px;
  width: 400px;
  padding-bottom: 30px;
}
</style>


