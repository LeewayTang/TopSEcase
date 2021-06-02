<template>
  <div class="layout">
    <Layout>
      <Sider breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed" width="400">
        <Menu active-name="1-2" theme="dark" width="auto" :class="menuitemClasses"
              :style="{backgroundColor:color,height:'100vh'}">
            <span style="position: fixed;left: 60px">
              <div>
<!--                <img :src="">-->
              </div>
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
                <span class="menu-text">作品</span>
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
                <div style="display: inline-block;top:0">
                  <cell>
                    <ol style="font-size: 25px;font-weight: bold" :style="{color:color}">所在圈子</ol>
                  </cell>
                </div>

            </card>
            <Divider dashed/>
            <card class="write" id="develop">
              <h1 class="-head-title" slot="title">
                我的笔记 Notes
              </h1>
            </card>
            <Divider dashed/>
            <card class="write" id="front">
              <h1 class="-head-title" slot="title">
                我的书帖 Books
              </h1>
                <h2 :style="{borderBottomColor:color}">
                  <span :style="{backgroundColor:color}">我的导师</span>
                </h2>
            </card>
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
@import "../css/table.css";
@import "../css/orangeheart.css";

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

</style>
