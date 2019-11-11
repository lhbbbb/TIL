# JS를 쓰는 이유

* Client Side(Browser) Rendering을 하기 위해
  * 사용자 경험
  * 서버 부담을 줄이기 위해
* 즉 클라이언트가 렌더링을 한다
* js를 쓰지 않을 때는 django가 해줬는데 이를 Server Side Rendering이라 한다

# Vue.js

* javascript보다 페이지를 만들기 쉬워서 배움
* addEventListener의 콜백함수로 arrow function을 사용하지 않는다
* input event 입력되는 순간을 캐치
* reactive 반응형(data의 변화) => 자동적용, 반영
* $, _ 로 변수명을 만드는 건 자제

## 만들어보기

### Vue.js install

* vue.js 홈페이지에서 cdn 긁어오기

* 객체 만들기

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>

<body>
  <div id='app'>
    <h1>댓글달기</h1>
    <input type="text" v-model="msg">
    <p>{{ msg }}</p>
  
    <h2>좋아요</h2>
    <p>좋아요 갯수: {{ likeCount }}</p>
    <button @click='like'>좋아요</button>

  </div>


  <script>
    const app = new Vue({
      el: '#app',
      data: {
        msg: '와 Vuejs 시작했다',
        likeCount: 0,
      },
      methods: {
        like: function() {
          this.likeCount += 1
        }
      },
    })
  </script>
</body>

</html>
```

* vue js element

```js
new Vue({
    el: '',
    data: {
        
    },
    methods: {
        
    },
})
```

* vue directive => methods를 어떻게 연결하는지 나옴

* vscode 에서 vetur, vue vscode snippets extension 설치

* chrome에서 vue.js devtools extension 추가



# Vue.js로 todo리스트 만들기

* 행위에 대한 것 vue directive
* vue for 문

```html
<div id="app">
    <h1>Vue ToDo</h1>
    <ul>
      <li v-for='todo in todos'>
        {{ todo }}
      </li>
    </ul>
  </div>
  <div id="app2">
```

* vue for 문  object의 list형태로 만들기

```html
<div id="app">
    <h1>Vue ToDo</h1>
    <ul>
        <li v-for='todo in todos'>
            {{ todo.content }}
            {{ todo.completed }}
        </li>
    </ul>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    // M (V VM)
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                { content: '꽃 사서 배달시키기', completed: false },
                { content:'IR 자료 만들기', completed: false },
                { content:'과목평가 문제 검토', completed: false },
                { content:'호호우!!', completed: false },
            ],
        },
        method: {
            changeName(input) { // ES6부터 축약형으로 사용 가능
                this.name = input
            }
        }
    })
</script>
```

* vue if 문

```html
<div id="app">
    <h1>Vue ToDo</h1>
    <ul>
        <li v-for='todo in todos' v-if="todo.completed"> <!-- vue if -->
            {{ todo.content }}
            {{ todo.completed }}
        </li>
    </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    // M (V VM)
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                { content: '꽃 사서 배달시키기', completed: true },
                { content:'IR 자료 만들기', completed: false },
                { content:'과목평가 문제 검토', completed: false },
                { content:'호호우!!', completed: false },
            ],
        },
        method: {
            changeName(input) { // ES6부터 축약형으로 사용 가능
                this.name = input
            }
        }
    })
    const app2 = new Vue({
        el: '#app2',
    })
</script>
```

* elif 문

```html
  <div id="app">
    <h1>Vue ToDo</h1>
    <ul>
      <li v-for='todo in todos' v-if="!todo.completed">
        {{ todo.content }}
        {{ todo.completed }}
      </li>
      <li v-else>
        완료!
      </li>
    </ul>
  </div>
```

*  vue method문

```html
<li v-for='todo in todos' v-if="!todo.completed" v-on:click="클릭되었을때 실행할 method_name">
```

* vue method문 다른 버전

```html
<div id="app">
    <h1>Vue ToDo</h1>
    <ul>
        <li v-for='todo in todos' v-if="!todo.completed" v-on:click="check(todo)">
            {{ todo.content }}
            {{ todo.completed }}
        </li>
        <li v-else v-on:click="uncheck(todo)">
            완료!
        </li>
    </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    // M (V VM)
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                { content: '꽃 사서 배달시키기', completed: true },
                { content:'IR 자료 만들기', completed: false },
                { content:'과목평가 문제 검토', completed: false },
                { content:'호호우!!', completed: false },
            ],
        },
        methods: {
            // check: function () {} 
            check(todo) { // ES6부터 축약형으로 사용 가능
                todo.completed = true
            },
            uncheck(todo) {
                todo.completed = false
            }
        }
    })
</script>
```

* vue method문 다른 버전

```html
<div id="app">
    <h1>Vue ToDo</h1>
    <ul>
        <li v-for='todo in todos' v-if="!todo.completed" v-on:click="check(todo)">
            {{ todo.content }}
            {{ todo.completed }}
        </li>
        <li v-else v-on:click="check(todo)">
            완료!
        </li>
    </ul>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
    // M (V VM)
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                { content: '꽃 사서 배달시키기', completed: true },
                { content:'IR 자료 만들기', completed: false },
                { content:'과목평가 문제 검토', completed: false },
                { content:'호호우!!', completed: false },
            ],
        },
        methods: {
            // check: function () {} 
            check(todo) { // ES6부터 축약형으로 사용 가능
                todo.completed = !todo.completed
            },
        }
    })
</script>
```

* img 넣기
  * 태그의 속성에는 mastache 값({{ value }})을 사용할 수 없고 v-bind를 사용해서 속성을 지정해준다

```html
<img v-bind:src="imgSrc" alt="" v-bind:height="height" v-bind:width="width">
  <script>
    // M (V VM)
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: "https://joshua1988.github.io/images/posts/web/vuejs/logo.png",
        height: 300,
        width: 300,
      },
    })
  </script>
```

* v-bind 축약

```html
<img :src="imgSrc" alt="" :height="height" :width="width">
```

* v-on 축약

```html
<li @click="check(todo)"> <!-- v-on:click="check(todo)" -->
```



* Vanilla JS 예시
  * input tag를 querySelector를 통해 잡는다
  * input 태그의 내용물을 userInput.target.value
  * let data = userInput.target.value
* Vue.js
  * VM(View-Model)

* js 컨벤션: single quote '', html은 double quote ""

* 리스트에 값넣기

```html
<input type="text" v-model="newTodo" @keyup.enter="addTodo">
<script>
    // M (V VM)
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                { content: '꽃 사서 배달시키기', completed: true },
            ],
            newTodo: '',
        },
        methods: {
            addTodo() {
                this.todos.push({
                    content: this.newTodo,
                    completed: false,
                })
                this.newTodo = ''
            },
        }
    })
</script>
```

* vue filter

```html
<button @click="clearCompleted">완료목록 전체삭제</button>
<script>
methods: {
    clearCompleted() {
    // 뭐만 남기면 될까? completed == false
    const notCompleted=this.todos.filter(todo => {
    return !todo.completed
    })
    this.todos = notCompleted
    }
}
</script>
```

* **vue.js key**
  * [참고](https://kr.vuejs.org/v2/guide/list.html)



## Vue 관련 VSCode Extension

* Vetur
* Vue VSCode Snippets