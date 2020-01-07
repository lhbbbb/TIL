<template>
  <div>
    <h2>Video Detail</h2>
    <p>{{ video.snippet.title }}</p>
    <iframe :src="iframeUrl" frameborder="0"></iframe>
    <h3>상세내용</h3>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    iframeUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>