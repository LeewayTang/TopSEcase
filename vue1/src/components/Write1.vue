<template>
  <div id="editor">
    <mavon-editor style="height: 100%"></mavon-editor>
  </div>
</template>
<script>
// Local Registration
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
export default {
  name: 'editor',
  components: {
    mavonEditor
    // or 'mavon-editor': mavonEditor
  }
}
</script>
<style>
#editor {
  margin-top: 250px;
  margin-right: auto;
  margin-left: auto;
  width: 80%;
  height: 900px;
  /*z-index:1 !important;*/
}
</style>