<template>
  <div class="contentListWrapper">
    <ul class="contentList">
      <li class="tip"
          v-for="(item,index) in contentList"
          :key="item.id"
          :class="'essayLi border-bottom '+item.id"
          @click="pushPage(item.id)"
      >
        <div class="liTop">
            <h3>{{item.question}}</h3>
          <span class="iconfont deleteIcon" @click="deleteEssayItem(index)">&#xe621;</span>
        </div>
        <div v-if="item.content !== ''" class="liMiddle">
          <p>{{item.content}}</p>
        </div>
        <div class="liBottom">
          <div class="liBottomLeft">
            <span class="forum">{{item.ownerName}}</span>
            <span v-if="item.tags !== []" class="category" v-for="it in item.tags">&nbsp;·&nbsp;{{it}}</span>
            <span class="date">·&nbsp;{{item.time}}</span>
          </div>
          <div class="liBottomRight">
            💬
            <span class="comment">{{item.reply}}</span>
          </div>
        </div>
        <div v-if="item.id == 1" class="setTopIcon">
          <span>置顶</span>
        </div>
      </li>
<!--      <li v-for="item of fixContentItem('adv')" :key="item.id" :class="'advLi '+item.id">-->
<!--        <img :src="item.avatar" class="advLiImg" />-->
<!--        <div class="advRight">-->
<!--          <h3 class="title">{{item.question}}</h3>-->
<!--          <p class="content">{{item.content}}</p>-->
<!--          <div class="advIcon">广告</div>-->
<!--        </div>-->
<!--      </li>-->
    </ul>
  </div>
</template>

<script>
import {fetchDiscussionQues} from "../../api";

export default {
  name: "forumList.vue",
  data () {
    return {
      contentList: []
    }
  },
  created() {
    this.fetchContentList();
  },
  methods: {
    pushPage(v){
      this.$router.push({
        name: 'discussion',
        query:{
          id:v
        }
      })
    },
    fetchContentList(){
      fetchDiscussionQues().then(res=>{
        this.contentList = res.data || []
      })
    },
    fixContentItem (param) {
      let res = []
      this.contentList.forEach(element => {
        if (element.type === param) {
          res.push(element)
        }
      })
      return res
    },
    deleteEssayItem (index) {
      this.contentList.splice(index, 1)
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/styles/mixins.styl'
.contentListWrapper
  width 100%
  height fit-content
  .contentList
    .essayLi
      padding 18px 24px
      background-color #fff
      box-shadow 0 3px 2px 0 rgba(0, 0, 0, 0.04)
      border 1px solid lightgrey
      position relative
      top 0
      left 0
      height 120px
      margin-bottom 10px
      &:hover
        background-color #fafafa
      .liTop
        display flex
        position relative
        left 0
        top 0
        margin-bottom 4px
        .title
          max-width 98%
          height 24px
          line-height 24px
          color #3d3d3d
          &:hover
            color #ca0c16
          &:acitve
            color #ca0c16
        .deleteIcon
          position absolute
          right 20px
          font-size 12px
          margin-left 16px
          color #ccc
          cursor pointer
      .liMiddle
        height 24px
        line-height 24px
        margin-bottom 4px
        color #8a8a8a
        font-size 14px
        p
          ellipsis()
      .liBottom
        display flex
        position relative
        left 0
        margin-bottom 0
        height 24px
        line-height 24px
        .liBottomLeft
          display flex
          height 24px
          .headImg
            width 20px
            height 20px
            margin-right 6px
          .forum
            display block
            height 24px
            line-height 24px
            margin-right 6px
            font-size 14px
            color #3d3d3d
            &:hover
              color #157dcf
          .category
            &:hover
              color #157dcf
          .category, .date
            margin-right 6px
            font-size 14px
            color #8a8a8a
        .liBottomRight
          position absolute
          right 20px
          line-height 24px
          font-size 14px
          color #999
          .read, .comment
            color #3399ea
            margin-right 5px
      .setTopIcon
        width 0
        height 0
        position absolute
        right 0
        top 0
        color #fdf5f5
        font-size 12px
        border-top 20px solid #7ed321
        border-right 20px solid #7ed321
        border-bottom 20px solid transparent
        border-left 20px solid transparent
        span
          transform rotate(45deg)
          margin-top -15px
          display block
          margin-left -12px
          width 30px
          position absolute
          height 30px
    .advLi
      padding 18px 24px
      background-color #fff
      box-shadow 0 1px 2px 0 rgba(0, 0, 0, 0.04)
      display flex
      &:hover
        background-color #fafafa
      .advLiImg
        width 120px
        height 90px
        margin-right 24px
      .advRight
        width 568px
        position relative
        top 0
        left 0
        .title
          color #3d3d3d
          max-width 98%
          height 24px
          line-height 24px
          margin-bottom 4px
        .content
          display block
          width 100%
          color #6b6b6b
          line-height 24px
          font-size 14px
        .advIcon
          width 40px
          height 18px
          line-height 18px
          position absolute
          right 0
          top 0
          border 1px solid #ccc
          border-radius 3px
          color #ccc
          font-size 12px
          font-weight lighter
          text-align center
          text-shadow 1px 1px 0px #000000
          verticalMiddle()
</style>

