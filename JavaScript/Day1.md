# JavaScript

* 객체: 자기 자신이 주어이면서 속성을 가지고 동사 행위(method)를 할 수 있으면 객체
* 클래스 없이 객체를 생성할 수 있는 대표적인 언어
* 브라우저 조작 언어였었음. (Node js가 나오기 전까지)
* 지금은 상용 프로그래밍 언어

## 기원

* ecma script

* ES2015(ES6)

## Vanilla JS

* Vanilla 뜻: 아무것도 없는 것, 즉 기본

## Typescript

* Javascript가 빡빡해진 언어

## 기본 사용법

* let
  * 지역 변수로 선언
  * let은 한 변수에 대해 한번만 사용 가능

```js
let x = 1 // 지역 변수로 설정 let, let 안쓰면 전역 변수
x = 2
console.log(x) // print 기능
```

* 변수의 생존영역은 block scope 기반

```js
x = 2
if (x == 2) {
    let x = 3

    console.log(x)
}

console.log(x)
```

```js
if (x == 2) {
    let x = 3
    let y = 4
    console.log(x)
}

console.log(x)
console.log(y) // error 발생, y는 if block 안에서 선언되었기 때문
```

* 상수 선언

```js
const MY_FAV = 3 // 변하지 않는 값, 후에 다른 값을 할당하면 error

console.log('내가 좋아하는 숫자는' + MY_FAV) // concatenate 가능
console.log(`내가 좋아하는 숫자는 ${MY_FAV}`) // interpolate 가능
```

* var 선언: legacy code에서 주로 볼 수 있음, 현재는 보통 사용하지 않음. 사용하지 않는 걸 추천

```js
var x = 1
```

* javascript에서 비교연산을 할 때는 '==' 보다 '==='을 사용하는게 좋다
  * '===' 은 객체, 값, 주소를 다 비교한다(엄밀하게 다 비교)
* 삼항연산자

```js
// 참/거짓 ? '참입니다' : '거짓입니다'
true ? '참입니다' : '거짓입니다'
false ? '참입니다' : '거짓입니다'
const result = Math.PI > 4 ? '네' : '아니오'
console.log(result)
```

* 입력

```js
prompt('당신의 이름을 입력') // python의 input과 같은 기능
```

* 조건문

```js
// 만약에 이름이 3글자 이상이면
// 이름이 3글자 이상
// 아니면,
// 3글자 이하
if (userName.length >= 3) {
    alert('이름이 3글자 이상입니다.') // alert 경고창 띄움
}
else {
    alert('이름이 3글자 미만입니다.')
}
```

* 반복문

```js
//for (변수 of 컨테이너) {
//    
//}
// 기존 방법
for (let menu of menus) {
  console.log(menu)  
}
for (let i ; i < menus.length ; i++){
    console.log(menus[i])
}
// 일반적 방법
menus.forEach(function(menu) {
	console.log(menu)         
})
// 가장 모던한 방법
menus.forEach(menu => {
    console.log(menu)
})
```

* 함수

```js
//function 함수명(인자) {
//    내용
//    return
//}
// 함수 표현식
// 방법 1
function add(num1, num2) {
    return num1 + num2
}
// 방법 2, 주로 방법 2를 사용한다. js에서 방법 1을 사용하면 귀찮은 상황이 많이 발생하므로
const sub = function (num1, num2) {
    return num1 - num2
}
// 방법 3, 가장 모던한 방법 (arrow function. ES6)
const mul = (x, y) => {
    return x * y
}
const ssafy = function (name) {
    return `안녕, ${name}`
}
// 함수의 인자(매개변수)가 한 개라면 괄호, 블락, return을 생략가능하다
// 블락을 없애는 조건은 표현식이 하나만 있을 경우
const ssafy1 = name => `안녕, ${name}`
const ssafy1 = () => {} // 인자가 없을 경우
const square = num => num ** 2
square(2)
```

* array

