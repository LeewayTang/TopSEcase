<template>
  <div class="articles">
    <div class="header" :style="{backgroundImage: 'url(' + bg + ')'}">
      <div class="header-text">{{articles.header}}</div>
    </div>
    <div class="site-content animate">
      <!--            &lt;!&ndash; 文章目录 &ndash;&gt;-->
      <!--            <div id="article-menus">-->
      <!--              <h1>目录</h1>-->
      <!--              <br>-->
      <!--                <menu-tree :menus="menus" child-label="child"></menu-tree>-->
      <!--            </div>-->
      <main class="site-main">
        <article class="hentry">
          <!-- 文章头部 -->
          <div class="markdown-body">
            <VueMarkdown :source="articles.content" v-highlight></VueMarkdown>
          </div>
          <!-- 文章底部 -->
          <section-title>
            <footer class="post-footer">
              <el-button @click.stop="showCommentEditor=true">评论</el-button>
              <!-- 阅读次数 -->
              <div class="post-like">
                <i class="iconfont iconeyes"></i>
                <span class="count">{{views}}</span>
              </div>
              <!-- 文章标签 -->
              <div class="post-tags" v-for="(tag) in category">
                <i class="iconfont iconcategory" v-if="firstCategory.id === tag.id"></i>
                <el-tag @click="search(tag.tag)" style="cursor: pointer">{{tag.tag}}</el-tag>
              </div>
            </footer>
          </section-title>
          <div v-if="showCommentEditor" @click.stop="">
            <mavon-editor v-model="myComment" :toolbars="{
                  bold: true, // 粗体
                  italic: true,// 斜体
                  header: true,// 标题
                  quote: true, // 引用
                  code: true, // code
                  table: true, // 表格
                  imagelink: true, // 图片链接
                  fullscreen: true, // 全屏编辑
                  subfield: true, // 单双栏模式
                  preview: true, // 预览
                }"></mavon-editor>
            <el-button type="success" @click="submitReply">提交</el-button>
          </div>
          <!--评论-->
          <div class="comments">
            <comment v-for="item in comments" :comment="item">
<!--              <template v-if="item.reply.length">-->
<!--                <comment v-for="reply in item.reply" :key="reply.id" :comment="reply"></comment>-->
<!--              </template>-->
            </comment>
          </div>
        </article>
      </main>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/banner'
