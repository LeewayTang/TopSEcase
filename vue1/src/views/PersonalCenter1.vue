<template>
<div class="personal-center-wrap">
  <div class="header-wrap">
  <el-card class="header" :style="{backgroundImage: 'url('+ bg+ ')'}" style="width: 80%; background-size: cover">
    <img :src="websiteInfo.avatar" alt="头像" style="cursor:pointer;" @click="picture.dialogVisible=true">
    <div style="display: flex">
      <div class="username">{{websiteInfo.username}}</div>
      <div class="el-icon-edit" style="color: white; cursor: pointer" @click="renameClick" v-if="$store.state.websiteInfo.username === $route.params.username"></div>
      <div style="width: 10%"></div>
      <div class="button-wrap" style="margin-left: 25%">
        <el-button class="button1" icon="el-icon-success" @click="titleClick">{{websiteInfo.title}}</el-button>
      </div>
    </div>
    <div style="display: flex">
      <div class="slogan">{{websiteInfo.slogan}}</div>
      <div class="el-icon-edit" style="color: white; cursor: pointer" @click="sloganClick" v-if="$store.state.websiteInfo.username === $route.params.username"></div>
    </div>
    <div>
      <div v-for="q in websiteInfo.quanzi" class="qz" v-show="removeQuanzi">
        <el-tag closable type="info" @close="handleTagClose(q)" :class="{deleting:removeQuanzi}">{{q.name}}</el-tag>
      </div>
      <div v-for="q in websiteInfo.quanzi" class="qz" v-show="!removeQuanzi" @click="q.dialogVisible = true">
        <el-tag type="info">{{q.name}}</el-tag>
      </div>
      <div class="button-wrap">
        <el-button :class="{deleting:removeQuanzi}" class="button1" v-if="websiteInfo.title === '导师' && $store.state.websiteInfo.username === websiteInfo.username"
                   size="mini" icon="el-icon-remove"
                   @click="removeQuanzi = !removeQuanzi">删除圈子</el-button>
        <el-button class="button1" v-if="websiteInfo.title === '导师' && $store.state.websiteInfo.username === websiteInfo.username"
                   size="mini" icon="el-icon-circle-plus"
                   @click="dialogFormVisible = true">创建圈子</el-button>
      </div>
    </div>
  </el-card>
  </div>
  <div class="choose">
    <div class="choose-button-wrap" v-for="(item,index) in category">
      <el-button type="text" v-if="$store.state.username === $route.params.username || item.name === '动态'" :class="{ active: item.isActive }" @click="handleClick(index)">{{ item.name }}</el-button>
    </div>
  </div>
  <div class="body">
    <div class="body-left">
      <div class="content" v-for="(item, index) in category">
        <div v-show="item.isActive" v-for="it in category[index].contents">
          <el-card>
            <post :post="it" :key="it.id"></post>
          </el-card>
        </div>
      </div>
    </div>
    <!-- 弹出层-裁剪 -->
    <el-dialog title="编辑头像" :visible.sync="picture.dialogVisible && $store.state.websiteInfo.username === $route.params.username" :before-close="handleClose">
      <span>
        <el-row>
          <input
              ref="filElem"
              type="file"
              id="uploads"
              accept="image/png, image/jpeg, image/gif, image/jpg"
              @change="uploadImg($event,1)"
              class="el-button hide"
              style="font-size: 15px; margin-bottom:15px; margin-left: 0px"
          />
          <div class="upload-img" @click="clickUpload">点击上传图片</div>
        </el-row>
        <el-row>
          <el-col :span="14">
            <!-- 裁剪 -->
            <vueCropper
                style="width:100%;height:300px"
                ref="cropper"
                :img="picture.attach.customaryUrl"
                :autoCrop="picture.options.autoCrop"
                :fixedBox="picture.options.fixedBox"
                :canMoveBox="picture.options.canMoveBox"
                :autoCropWidth="picture.options.autoCropWidth"
                :autoCropHeight="picture.options.autoCropHeight"
                :centerBox="picture.options.centerBox"
                @realTime="realTime"
            ></vueCropper>
          </el-col>
          <el-col :span="6.5">
            <h2 align="center" class=" mar-left-50">头像预览</h2>
            <div class="show-preview">
              <div :style="picture.previews.div" class="preview">
                <img :src="picture.previews.url" :style="picture.previews.img" width="100%" />
              </div>
            </div>
          </el-col>
        </el-row>
        <el-row class="footerBtn" align="center">
          <el-button type="primary " size="medium" round @click="confirm('blob')">确认</el-button>
          <el-button type="info" size="medium" round @click="handleClose">取消</el-button>
        </el-row>
      </span>
    </el-dialog>

  <!--  弹出层——圈子信息-->
  <div v-for="item in websiteInfo.quanzi">
    <el-dialog
        title="圈子信息"
        :visible.sync="item.dialogVisible"
        width="30%"
        >
      <div class="qz-name">{{item.name}}</div>
      <div class="tutorInfo">
        <div class="title">创建者信息</div>
        <div class="infoInstance">
          <img :src="item.tutorInfo.avatar" alt="导师头像">
          <div class="tutorNameID">{{item.tutorInfo.trueName}} | {{item.tutorInfo.iid}}</div>
        </div>
      </div>
      <div class="studentInfo">
        <div class="title">成员信息</div>
        <div class="infoInstance" v-for="it in item.studentsInfo">
          <div style="cursor:pointer;" @click="goToPC(it, item)">
            <img :src="it.avatar" alt="学生头像">
            <div class="studentNameID">{{it.trueName}} | {{it.iid}}</div>
          </div>
        </div>
      </div>
