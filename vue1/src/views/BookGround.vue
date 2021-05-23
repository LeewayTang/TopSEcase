<template>
  <div class="wrapper">
    <div class="main">
    <h2 class='sector'>
      <section-title>导师推荐</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>

    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in products" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <div>
              <a :title=item.name>
                <img :src="item.icon" height="280px" width="200px;">
                <div class="book-name">{{ item.name }}</div>
              </a>
            </div>
          </router-link>
        </li>
      </ul>
    </div>


    <h2 class='sector'>
      <section-title>同学推荐</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>

    <div class="book-bubble">
      <ul class="books">
        <li>
          <router-link v-for="item in products" :to="{ path : item.path }" tag="li" active-class="active" :key="item.id" class="link-to">
            <div>
              <a :title=item.name>
                <img :src="item.icon" height="280px" width="200px;">
                <div class="book-name">{{ item.name }}</div>
              </a>
            </div>
          </router-link>
        </li>
      </ul>
    </div>

    <h2 class='sector'>
      <section-title>精彩点评</section-title>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
        > 更多»</a>
      </span>
    </h2>
    </div>

    <div class="aside">
      <h2 class=''>
        <section-title>热门标签</section-title>
        <span class="link-more">
        <a class="" href="/tag/?view=type&amp;icn=index-sorttags-all"
        >所有热门标签»</a>
      </span>
      </h2>

      <ul class="hot-tags-col5 s" data-dstat-areaid="54" data-dstat-mode="click,expose">



        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              文学
            </ul>
            <li>
              <a href="/tag/小说" class="tag">小说</a>
            </li>
            <li>
              <a href="/tag/随笔" class="tag">随笔</a>
            </li>
            <li>
              <a href="/tag/日本文学" class="tag">日本文学</a>
            </li>
            <li class="last">
              <a href="/tag/散文" class="tag">散文</a>
            </li>
            <li>
              <a href="/tag/诗歌" class="tag">诗歌</a>
            </li>
            <li>
              <a href="/tag/童话" class="tag">童话</a>
            </li>
            <li>
              <a href="/tag/名著" class="tag">名著</a>
            </li>
            <li class="last">
              <a href="/tag/港台" class="tag">港台</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文学" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>

        <li> </li>

        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              流行
            </ul>
            <li>
              <a href="/tag/漫画" class="tag">漫画</a>
            </li>
            <li>
              <a href="/tag/推理" class="tag">推理</a>
            </li>
            <li>
              <a href="/tag/绘本" class="tag">绘本</a>
            </li>
            <li class="last">
              <a href="/tag/青春" class="tag">青春</a>
            </li>
            <li>
              <a href="/tag/科幻" class="tag">科幻</a>
            </li>
            <li>
              <a href="/tag/言情" class="tag">言情</a>
            </li>
            <li>
              <a href="/tag/奇幻" class="tag">奇幻</a>
            </li>
            <li class="last">
              <a href="/tag/武侠" class="tag">武侠</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#流行" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>


        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              文化
            </ul>
            <li>
              <a href="/tag/历史" class="tag">历史</a>
            </li>
            <li>
              <a href="/tag/哲学" class="tag">哲学</a>
            </li>
            <li>
              <a href="/tag/传记" class="tag">传记</a>
            </li>
            <li class="last">
              <a href="/tag/设计" class="tag">设计</a>
            </li>
            <li>
              <a href="/tag/建筑" class="tag">建筑</a>
            </li>
            <li>
              <a href="/tag/电影" class="tag">电影</a>
            </li>
            <li>
              <a href="/tag/回忆录" class="tag">回忆录</a>
            </li>
            <li class="last">
              <a href="/tag/音乐" class="tag">音乐</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文化" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>




        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              生活
            </ul>
            <li>
              <a href="/tag/旅行" class="tag">旅行</a>
            </li>
            <li>
              <a href="/tag/励志" class="tag">励志</a>
            </li>
            <li>
              <a href="/tag/教育" class="tag">教育</a>
            </li>
            <li class="last">
              <a href="/tag/职场" class="tag">职场</a>
            </li>
            <li>
              <a href="/tag/美食" class="tag">美食</a>
            </li>
            <li>
              <a href="/tag/灵修" class="tag">灵修</a>
            </li>
            <li>
              <a href="/tag/健康" class="tag">健康</a>
            </li>
            <li class="last">
              <a href="/tag/家居" class="tag">家居</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#生活" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>




        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              经管
            </ul>
            <li>
              <a href="/tag/经济学" class="tag">经济学</a>
            </li>
            <li>
              <a href="/tag/管理" class="tag">管理</a>
            </li>
            <li>
              <a href="/tag/商业" class="tag">商业</a>
            </li>
            <li class="last">
              <a href="/tag/金融" class="tag">金融</a>
            </li>
            <li>
              <a href="/tag/营销" class="tag">营销</a>
            </li>
            <li>
              <a href="/tag/理财" class="tag">理财</a>
            </li>
            <li>
              <a href="/tag/股票" class="tag">股票</a>
            </li>
            <li class="last">
              <a href="/tag/企业史" class="tag">企业史</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#经管" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>




        <li>
          <ul class="clearfix">
            <ul class="tag_title">
              科技
            </ul>
            <li>
              <a href="/tag/科普" class="tag">科普</a>
            </li>
            <li>
              <a href="/tag/互联网" class="tag">互联网</a>
            </li>
            <li>
              <a href="/tag/编程" class="tag">编程</a>
            </li>
            <li class="last">
              <a href="/tag/交互设计" class="tag">交互设计</a>
            </li>
            <li>
              <a href="/tag/算法" class="tag">算法</a>
            </li>
            <li>
              <a href="/tag/通信" class="tag">通信</a>
            </li>
            <li>
              <a href="/tag/神经网络" class="tag">神经网络</a>
            </li>
            <li class="last">
              <a href="/tag/?view=type&amp;icn=index-sorttags-hot#科技" class="tag more_tag">更多»</a>
            </li>
          </ul>
        </li>

      </ul>
    </div>
  </div>
