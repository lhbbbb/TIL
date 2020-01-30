# React 공식 문서 정리

이 글은 [리액트공식문서](https://ko.reactjs.org/docs/hello-world.html)를 정리했음을 밝힙니다.

나중에 복기할 목적으로 세부사항은 적지 않고 키워드 위주로 정리하도록 한다.

## 1. JSX 소개

> JSX는 JavaScript를 확장한 문법이다. JSX는 React 엘리먼트를 생성한다.

### JSX란?

JavaScript 코드 안에서 UI 코드 관련 작업을 할 때 시각적으로 도움을 준다. 또한 React가 도움이 되는 에러 및 경고 메시지를 표시할 수 있게 해준다.

### JSX에 표현식 포함하기

JSX의 중괄호 안에는 유효한 모든 `JavaScript 표현식`을  넣을 수 있다.

### JSX도 표현식

JSX를 `if` 구문 및 `for` loop 안에 사용하고, 변수에 할당하고, 인자로서 받아들이고, 함수로부터 반환할 수 있다.

### JSX 속성 정의

중괄호를 사용하여 어트리뷰트에 JavaScript 표현식을 삽입할 수 있다. 이 때 따옴표 또는 중괄호 중 하나만을 사용한다.

```react
const element = <div tabIndex="0"></div>; // 따옴표
const element = <img src={user.avatarUrl}></img>; // 중괄호
```

JSX는 camelCase 프로퍼티 명명 규칙을 사용한다.

### JSX는 주입 공격을 방지 -----???

JSX에 사용자 입력을 삽입하는 것은 안전하다. 기본적으로 React DOM은 JSX에 삽입된 모든 값을 렌더링하기 전에 `이스케이프` 하므로, 애플리케이션에 명시적으로 작성되지 않은 내용은 주입되지 않는다. 모든 항목은 렌더링 되기 전에 문자열로 변환된다. 이른 특성으로 인해 `XSS(cross-site-scripting)` 공격을 방지할 수 있다.

### JSX는 객체를 표현

Babel은 JSX를 `React.createElement()` 호출로 컴파일한다. 즉, 버그가 없는 코드를 작성하는데 도움이 되도록 몇 가지 검사를 수행하며, `React 엘리먼트` 라고 불리는 객체를 생성한다. 이는 곧 화면에 표시하려는 항목에 대한 설명이라고 생각할 수 있다.

## 2. 엘리먼트 렌더링

> 엘리먼트는 React 앱의 가장 작은 단위이다.

### DOM에 엘리먼트 렌더링하기

React 엘리먼트를 루트 DOM 노드에 렌더링하려면 둘 다 `ReactDOM.render()` 로 전달하면 된다.

```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

### 렌더링 된 엘리먼트 업데이트하기

React 엘리먼트는 **불변객체**이다. 따라서 영화에서의 하나의 프레임과 같이 특정 시점의 UI를 보여준다. 따라서 업데이트를 하기 위해선 새로운 엘리먼트를 생성하고 이를 `ReactDOM.render()` 로 전달해야한다.

### 변경된 부분만 업데이트하기

React DOM은 해당 엘리먼트와 그 자식 엘리먼트를 이전의 엘리먼트와 비교하고 DOM을 원하는 상태로 만드는데 **필요한 경우에만 DOM을 업데이트**한다.

## 3. Components와 Props

> 개념적으로 컴포넌트는 JavaScript 함수와 유사하다. "props" 라고 하는 임의의 입력을 받은 후, 화면에 어떻게 표시되는지를 기술하는 React 엘리먼트를 반환한다.

### 함수 컴포넌트와 클래스 컴포넌트

```react
// 함수
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
// 클래스
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

### 컴포넌트 렌더링

React 엘리먼트는 DOM 태그 뿐만 아니라, 사용자 정의 컴포넌트로도 나타낼 수 있다. React가 사용자 정의 컴포넌트로 작성한 엘리먼트를 발견하면 JSX 어트리뷰트를 해당 컴포넌트에 단일 객체로 전달한다. 이 객체를 `props` 라고 한다.

컴포넌트의 이름은 **항상 대문자로 시작**해야하는 규칙이 있음을 명심하자.

### 컴포넌트 합성

컴포넌트는 자신의 출력에 다른 컴포넌트를 참조할 수 있다. 기존 앱에 React를 통합하는 경우에는 작은 컴포넌트부터 시작해서 뷰 계층의 상단으로 올라가며 점진적으로 작업해야 할 수 있다.

### 컴포넌트 추출

컴포넌트를 여러 개의 작은 컴포넌트로 나누는 것을 두려워하지 말라.

컴포넌트의 구성요소들이 중첩 구조를 이루면 변경하기가 어려울 수 있고, 각 구성요소를 개별적으로 재사용하기도 힘들다. 따라서 여러 개의 작은 컴포넌트로 쪼개 단순화하는 것이 좋다.

### props는 읽기 전용이다.

함수 컴포넌트나 클래스 컴포넌트 모두 컴포넌트의 자체 props를 수정해서는 안된다.

React는 매우 유연하지만 한 가지 엄격한 규칙이 있다.

> 모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야 한다.