import sectionTitle from '@/components/section-title'
import comment from '@/components/comment'
import menuTree from '@/components/menu-tree'
import {fetchComment,fetchArticle} from '../api'
import VueMarkdown from 'vue-markdown'
export default {
  name: 'discuss',
  data(){
    return{
      showDonate: false,
      value: '',
      comments: [],
      menus: [],
      articles: {},
      views: 0,
      category: [],
      firstCategory: '',
      myComment: '',
      showCommentEditor: false,
      bg: require('../assets/images/background.jpeg'),
    }
  },
  components: {
    Banner,
    sectionTitle,
    comment,
    menuTree,
    VueMarkdown
  },
  methods: {
    getComment(){
      let self = this;
      self.$axios({
        url: '/api/discuss/getIdComment/',
        method: 'post',
        data:{
          id: self.$route.params.id,
        }
      }).then(res => {
        self.comments = res.data.data || [];
      }).catch(err => {
        console.log(err);
      })
    },
    search(v){
      // console.log(this.searchValue)
      this.$router.push({name:'search',params:{words: v, type: 'tag2'}});
      this.close()
    },
    fetchH(arr,left,right){
      if (right) {
        return arr.filter(item => item.offsetTop > left && item.offsetTop < right)
      }else {
        return arr.filter(item => item.offsetTop > left)
      }
    },
    getArticle(){
      let self = this;
      self.$axios(
          {
            url: '/api/discuss/getIdDiscuss/',
            method: 'post',
            data:{
              id: self.$route.params.id,
            }
          }
      ).then(res => {
        switch (res.data.status){
          case -1:
            self.$Notice.open({
              title: '讨论不存在'
            });
            self.$router.push({
              path: '/home'
            });
            break;
          case 1:
            self.articles = res.data.data || []
            self.views = res.data.data.views
            self.category = res.data.data.tag
            self.firstCategory = res.data.data.tag[0]
            console.log(res)
            break;
        }
      }).catch(err => {
        console.log(err)
      })
    },
    reply(id){
      const ref = `comment${id}`
    },
    submitReply(){
      let self = this
      self.$axios({
        url: '/api/discuss/setComment/',
        method: 'post',
        data: {
          id: self.$route.params.id,
          content: self.myComment,
          token: sessionStorage.getItem('Authorization'),
          toUsername: '',
        }
      }).then(res => {
        switch (res.data.status){
          case -3:
            self.$Notice.open({
              title: '游客禁止发布评论',
            });
            break;
          case 1:
            self.$Notice.open({
              title: '评论成功'
            })
            window.location.reload();
            break;
        }
      }).catch(err => {
        console.log(err);
      })
    },
    close(){
      this.showCommentEditor = false
    },
  },
  created() {
    this.getComment()
    this.getArticle()
  },
  watch:{
    showCommentEditor(value) {
      if (value) {
        document.body.addEventListener('click', this.close)
      } else {
        document.body.removeEventListener('click', this.close)
      }
    }
  },
}
</script>
<style scoped lang="less">
.site-content {
  position: relative;
  .site-main {
    padding: 80px 0 0 0;
  }
}
#article-menus{
  position: sticky;
  top: 0;
  box-shadow: 0 2px 6px rgba(0, 0, 0, .1);
  border-radius: 3px;
  padding: 15px;
  width: 280px;
  transform: translateX(-120%) translateY(150px);
  font-size: 14px;
  margin-left: 40px;
  margin-right: 10px;
}
article.hentry {
  .entry-header {
    .entry-title {
      font-size: 23px;
      font-weight: 600;
      color: #737373;
      margin: 0.67em 0;

      &:before {
        content: "#";
        margin-right: 6px;
        color: #d82e16;
        font-size: 20px;
        font-weight: 600;
      }
    }

    hr {
      height: 1px;
      border: 0;
      background: #EFEFEF;
      margin: 15px 0;
    }

    .breadcrumbs {
      font-size: 14px;
      color: #D2D2D2;
      text-decoration: none;
      margin-bottom: 30px;
    }
  }

  .entry-content {}

  footer.post-footer {
    width: 100%;
    padding: 20px 10px;
    margin-top: 30px;
    height: 65px;
    position: relative;
    i{
      font-size: 18px;
      margin-right: 5px;
    }
    .post-like {
      float: right;
      margin: 7px 0 0 20px;
    }

    .post-share {
      float: right;
      list-style: none;
      margin-right: 20px;
    }

    .donate {
      float: left;
      line-height: 36px;
      border-radius: 100%;
      -webkit-border-radius: 100%;
      -moz-border-radius: 100%;
      border: 1px solid #2B2B2B;
      &:hover{
        border: 1px solid goldenrod;
        span{
          color: goldenrod;
        }
      }
      span {
        color: #2B2B2B;
        padding: 10px;
        position: relative;
        cursor: pointer;
      }

      .donate_inner {
        display: none;
        margin: 0;
        list-style: none;
        position: absolute;
        left: 80px;
        top: -40px;
        background: #FFF;
        padding: 10px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 6px rgba(0, 0, 0, .08);
        border-radius: 3px;
        &.show{
          display: block;
        }
        li {
          float: left;
        }

        img {
          width: 100px;
        }
        p {
          text-align: center;
          font-size: 15px;
          color: #D2D2D2;
          line-height: 1rem;
        }
      }

      .donate_inner:after, .donate_inner:before {
        content: "";
        position: absolute;
        left: 0;
        bottom: 45%;
        margin-left: -8px;
        border-top: 8px solid transparent;
        border-bottom: 8px solid transparent;
        border-right: 8px solid #fff;
      }

      .donate_inner:before {
        left: -1px;
        border-right: 8px solid #ddd;
      }

    }

    .post-tags {
      margin: 7px 0 0 20px;
      float: left;
      text-transform: uppercase;
      a:hover{
        color: #ff6d6d;
      }
    }
    .el-button {
      margin-left: 50px;
      float: right;
      color: #199c86;
    }
  }
  .open-message {
    margin: 50px 0;
    position: relative;
    background: #2B2B2B;
    padding: 10px 30px;
    border-radius: 3px;
    font-size: 14px;
    color: #fff;
    &:after {
      content: "";
      border-left: 10px solid transparent;
      border-right: 10px solid transparent;
      border-bottom: 10px solid #2B2B2B;
      position: absolute;
      top: -8px;
      left: 48%;
    }
    p {
      margin: 10px 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    a {
      color: #A0DAD0;
      padding: 0 5px;
    }
  }
}
.header{
  height: 200px;
  width: 100%;
  background-size: cover;
}
.header-text{
  color: white;
  font-size: xxx-large;
  text-align: center;
  padding-top: 100px;
}
.v-note-wrapper {
  z-index: 0;
}
</style>
