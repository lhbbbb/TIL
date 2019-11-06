# Single file component

* 확장자명
  * .vue

* vue cli

`npm install -g @vue/cli`

`vue create todo-vue-cli`



## babel.config

* 번역가



## package.json



## package-lock.json

* package.json을 기반으로 만들어주는것
* 건드릴 필요 없음



## VSCode settings

* indentation set
  * f1 => preference => open settings(Json)=> 다음 내용 추가

```json
    "[vue]": {
        "editor.tabSize": 2
    },
```

* server 돌리기 `npm run serve`

## App.vue

약어 vue 치고 tab



## mockup

* 카카오 오븐



## package.json 설정

```json
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {
      "no-console": "off"
    },
```



## component

### 부모-자식 데이터 주고받기

#### 부모

```ㅗ싀
<template>
  <div>
    <h1>Youtube Searcher</h1>
    <SearchBar @inputChange="onInputChange"/>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar'
export default {
  name: 'App',
  components: {
    SearchBar,
  },
  methods: {
    onInputChange (inputValue) {
      console.log(inputValue)
    }
  }
}
</script>

<style>

</style>
```

#### 자식

* emit

```js
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      console.log(event.target.value)
      // $emit 메소드는 자식 컴포넌트 -> 부모 컴포넌트 data를 올려줄때
      this.$emit('이벤트', 보내줄데이터)
    }
  }
}
```

```html
<template>
  <div>
    <input v-on:input="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      // console.log(event.target.value)
      // $emit 메소드는 자식 컴포넌트 -> 부모 컴포넌트 data를 올려줄때
      this.$emit('inputChange', event.target.value)
    }
  }
}
</script>

<style>

</style>
```



## googleapi 사용하기

`https://www.googleapis.com/youtube/v3/search?key=API_KEY&type=video&part=snippet&q=검색어`

### API KEY 숨기기

* .env.local 파일 만들기
  * 접두어로 VUE_APP_[*var_name*]=[*value*]

```js
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY // django decouple
```

## 1. onInputChange 메서드 호출

## 2. Youtube API 요청

## 3. Youtube 응답 받고

## 4. Youtube Response 비디오 리스트 App Component의 data로 저장

## 5. data가 업데이트 되면, 컴포넌트가 템플릿을 다시 렌더링을 함(Vue가 해줌)

## 6. VideoList에서 변경된 결과를 보여줌



## 기타

* 부모, 자식 컴포넌트간의 props, $emit 관계가 궁금하다면 observer pattern을 공부해보도록 하자