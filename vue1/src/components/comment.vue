<template>
    <div class="comment" :id="`comment`">
        <div class="comment-head">
            <div class="user-avatar"><img :src="comment.fromUserAvatar" alt=""></div>
            <div class="head-right">
                <section-title>
                    <div style="display: flex;align-items: center;justify-content: space-between;">
                        <div>
                            <span class="from-user user-name">{{comment.fromUserName}}</span>
                            <span class="to-user" v-if="comment.toUserId"><span style="margin: 0 5px;">@</span><span class="user-name">{{comment.toUserName}}</span></span>
                        </div>
                        <div style="font-size: 13px;">
                            <span style="color: #9c9c9c;margin-right: 20px;">{{comment.createTime | parseTime}}</span>
<!--                            <span @click.stop="showCommentEditor=true" style="cursor: pointer;">回复</span>-->
                        </div>
                    </div>
                </section-title>
            </div>
        </div>
        <div class="comment-body">
            <div class="content-text">
              <VueMarkdown :source="comment.content" v-highlight></VueMarkdown>
            </div>
            <div v-if="showCommentEditor" @click.stop="">
                <mavon-editor :toolbars="{
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
            <slot></slot>
        </div>
    </div>
</template>

<script>
    import sectionTitle from '@/components/section-title'
    import commentMessageEditor from 'comment-message-editor'
    import VueMarkdown from 'vue-markdown'

    export default {
        name: "comment",
        props: {
          comment: {
              type: Object,
          }
        },
      data(){
          return{
              showCommentEditor: false,

          }
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
        components: {
            sectionTitle,
            commentMessageEditor,
          VueMarkdown
        },
        methods: {
            reply(id){
                const ref = `comment${id}`
            },
            submitReply(v){
                console.log(v)
            },
            close(){
              this.showCommentEditor = false
            }
        },
    }
</script>

<style scoped lang="less">
    .comment{
      margin: 20px 0;
      box-sizing: border-box;
      border: 1px solid #EEF0F6;
      vertical-align: middle;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .comment-head{
        display: flex;
        .head-right{
            flex: 1;
        }
        .user-name{
            color: #8fd0cc;
        }
    }
    .comment-body{
        padding-left: 80px;
        .content-text{
            /*padding-bottom: 30px;*/
            margin-bottom: 30px;
            font-size: 14px;
            color: #9c9c9c;
            line-height: 1.3rem;
        }
    }

    .user-avatar{
        width: 50px;
        height: 50px;
        margin-right: 30px;
        img{
            width: 100%;
            height: 100%;
            border-radius: 100%;
        }
    }
    @media (max-width: 600px){
        .comment-body{
            padding-left: 15px;
            .content-text{
                margin-top: 10px;
            }
        }
        .user-avatar{
            margin-right: 10px;
        }
    }
    .v-note-wrapper {
      z-index: 0;
    }
</style>
