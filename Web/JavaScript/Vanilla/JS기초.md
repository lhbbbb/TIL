# Vanilla Js

- vanilla의 뜻은 우리가 흔히 아는 바닐라 향 말고도 평범한, 기본적인(ordinary)이라는 뜻도 가지고 있다.

## Vanilla JS 프로젝트의 장단점

### 장점

- 순수한 JS로 구성할 수 있어 단순한 구조로 진행 가능
- JS 이외의 별도의 학습이 불필요
- 라이브러리나 프레임워크를 사용하지 않아 가벼운 스크립트로 구성 가능
- 별도의 기반 기술이 업데이트되는 데에 영향을 받지 않음

### 단점

- 필요한 기능에 대해 자체 개발이 필요, 그에 따른 작업 일정 필요
- 지원 브라우저에 대한 이슈를 자체적으로 해결하는 것이 필요
- 개발자의 개발 수준에 따른 코드 품질 차이가 발생
- 라이브러리나 프레임워크와 비교해서 같은 일정에 같은 코드 품질이 나오기 어려움
- 높은 수준의 결과물을 위해서는 더 많은 개발 일정이 필요

##  기본문법

### var, let

var과 let의 차이점은 변수 범위 스코프와 호이스팅 여부로 말할 수 있다. 

ECMAScript 6 이전의 JavaScript는 [block 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#Block_문) 범위가 없다. 그래서 오히려, 블록 내에 선언된 변수는 그 블록 내에 존재하는 *함수(혹은 전역 범위)*에 지역적이다. 예를 들어서 아래의 코드는 5라는 로그를 남긴다. `x`의 범위가 이 경우 `if`문 블록이 아니라 x가 선언된 함수(나 전역 문맥)이기 때문이다.

```js
if (true) {
  var x = 5;
}
console.log(x); // 5
```

ECMAScript 6에 도입된 `let` 선언을 사용했을 때, 이 동작은 다음과 같이 바뀌었다.

```js
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```

JavaScript 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 것이다. 이 개념은 변수 호이스팅으로 알려져 있다. 즉 JavaScript 변수가 "끌어올려지거나" 함수나 문의 최상단으로 올려지는 것을 말한다. 하지만, 끌어올려진 변수는 `undefined` 값을 반환한다.

다음 예시로 간단하게 이해해보자.

```javascript
/**
 * Example 1
 */
console.log(x === undefined); // logs "true"
var x = 3;


/**
 * Example 2
 */
// undefined 값을 반환함.
var myvar = "my value";

(function() {
  console.log(myvar); // undefined
  var myvar = "local value";
})();
```



### const

[`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 키워드로 읽기 전용 상수를 만들 수 있다.  문자, 밑줄이나 달러 기호로 시작해야 하고 문자, 숫자나 밑줄을 포함할 수 있다.

```js
const PI = 3.14;
```

상수는 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나 재선언될 수 없다. 값으로 초기화해야 한다.

상수에 대한 범위 규칙은 `let` 블록 범위 변수와 동일하다. 만약 `const` 키워드가 생략된 경우에는, 식별자는 변수를 나타내는 것으로 간주된다.

상수는 같은 범위에 있는 함수나 변수와 동일한 이름으로 선언할 수 없다. 예를 들어,

```js
// 오류가 발생합니다
function f() {};
const f = 5;

// 역시 오류가 발생합니다
function f() {
  const g = 5;
  var g;

  //statements
}
```

그러나, 상수에 할당된 객체의 속성은 보호되지 않아서 다음의 문은 문제없이 실행된다.

```js
const MY_OBJECT = {'key': 'value'};
MY_OBJECT.key = 'otherValue';
```

또한, 배열의 내용도 보호되지 않아서 다음의 문도 문제없이 실행된다.

```js
const MY_ARRAY = ['HTML','CSS'];
MY_ARRAY.push('JAVASCRIPT');
console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
```