```js
const nums = [1, 2, 3, 4]
console.log(nums[0])
console.log(nums[nums.length - 1])

console.log(nums.reverse()) // 원본이 바뀌니 주의
console.log(nums)

nums.push(0) // python .append
console.log(nums)
nums.pop() // python .pop
console.log(nums)

// unshift, shift, includes, indexOf
nums.unshift(5) // 맨 앞에 인자 넣어줌
console.log(nums)
nums.shift() // 맨 앞 인자 빼줌
console.log(nums) 

console.log(nums.includes(0)) // python in 연산자 기능
console.log(nums.includes(4))

console.log(nums.indexOf(3)) // 해당 원소의 인덱스 return
```

```js
// 반복문
// map(함수, 리스트(iterable)) python
// iterable.map(함수) python
// nums.forEach(함수)
// nums 배열을 순회하며, 함수를 각각의 요소에 실행
// nums 안의 요소 각각을 제곱하시오
nums.forEach(function(num) {
    console.log(num ** 2)
})

let newNums = []
nums.forEach(function(num) {
    newNums.push(num ** 2)
})
console.log(newNums)

const squaredNums = nums.map(function(num) {
    return num ** 2
})
const squaredNums = nums.map(num => num ** 2)
console.log(squaredNums)
```

* object

```js
const me = {
    name: 'john',
    sleep: function() {
        console.log('쿨쿨')
    },
    appleProducts: {
        macBook: '2018Pro',
        iPad: '2018Pro',
    },
}

console.log(me.name)
console.log(me['name'])
// console.log(me[name]) 은 작동 X
console.log(me.sleep)
console.log(me.sleep())

console.log(me.appleProducts.macBook)
```

```js
// JSON(Javascript Object Notation)
const data = {
    name: 'john',
    appleProducts: {
        macBook: '2018Pro',
        iPad: '2018Pro',
    },
}

// object to JSON(string)
const meJSON = JSON.stringify(data)
console.log(typeof meJSON)
// write file
fs.writeFile('me.json', meJSON, err => {}) // 비동기

fs.writeFileSync('me2.json', meJSON) // 동기

// JSON to object
const meObject = JSON.parse(meJSON)
console.log(meObject)
console.log(meJSON)
```

### 저장

> 무엇을 | 어디에 | 어떻게(=) 저장하는지

#### 무엇을(자료형, Data Type)

* Primitive Types(원시자료형)
  1. 숫자: 아무숫자, (-)Infinity, NaN
  2. 글자: ' ', " ", ``
  3. 불리언: true, false
  4. Empty Value: undefined(default), null

#### 어디에(identifier 변수명, Container Type)

- 상수명 : ALLCAP

- 변수명, 함수명 : camelCase

- 클래스 : PascalCase

## 설치

* 브라우저가 아닌 밖에서 사용하기 위해 nodejs 설치
* git bash에서 `node --version`으로 설치 확인
* 파일 실행은 `node [file_name.js]`

## 브라우저

### Dino 뛰어놀게 만들기

```js
const dino = document.querySelector('#dino')

dino.addEventListener('click', event => {
    alert('아야')
    console.log(event)
})

let x = 0
let y = 0

document.addEventListener('keydown', e => {
    // console.log(e.keyCode)
    if (e.keyCode === 37) {
        console.log('왼쪽으로 이동')
        x -= 40
        dino.style.marginLeft = `${x}px`
    } else if (e.keyCode === 38) {
        console.log('위로 이동')
        y -= 40
        dino.style.marginTop = `${y}px`
    } else if (e.keyCode === 39) {
        console.log('오른쪽으로 이동')
        x += 40
        dino.style.marginLeft = `${x}px`
    } else if (e.keyCode === 40) {
        console.log('아래로 이동')
        y += 40
        dino.style.marginTop = `${y}px`
    } else {
        alert('잘못된 키를 눌렀어요. 방향키를 눌러주세요.')
    }
})
```



# 프로그래밍 언어를 보는 법

1. 저장과 조작 방법

2. 다른 언어와의 문법적 차이

3. 언어의 관례

4. 바로 구현

   1. 기존 언어에서 할 수 있었던 걸 새로 배우는 언어로 옮기는 작업

   