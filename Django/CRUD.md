# CRUD

### 프로젝트 진행 순서

1. model
2. workflow
   * url
   * view
   * template

[CRUD 관련 프로젝트](https://lab.ssafy.com/lhbbbb/projects_05)

### 게시판 만들기

CRUD 방식으로 진행

#### 1) Create

1. model 만들기(DB table)

   ```python
   # models.py
   from django.db import models
   
   # Create your models here.
   class Post(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       image_url = models.CharField(max_length=300)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       # 작성자,태그,조회수,추천,좋아요,댓글 추후 작성
   ```

2. Django ORM으로 migration 수행

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. 각 필드에 해당하는 데이터를 넣기 위한 페이지 작성

   ```html
   <!-- new.html -->
     <form action="{% url 'posts:create' %}"> <!-- DTL 문법 urls.py에서 별칭이 create인 곳 -->
       <div class="form-group">
         <label for="title">제목</label>
         <input type="text" class="form-control" id="title" name="title" placeholder="제목을 입력해주세요">
         <label for="content">내용</label>
         <textarea class="form-control" name="content" id="content" cols="30" rows="10"></textarea>
         <label for="img-url">이미지 URL</label>
         <input type="text" class="form-control" name="img_url" id="img_url" placeholder="사진 URL을 넣어주세요">
       </div>
       <button type="submit" class="btn btn-primary">글쓰기</button>
     </form>
   ```

   * POST 방식

   ```html
   <!-- new.html -->
     <form action="{% url 'posts:create' %}" method="POST"> <!-- DTL 문법 urls.py에서 별칭이 create인 곳 -->
       {% csrf_token %} <!-- POST 방식일 때 써줘야함-->
       <div class="form-group">
         <label for="title">제목</label>
         <input type="text" class="form-control" id="title" name="title" placeholder="제목을 입력해주세요">
         <label for="content">내용</label>
         <textarea class="form-control" name="content" id="content" cols="30" rows="10"></textarea>
         <label for="img-url">이미지 URL</label>
         <input type="text" class="form-control" name="img_url" id="img_url" placeholder="사진 URL을 넣어주세요">
       </div>
       <button type="submit" class="btn btn-primary">글쓰기</button>
     </form>
   ```

   

4. urls 문지기에서 중간관리자인 view 로 보내주기

   ```python
   # urls.py
   from django.urls import path
   from . import views
   
   app_name = 'posts' # 이 앱의 별칭 설정
   
   urlpatterns = [
       path('new/', views.new, name='new'), # app_name을 설정해줬기 때문에 실질적으론 name=post_new의 느낌
       path('create/', views.create, name='create'),
   ]
   ```

5. view에서 입력한 정보 DB에 저장

   ```python
   # views.py
   def create(request):
       # new에서 날아온 데이터로 DB에 저장한다
       context = {
           'title': request.GET.get('title'),
           'content': request.GET.get('content'),
           'image_url': request.GET.get('img_url'),
       }
       
       Post(**context).save() # 유효성 검사
       # Post.objects.create(**context) # 유효성 검사 안함. 기능은 save랑 같음
       return redirect('home') # home 별칭 가진 곳의 url로 이동
   ```

#### 2) Read

1. DB에 저장한 정보 불러오기

   ```python
   def index(request):
       # table 형태로 게시판을 보여줌
       context = {
           'posts': Post.objects.all() # DB에 있는 모든 데이터 불러옴
       }
       return render(request, 'posts/index.html', context)
   ```

2. 불러온 정보를 이용한 페이지 작성

   ```html
   {% for ele in posts %}
   <tr>
       <th scope="row">{{ ele.id }}</th>
       <td><a href="/posts/{{ ele.id }}/">{{ ele.title }}</a></td>
       <td>{{ ele.created_at }}</td>
       <td>{{ ele.updated_at }}</td>
   </tr>
   {% endfor %}
   ```

#### 3) Update

1. url, view 설정하기

   ```python
   # urls.py
   from django.urls import path
   from . import views
   
   app_name = 'posts' 
   
   urlpatterns = [
       path('new/', views.new, name='new'), # app_name을 설정해줬기 때문에 실질적으론 name=post_new
       path('create/', views.create, name='create'),
       path('<int:pk>/', views.detail, name='detail'),
       path('<int:pk>/edit/', views.edit, name="edit"),
   ]
   ```

   ```python
   # views.py
   def edit(request, pk):
       # pk라는 id를 가진 글을 편집하게 함
       post = Post.objects.get(pk=pk)
       context = {
           'post': post,
       } # 기존에 작성한 내용
       return render(request, 'posts/edit.html', context)
   ```

2. 게시글 수정하기

   ```html
   <div class="container">
     <h1>수정</h1>
   
     <form action="{% url 'posts:update' post.id %}">
     <!-- <form action="/posts/{{ post.id }}/update/"> -->
       <div class="form-group">
         <label for="title">제목</label>
         <input type="text" class="form-control" id="title" name="title" value="{{ post.title }}" placeholder="제목을 입력해주세요">
           <!-- input의 value속성에 기존에 작성한 내용 입력-->
         <label for="content">내용</label>
         <textarea class="form-control" name="content" id="content" cols="30" rows="10">{{ post.content }}</textarea>
         <label for="img-url">이미지 URL</label>
         <input type="text" value="{{ post.image_url }}"class="form-control" name="img_url" id="img_url" placeholder="사진 URL을 넣어주세요">
       </div>
       <button type="submit" class="btn btn-primary">수정하기</button>
     </form>
   </div>
   ```

3. 수정한 내용  DB에 적용하기

   ```python
   # views.py
   def update(request, pk):
       # 1. pk라는 id를 가진 글을 찾아서,
       post = Post.objects.get(pk=pk)
       # 2. /edit/으로부터 날아온 데이터를 적용하여 변경함
       post.title = request.GET.get('title')
       post.content = request.GET.get('content')
       post.image_url = request.GET.get('img_url')
       post.save()
   
       return redirect('posts:detail', pk) # 별칭 사용하기
       # return redirect(f'/posts/{pk}/')
   ```

#### 4) Delete

1. 수정, 삭제 페이지 작성

   ```html
   <div class="container">
     <a href="/posts/{{ post.id }}/edit/" class="btn btn-success">수정</a>
     <a href="/posts/{{ post.id }}/delete/" class="btn btn-danger">삭제</a>
     <h1>{{ post.title }}</h1>
     <p>{{ post.content }}</p>
     <img src="{{ post.image_url }}" alt="">
     <p>{{ post.created_at }}</p>
     <p>{{ post.updated_at }}</p>
   </div>
   ```

2. DB에서 데이터 삭제

   ```python
   # views.py
   def delete(request, pk):
       post = Post.objects.get(pk=pk) # id=pk에 해당하는 데이터 찾기
       post.delete() # 삭제, 단 여기서 id는 초기화되지 않고 그대로 유지된다.
   
       return redirect('home')
   ```

### 기타

#### redirect시 이름 설정

```python
# urls.py
from django.urls import path
from . import views

app_name = 'posts' # 공통적으로 붙는 name 설정

urlpatterns = [
    path('new/', views.new, name='new'),
    # app_name을 설정해줬기 때문에 실질적으론 name='posts_new'의 느낌
]
```

* 데이터베이스는 데이터를 지워도 id는 그대로 보존된다.

#### url 별명 받기

```html
<a class="nav-link" href="{% url 'posts:new' %}">새글쓰기</a>
<!-- urls.py에서 app_name=posts, path에서 별명을 new로 해줬기때문 -->
```

#### 제목에 링크달기

1. ```html
   <td><a href="/posts/{{ ele.id }}/">{{ ele.title }}</a></td>
   ```

2. ```python
   # urls.py
   urlpatterns = [
       path('<int:pk>/', views.detail, name='detail'), 
       # 가변인자기 때문에 <> // int형 변수 pk
   ]
   ```

3. ```python
   def detail(request, pk):
       # pk라는 id를 가진 글을 찾아와 보여줌
       post = Post.objects.get(pk=pk) # DB에 있는 데이터 중 id(pk)==pk에 해당하는 정보 가져오기
       context = {
           'post': post,
       }
   
       return render(request, 'posts/detail.html', context)
   ```



## Tip

* django model field 검색

* django orm delete 검색