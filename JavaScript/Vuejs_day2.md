# Vuejs 패턴

* View(보여지는 부분)-ViewModel-Model(데이터 관리하는 부분)



# Vue.js

### Vue 인스턴스

```js
const app = new Vue({
    // Vue 인스턴스(ViewModel)가 어떤 HTML 요소에 마운트될지(적용될지)
    el: '#app',
    
    // Vue 인스턴스가 사용할 Data
    data: {},
    
    // Vue 인스턴스가 사용할 메소드들
    methods: {
        함수정의:,
    },
    
    // '미리' 계산된 값을 반환 -> 캐싱 => 성능상의 이슈로 사용하는 경우가 많음
    computed: {},
    
    // Vue 인스턴스의 data 변경을 관찰하고 이에 반응
    watch: {
        지켜볼 data: {
        	handler 메소드 정의 -> 지켜볼 데이터가 변경되었을 때 실행할 함수 // handler 이름으로만 사용해야한다
    	}
    }
})
```

### *Vue Directive*

```html
<p v-for></p>
<p v-if v-else v-else-if></p>
<p v-model></p>
<p v-on:[event]></p>, <p @[event]></p>
<p v-bind:[html속성이름]></p>, <p :[html속성이름]></p>
<p v-html></p>
<p v-text></p>
<p v-show></p>
```

### methods와 computed 비교하기

* methods는 호출이 될때마다 계속해서 수행함
* methods는 함수처럼 호출해야함 => method()
* computed는 계산된 값을 부르기 때문에 변수나, 속성 호출하듯이 사용하면 됨 => method (캐싱의 느낌)
* 따라서 계속해서 값이 변하는 값(ex. 날짜(시간)) 같은 경우는 computed가 아닌 method를 사용해야한다

```html
  <div id="app">
    <button @click="visible=!visible">토글버튼</button>
    <ul v-if="visible">
      <li>methods로 불렸을 때: {{ dateMethod() }}</li>
      <li>computed로 불렸을 때: {{ dateComputed }}</li>
    </ul>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        visible: true,
      },
      methods: {
        dateMethod() {
          return new Date()
        }
      },
      // 이미 계산된 값을 사용하기 때문에 호출해도 값이 변하지 않음
      computed: {
        dateComputed() {
          return new Date()
        }
      },
    })
  </script>
```

### localStorage API

* string 형태로 저장됨
* 따라서 value 넣을 때 JSON.stringify 해줘야함
* 새로고침해도 데이터가 바뀌지 않음

```js
// Creation
localStorage.setItem('key', 'value')

// Read
localstorage.getItem('key')

// Delete
localStorage.removeItem('key')

// Count
localStorage.length
```

```js
// chrome localStorage
const STORAGE_KEY = 'vue-todos'

const todoStorage = {
    save(todos) {
        // localStorage에 데이터를 저장
        return localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
    },
    fetch() {
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []
    }
}

// todoStorage.save(데이터)

// todoStorage.fetch()
const app = new Vue({
    el: '#app',
    data: {
    },
    methods: {
    },
    computed: {
    },
    watch: {
        todos: {
            handler (todos) {
                // todos가 변경될때마다, localStorage에 저장 => save()
                todoStorage.save(todos)
            },
            deep: true, // python copy.deepcopy 역할
        },
    }
})
```

## Vue Component

```js
Vue.component(컴포넌트 이름, {컴포넌트 속성})
```

```js
Vue.component('todo-list', {
    // 메소드화 시켜서 리턴문으로 표현
    data:,
    methods:,
    // div태그로 감싸줘야하는게 약속, 안쓰면 input만 뜸
    template:`
	<div>
	
	</div>
	`,
})
```

* 부모컴포넌트와 자식컴포넌트의 관계 => 건물주와 세입자의 관계. 방의 구조는 변경불가하지만 내용물은 변경 가능
* 자식컴포넌트가 부모로부터 데이터를 허락받고 받을 때(props) 일방적
* $emit 이벤트: 자식이 부모한테 무언가를 넘겨줄 때

### props

* props를 나타내는 방법

  ```js
  // 1. Array로 표현
  props : ['category']
  
  // 2. Object로 자료형 표현
  props : {
      category: String
  }
  
  // 3. Object로 옵션 추가
  props : {
      category: {
          type: String,
          required: true,
          validator: function(value) {
              if (value.length !== 0) {
                  return true
              } else {
                  return false
              }
          }
      }
  }
  ```

