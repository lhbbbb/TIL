# Async

## What

* setTimeout
* addEventListener
* readFile

```js
const fs = require('fs')

console.log('파일 읽기 전')

fs.readFile('me2.json', () => {
    console.log('파일 읽기')
})

console.log('파일 읽기 끝')

//result
//파일 읽기 전
//파일 읽기 끝
//파일 읽기
```

```js
const fs = require('fs')

let content = ''

console.log('파일 읽기 전')

fs.readFile('me2.json', (err, data) => {
    setTimeout(() => {
        console.log(JSON.parse(data))
    }, 10000)
    
})
console.log(content)
console.log('파일 읽기 끝')
```

```js
// sync version
let content = ''
console.log('파일 읽기 전')
content = fs.readFileSync('me2.json')
console.log('읽기종료')
console.log(JSON.parse(content))
console.log('끝')
```

* axios // promise

```js
const result = axios.get(URL)
// Promise 객체(resolved)

// Promise 객체를 까보기 위해서 .then()
result.then((res) => {
    console.log(res.data.message)
})
```



## Why

## How

1. callback
2. **promise**
3. asyncawait



# Axios

## 개

* dogceo 사이트 활용

```js
const dogBtn = document.querySelector('#dog')
const URL = 'https://dog.ceo/api/breeds/image/random'
const getDogAndPush = () => {
    //뭐할지
    // 1. axios -> dog 사진 요청
    // 2. <body> 아래에 <img> 받아온 사진 보여주기
    axios.get(URL)
        .then(response => {
            const imgURL = response.data.message
            const imgTag = document.createElement('img')
            imgTag.src = imgURL
            document.querySelector('body').appendChild(imgTag)
        })
}
dogBtn.addEventListener('click', getDogAndPush)
```

## 고양이

* catapi 사이트 활용

```js
const catBtn = document.querySelector('#cat')
const catURL = "https://api.thecatapi.com/v1/images/search"
const getCatAndPush = () => {
    axios.get(catURL)
            .then(response => {
                const imgURL = response.data[0].url
                const imgTag = document.createElement('img')
                imgTag.src = imgURL
                document.querySelector('#showroom').appendChild(imgTag)
            })
}
catBtn.addEventListener('click', getCatAndPush)
```



# 좋아요 기능 구현

* addeventlistener는 function 정의할 때 arrow function을 쓰지 않고 원래 정의 방법을 사용한다

* axios cdn base.html의 가장 상단, `<title> `아래에 넣기
* detail.html

```html
  </p>
    <button data-id="{{ article.pk }}" class="btn btn-primary" id='like-button'>좋아요</button>
  {% endwith %}
  <h2>댓글목록</h2>
  {% for comment in comments %}
    <p>{{ comment.content }} {{ comment.user.first_name }}</p>
  {% endfor %}
<script>
  // 좋아요 버튼을 클릭하면, 좋아요 DB를 업데이트하고, 버튼을 변경. (addEventListener를 통해 가능)
  const likeBtn = document.querySelector('#like-button')
  likeBtn.addEventListener('click', function (e) {
    // 좋아요 DB를 업데이트 == articles/:id/like 요청을 보냄
    const articleId = e.target.dataset.id
    axios.get(`/articles/${articleId}/like/`)
      .then(response => {
        if (response.data.liked) {
          e.target.classList.remove('btn-primary')
          e.target.classList.add('btn-outline-primary')
          e.target.innerText = '좋아요 취소'
        } else {
          e.target.classList.remove('btn-outline-primary')
          e.target.classList.add('btn-primary')
          e.target.innerText = '좋아요'
        }
        document.querySelector('#like-count').innerText = response.data.count
        const likers = document.querySelector('#likers')
        const like_users = response.data.like_users
        likers.innerText = ''
        like_users.forEach(liker => {
          let person = document.createElement('span')
          person.innerText = liker.username
          likers.appendChild(person)
        })
      })
  })
</script>
```

* `data-[key_name]` property

  *  addEventListener를 사용할 때 데이터를 쉽게 넘길 수 있도록 제공해주는 기능

  ```html
  <button data-id="{{ article.pk }}" id='like-button'>좋아요</button>
  ```

  * ex) data-id, data-name, data-ssafy, data-anything 등 의 이름 가능. key_name이 키가 된다.

* views.py

```python
from django.http import JsonResponse
def like(request, article_pk):
    # article_pk로 넘어온 글에 현재 접속중인 유저를 추가한다.
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    # 만약 좋아요 리스트에 현재 접속중인 유저가 있다면,
    # -> 해당 유저는 좋아요를 했다
    if article.like_users.filter(pk=user.pk).exists():
        # 그렇지 않으면,
        # -> 해당 유저는 아직 좋아요를 하지 않았다
        article.like_users.remove(user)
        liked = False
    else:
        # request.user.like_articles.add(article)
        article.like_users.add(user)
        liked = True
    like_users = list(article.like_users.all().values())
    context = {
        'liked': liked,
        'count': article.like_users.count(),
        'like_users': like_users
    }
    return JsonResponse(context)
```



# 기타

* beautifier javascript 검색해서 사용하면 깔끔하게 정리 가능