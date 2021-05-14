<template>
  <div class="wrapper">
    <div class="content-prop">
      <fieldset>
        <legend>书籍属性</legend>
        <ul class="inline-fields">
        <li>
          <section-title>书名</section-title>
          <el-input v-model="title" placeholder="请填写书名"></el-input>
        </li>
        </ul>
        <ul class="inline-fields">
          <li>
            <section-title>作者</section-title>
            <el-input v-model="author" placeholder="请填写作者"></el-input></li>
        </ul>
        <ul class="inline-fields">
          <li>
            <section-title>语言</section-title><br>
            <el-radio v-model="language" label="中文"></el-radio>
          </li>
          <li><el-radio v-model="language" label="English"></el-radio></li>
        </ul>
        <ul class="inline-fields">
          <li>
            <section-title>ISBN</section-title>
            <el-input v-model="ISBN" placeholder="请填写ISBN号"></el-input>
          </li>
        </ul>
        <fieldset>
          <legend>分类</legend>
          <ul class="inline-fields">
            <li>
              <section-title>主题</section-title>
              <el-input v-model="topic" placeholder="请填写主题"></el-input>
            </li>
            <li>
              <section-title>标签</section-title>
              <el-input v-model="tags" placeholder="请填写标签（#分割）"></el-input>
            </li>
          </ul>
        </fieldset>
          <ul class="inline-fields">
            <li>
              <section-title>简要介绍</section-title>
              <el-input type="textarea" :autosize="{minRows: 2, maxRows: 5}" v-model="description" placeholder="请输入内容"></el-input></li>
          </ul>

      </fieldset>
    </div>
    <div class="file-prop">
      <fieldset>
        <legend>书籍上传</legend>
        <el-upload
            class="upload"
            action="uploadUrl"
            accept=".pdf,.epub,.mobi"
            ref="upload"
            :limit=1
            on-success="onSuccess"
            on-fail="onFail"
            :auto-upload="false"
            :file-list="fileList"
            :on-exceed="handleExceed">
          <el-button size="small" type="primary" style="margin: 10%">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">支持pdf, mobi, epub格式文件</div>
        </el-upload>
      </fieldset>
    </div>
    <div class="submit-holder">
      <el-button type="success" v-if="this.fileList.length===0|| this.ISBN === ''" disabled>提交</el-button>
      <el-button type="success" v-else @click="submit">提交</el-button>
    </div>
  </div>
</template>

<script>
import SectionTitle from "../components/section-title";
export default {
  name: "newBook",
  components: {SectionTitle},
  data() {
    return {
      title: '',
      author: '',
      language: '',
      year: '',
      ISBN: '',
      description: '',
      topic: '',
      tags: '',
      cover_img_url: '',
      fileList: []
    };
  },
  methods:{
    handleExceed(){
      alert('一篇书帖只能上传一本书')
    },
    submit(){
      this.uploadUrl = ''
      this.$refs.upload.submit()
    },
    onSuccess(){
      this.$Notice.open({
        title: '书帖上传成功！'
      })
    },
    onFail(){
      alert('上传失败')
    }
  }
}
</script>

<style scoped>
.wrapper {
  margin-top: 100px;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}
.inline-fields {
  margin: 5%;
}
.inline-fields li{
  display: inline-block;
  padding-right: 10%;
}
.content-prop fieldset {
  color: rgb(240, 240, 240);
}
.content-prop legend {
  color: rgb(0, 0 ,0);
  font-weight: bolder;
  font-size: 30px;
}

.file-prop fieldset {
  color: rgb(240, 240, 240);
}
.file-prop legend {
  color: rgb(0, 0 ,0);
  font-weight: bolder;
  font-size: 30px;
}
.el-upload__tip {
  padding-left: 10%;
  display: inline-block;
}
.submit-holder {
  margin-top: 5%;
  text-align: center;
}

</style>
