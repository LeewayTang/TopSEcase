<template>
  <div class="layout">
    <Layout>
      <Sider breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" width="400">
        <Menu active-name="1-2" theme="dark" width="auto" :class="menuitemClasses"
              :style="{backgroundColor:color,height:'100vh'}">
            <span style="position: fixed;left: 60px">
            <Img style="width: 280px;border-radius: 10px;margin-top:30%"
                 src="https://s1.ax1x.com/2020/09/22/wXa0JI.png"/>
            </span>
          <br><br>
          <MenuGroup style="padding-top:120px;text-align: center">
            <a href="#message">
              <MenuItem name="1">
                <Icon size="50" type="md-body"/>
                <span class="menu-text">信息</span>
              </MenuItem>
            </a>
            <a href="#develop">
              <MenuItem name="2">
                <Icon size="50" type="ios-cafe"/>
                <span class="menu-text">圈子</span>
              </MenuItem>
            </a>
            <a href="#front">
              <MenuItem name="3">
                <Icon size="50" type="md-clock"/>
                <span class="menu-text">书评</span>
              </MenuItem>
            </a>
            <div class="colorPick">
              <ColorPicker v-model="color" @change="change"/>
            </div>
            <!--        导航栏-->
          </MenuGroup>
        </Menu>
        <!--        菜单栏-->
      </Sider>

      <Layout>
        <div class="con">
          <Content :style="{ margin: '20px', background: '#fff', minHeight: '220px'}">
            <card class="write" id="message">
              <h1 class="-head-title" slot="title">
                个人信息 About Me
              </h1>

<!--                <div style="display: inline-block;top: 0;height: 47vh;margin: 0 20px">-->
<!--                  <img v-if="headImg" src="https://s3.ax1x.com/2021/02/12/yDqk7V.jpg" alt="face"-->
<!--                       style="position:relative;object-fit:cover;height:20vh;width: 30vh"/>-->
<!--                </div>-->
                <div style="display: inline-block;top:0">
                  <cell>
<!--                    <ol style="font-size: 25px;font-weight: bold" :style="{color:color}">information</ol>-->
                  </cell>
<!--                  <card>-->
<!--                    <blockquote :style="{borderLeftColor:color}">-->
<!--                      <p :style="{lineHeight:'40px'}">-->
<!--                        <span>鄙人姓林，名柏仲，生于四川，长于重庆。</span>-->
<!--                        <span>一介重邮大四书生耳，苦读十四载，于辛丑年闻道社会。</span>-->
<!--                        <span>“修德、博学、求实、创新”乃吾校真言，在校期间钻研于软件工程学院。</span>-->
<!--                        <span>并非前端科班出生，一年根据学业习得C++，其后一年习得Java，<br>前端自寻道路深入，无贵人相助，无益友与之共道。</span>-->
<!--                      </p>-->
<!--                    </blockquote>-->
                    <Row>
<!--                      <Col span="12">主页：<a href="http://lbzz.3vkj.net">lbzz.net</a><br>-->
<!--                        博客：<a href="https://segmentfault.com/u/lbzz">lbzzblog.net</a></Col>-->
<!--                      <Col span="12">qq：<a href="http://wpa.qq.com/msgrd?v=3&uin=1906712915&site=qq&menu=yes">1906712915</a></Col>-->
                    </Row>
<!--                  </card>-->
                </div>

            </card>
            <!--          关于我-->
            <Divider dashed/>
            <card class="write" id="develop">
              <h1 class="-head-title" slot="title">
                圈子 Circle
              </h1>
