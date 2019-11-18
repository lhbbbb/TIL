# Vue Directives

* [v-text](#v-text)
* [v-html](#v-html)
* [v-bind](#v-bind)
* [v-model](#v-model)
* [v-show](#v-show)
* [v-if, v-else-if, v-else](#v-if,-v-else-if,-v-else)
* [v-for](#v-for)
* [v-pre](#v-pre)
* [v-once](#v-once)
* [v-on](#v-on)

## 개념

디렉티브란 `v-` 접두사가 있는 특수 속성이다. Directive(지시) 라는 단어에서 유추할 수 있듯이, Vue 에게 지시하는 구문이다.

디렉티브 속성값은 `v-for`를 제외하고는 모두 **단일 JS 표현식** 이다.

디렉티브의 역할은 표현식의 값이 변경될 때, 반응적으로 DOM에 적용하는 것이다.

## Directives

### `v-text`

Vanilla JS(기본 형태)에서 `.innerText`와 동일한 기능을 수행한다. 태그를 일반 문자 상태로 보여준다.

보간법(`{{ }}`)을 사용하는 것과 같으며 보간법 사용을 권장한다.

```js
<template>
  <div id="app">
    <p v-text="message"></p>
    <p>{{ message }}</p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        message: '<h1>hi</h1>',
      }
    }
  }
</script>
```

### `v-html`

Vanilla JS에서 `.innerHTML`과 동일한 기능을 수행한다. 태그를 파싱하여 화면에 구현한다.

XSS(Cross Site Scripting) 공격에 주의해야 한다.

```js
<template>
  <div id="app">
    <p v-html="message"></p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        message: '<h1>hi</h1>',
      }
    }
  }
</script>
```

### `v-bind`

HTML 태그의 값을 다루는 것이 아니라 속성을 다룰 때 사용한다. 기존 HTML5 속성 뿐만 아니라, Vue 내부에서 사용하는 속성들도 `v-bind`를 통해 조작한다. 줄여서 `:`로 사용할 수 있다.

```js
<template>
  <div id="app">
    <div v-bind:class="classRed">
      red
    </div>
    <div :class="classBlue">
      blue
    </div>
    <img :src="imageUrl">
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        imageUrl: 'https://picsum.photos/100',
        classRed: 'red',
        classBlue: 'blue',
      }
    }
  }
</script>
<style>
  .red {
    background-color: red;
  }

  .blue {
    background-color: blue;
  }
</style>
```

### `v-model`

`input`/`textarea`와 같은 요소에서 사용자의 입력과 양방향 데이터 바인딩을 공유할 때 사용한다. 일반적인 HTML에서의 초기값인 `value`, `checked`, `selected` 등의 속성을 무시한다.

```js
<template>
  <div id="app">
    <input type="text" v-model="inputData">
    <p>실시간: {{ inputData }}</p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        inputData: ''
      }
    }
  }
</script>
```

### `v-show`

CSS `display:none;`과 동일한 기능

```js
<template>
  <div id="app">
    <p v-show="false">{{ data }}</p>
    <p v-show="true">{{ data }}</p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        data: 'This is v-show',
      }
    }
  }
</script>
```

### `v-if`, `v-else-if`, `v-else`

`if`, `else if`, `else` 조건문을 표현함.

```js
<template>
  <div id="app">
    <p v-if="userName === 'admin'">
      You are a admin
    </p>
    <p v-else-if="username === 'bad user'">
      Banned
    </p>
    <p v-else>
      You are normal user
    </p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        userName: 'admin',
      }
    }
  }
</script>
<style></style>
```

#### `v-show` VS `v-if`

특정 요소를 보이게하거나 안보이게 하고 싶다면, `v-if`와 `v-show` 두가지 선택지가 있다.

해당 요소의 화면 표현 전환(on/off)이 빈번하다면, `v-show`를 사용하는 것이 렌더링 비용이 적다.

반면 요소의 전환이 빈번하지 않고 고정되어 있다면, `v-if`를 사용하는 것이 컴파일 비용이 적다.

### `v-for`

`for` 반복문을 구현한다. `v-bind:key`를 필요로 한다.

```js
<template>
  <div id="app">
    <p>
      <span v-for="number in numbers" :key="`key-${number}`">
        {{ number }}
      </span>
    </p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        numbers: [1, 2, 3, 4],
      }
    }
  }
</script>
```

#### `v-for` & `v-if`

한 HTML 태그에 `v-for`와 `v-if`를 같이 사용할 경우, 표기 순서에 상관없이 `v-for`의 우선순위가 더 높다. 그리고 `v-for`와 `v-if`를 같이 사용하는 구문은 애초에 `computed` 속성을 통해 필터링된 배열을 사용하는게 더 옳다.

Vue cli 환경에서는 기본적으로 `v-for`와 `v-if`를 함께 사용하면 에러를 발생시키도록 eslint 설정이 되어있다.

```js
<template>
  <div id="app">
    <p v-for="student in students" v-if="student.pass" :key="student.name">
    </p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        testResults: [{
            name: 'ssafy',
            pass: true
          },
          {
            name: 'yfass',
            pass: false
          },
        ],
      }
    }
  }
</script>
```

### `v-pre`

Vue.js 가 컴파일 하지 않는다. 보간법(`{{ }}`)도 그대로 브라우저에 나타난다.

```js
<template>
  <div id="app">
    <p v-pre>
      {{ message }}
    </p>
  </div>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        message: 'hi'
      }
    }
  }
</script>
```

### `v-once`

최초 렌더링 단 한번만 수행한다. `data`가 수정되어도 처음 렌더링된 값만을 보여준다.

### `v-on`

`v-on` 디렉티브를 사용하여 DOM 이벤트 핸들링이 가능하다. 줄여서 `@`로 사용 가능하다.

#### 활용 가능한 이벤트명

활용 가능한 이벤트 명에는 다음과 같은 것들이 있다.

| 이벤트 이름  | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| `@click`     | 마우스를 클릭했을 때 실행                                    |
| `@dbclick`   | 마우스를 더블 클릭했을 때 실행                               |
| `@mouseover` | 마우스 포인터가 요소 위로 올라왔을 때 실행                   |
| `@mousemove` | 마우스의 포인터가 요소 안에서 이동했을 때 실행               |
| `@mouseup`   | 마우스의 버튼을 놓았을 때 실행                               |
| `@keydown`   | 키보드의 키를 눌렀을 때 실행                                 |
| `@keypress`  | 키보드의 키를 눌렀다가 놓았을 때 실행                        |
| `@change`    | 요소가 변경될 때 실행(`checkbox` 및 `radiobutton`은 이 이벤트를 사용) |
| `@input`     | 입력값이 변경될 때 실행(`input` 및 `textarea`는 이 이벤트를 사용) |
| `@submit`    | `<form>`이 제출될 때 실행                                    |
| `@focus`     | `<input>` 요소에 포커스가 있을 때 실행                       |
| ...          | ...                                                          |

