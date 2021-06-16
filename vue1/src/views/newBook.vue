<template>
  <div class="wrapper">
    <div class="content-prop">
      <el-card>
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
          <li><el-radio v-model="language" label="其他"></el-radio></li>
        </ul>
        <ul class="inline-fields">
          <li>
            <section-title>ISBN</section-title>
            <el-input v-model="ISBN" placeholder="请填写ISBN号"></el-input>
          </li>
          <li>
            <section-title>出版社</section-title>
            <el-input v-model="press" placeholder="请填写出版社"></el-input>
          </li>
        </ul>

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

          <ul class="inline-fields">
            <li>
              <section-title>书籍简介</section-title>
              <el-input type="textarea" :autosize="{minRows: 2, maxRows: 5}" v-model="description" placeholder="请输入内容"></el-input></li>
            <li>
              <section-title>书评</section-title>
            <el-input type="textarea" :autosize="{minRows: 2, maxRows: 5}" v-model="review" placeholder="请输入内容"></el-input></li>
          </ul>

        <div class="file-prop">
          <el-card>
            <legend>书籍上传</legend>
            <el-upload
                class="upload"
                action="/api/upload/uploadBook/"
                accept=".pdf,.epub,.mobi"
                ref="upload"
                :limit=1
                :on-success="handleSuccess"
                :on-fail="onFail"
                :on-change="printFuckingFileList"
                :on-remove="onRemove"
                :data="paramsData"
                :auto-upload="false"
                :file-list="fileList"
                :on-exceed="handleExceed"
                prop="fileList">
              <el-button size="small" type="primary" style="margin: 10%">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">支持pdf, mobi, epub格式文件</div>
            </el-upload>
          </el-card>
        </div>
      </el-card>
    </div>

<!--    <div class="file-prop">-->
<!--      <fieldset>-->
<!--        <legend>封面上传</legend>-->
<!--        <el-upload-->
<!--            class="upload"-->
<!--            action="/api/upload/uploadBook/"-->
<!--            accept=".jpg, .jpeg, .png"-->
<!--            ref="upload"-->
<!--            :on-success="handleSuccess"-->
<!--            :on-fail="onFail"-->
<!--            :on-change="printFuckingFileList"-->
<!--            :on-remove="onRemove"-->
<!--            :data="paramsData"-->
<!--            :auto-upload="false"-->
<!--            :file-list="fileList"-->
<!--            :on-exceed="handleExceed"-->
<!--            prop="fileList">-->
<!--          <el-button size="small" type="primary" style="margin: 10%">点击上传</el-button>-->
<!--          <div slot="tip" class="el-upload__tip">支持jpg, jpeg, png格式文件</div>-->
<!--        </el-upload>-->
<!--      </fieldset>-->
<!--    </div>-->
    <div class="submit-holder">
      <el-button type="success" v-if="!hasFile || ISBN === '' || title === '' || author === '' || language === ''
        || tags === ''" disabled>提交</el-button>
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
      fileList: [],
      hasFile: false,
      hasImage: false,
      paramsData: {},
      press: '',
      review: ''
    };
  },
  methods:{
    handleExceed(){
      alert('一篇书帖只能上传一本书')
    },
    handleSuccess(res){
      let self = this;
      switch (res.status){
        case -3:
          self.$Notice.open({
            title: '游客禁止发布新书'
          });
          self.$router.push({
            path: '/home'
          });
          break;
        case -1:
          self.$Notice.open({
            title: '请登录'
          });
          self.$router.push({
            path: '/login'
          });
          break;
        case 1:
          self.$Notice.open({
            title: '发布成功'
          });
          self.$router.push({
            path: '/book-ground'
          });
          break;
      }
    },
    submit(){
      let self = this
      self.$Notice.open({title: '正在传输，请等待'})
      self.paramsData.token = sessionStorage.getItem('Authorization')
      self.paramsData.title = self.title;
      self.paramsData.author = self.author;
      self.paramsData.language = self.language;
      self.paramsData.year = self.year;
      self.paramsData.ISBN = self.ISBN;
      self.paramsData.description = self.description;
      self.paramsData.topic = self.topic;
      self.paramsData.tags = self.tags;
      self.paramsData.press = self.press;
      self.paramsData.review = self.review;
      console.log(self.paramsData)
      this.$refs.upload.submit();
      console.log(this.$refs.upload)
      console.log(this.$refs.upload.uploadFiles)
      this.hasFile = false
      this.hasImage = false
    },
    onSuccess(res, file, fileList){
      this.$Notice.open({
        title: '书帖上传成功！'
      })
      this.hasFile = false
    },
    onRemove() {
      this.hasFile = false
    },
    onFail(){
      alert('上传失败')
      this.hasFile = false
    },
    // el-loader不是把选择了的文件和fileList动态绑定的，是文件传到后台之后通过回调绑定的
    // 所以如果只选择但是没有传，那么fileList永远为空
    // 传上去的书的数据被放在一个this.$refs.upload._data.uploadFiles
    // 的地方，但是其实很难取到，只能在el-loader的接口里调出来
    printFuckingFileList() {
      this.hasFile = true
      // let type = this.$refs.upload.uploadFiles[0].raw.type

      // if (type === 'image/jpeg') {
      //     this.hasImage = true
      // }
      // else if (type === 'pdf') {
      //   this.hasFile = true
      // }
      // console.log(type)
      console.log(this.$refs.upload.uploadFiles)
    },
  },
}
</script>

<style scoped>
.wrapper {
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
