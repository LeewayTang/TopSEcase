<template>
    <div class="feature">
        <div @click="selectContent(data.name)">
            <div class="feature-title"><span class="foverlay">{{data.title}}</span></div>
            <img :src="data.img">
        </div>
    </div>
</template>

<script>
import {fetchArticle, fetchBooksOnly, fetchRelative} from "@/api";

    export default {
        name: "feature",
        props: {
            data: {
                type: Object,
                default: () =>{
                    return{
                        title: 'Akina',
                        img: 'https://cdn.zhebk.cn/usr/themes/Akina//images/feature/feature1.jpg',
                        href: 'https://zhebk.cn/Web/Akina.html'
                    }
                }
            }
        },
      methods:{
          selectContent(v){
            switch (v){
              case 'Articles':
                fetchArticle().then(res=>{
                  this.data = res
                })
                    break
              case 'Books':
                fetchBooksOnly().then(res=>{
                  this.data = res
                })
                    break
              case 'Relative':
                fetchRelative().then(res=>{
                  this.data = res
                })
                    break
            }
          }
      }
    }
</script>

<style scoped lang="less">
    .feature {
        width: inherit;
        position: relative;
        margin-bottom: 50px;
        img {
            height: 100px;
            width: 257px;
            object-fit: cover;
            border-radius: 10px;
        }
        & a:hover .foverlay{
            opacity:1;
        }
        .foverlay {
            position: absolute;
            z-index: 2;
            width: 257px;
            height: 100px;
            text-align: center;
            line-height: 100px;
            background: #4f5b69;
            color: white;
            font-size: 16px;
            opacity: 0;
            border-radius: 5px;

            -moz-transition: opacity .4s ease-out;
            -o-transition: opacity .4s ease-out;
            -webkit-transition: opacity .4s ease-out;
            transition: opacity .4s ease-out;
        }
    }
</style>
