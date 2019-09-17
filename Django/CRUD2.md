# CRUD2

## 댓글달기

## 이미지 파일 넣기

### 파이썬에서의 이미지 처리

-  Pillow: 파이썬에서의 이미지를 처리하고 핸들링하기 위해서 설치하는 패키지

- `pip install Pillow`

- form 태그 `enctype` 속성: 파일 형태로 값이 전달된다는 걸 알려주는 역할

```html
<form action="{% url 'posts:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="form-group">
      <label for="">image</label><br>
      <!-- type=file 인풋값으로 파일을 받음, accept="image/*" 이미지 파일만 받음 -->
      <input class="form-control" type="file" name="image" accept="image/*">
    </div>
    <button type="submit" class="btn btn-primary">전송</button>
  </form>
```

### 이미지 저장하기

1. 저장되는 위치 지정

   - settings.py

   ```python
   # 1. 실제 파일 저장소의 경로를 지정 (절대경로)
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   # 2. 업로드된 파일의 주소(URL)를 만들어줌, default:''
   MEDIA_URL = '/media/'
   ```

   - urls.py

   ```python
   from django.conf.urls.static import static
   from django.conf import settings # settings.py에 있는 거 사용 가능
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('posts/', include('posts.urls')),
   ]
   
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

2. 경로 DB에 넣어주기

   ```python
   {% if post.image %}
    <img src="{{ post.image.url }}" alt="{{ post.image }}">
   {% else %}
    <img src="/media/noimage.jpg" alt="no_image">
   {% endif %}
   ```

## 파비콘 넣기

### 파비콘 생성

* favicon generator 구글에 검색

### static URL  설정

* 기본 앱의 settings.py
* STATIC_URL 변수와 관련 있음
* 기본 앱 하위에 assets 폴더 생성
* 변수 설정

```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'board', 'assets')]
```

### Template

* 기본 앱의 base.html
* {% load static %} 필수

```html
<!-- base.html -->
{% load static %}
<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <!-- Favicon -->
  <link rel="icon" type="image/png" sizes="16x16" href="{% static 'images/favicon-16x16.png' %}">
  <title>게시판</title>
</head>
```

