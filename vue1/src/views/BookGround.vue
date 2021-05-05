<template>
  <div class="wrapper">
    <h2 class='sector'>
      <span class="sec-title">导师推荐</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>
    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in products" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <a :title=item.name> <img :src="item.icon" height="280px" width="220px;"> </a>
            <div class="book-name"><a>{{ item.name }}</a></div>
          </router-link>
        </li>
      </ul>
    </div>
    <br>
    <h2 class='sector'>
      <span class="sec-title">同学推荐</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>
    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in products" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <a :title=item.name> <img :src="item.icon" height="280px" width="220px;"> </a>
            <div class="book-name"><a>{{ item.name }}</a></div>
          </router-link>
        </li>
      </ul>
    </div>
    <h2 class='sector'>
      <span class="sec-title">精彩点评</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>
  </div>
</template>

<script>
export default {
  data () {
    return {
      products: [
        {
          name: '深入浅出Vue.js',
          path: '/book/count',
          icon: require('../assets/images/1.png'),
          active: false
        },
        {
          name: 'JavaScript高级程序设计',
          path: '/book/forecast',
          icon: require('../assets/images/2.png'),
          active: false
        },
        {
          name: 'Node.js源码分析',
          path: '/book/analysis',
          icon: require('../assets/images/3.png'),
          active: false
        },
        {
          name: 'Spring Boot实战',
          path: '/book/publish',
          icon: require('../assets/images/4.png'),
          active: false
        }
      ],
    }
  },
  computed: {
  }
}
</script>

<style scoped>
.wrapper {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 120px;
}
.sec-title {
  font-weight: bolder;
  color: #0f0f0f;
  padding-right: 20px;
  font-size: 35px;
}
.link-to {
  width: 220px;
}
.book-bubble {
  margin-top: 40px;
}
.books li {
  float: left;
  margin-right: 40px;
}
.book-name {
  margin-top: 20px;
  font-size: 20px;
}
.sector {
  width: 1000px;
}
</style>
