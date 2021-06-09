import Vue from 'vue'
import Vuex from 'vuex'
import {getTimeInterval} from '../utils/index'
import {fetchSiteInfo0,fetchSocial} from '@/api'
import {fetchTravelerInfo} from "../api";

Vue.use(Vuex)
// 略:后台获取系统运行时间
const runAt = '1589878800000';
let timer = null;
const state = {
    loading: false,
    isLogging: true,
    hasLogin:false,
    runTimeInterval: '',
    socials: '',
    websiteInfo: '',
    username: '没有共产党就没有新中国'
}
const mutations = {
    SET_LOADING: (state, v) => {
        state.loading = v;
    },
    SET_SOCIALS: (state, v) => {
        state.socials = v;
    },
    SET_SITE_INFO: (state, v) =>{
      state.websiteInfo = v;
    },
    GET_RUNTIME_INTERVAL: (state) => {
        if (!timer || !state.runTimeInterval) {
            clearInterval(timer)
            timer = setInterval(() => {
                state.runTimeInterval = getTimeInterval(runAt);
            }, 1000);
        }
    },
    SET_LOGGING_STATE:(state)=>{
        if(state.isLogging)
            state.isLogging = false
        else
            state.isLogging = true
    },
    SET_LOG_STATE:(state ,v)=>{
        state.hasLogin = v
    }
}

const actions = {
    setLoading: ({commit}, v) => {
        commit('SET_LOADING', v);
    },
    initComputeTime: ({commit}) => {
        commit('GET_RUNTIME_INTERVAL');
    },
    getSiteInfo0: ({commit,state}) =>{
        return new Promise(resolve => {
            fetchSiteInfo0().then(res => {
                let data = res.data || {}
                commit('SET_SITE_INFO',data);
                resolve(data);
            }).catch(err => {
                resolve({});
            })
        })
    },
    getSocials: ({commit,state}) =>{
        return new Promise((resolve => {
            if (state.socials){
                resolve(state.socials)
            } else {
                fetchSocial().then(res =>{
                    let data = res.data || []
                    commit('SET_SOCIALS',data);
                    resolve(data);
                }).catch(err =>{
                    resolve([]);
                })
            }
        }))
    }
}
const getters = {
    loading: state => state.loading,
    runTimeInterval: state => state.runTimeInterval,
    notice: state => state.websiteInfo?state.websiteInfo.notice:''
}
export default new Vuex.Store({
    state,
    mutations,
    actions,
    modules: {},
    getters
})
