# Input 태그 input 값 핸들링 하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>My Shopping List</h1>
  Enter a new item: <input id="item-input" type="text">
  <button id="add-button">Add Item</button>
  <ul id="shopping-list">

  </ul>

  <script>
    const input = document.querySelector('#item-input')
    const button = document.querySelector('#add-button')
    const shoppingList = document.querySelector('#shopping-list')
    button.addEventListener('click', e => {
      const itemName = input.value
      input.value = ''
      const item = document.createElement('li')
      item.innerText = itemName
      
      shoppingList.appendChild(item)
    })
  </script>
</body>
</html>
```

* SPA(Single Page Application)



# JavaScript API 사용하기

## Giphy API 사용하기

### main.js

1. input 태그 안의 값을 잡는다

```js
const inputArea = document.querySelector('#js-userinput')
const button = document.querySelector('#js-go')
const resultArea = document.querySelector('#result-area')

button.addEventListener('click', e => {
    searchAndPush(inputArea.value)
})
inputArea.addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        searchAndPush(inputArea.value)
    }
})
```

2. Giphy API를 통해 data를 받아서 가공한다

```js
const searchAndPush = (keyword) => {
    const GiphyAPICall = new XMLHttpRequest()
    const API_KEY = 'OwhnF6eqwLccejIfHAtLj4M7Ld4n1aI4'    
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`
    GiphyAPICall.open('GET', URL) // 어디로 무엇을 보낼지 설정
    GiphyAPICall.send()        
    GiphyAPICall.addEventListener('load', e => {
        const parsedData = JSON.parse(e.target.response)
        const imageURL = parsedData.data
        pushToDOM(imageURL) // addEventListener가 async한 함수기 때문에 pushToDom 함수를 아래에서 정의해도 실행이 된다
    })
    /* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */
    const pushToDOM = data => {
        resultArea.innerHTML = null // HTML Reset
        data.forEach(ele => {
            // resultArea.innerHTML += `<img src="${ele.images.original.url}">`
            let image = document.createElement('img')
            image.src = `${ele.images.original.url}`
            image.className = 'container-image'
            resultArea.appendChild(image)
        })
    }
}
```

# Async

* .js의 파일은 싱글스레드라고 생각하고 작성
* 브라우저란 특성때문에 몇몇 기능이 asynchronous하게 구현됐음
  * javascript는 async한 언어는 아니다
  * javascript의 엔진은 싱글스레드가 아닌 멀티스레드다
* async 안에 async 를 구현하지 않으면 병렬처리로 먼저 끝나는게 나옴
* async 안에 async를 구현하면 stack 구조로 후에 있는게 먼저 끝나야 처음 부른 함수가 실행된다
* 하다가 어떻게 써야할지 헷갈리면 latentflip 에서 실험
  * pythontutor와 비슷한 기능
* async 함수는 이미 정의된 함수. 내가 커스터마이징하거나 만들 수 없다
* 대표적으로 그림이 로드되는 동안 다른 작업을 할 때 async가 사용된다

### SetTimeout

### addEventListener

# 기타

* coursera the bits and bytes of computer networking