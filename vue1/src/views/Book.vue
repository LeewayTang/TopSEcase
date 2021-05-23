<template>
  <div class="book-wrap">
    <div class="book-left">
      <div class="product-board">
        <img :src="productIcon" width="220px;">
        <ul>
          <router-link v-for="item in products" :to="{ path: item.path }" tag="li" active-class="active" :key="item.id">
            {{ item.name }}
          </router-link>
        </ul>
      </div>
    </div>
    <div class="book-right">
      <keep-alive>
        <router-view></router-view>
      </keep-alive>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      products: [
        {
          name: '深入浅出Vue.js',
          path: 'count',
          active: false
        },
        {
          name: 'JavaScript高级程序设计',
          path: 'forecast',
          active: false
        },
        {
          name: 'Node.js源码分析',
          path: 'analysis',
          active: false
        },
        {
          name: 'Spring Boot实战',
          path: 'publish',
          active: false
        },
        {
          name: "fuck you",
          path: 'library',
          active: false
        }
      ],
      imgMap: {
        '/book':require('./../assets/images/1.png'),
        '/book/count': require("./../assets/images/1.png"),
        '/book/library': require("./../assets/images/1.png"),
        '/book/forecast': require("./../assets/images/2.png"),
        '/book/analysis': require("./../assets/images/3.png"),
        '/book/publish': require("./../assets/images/4.png")
      }
    }
  },
  computed: {
    productIcon () {
      return this.imgMap[this.$route.path]
    }
  }
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
.sales-board {
  background: #fff;
}
.sales-board-form {

}
.sales-board-intro h2 {
  font-size: 20px;
  padding: 20px;
}
.sales-board-intro p {
  background: #f7fcff;
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
  width: 100px;
}
.sales-board-line-right {
  display: inline-block;
  width: 75%;
}
.sales-board-des {
  border-top: 20px solid #f0f2f5;
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
</style>
