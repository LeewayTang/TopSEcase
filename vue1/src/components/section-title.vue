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
        color: #007575;
        font-size: 20px;
        font-weight: 400;
        padding-bottom: 15px;
        border-bottom: 1px dashed #ECECEC;
        display: inline-block;
    }
</style>
