<template>
    <div id="layout-header" :class="{'fixed':fixed,'hidden':hidden}" @click.stop="mobileShow=false">
        <div class="site-logo">
            <router-link to="/">
<!--                <img src="@/assets/site-logo.svg" alt="">-->
              <img src="@/assets/reading.png" alt="">
                <p class="site-name">墨韵 | MoYun</p>
            </router-link>
        </div>
        <div class="menus-btn" @click.stop="mobileShow=!mobileShow">
            Menus
        </div>
        <div v-if="$store.state.isLogging" class="site-menus" :class="{'mobileShow':mobileShow}" @click.stop="mobileShow=!mobileShow">
            <div class="menu-item header-search"><header-search/></div>
            <div class="menu-item"><router-link to="/notLogin">全站笔记</router-link></div>
            <div class="menu-item"><router-link to="/book-ground">全站藏书</router-link></div>
          <div class="menu-item"><router-link to="/personalCenter">我的圈子</router-link></div>
<!--               <div class="menu-item hasChild"><router-link to="/writeBlog">创作中心</router-link></div>-->
            <div class="menu-item hasChild">
                <a>创作中心</a>
                <div class="childMenu" v-if="category.length">
                    <div class="sub-menu" v-for="item in category" :key="item.title"><router-link :to="`${item.href}`">
                      {{item.title}}</router-link></div>
                </div>
            </div>
          <div class="menu-item" v-if="!$store.state.hasLogin"><router-link to="/login">登录/注册</router-link></div>
          <div class="menu-item hasChild" v-else>
                <img class="menu-img" :src="$store.state.websiteInfo.avatar" >
                <div class="childMenu" v-if="category.length">
                    <div class="sub-menu" v-for="item in profile" :key="item.title">
                    <router-link :to="`${item.href}`" @click.native="quit(item.title)"> {{item.title}}</router-link>
                    </div>
                </div>
            </div>
        </div>
      <button class="bbutton" @click="travelerLogin" v-else>以游客身份登录</button>
    </div>
</template>

<script>
    import HeaderSearch from '@/components/header-search'
    import {fetchCategory, fetchProfile} from '../../api'
    export default {
        name: "layout-header",
        components: {HeaderSearch},
        data() {
            return {
                lastScrollTop: 0,
                fixed: false,
                hidden: false,
                category: [],
                profile:[],
                mobileShow: false
            }
        },
        mounted(){
            window.addEventListener('scroll', this.watchScroll)
            this.fetchCategory()
          this.fetchProfile()
            this.checkLogin()
        },
        beforeDestroy () {
            window.removeEventListener("scroll", this.watchScroll)
        },
        methods: {
          quit(v){
            if(v === '退出'){
            this.$store.commit('SET_LOG_STATE', false)
              // this.$store.commit('SET_SITE_INFO', null)
              localStorage.removeItem('Authorization')
              // alert(localStorage.getItem('Authorization'))
            }
          },
          travelerLogin(){
            this.$store.dispatch('getSiteInfo').then(data =>{
                    this.websiteInfo = data
                })
            localStorage.setItem('Authorization', 'I_am_a_traveler')
            this.$store.commit('SET_LOG_STATE', true)
            this.$router.push({
              path:'/'
            })
          },
          checkLogin(){
            if(localStorage.getItem('Authorization') === null||localStorage.getItem('Authorization') ===''){
              this.$store.commit('SET_LOG_STATE',false)
            }else this.$store.commit('SET_LOG_STATE',true)
          },
            watchScroll() {
                let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
                if (scrollTop===0){
                    this.fixed = false;
                } else if (scrollTop>=this.lastScrollTop){
                    this.fixed = false;
                    this.hidden = true;
                } else {
                    this.fixed = true
                    this.hidden = false
                }
                this.lastScrollTop = scrollTop
            },
            fetchCategory() {
                fetchCategory().then(res => {
                    this.category = res.data
                }).catch(err => {
                    console.log(err)
                })
            },
          fetchProfile(){
            fetchProfile().then(res=>{
                this.profile = res.data
            }).catch(err => {
              console.log(err)
            })
          }
        }
    }
