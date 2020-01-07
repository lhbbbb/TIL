<template>
  <div>
    <h2>VideoList</h2>
    <ul>
      <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video" @videoSelect="onVideoSelect"/>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'
export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    }
  },
  methods: {
    onVideoSelect(video) {
      this.$emit('selectedVideo', video)
    }
  }
}
</script>

<style>

</style>