<!--      <span>还应该包括导师信息，圈内同学等信息</span>-->
      <span slot="footer" class="dialog-footer">
<!--    <el-button @click="item.dialogVisible = false">取 消</el-button>-->
    <el-button type="success" @click="item.dialogVisible = false" size="mini">确 定</el-button>
  </span>
    </el-dialog>
  </div>


<!--  弹出层——创建圈子-->
  <el-dialog title="新建圈子" :visible.sync="dialogFormVisible">
    <el-form :model="quanzi">
      <el-form-item label="圈子名称" :label-width="formLabelWidth">
        <el-input v-model="quanzi.name" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="圈子描述" :label-width="formLabelWidth">
        <el-input v-model="quanzi.description" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="添加学生" :label-width="formLabelWidth">
        <el-tag
            :key="tag"
            v-for="tag in quanzi.dynamicTags"
            closable
            :disable-transitions="false"
            @close="handleStudent(tag)">
          {{tag}}
        </el-tag>
        <el-input
            class="input-new-tag"
            v-if="quanzi.inputVisible"
            v-model="quanzi.inputValue"
            ref="saveTagInput"
            size="small"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ 学生</el-button>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false" size="mini">取 消</el-button>
      <el-button type="primary" size="mini" @click="commitNewQuanzi(quanzi.name)">确 定</el-button>
    </div>
  </el-dialog>
  </div>
</div>
</template>

<script>

