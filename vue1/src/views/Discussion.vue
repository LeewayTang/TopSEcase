<template>
  <div class="discussion-wrapper">
    <div class="default">
      这里是讨论区，尽情进行思想的碰撞吧！
    </div>
    <div class="header">
      <div class="owner">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <img :src="Avatar" alt="头像">
            <span class="user-name">{{ ownerName }}</span>
            <span>{{time}}</span>
          </div>
          <div>
            {{content}}
            <span> <el-button type="primary">回复</el-button></span>
          </div>

        </el-card>
      </div>
      <div class="tags">
        <el-tag>标签一</el-tag>
        <el-tag type="success">标签二</el-tag>
        <el-tag type="info">标签三</el-tag>
        <el-tag type="warning">标签四</el-tag>
        <el-tag type="danger">标签五</el-tag>
        </div>
    </div>
    <div class="site-content animate">
      <main class="site-main">
        <div class="comments">
          <comment v-for="item in comments" :key="item.comment.id" :comment="item.comment">
            <template v-if="item.reply.length">
              <comment v-for="reply in item.reply" :key="reply.id" :comment="reply"></comment>
            </template>
          </comment>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import comment from '../components/comment'
import {fetchComment} from "../api";
export default {
  name: "Discussion",
  data(){
    return{
      showDonate: false,
      value: '',
      comments: [],
      menus: [],
      question: '',
      ownerName: '吕云翔',
      Avatar: '../assets/images/rzdf.jpg',
      time: new Date(),
      content: '你期末想及格吗？'
    }
  },

  components: {
    comment,
  },
  methods: {
    getComment(){
      fetchComment().then(res => {
        this.comments = res.data || []
      }).catch(err => {
        console.log(err)
      })
    },
    fetchH(arr,left,right){
      if (right) {
        return arr.filter(item => item.offsetTop > left && item.offsetTop < right)
      }else {
        return arr.filter(item => item.offsetTop > left)
      }
    },
    // 生成目录
    createMenus(){
      let arr = []
      for(let i=6;i>0;i--){
        let temp = []
        let e = document.querySelector(".entry-content").querySelectorAll(`h${i}`)
        for (let j=0;j<e.length;j++){
          let child = this.fetchH(arr,e[j].offsetTop,(j+1 === e.length)?undefined:e[j+1].offsetTop)
          temp.push({
            h: i,
            title: e[j].innerText,
            id: e[j].id,
            offsetTop: e[j].offsetTop,
            child
          })
        }
        if (temp.length){
          arr = temp
        }
      }
      this.menus = arr
    }
  },
  mounted(){
    this.createMenus()
  },
  created() {
    this.getComment()
  }
}
</script>

<style scoped lang="less">
  .site-content {
    position: relative;
    .site-main {
      padding: 80px 0 0 0;
    }
  }
  .header {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
  .default {
    width: 80%;
    color: black;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    font-size: 200%;
    font-weight: bolder;
    margin: 120px auto 20px;
  }
  .clearfix span {
    margin-left: 10px;
  }
</style>
