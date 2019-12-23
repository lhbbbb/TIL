<template>
  <div>
    <li @click="onSelect">
      <img :src="thumbnailUrl" alt="">
    </li>
  </div>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {
    onSelect() {
      this.$emit('videoSelect', this.video)
    }
  },
  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>

</style>