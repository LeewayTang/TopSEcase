<template>
  <div class="mainWrapper">
    <content-list></content-list>
  </div>
</template>

<script>
import contentList from './content-list'

export default {
  name: 'logPageMain',
  components: {
    contentList
  }
}
</script>

<style lang="stylus" scoped></style>
