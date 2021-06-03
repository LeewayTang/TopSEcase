<template>
  <div class="personal-center-wrap">
    <div class="header-wrap">
      <el-card class="header" :style="{backgroundImage: 'url('+ bg+ ')'}" style="width: 80%; background-size: cover">
        <img :src="websiteInfo.avatar" alt="头像" @click="picture.dialogVisible=true">
        <div class="username">{{websiteInfo.username}}</div>
        <div v-for="q in websiteInfo.quanzi" class="qz">
          <el-tag type="info">{{q.name}}</el-tag>
        </div>
      </el-card>
    </div>
    <div class="choose">
      <div class="button-wrap" v-for="(item,index) in category">
        <el-button type="text" @click="handleClick(index)">{{ item.name }}</el-button>
      </div>
    </div>
    <div class="body">
      <div class="body-left">
        <div class="content" v-for="(item, index) in category">
          <div v-show="index === showIndex" v-for="it in category[index].contents">
            <el-card>
              <post :post="it" :key="it.id"></post>
            </el-card>
          </div>
        </div>
      </div>
    </div>
    <!-- 弹出层-裁剪 -->
    <el-dialog title="编辑头像" :visible.sync="picture.dialogVisible" :before-close="handleClose">
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
  </div>
</template>

<script>

import {fetchList, fetchSiteInfo} from "../api";
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
          name: '我的笔记',
          contents: []
        },
        {
          name: '我的收藏',
          contents: []
        }
      ],
      showIndex: 0,
      bg: require('../assets/images/bg2.jpg')
    }
  },
  methods: {
    getPersonInfo() {
      if(this.$store.state.hasLogin){
        this.$store.dispatch('getSiteInfo').then(data =>{
          this.websiteInfo = data
        })
      }else{
        this.$store.dispatch('getSiteInfo0').then(data =>{
          this.websiteInfo = data
        })
      }
    },
    // 这里应该是从两个地方拿数据，但是类型相同，只是具体内容有差异。
    fetchList0() {
      fetchList().then(res => {
        this.category[0].contents = res.data.items || []
      }).catch(err => {
        console.log(err)
      })
    },
    fetchList1() {
      fetchList().then(res => {
        this.category[1].contents = res.data.items || []
      }).catch(err => {
        console.log(err)
      })
    },
    //控制弹出层关闭
    handleClose(v) {
      this.picture.dialogVisible = false;
    },
    handleClick(index) {
      // console.log(tab, event);
      this.showIndex = index
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
      this.$refs.cropper.getCropData(res => {
        console.log(res)//这里截图后的url 是base64格式 让后台转下就可以
        const self = this
        self.$axios({
          method: 'post',
          url: '/api/upload/uploadAvatar/',
          data: {
            token: sessionStorage.getItem('Authorization'),
            avatar: res
          }
        })
            .then(Res => {
              switch (Res.data.status) {
                case 1:
                  this.$Notice.open({
                    title: '上传成功'
                  })
                  this.$router.push({
                    path:`/personalCenter`}, onComplete => { }, onAbort => { })
                  break
                case -2:
                  this.$Notice.open({
                    title: '游客不能更改头像'
                  })
                  this.$router.push({
                    path:`/personalCenter`}, onComplete => { }, onAbort => { })
                  break
                case -1:
                  this.$Notice.open({
                    title: '未登录'
                  })
                  break
              }
            })
            .catch(err => {
              console.log(err)
            })
      })
    }
},
watch:{
  '$store.state.hasLogin'(){
    this.getWebSiteInfo()
  }
},
mounted() {
  this.getPersonInfo();
  this.fetchList0();
  this.fetchList1();
}
}
</script>

<style scoped>
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
  font-size: x-large;
  font-weight: bold;
  font-family: "Bitstream Vera Sans Mono", Monaco, "Courier New", Courier, monospace;
}
.header {
  width: 80%;
  height: 40%;
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
.el-button{
  font-size: xx-large;
  color: #1b1b1b;
  margin-left: 25%;
}
.button-wrap {
  display: inline-block;
  margin-left: 25%;
}
.el-card {
  margin-left: 10%;
  width: 80%;
  margin-top: 1%;
}
.body {
}

</style>
