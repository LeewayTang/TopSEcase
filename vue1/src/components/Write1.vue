<template>
  <div id="editor-wrap">
    <el-card class="titleTag">
    <el-input placeholder="请输入标题" v-model="title" clearable></el-input>
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
    <div id="editor">
      <mavon-editor style="height: 100%"></mavon-editor>
    </div>
    <el-button type="primary" @click="saveTmp">
      保存草稿
    </el-button>
    <el-button type="success" @click="submit">
      提交笔记
    </el-button>
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
      dynamicTags: ['标签一', '标签二', '标签三'],
      inputVisible: false,
      inputValue: '',
      // handbook: "#### how to use mavonEditor in nuxt.js"
      title: ''
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
      // 这咋把markdown编辑器里的内容传出去啊，俺也不会，俺也不敢问
    },
    saveTmp() {
      // 同样不会
      // mavonEditor.save()
    }
  }
}
</script>
<style>
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

</style>