<!--              <Timeline>-->
<!--                <TimelineItem>-->
<!--                  <p class="time" :style="{color:color,fontSize:'20px'}">2017年9月-2018年6月</p>-->
<!--                  <card class="content">公众号自媒体<br>-->
<!--                    <blockquote :style="{borderLeftColor:color}">-->
<!--                      在一学年结束之际粉丝数量达到2000+。类型为互联网新闻和软件分享，以及一些网站前沿技术、动效开源代码分享等。<br>-->
<!--                      后期主要以在前端学习的经验知识记录为主要输出手段，记录自己在学习中遇到的问题和对问题的-->
<!--                      解答。<br>-->
<!--                      下半年尝试小程序开发，类型为信息推送，内容与公众号内容保持同步，以信息瀑布-->
<!--                      流的形式展示公众号的内容，以及个人中心等界面方便用户管理自己的留言。<br>-->
<!--                      因为需要投入大量精力和时间，后续并未维护。<br>-->
<!--                      后因微信官方打击非正版资源，又因发布了破解内容，公众号被封号，最后也不了了之。<br>-->
<!--                      希望大家都支持正版！-->
<!--                    </blockquote>-->
<!--                  </card>-->
<!--                </TimelineItem>-->
<!--                <TimelineItem>-->
<!--                  <p class="time" :style="{color:color,fontSize:'20px'}">2018年9月-2019年6月</p>-->
<!--                  <card class="content">-->
<!--                    UI组组长<br>-->
<!--                    <blockquote :style="{borderLeftColor:color}">-->
<!--                      加入了学校图灵实验室，期间主要以PhotoShop和Premiere工具为主要生产力，多次对校内展开的活动设计海报和产品包装设计。<br>-->
<!--                      在后期组织团队用Html+Css对多个旧版网站进行翻新美化。-->
<!--                    </blockquote>-->
<!--                  </card>-->
<!--                </TimelineItem>-->
<!--                <TimelineItem>-->
<!--                  <p class="time" :style="{color:color,fontSize:'20px'}">2019年9月-2020年6月</p>-->
<!--                  <card class="content">-->
<!--                    自学前端-->
<!--                    <blockquote :style="{borderLeftColor:color}">-->
<!--                      尝试开发个人简历网站。但是在后面不知道怎么就不在了，也没有存Github。<br>-->
<!--                      陆陆续续参加各种比赛，用qt可视化界面做过界面设计，之后采用B/S架构就改成网页前端了。<br>-->
<!--                    </blockquote>-->
<!--                  </card>-->
<!--                </TimelineItem>-->
<!--                <TimelineItem>-->
<!--                  <p class="time" :style="{color:color,fontSize:'20px'}">2020年7月-2020年9月</p>-->
<!--                  <card class="write">-->
<!--                    项目组长-->
<!--                    <blockquote :style="{borderLeftColor:color}">开发一个二手手机的线上交易平台名为板砖交易系统。<br>-->
<!--                      因为初次带领项目，整个开发周期用了半个月，团队共两人参与编码设计。<br>-->
<!--                      采用B/S架构的ssm框架，独自一人完成前端工作及部分后端编码，组织包括数据库设计、需求建模，多次协调团队内部问题，<br>-->
<!--                      最终在预定时间完成该项目的发布。-->
<!--                    </blockquote>-->
<!--                    项目地址：<a href="https://gitee.com/lbzz1906/banzhuan.git">banzhuan.git</a>-->
<!--                    <Divider/>-->
<!--                  </card>-->
<!--                  <Carousel autoplay v-model="value2" style="max-width: 600px" loop>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6dYT.png" alt="登陆">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6BpF.png" alt="店铺信息">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6akV.png" alt="订单信息">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6Dl4.png" alt="交易">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6sX9.png" alt="卖家商品修改">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv66mR.png" alt="添加操作">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6Rk6.png" alt="用户信息">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wv6WtK.png" alt="注册">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                  </Carousel>-->
<!--                  &lt;!&ndash;                    板砖截图&ndash;&gt;-->

