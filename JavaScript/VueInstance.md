# Vue Instance

* [Vue Instance 초기화에 사용되는 속성들](###Vue-Instance-초기화에-사용되는-속성들)
* [Components에서 활용되는 속성들](###Components에서-활용되는-속성들)

## 개념

모든 Vue App은 `new Vue()` 함수로 새로운 인스턴스를 만드는 것부터 시작한다.

```js
new Vue ({
    // options
})
```

Vue 인스턴스를 생성할 때, `data`, `template`, `el`, `methods`, 라이프 사이클 콜백함수 등을 포함할 수 있는 options 객체를 전달한다.

## Vue Instance의 속성들

### Vue Instance 초기화에 사용되는 속성들

#### `el`

마운트할 대상 HTML 요소(노드)를 정의한다. Vue 인스턴스 초기화에서 `.$mount()`로 대체 가능하다.

#### `data`

Vue 인스턴스가 최초 생성될 때의 속성값들을 정의한다. Vue 인스턴스가 최초 생성되면, `data` 객체 안의 모든 값들을 반응 시스템에 등록한다. 이 `data` 객체에 등록된 key 에 대해서만 value 수정에 대하여 반응하기 때문에, 최초 생성시에 할당할 값이 없다면, `''`, `[]`, `{}`, `0` 과 같은 값으로 초기화한다.

##### Vue는 `data`가 변경되면 기본적으로 DOM을 다시 렌더링한다. (`v-once` 같은 디렉티브는 예외)

컴포넌트를 사용할 때에는 반드시 `data`는 함수여야하며, 객체를 `return` 해야한다.

#### `methods`

사용할 다양한 함수들을 정의한다. 기본적으로 `data`들을 조작한다.

모든 경우에 자유롭게 사용할 수 있지만, 만약 `methods`에 정의한 함수가 단순히 `data`의 속성을 가공해서 `return`할 것이라면, 아래의 `computed`를 사용하는 것이 좋다.