import {fetchList} from "../api";
import post from '../components/post'
export default {
  name: "PersonalCenter1",
  components: {
    post
  },
  data()  {
    return{
      websiteInfo: {},
      picture:{
        dialogVisible: false,
        options: {
          autoCrop: true, //默认生成截图框
          fixedBox: true, //固定截图框大小
          canMoveBox: false, //截图框不能拖动
          centerBox: false, //截图框被限制在图片里面
          autoCropWidth:200,  //截图框宽度
          autoCropHeight:200, //截图框高度
        },
        previews: {}, //实时预览图数据
        attach: {
          //后端附件表
          id: "",
          userId: "",
          customaryUrl: "", //原图片路径
          laterUrl: "", //裁剪后图片路径  /static/logo.png
          attachType: "photo" //附件类型
        }
      },
      category: [
        {
          name: '动态',
          contents: [],
          isActive: true
        },
        {
          name: '我的收藏',
          contents: [],
          isActive: false
        }
      ],
      showIndex: 0,
      bg: require('../assets/images/bg2.jpg'),
      dialogFormVisible: false,
      quanzi: {
        dynamicTags: [],
        inputVisible: false,
        inputValue: '',
        name: '',
        description: '',
        dialogVisible: false
      },
      formLabelWidth: '120px',
      removeQuanzi: false,
      currentPage: 1,
      hasNextPage: false,
      studentList: [],
    }
  },
  methods: {
    getPersonInfo() {
      if(this.$store.state.hasLogin  && this.$store.state.websiteInfo.username === this.$route.params.username){
        let self = this
        self.$axios({
          method: 'post',
          url: 'api/user/getUserInfo/',
          data: {
            token: sessionStorage.getItem('Authorization')
          }
        }).then(res => {
          self.websiteInfo = res.data.data
        })
      }
      else if (!this.$store.state.hasLogin){
        this.$store.dispatch('getSiteInfo0').then(data =>{
          this.websiteInfo = data
        })
      }
      else {
        let self = this
        self.$axios({
          method: 'post',
          url: 'api/user/getUserInfoByName/',
          data: {
            username: self.$route.params.username
          }
        }).then(res => {
          switch (res.data.status) {
            case -1:
              self.$Notice.open({
                title: '用户不存在'
              })
              self.$router.push({
                path:`/`}, onComplete => { }, onAbort => { })
              break
            case 1:
              self.websiteInfo = res.data.data
              break
          }
        })
      }
    },
    getStudentList() {
      this.$axios(
          {
        url: '/studentList',
        }
      ).then(res => {
        this.studentList = res.data.data
        console.log(this.studentList)
      })
    },
    handleStudent(tag){
      this.quanzi.dynamicTags.splice(this.quanzi.dynamicTags.indexOf(tag), 1);
    },
    handleTagClose(tag) {
      console.log(tag)

      let self = this;
      self.$axios({
        url: '/api/quanzi/delQuanzi/',
        method: 'post',
        data: {
          name: tag.name,
          token: sessionStorage.getItem('Authorization'),
        }
      }).then(res => {
        switch (res.data.status){
          case -1:
            self.$Notice.open({
              title: '非创建者禁止删除圈子'
            });
            break;
          case 1:
            this.websiteInfo.quanzi.splice(this.websiteInfo.quanzi.indexOf(tag), 1);
            self.$Notice.open({
              title: '删除成功'
            });
            self.$axios({
              method: 'post',
              url: 'api/user/getUserInfo/',
              data: {
                token: sessionStorage.getItem('Authorization')
              }
            }).then(res => {
              self.$store.commit('SET_SITE_INFO', res.data.data)
              sessionStorage.setItem('siteInfo', JSON.stringify(res.data.data))
            })
            break;
        }
      }).catch(err => {
        console.log(err)
      })
    },

    showInput() {
      this.quanzi.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.quanzi.inputValue;
      if (inputValue) {
        this.quanzi.dynamicTags.push(inputValue);
      }
      this.quanzi.inputVisible = false;
      this.quanzi.inputValue = '';
    },
    // 这里应该是从两个地方拿数据，但是类型相同，只是具体内容有差异。
    fetchList0() {
      let self = this;
      self.$axios({
        url: 'api/articleTag/getUsernameArticle/',
        method: 'post',
        data: {
          username: self.$route.params.username
        }
      }).then(res => {
        self.category[0].contents = res.data.data || [];
      }).catch(err => {
        console.log(err)
      })
    },
    fetchList1() {
      let self = this;
      self.$axios({
        url: 'api/articleTag/getUsernameArticle/',
        method: 'post',
        data: {
          username: self.$route.params.username
        }
      }).then(res => {
        self.category[1].contents = res.data.data || [];
      }).catch(err => {
        console.log(err)
      })
    },
    //控制弹出层关闭
    handleClose(v) {
      this.picture.dialogVisible = false;
    },
    // 控制展示圈子信息的弹出层关闭
    handleQZInfoClose(qz) {
      qz.dialogVisible = false;
    },

    handleClick(index) {
      let anotherIndex = index?0:1
      this.category[anotherIndex].isActive = false
      this.category[index].isActive = true
      // console.log(this.category)
    },
    titleClick() {
      if (this.websiteInfo.title === '学生') {
        this.$message('学生认证，有加入和退出圈子的权限\n' +
            '导师认证请联系管理员')
      }
      else if (this.websiteInfo.title === '导师') {
        this.$message('导师认证，有创建和删除圈子的权限')
      }
    },
    renameClick() {
      console.log("rename!!!")
      let self = this
      self.$prompt('请输入您想更改的昵称', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(({value}) => {
        if(value === '' || value === null){
          self.$message({
            type: 'error',
            message: '输入不能为空'
          })
        }else {
          self.$axios({
            url: 'api/user/setUserName/',
            method: 'post',
            data: {
              token: sessionStorage.getItem('Authorization'),
              username: value
            }
          })
              .then(res => {
                switch (res.data.status) {
                  case 1:
                    self.$store.commit('SET_SITE_INFO', res.data.data)
                    sessionStorage.setItem('siteInfo', JSON.stringify(res.data.data))
                    self.$message({
                      type: 'success',
                      message: '你的昵称已更改为' + value
                    });
                    self.websiteInfo = self.$store.state.websiteInfo
                    self.$router.push({
                      path: '/personalCenter/' + self.websiteInfo.username
                    })
                    break
                  case -1:
                    self.$message({
                      type: 'error',
                      message: '请登录'
                    });
                    self.$router.push(
                        {path: `/login`}, onComplete => {
                        }, onAbort => {
                        })
                    break
                  case -2:
                    self.$message({
                      type: 'error',
                      message: '用户名已存在'
                    });
                    break
                  case -3:
                    self.$message({
                      type: 'error',
                      message: '游客账号禁止修改姓名'
                    });
                    break
                }

              })
              .catch(err => {
                console.log(err)
              })
        }
      }).catch(() => {
        self.$message({
          type: 'info',
          message: '取消输入'
        });
      });
    },
    created(){
      this.getPersonInfo();
      this.fetchList0();
      this.fetchList1();
    },
    sloganClick() {
      console.log("slogan!!!")
      let self = this
      self.$prompt('请输入您想更改的个性签名', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(({value}) => {
        if(value === '' || value === null){
          self.$message({
            type: 'error',
            message: '输入不能为空'
          })
        }else {
          self.$axios({
            url: 'api/user/setUserSlogan/',
            method: 'post',
            data: {
              token: sessionStorage.getItem('Authorization'),
              slogan: value
            }
          })
              .then(res => {
                switch (res.data.status) {
                  case 1:
                    self.$store.commit('SET_SITE_INFO', res.data.data)
                    sessionStorage.setItem('siteInfo', JSON.stringify(res.data.data))
                    self.$message({
                      type: 'success',
                      message: '你的签名已更改为' + value
                    });
                    self.websiteInfo = self.$store.state.websiteInfo
                    self.$router.push({
                      path: '/personalCenter/' + self.websiteInfo.username
                    })
                    break
                  case -1:
                    self.$message({
                      type: 'error',
                      message: '请登录'
                    });
                    self.$router.push(
                        {path: `/login`}, onComplete => {
                        }, onAbort => {
                        })
                    break
                  case -3:
                    self.$message({
                      type: 'error',
                      message: '游客账号禁止修改签名'
                    });
                    break
                }
              })
              .catch(err => {
                console.log(err)
              })
        }
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });
    },
    //实时预览
    realTime(data) {
      this.picture.previews = data;
    },
    //点击图片调取input
    clickUpload(){
      this.$refs.filElem.dispatchEvent(new MouseEvent('click'))
    },
    //选择本地图片
    uploadImg(e, num) {
      const file = e.target.files[0];
      if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
        this.$message.error("图片类型必须是.gif,jpeg,jpg,png,bmp中的一种");
        return false;
      }
      //fileReader 接口，用于异步读取文件数据
      const reader = new FileReader();
      reader.readAsDataURL(file); //重要 以dataURL形式读取文件
      reader.onload = e => {
        // data = window.URL.createObjectURL(new Blob([e.target.result])) 转化为blob格式
        let data = e.target.result;
        this.picture.attach.customaryUrl = data;
        // 转化为base64
        // reader.readAsDataURL(file)
        // 转化为blob
      };
    },
    //确认截图,上传
    confirm(type) {
      let self = this
      self.$refs.cropper.getCropData(res => {
        if(res === '' || res === null){
          self.$message({
            type: 'error',
            message: '输入不能为空'
          })
        }else {
          self.$axios({
            url: 'api/user/setUserAvatar/',
            method: 'post',
            data: {
              token: sessionStorage.getItem('Authorization'),
              avatarBase64: res
            }
          })
              .then(res => {
                switch (res.data.status) {
                  case 1:
                    self.$store.commit('SET_SITE_INFO', res.data.data)
                    sessionStorage.setItem('siteInfo', JSON.stringify(res.data.data))
                    self.$message({
                      type: 'success',
                      message: '你的头像已更改'
                    });
                    self.websiteInfo = self.$store.state.websiteInfo;
                    this.picture.dialogVisible = false
                    window.location.reload()
                    break
                  case -1:
                    self.$message({
                      type: 'error',
                      message: '请登录'
                    });
                    self.picture.dialogVisible = false
                    self.$router.push(
                        {path: `/login`}, onComplete => {
                        }, onAbort => {
                        })
                    break
                  case -3:
                    self.$message({
                      type: 'error',
                      message: '游客账号禁止修改头像'
                    });
                    break
                }
              })
              .catch(err => {
                console.log(err)
              })
          console.log(res)//这里截图后的url 是base64格式 让后台转下就可以
        }
      });
    },
    commitNewQuanzi(v) {
      // 没有传到服务器！！！！
      let self = this;
      self.$axios({
        url: '/api/quanzi/setQuanzi/',
        method: 'post',
        data: {
          name: self.quanzi.name,
          token: sessionStorage.getItem('Authorization'),
          member: self.quanzi.dynamicTags,
        }
      }).then(res => {
        switch (res.data.status){
          case -1:
            self.$Notice.open({
              title: '学生信息不存在'
            });
            break;
          case -2:
            self.$Notice.open({
              title: '圈子名称重复'
            });
            break;
          case 1:
            self.$Notice.open({
              title: '创建成功'
            });
            this.dialogFormVisible = false;
            self.$axios({
              method: 'post',
              url: 'api/user/getUserInfo/',
              data: {
                token: sessionStorage.getItem('Authorization')
              }
            }).then(res => {
              self.$store.commit('SET_SITE_INFO', res.data.data)
              sessionStorage.setItem('siteInfo', JSON.stringify(res.data.data))
            })
            window.location.reload()
            break;
        }
      }).catch(err => {
        console.log(err)
      })
    },
    commitDeleteQuanzi() {
      // 具体的数据传输没搞明白呢，不着急
      console.log(this.websiteInfo.quanzi)
    },
    goToPC(v1, v2) {
      v2.dialogVisible = false
      this.$router.push('/personalCenter/' + v1.username)
    }
  },
  watch:{
    '$store.state.hasLogin'(){
      this.getWebSiteInfo()
    },
    '$route.params'() {
      this.getPersonInfo();
      this.fetchList0();
      this.fetchList1();
    },
    'slogan'() {
      this.getPersonInfo();
    }
  },
  computed: {
    slogan(){
      return this.websiteInfo.slogan;
    }
  },
  mounted() {
    this.getPersonInfo();
    this.getStudentList();
    this.fetchList0();
    this.fetchList1();
    // console.log(this.$route.params);
  }
}
</script>

<style lang="less" scoped>
.personal-center-wrap{
  padding-top: 20px;
}
img {
  margin-left: 5%;
  margin-top: 5%;
  border-radius: 50%;
  width: 15vmin;
  height: 15vmin;
  object-fit: cover;
  object-position: center;
}
.qz {
  display: inline-block;
  margin-left: 5%;
  margin-top: 2%;
}
.el-tag {
  display: inline-block;
}
.el-dialog{
  width: 700px !important;
  height: auto;

  .el-button {
    font-size: x-large;
    color: #e4eef5;
  }

  img {
    margin-left: 5%;
    margin-top: 5%;
    border-radius: 50%;
    width: 5vmin;
    height: 5vmin;
    object-fit: cover;
    object-position: center;
  }
  .infoInstance {
    display: inline-block;
    margin-right: 10px;
    text-align: center;
  }

  .qz-name {
    font-size: xxx-large;
    text-align: center;
    color: #6cd0b9;
  }
  .title {
    font-size: x-large;
    margin-top: 10px;
  }
}
.show-preview {
  display: flex;
  justify-content: center;
}
.preview {
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #cccccc;
  background: #cccccc;
  width: 150px !important;
  height: 150px !important;
  margin-left: 50px;
  margin-top: 50px;
}
.upload-img{
  width: 100px;
  height: 30px;
  border:1px solid #f08512;
  margin-bottom: 5px;
  line-height: 30px;
  text-align: center;
  cursor: pointer;
}
.footerBtn {
  display: flex;
  justify-content: center;
  margin-top: 15px;
}
.username {
  padding-left: 5%;
  padding-top: 2%;
  color: #FFFFFF;
  font-size: xxx-large;
  font-weight: bold;
  font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
}
.slogan {
  padding-left: 5%;
  padding-top: 2%;
  color: #FFFFFF;
  font-size: xx-large;
  font-weight: bold;
  font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
}
.header {
  width: 80%;
  height: 50%;
  margin-left: 10%;
  background-size: cover
}
.choose {
  margin-top: 1%;
  width: 80%;
  margin-left: 10%;
  background-color: #FFFFFF;
  color: #1b1b1b;
}
.el-button {
  font-size: xx-large;
  color: #b9bec1;
}
.choose-button-wrap {
  display: inline-block;
  padding-left: 25%;
}
.button-wrap {
  position: absolute;
  right: 12%;
  /*float: right;*/
  display: inline-block;
}
.el-card {
  margin-left: 10%;
  width: 80%;
  margin-top: 1%;
}
.active {
  color: black;
}
.button1{
  /*float: right;*/
  color: #56c4b7;
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
.deleting {
  color: red;
  animation: shake 0.82s cubic-bezier(.36, .07, .19, .97) both infinite;
}

@keyframes shake {
  10%, 90% {transform: translate3d(-1px, 0, 0);}

  20%, 80% {transform: translate3d(2px, 0, 0);}

  30%, 50%, 70% {transform: translate3d(-4px, 0, 0);}

  40%, 60% {transform: translate3d(4px, 0, 0);}
}
.el-tag {
  cursor: pointer;
}
</style>