</script>

<style scoped lang="less">
.menu-img{
  height: 40px;
  width: 40px;
  border-radius: 50%;
}
.bbutton{
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: #13c2c2;
  color: #ffffff;
  font-size: 0.9em;
  cursor: pointer;
}
    #layout-header {
        position: fixed;
        top: 0;
        z-index: 9;
        width: 100%;
        height: 80px;
        padding: 0 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: .3s all ease;
        -webkit-transition: .3s all ease;
        -moz-transition: .3s all linear;
        -o-transition: .3s all ease;
        -ms-transition: .3s all ease;
        &.hidden{
            top: -100px;
        }
        &.fixed{
            background-color: #FFFFFF;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        }
    }

    .site-logo {
        text-align: center;

        img {
            width: 60px;
            height: 60px;
        }

        p.site-name {
            font-size: 15px;
            font-weight: bold;
            position: relative;
            top: -10px;
        }
    }
    .menus-btn{
        display: none;
        visibility: hidden;
    }
    .site-menus {
        display: flex;
        align-items: center;

        .menu-item {
            min-width: 60px;
            height: 50px;
            line-height: 50px;
            text-align: center;
            position: relative;
            a{
                padding: 12px 10px;
                color: #545454;
                font-weight: 500;
                font-size: 16px;
                &:hover {
                    color: #ff6d6d;
                }
            }
            &:not(:last-child) {
                margin-right: 15px;
            }
            &.hasChild:hover .childMenu{
                opacity:1;
                visibility: visible;
                transform: translateY(-5px);
            }
        }
        .childMenu{
            width: 130px;
            background-color: #FDFDFD;
            border-radius: 3px;
            border: 1px solid #ddd;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
            position: absolute;
            top: 55px;
            z-index: 2;
            opacity: 0;
            visibility: hidden;
            transition: .7s all ease;
            -webkit-transition: .6s all ease;
            -moz-transition: .6s all linear;
            -o-transition: .6s all ease;
            -ms-transition: .6s all ease;
            &:before,&:after{
                content: '';
                position: absolute;
                width: 0;
                height: 0;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-bottom: 8px solid white;
                top: -8px;
                left: 20px;
            }
            &:before {
                top: -9px;
                border-bottom: 8px solid #ddd;
            }
            .sub-menu{
                height: 40px;
                line-height: 40px;
                position: relative;
                &:not(:last-child):after{
                    /*position: absolute;*/
                    content: '';
                    width: 50%;
                    height: 1px;
                    color: #ff6d6d;
                    bottom: 0;
                    left: 25%;
                    z-index: 99;
                }
            }
        }
    }
    @media (max-width: 960px){
        #layout-header{
            padding: 0 20px;
        }
    }
    @media (max-width: 600px){
        #layout-header{
            padding: 0 10px;
        }
        .menus-btn{
            display: block;
            visibility: visible;
        }
        .site-menus{
            position: absolute;
            display: none;
            visibility: hidden;
            background-color: #F9F9F9;
            width: 100%;
            left: 0;
            top: 80px;
            z-index: -9;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
            .menu-item{
                position: relative;
                height: unset;
                &:not(:last-child) {
                    margin-right: 0;
                }
            }
            .childMenu{
                position: relative;
                width: 100%;
                top: 0;
                background-color: #F3F3F3;
                opacity: 1;
                visibility: visible;
                border: none;
                box-shadow: none;
                &:before,&:after{
                    content: '';
                    position: relative;
                    width: 0;
                    height: 0;
                    border-left: 0;
                    border-right: 0;
                    border-bottom: 0;
                }
            }
        }
        .site-menus.mobileShow{
            display: inline-block;
            visibility: visible;
            z-index: 99;
        }
    }

</style>
