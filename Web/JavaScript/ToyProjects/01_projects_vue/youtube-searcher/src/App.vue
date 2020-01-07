<template>
  <div id="app">
    <h1>Youtube Searcher</h1>
    <SearchBar @inputChange="onInputChange"/>
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos" @selectedVideo="renderVideo"/>
  </div>
</template>

<script>
import axios from 'axios'

import SearchBar from './components/SearchBar'
import VideoList from './components/videos/VideoList'
import VideoDetail from './components/videos/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'app',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange (inputValue) {
      console.log(inputValue)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      }).then(res => {
        this.videos = res.data.items
      }).catch(err => {
        console.log(err)
      })
    },
    renderVideo(video) {
      this.selectedVideo=video
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>