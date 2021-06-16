<template>
  <div id="editor-wrap">
    <div class="chooseType">
      <el-radio-group v-model="type" fill="#6cd0b9">
        <el-radio-button label="笔记"></el-radio-button>
        <el-radio-button label="讨论"></el-radio-button>
      </el-radio-group>
    </div>
    <el-card class="titleTag">
    <el-input placeholder="请输入标题" v-model="title" clearable></el-input>
    <el-input placeholder="摘要" v-model="summary" clearable></el-input>
    <div id="edit-tag">
      <el-tag
          :key="tag"
          v-for="tag in dynamicTags"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)">
        {{tag}}
      </el-tag>
      <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
      >
      </el-input>
      <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
    </div>
    </el-card>
    <div id="editor" v-if="ready">
      <div v-if="type === '笔记'">
        <mavon-editor placeholder="请输入详细内容" style="height: 100%" v-model="content"></mavon-editor>
        <el-button type="success" @click="submit">
          确认提交
        </el-button>
      </div>
      <div v-else>
        <el-button type="success" @click="submitDiscuss">
          确认提交
        </el-button>
      </div>
    </div>
  </div>
</template>
<script>
// Local Registration
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

export default {
  name: 'editor',
  components: {
    mavonEditor
    // or 'mavon-editor': mavonEditor
  },
  data() {
    return {
      dynamicTags: [],
      inputVisible: false,
      summary: '',
      inputValue: '',
      title: '',
      ready: false,
      content: '',
      type: '笔记',
    }
  },
  methods: {
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    submit() {
      // let meditor=document.getElementById('mavon-editor');
      // console.log(meditor.innerText);
      let self = this
      if(self.content !== '' && self.title !== '' && self.summary !== '' && self.dynamicTags !== []){
        self.$axios({
          url: 'api/upload/UploadArticle/',
          method: 'post',
          data: {
            token: sessionStorage.getItem('Authorization'),
            title: self.title,
            summary: self.summary,
            content: self.content,
            tag: self.dynamicTags
          }
        }).then(res => {
          switch (res.data.status){
            case -1:
              self.$Notice.open({
                title: '请登录',
              });
              self.$router.push({
                path: '/login'
              });
              break;
            case -3:
              self.$Notice.open({
                title: '游客禁止发布文章',
              });
              break;
            case 1:
              self.$Notice.open({
                title: '发布成功',
              });
              self.$router.push({
                path: '/home'
              });
              break;
          }
        })
      }else if (self.content === ''){
        self.$Notice.open({
          title: '正文不能为空'
        })
      }else if (self.title === ''){
        self.$Notice.open({
          title: '标题不能为空'
        })
      }else if (self.summary === ''){
        self.$Notice.open({
          title: '摘要不能为空'
        })
      }else if (self.dynamicTags === []){
        self.$Notice.open({
          title: '标签不能为空'
        })
      }
    },
    saveTmp() {
      // 同样不会
      // mavonEditor.save()
    },
    submitDiscuss() {
      // let meditor=document.getElementById('mavon-editor');
      // console.log(meditor.innerText);
      let self = this
      if(self.title !== '' && self.summary !== '' && self.dynamicTags !== []){
        self.$axios({
          url: 'api/upload/UploadDiscuss/',
          method: 'post',
          data: {
            token: sessionStorage.getItem('Authorization'),
            title: self.title,
            summary: self.summary,
            tag: self.dynamicTags
          }
        }).then(res => {
          switch (res.data.status){
            case -1:
              self.$Notice.open({
                title: '请登录',
              });
              self.$router.push({
                path: '/login'
              });
              break;
            case -3:
              self.$Notice.open({
                title: '游客禁止发布文章',
              });
              break;
            case 1:
              self.$Notice.open({
                title: '发布成功',
              });
              self.$router.push({
                path: '/home'
              });
              break;
          }
        })
      }else if (self.title === ''){
        self.$Notice.open({
          title: '标题不能为空'
        })
      }else if (self.summary === ''){
        self.$Notice.open({
          title: '摘要不能为空'
        })
      }else if (self.dynamicTags === []){
        self.$Notice.open({
          title: '标签不能为空'
        })
      }
    },
    waitSomeTime() {
      setTimeout(() => {
        this.ready = true
      }, 1500)
    }
  },
  mounted() {
    this.waitSomeTime()
  },
}
</script>
<style lang="less" scoped>
#editor-wrap {
  /*margin-top: 100px;*/
  padding-top: 30px;
  margin-right: auto;
  margin-left: auto;
  width: 80%;
  height: 1200px;
  /*z-index:1 !important;*/
}
#editor {
  height: 50%;
}
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
.el-card{
  margin-bottom: 20px;
}
.v-note-wrapper {
  z-index: 0;
}
.chooseType {
  margin-bottom: 20px;
  color: #6cd0b9;
}
</style>
