import request from '@/utils/request'

export function fetchList(params) {
    return request({
        url: '/post/list',
        method: 'get',
        params: params
    })
}

export function fetchFocus() {
    return request({
        url: '/focus/list',
        method: 'get',
        params: {}
    })
}

export function fetchCategory() {
    return request({
        url: '/category',
        method: 'get',
        params: {}
    })
}

export function fetchProfile() {
    return request({
        url: '/profile',
        method: 'get',
        params: {}
    })
}
export function fetchFriend() {
    return request({
        url: '/friend',
        method: 'get',
        params: {}
    })
}

export function fetchSocial() {
    return request({
        url: '/social',
        method: 'get',
        params: {}
    });
}

export function fetchSiteInfo0() {
    return request({
        url: '/site0',
        method: 'get',
        params: {}
    })
}

export function fetchSiteInfo() {
    // alert('000')
    return request({
        // url: '/api/try/Try/',
        url: '/site1',
        method: 'get',
        params: {}
    })
}

export function fetchComment() {
    return request({
        url: '/comment',
        method: 'get',
        params: {}
    })
}

export function addBook(){
    return request({
        url: '/book_tag/add_book',
        method: post,
        params:{}
    })
}

// export function addArticle(){
//     return request({
//         rul: '/'
//     })
// }