<!--                </TimelineItem>-->
<!--                <TimelineItem>-->
<!--                  <p class="time">2020年9月</p>-->
<!--                  <p class="content">项目组组长</p>-->
<!--                  <blockquote :style="{borderLeftColor:color}">开发一个医院医疗管理系统。<br>-->
<!--                    再次带领团队，整个开发周期只用了一周，团队共两人参与编码设计。-->
<!--                    名称为重邮云医疗平台，主要用于减轻校 医院的工作压力。<br>-->
<!--                    项目前端采用vue脚手架独立完成开发，项目后端采用springboot架构进行开 发提供给我接口。<br>-->
<!--                    参与并指导包括需求分析、需求建模、数据库构建。界面ui使用iview框架进 行开发，整个项目使用纯组件化开发，与数据库交互使用的axios。-->
<!--                  </blockquote>-->
<!--                  项目地址：<a href="https://gitee.com/lbzz1906/chongyouyun.git">chongyouyun.git</a>-->
<!--                  <Divider/>-->
<!--                  <Carousel autoplay v-model="value2" style="max-width: 600px" title="项目界面展示" loop>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvhSjU.png" alt="登陆">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvfzcT.png" alt="挂号">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvhCB4.png" alt="人事">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvh9uF.png" alt="药品">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvhPHJ.png" alt="药品出库">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                    <CarouselItem>-->
<!--                      <div class="demo-carousel">-->
<!--                        <img src="https://s1.ax1x.com/2020/09/23/wvhkNR.png" alt="医生">-->
<!--                      </div>-->
<!--                    </CarouselItem>-->
<!--                  </Carousel>-->
<!--                  &lt;!&ndash;云医疗截图&ndash;&gt;-->
<!--                </TimelineItem>-->
<!--              </Timeline>-->
            </card>
            <!--          发展历程-->
            <Divider dashed/>
            <card class="write" id="front">
              <h1 class="-head-title" slot="title">
                书评 Book Review
              </h1>
                <h2 :style="{borderBottomColor:color}">
                  <span :style="{backgroundColor:color}">我的导师</span>
                </h2>
              <card>
<!--              舍弃多年前制作的个人主页，用vue cli彻底重构。<br>-->
<!--              整个网页为响应式布局，可支持PC端和移动端的浏览，在移动端会自动隐藏Menu组件，在项目图片轮播窗口大小也会自适应改变。<br>-->
<!--              框架由viewui的layout布局打底，期间使用Sider、MenuGroup、、Gird布局等技术以及card、cell、时间线TimeLine等组件。<br>-->
<!--              主题由颜色选择器获取颜色，再通过Vue的：style属性动态绑定实现同步颜色，改变Menu和内容页部分组件颜色和部分字体。<br>-->
<!--              个人网站源代码已开源，欢迎大家学习，<a href="https://github.com/lbzz1906/lbzz1906.github.io.git">项目地址</a>-->
              </card>
            </card>
<!--            前端之路-->
            <BackTop></BackTop>
          </Content>
        </div>
      </Layout>
    </Layout>

  </div>

</template>

<script>
export default {
  name: 'table',
  data() {
    return {
      headImg:true,
      value2: 0,
      isCollapsed: false,
      color: '#abacb3',
      ifShow: true,
      websiteInfo: {}
    }
  },
  created() {
    this.getWebSiteInfo()
  },
  computed: {
    rotateIcon() {
      return [
        'menu-item',
        this.isCollapsed ? 'collapsed-menu' : '',
        this.isCollapsed ? 'img' : ''
      ];
    },
    menuitemClasses() {
      return [
        'menu-item',
        this.isCollapsed ? 'collapsed-menu' : ''
      ]
    }
  },
  // mounted(){
  //   let windowWidth =document.body.clientWidth
  //   if(windowWidth < 600){
  //     this.headImg=false;
  //   }
  // },
  methods: {
    change() {
      style.setProperty('background', this.color)
    },
    getWebSiteInfo(){
                this.$store.dispatch('getSiteInfo').then(data =>{
                    this.websiteInfo = data
                })
            },
    collapsedSider() {
      this.$refs.side1.toggleCollapse();
      this.ifShow = !this.ifShow
    }
  }
}
</script>
<style scoped="scoped">
.menu-text{
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 3.0em;
  font-weight: bold;
  color: #6cd0b9;
}
.-head-title{
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  font-size: 4.0em;
  font-weight: bold;
  color: #6cd0b9;
}
.con{
  margin-top: 60px;
}

/*<!-- Add "scoped" attribute to limit CSS to this component only -->*/

@import "../css/table.css";
@import "../css/orangeheart.css";
</style>
