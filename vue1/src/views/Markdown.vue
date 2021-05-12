// index.vue
// 只需要这个文件
<template>
  <div class="post">
    <div class="title">
      <h2>{{this.article.title}}</h2>
    </div>
    <div class="container">
      <div class="markdown-body">
        <div v-html="compileMarkdown" v-highlight></div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import Marked from "Marked";
// 这里引入想要的样式
import "../../../node_modules/github-markdown-css/github-markdown.css";
let renderMd = new Marked.Renderer();
Marked.setOptions({
  renderer: renderMd,
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  // 引入样式
  highlight: function(code) {
    return require("highlight.js").highlightAuto(code).value;
  }
});

export default {
  components: {
  },
  data() {
    return {
      article: {
        content: "加载中……"
      }
    };
  },
  computed: {
    compileMarkdown() {
      return Marked(this.article.content, { sanitize: true });
    }
  },
  created: function() {
    this.$ajax({
      url: "/api/article/id",
      method: "get",
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      if (res.status === 200) {
        this.article = res.data;
      } else {
        //报错
      }
    });
  }
};
</script>

<style scoped >
.post .title {
  margin-top: 50px;
  text-align: center;
  font-size: 24px;
}
</style>