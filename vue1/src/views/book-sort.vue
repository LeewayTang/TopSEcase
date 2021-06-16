<template>
  <div class="book-wrap">
    <div class="main">
      <div v-for="item in books">
        <el-card>
          <book :book="item" :key="item.id"></book>
        </el-card>
      </div>
    </div>
    <div class="aside">
      <el-card>
        <h2>
          <section-title>相关热门标签</section-title>
        </h2>
        <ul>
            <router-link v-for="tag in tags" :to="{ path : '/books/tag/' + tag.tag }" :key="tag.tag">
              <el-tag class="tag">{{tag.tag}}</el-tag>
            </router-link>
        </ul>
      </el-card>
    </div>
  </div>
</template>

<script>
import book from '../components/book'
import SectionTitle from "../components/section-title";

export default {
  name: "book-sort",
  components: {
    book,
    SectionTitle,
  },
  data() {
    return {
      books: [],
      tags: ['Java', 'C#', 'Vue', 'Django', 'Verilog', 'OS']
    }
  },
  methods: {
    getBook() {
      this.$axios({
            url: '/api/search/searchBook/',
            method: 'post',
            data:{
              tag: this.$route.params.tag
            }
      }).then(res => {
        // console.log(res)
        this.books = res.data.data || []
        // console.log(this.articles)
        // console.log('get articles ok')
      }).catch(err => {
        console.log(err)
      })
    },
    getTag(){
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
  },
  mounted() {
    this.getBook()
    this.getTag()
  },
  watch:{
    '$route.params.tag'(){
      this.getBook()
    }
  }
}
</script>

<style scoped>
.book-wrap {
  width: 90%;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 20px;
  display: flex;
}
.main {
  width: 950px;
}
.aside {
  margin-left: 10px;
  flex-grow: 1;
}
.el-card {
  margin-bottom: 10px;
}
.tag {
  font-size: 20px;
  display: inline-block;
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
</style>
