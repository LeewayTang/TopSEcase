<template>
  <div class="discussion-wrapper">
    <div class="default">
      {{ question }}
    </div>
    <div class="header">
      <div class="owner">
        <el-card class="box-card" type="flex">
          <div class="user"><img class="askAvatar" :src="Avatar" alt="头像"></div>
          <div class="user">{{ownerName}}</div>
          <el-button class="answerButton" type="primary">回复</el-button>
        </el-card>
      </div>
      <div class="tags" v-for="tag in tags">
        <el-tag type="succuess">{{tag}}</el-tag>
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
import {fetchComment,fetchDiscussionQues} from "../api";

export default {
  name: "Discussion",
  data(){
    return{
      showDonate: false,
      value: '',
      comments: [],
      menus: [],
      question: '',
      ownerName: '',
      Avatar: '',
      time: new Date(),
      tags: []
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
  getDiscussionQues() {
      fetchDiscussionQues().then(res => {
        this.tags = res.data.tags || []
        this.Avatar = res.data.Avatar
        this.question = res.data.question
        this.time = res.data.time
        this.ownerName = res.data.ownerName
        // console.log(res.data.tags)
        // console.log(res.data.Avatar);
        // console.log(res.data.question);
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
    // this.createMenus()
    this.getDiscussionQues()
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
      padding: 0 0 0 0;
    }
  }
  .answerButton{
    display: inline-block;
    vertical-align: middle;
    margin-right: 10%;
  }
  .user{
    display: inline-block;
    vertical-align: middle;
    margin-right: 30px;
  }
  .askAvatar{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 3px solid rgba(255,255,255,0.4);
    display: inline-block;
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
    margin: 0px auto 20px;
  }
  .clearfix{
    display: inline-block;
  }
  .clearfix span {
    margin-left: 10px;
  }
  .tags {
    display: inline-block;
  }
</style>
