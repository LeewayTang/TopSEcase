<template>
    <h1 class="section-title"><slot></slot></h1>
</template>
<!--聚焦、推荐等标题的格式-->

<script>
    export default {
        name: "section-title"
    }
</script>

<style scoped>
    h1.section-title {
        color: #2f3034;
        font-size: 30px;
        font-weight: 400;
        padding-bottom: 15px;
        border-bottom: 1px dashed #ECECEC;
    }
</style>
