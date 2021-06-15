<template>
  <div class="login-register">
    <div class="contain">
      <div class="big-box" :class="{active:isLogin}">
        <div class="big-contain" v-if="isLogin">
          <div class="btitle">账户登录</div>
          <div class="bform">
            <input type="email" placeholder="邮箱" v-model="form.useremail">
            <span class="errTips" v-if="emailError">* 邮箱填写错误 *</span>
            <input type="password" placeholder="密码" v-model="form.userpwd">
            <span class="errTips" v-if="passwordError">* 密码填写错误 *</span>
          </div>
          <button class="bbutton" @click="login">登录</button>
        </div>
        <div class="big-contain" v-else>
          <div class="btitle">创建账户</div>
          <div class="bform">
            <input type="text" placeholder="用户名" v-model="form.username">
            <span class="errTips" v-if="existed">* 用户名已经存在！ *</span>
            <input type="text" placeholder="真实姓名" v-model="form.trueName">
            <input type="text" placeholder="学号" v-model="form.studentID">
            <span class="errTips" v-if="existed">* 姓名学号验证失败！ *</span>
            <input type="email" placeholder="邮箱" v-model="form.useremail">
            <span class="errTips" v-if="emailError">* 邮箱填写错误 *</span>
            <input type="password" placeholder="密码" v-model="form.userpwd">
          </div>
          <button class="bbutton" @click="register">注册</button>
        </div>
      </div>
      <div class="small-box" :class="{active:isLogin}">
        <div class="small-contain" v-if="isLogin">
          <div class="stitle">你好，世界!</div>
          <p class="scontent"></p>
          <button class="sbutton" @click="changeType">我还没号</button>
        </div>
        <div class="small-contain" v-else>
          <div class="stitle">新世界大门</div>
          <p class="scontent"></p>
          <button class="sbutton" @click="changeType">我有号了</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default{
  name: 'login-register',
  data () {
    return {
      isLogin: false,
      emailError: false,
      passwordError: false,
      existed: false,
      form: {
        username: '',
        trueName: '',
        studentID: '',
        useremail: '',
        userpwd: ''
      }
    }
  },
  created:function(){
    this.loggingState()
  },
  destroyed:function() {
    this.loggingState()
  },
  methods: {
    loggingState(){
      this.$store.commit('SET_LOGGING_STATE')
    },
    changeType () {
      this.isLogin = !this.isLogin
      this.form.username = ''
      this.form.trueName = ''
      this.form.stuentID = ''
      this.form.useremail = ''
      this.form.userpwd = ''
      this.emailError = false
      this.passwordError = false
      this.existed = false
      this.confirmError = false
    },
    login () {
      let self = this;
      if (self.form.useremail !== '' && self.form.userpwd !== '') {
        self.$axios({
          method: 'post',
          url: 'api/login_register/login/',
          data: {
            uid: self.form.useremail,
            pwd: self.form.userpwd
          }
        })
          .then(res => {
            switch (res.data.status) {
              case 1:
                this.$Notice.open({
                  title: '成功登录'
                })
                sessionStorage.setItem('Authorization', /* "Bearer " + */ res.data.token)
                this.$store.commit('SET_LOG_STATE', true)
                this.$store.commit('SET_SITE_INFO', res.data)
                sessionStorage.setItem('siteInfo', JSON.stringify(res.data))
                this.$router.push({
                   path:`/`}, onComplete => { }, onAbort => { })
                break
              case -1:
                this.$store.commit('SET_LOG_STATE', false)
                this.$Notice.open({
                  title: '邮箱或密码错误'
                })
                break
            }
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        this.$Notice.open({
          title: '填写不能为空！'
        })
      }
    },
    register () {
      let self = this;
      if (self.form.username !== '' && self.form.useremail !== '' && self.form.userpwd !== '') {
        self.$axios({
          method: 'post',
          url: '/api/login_register/register/',
          data: {
            uid: self.form.username,
            mail: self.form.useremail,
            pwd: self.form.userpwd,
            studentId: self.form.studentID,
            trueName: self.form.trueName
          }
        })
          .then(res => {
            switch (res.data.status) {
              case 1:
                this.$Notice.open({
                  title: '成功注册！'
                })
                this.existed = false
                this.emailError = false
                this.isLogin = true
                this.form.username = ''
                this.form.useremail = ''
                this.form.userpwd = ''
                self.form.studentID = ''
                self.form.trueName = ''
                this.$router.push({
                  path:`/login`}, () => { }, () => { })
                // this.login()
                break
              case -2:
                this.$Notice.open({
                  title: '用户名已存在'
                })
                this.existed = true
                this.emailError = false
                break
              case -1:
                this.$Notice.open({
                  title: '邮箱格式错误'
                })
                this.existed = false
                this.emailError = true
                break
              case -3: {
                this.$Notice.open({
                      title: '学号已注册，请联系管理员'
                    }
                )
                this.confirmError = true
                break
              }

            }
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        this.$Notice.open({
          title: '填写不能为空！'
        })
      }
    }
  }
}
</script>

<style scoped="scoped">
.login-register{
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
}
.contain{
  width: 60%;
  height: 60%;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 3px #f0f0f0,
  0 0 6px #f0f0f0;
}
.big-box{
  width: 70%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 30%;
  transform: translateX(0%);
  transition: all 1s;
}
.big-contain{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btitle{
  font-size: 2.0em;
  font-weight: bold;
  color: rgb(57,167,176);
}
.bform{
  width: 100%;
  height: 40%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.bform .errTips{
  display: block;
  width: 50%;
  text-align: left;
  color: red;
  font-size: 0.7em;
  margin-left: 1em;
}
.bform input{
  width: 50%;
  height: 15%;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}
.bbutton{
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: rgb(57,167,176);
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}
.small-box{
  width: 30%;
  height: 100%;
  background: linear-gradient(135deg,rgb(57,167,176),rgb(56,183,145));
  position: absolute;
  top: 0;
  left: 0;
  transform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}
.small-contain{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.stitle{
  font-size: 1.8em;
  font-weight: bold;
  color: #fff;
}
.scontent{
  font-size: 1.2em;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}
.sbutton{
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #ffffff;
  font-size: 1.2em;
  cursor: pointer;
}

.big-box.active{
  left: 0;
  transition: all 0.5s;
}
.small-box.active{
  left: 100%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transform: translateX(-100%);
  transition: all 1s;
}
</style>