</template>

<script>
import SectionTitle from "../components/section-title";
import {fetchBookInfo, fetchBookList} from "../api";
export default {
  components: {SectionTitle},
  data () {
    return {
      tutorSugBooks: [],
      peerSugBooks: [],
      comments: []
    }
  },
  computed: {
  },
  methods: {
    fetchTSB(){
      fetchTSB().then(res=>{
        // console.log(id);
        this.tutorSugBooks = res.data || []
        // console.log(this.bookInfo);
      })
    },
    fetchPSB() {
      fetchPSB().then(res => {
        this.bookList = res.data || [];
        // console.log(this.bookList);
      })
    }
  },

}
</script>

<style scoped>
.wrapper {
  width: 80%;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 120px;
  display: flex;
}
.sec-title {
  font-weight: bolder;
  color: #0f0f0f;
  padding-right: 20px;
  font-size: 35px;
}
.link-more {
  padding-left: 20px;
  display: inline-block;
}
.link-to {
  width: 200px;
}
.book-bubble {
  margin-top: 20px;
}
.books li {
  float: left;
  margin-right: 30px;
}
.book-name {
  margin-top: 20px;
  font-size: 20px;
}
.sector {
  width: 950px;
}
.main {
  width: 950px;
}
.aside {
  /*margin-top: 50px;*/
  margin-left: 10px;
  flex-grow: 1;
}
.clearfix li {
  font-size: 20px;
  padding-right: 10px;
  display: inline;
  padding-top: 10px;
}
.tag {
  background-color: #eef1f3;
  color: #354b44;

}
.tag:hover {
  color: #e7051e;
}
.more_tag {
  color: #3b4151;
}
.tag_title {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 20px;
  padding-top: 20px;
  padding-bottom: 10px;
  color: #000000;
}
</style>
