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
export function fetchContentList(){
    return request({
        url: '/content-list',
        method: 'get',
        params: {}
    })
}
export function fetchBookInfo(id){
    return request({
        url: '/books/' + id,
        method: 'get',
        params: {}
    })
}

export function fetchBookList() {
    return request({
        url: '/book-list',
        method: 'get',
        params: {}
    })
}
export function fetchTags() {
    return request({
        url: 'book-ground/tags',
        methods: 'get',
        params: {}
    })
}
export function fetchReview() {
    return request({
        url: 'book-ground/review',
        methods: 'get',
        params: {}
    })
}
// export function fetchTSB() {
//     return request ({
//         url: '/book-list',
//         methods: 'get',
//         params: {}
//     })
// }

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

export function fetchTravelerInfo() {
    return request({
        // url: '/site1',
        url: '/api/login_register/loginTraveler',
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

export function fetchSuggest() {
    return request({
        url: '/suggest',
        method: 'get',
        params: {}
    })
}

export function fetchDiscussionQues() {
    return request({
        url: '/discussionQues',
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

export function fetchArticle(){
    return request({
        url: '/article/0',
        method: 'get',
        params:{}
    })
}
export function fetchArticlesOnly(){
    return request({
        url: '/select/Articles',
        method: 'get',
        params: {}
    })
}

export function fetchBooksOnly(){
    return request({
        url: '/select/Books',
        method: 'get',
        params: {}
    })
}

export function fetchRelative(){
    return request({
        url: '/select/Relative',
        method: 'get',
        params: {}
    })
}
