# Web Service 제작 방법

예를 들어 카페 창업이라고 생각해보자.

* 기초부터 하나하나 직접 만드는 방법
  * 인테리어부터 어떤 원두를 사용할 것인지, 어떤 커피머신을 사용할 것인지
* 프랜차이즈를 활용하는 방법
  * 프랜차이즈를 통한 창업은 본사에서 알려주는 매뉴얼만 잘 숙지하면 큰 무리없이 운영할 수 있다

위에서 언급한 예 중 프랜차이즈를 활용하는 방법이  framework를 활용하는 방법과 비슷하다고 볼 수 있다.

---



# Django framework

## 성격

### framework 성격

* framework들은 보통 두 가지의 성격으로 나뉜다. 그 두가지 성격 중 django는 다소 독선적(opinionated)인 성격이라고 할 수 있다.

1. **opinionated**

   * framework가 정한 규칙이 많음
   * 규칙이 많으므로 당연히 초반에 learning curve가 크다

2. unopinionated

   * 기능들이 잘 모듈화되어있지 않다

   * 코드의 유지보수가 힘듬

### web 성격

1. Static Web
2. **Dynamic Web**
   * django

django는 dynamic web이다.

## 개발 방식

### MTV 패턴

* 원래 일반적으로 사용하는 용어는 MVC 패턴이지만 django에서는 MTV라고 부른다
* model, template, view 중에서 view(중간관리자)의 역할이 가장 중요하다

#### Architecture

<img src="https://t1.daumcdn.net/cfile/tistory/991AD1365B448DA702">

#### Model

* 데이터를 관리한다

#### Template

* 사용자가 보는 화면을 구성한다

#### View

* Model과 Template을 이어주는 중간 관리자 역할을 수행한다



## Django 사용하기

### Install

* `pip install django`

### Set default environment

#### 1) Git bash

1. 만들고자 하는 project_name을 대문자로 하는 폴더 생성

2. `django-admin startproject project_name .`
* 대문자로 한 폴더로 들어가서 명령어 실행(django의 convention)
   * ex) project_name = first_app 이면 FIRST_APP 폴더 만들고 그 안에서 명령어 실행
* 다른 방식 `django-admin startproject project_name PROJECT_NAME/`
  
3.  `python manage.py runserver`
* 웹 서버 실행
   * 명령어가 너무 길면 `~` 경로에서 VSCode 실행 후 `.bashrc` 파일의 alias를 추가해주자
   
4. `python manage.py startapp app_name`
   * django에서 자체적으로 생성해준 기본 파일이 담긴 폴더를 app_name 명으로 만든다

#### 2) VSCode

1. F1 누르고 python interpreter 선택 후 가상환경으로 만들어준 python 선택

#### 3) Django

1. 프로젝트의 settings.py 에서 다음과 같이 설정

   ```python
   #settings.py
   INSTALLED_APPS = [
       'pages', # pages(app_name) // git bash에서 startapp 명령어로 만든 앱 이름
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

2.  프로젝트의 ulrs.py 에서 다음과 같이 설정

   ```python
   from pages import views # 내가 만든 app(pages)에서 views 모듈 import 해줘야함
   urlpatterns = [
       # path()
       # 첫번째 인자 : 주문서(url 경로)
       # 두번째 인자 : view 함수의 위치
       path('admin/', admin.site.urls),
       path('PageName/', views.FunctionName),
       path('PageName/<variable>/', views.FunctionName),
   ]
   ```



### Important File

1. settings.py
2. urls.py: view로 가는 문지기 역할 수행
3. manage.py: 서버 돌릴때 쓰는 파일



### 문법

#### 1) 규칙

##### 트레일링 콤마

자료 넣을 때, `,`를 마지막에 같이 입력해주는 걸 트레일링 콤마라고 한다.

```python
[1,2,3] # non 트레일링 콤마
[
    1,
    2,
    3, # 자료가 끝나는 지점에도 ,를 붙여준다
] # 트레일링 콤마
```

##### request

app의 views.py 에서 함수 작성시 request 인자를 꼭 넣어줘야한다.

```python
# Create your views here.
def index(request): #request 인자 넣어줘야함
    return render(request, 'index.html')
```

##### 데이터 인자 전달 방법

flask랑 다르게 데이터 인자를 dictionary 형태로 넣어준다.

```python
def home(request):
    name = 'Lee'
    data = ['Lee', 'Kim', 'Kang']
    return render(request, 'home.html', {'data':data, 'name':name})
```

### 상속

#### 1) Template Inheritance

1. 공통적으로 사용할 템플릿(코드)를 뽑아낸다
2. 해당 파일을 따로 만들고,
3. 활용할 다른 템플릿 파일에서 불러와 사용한다

#### 2) Django에서 template 파일 찾는 순서

1. 본인 앱(폴더)에 있는 templates 폴더에서 먼저 찾는다
2. 없으면 다른 app에 있는 templates 폴더를 찾는다
3. 이 설정을 바꾸려면 기본 앱(프로젝트와 이름이 같은 폴더)의 settings.py에 있는 TEMPLATES 변수에 내용을 추가해줘야 한다

#### 3) 공통 Template 만들기

앱과 그 앱에 해당하는 template의 갯수가 많아지다보면 html 문서를 만들때마다 같은 행위를 반복하는 쓸데없는 작업이 많아지게 된다. 따라서 공통되는 양식을 가진 template을 만들고 그 template을 상속하게 되면 불필요한 작업을 줄일 수 있다.

* 기본 앱(프로젝트와 이름이 같은 폴더)에 있는 settings.py의 BASE_DIR 변수에 현재 working directory 경로가 저장되어 있다
* os.path.join() 함수를 사용하여 경로를 지정
* 경로를 지정하게 되면 어느 폴더에 있어도 다 찾아갈 수 있지만, 관례상 기본 앱에 templates 폴더를 만들어 공통 html 파일을 넣는다

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'default_app','templates'),], # DIRS 항목에 내용 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### 4) Template Inheritance Grammar

1. partial view

   * _nav.html: 파일명 앞에 _를 붙인다

2. partial rendering(부분적 상속)

   * ```html
     {% include '_nav.html' %}
     ```

3. 사용 방법

   * ```html
     <!-- base.html(공통영역) -->
     <!DOCTYPE html> 
     <html lang="en">
     <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
     </head>
     <body>
       {% block body %} <!-- 구멍을 뚫을 부분(코드를 넣을 부분) -->
       {% endblock %}
     </body>
     </html>
     ```

   * ```html
     <!-- index.html -->
     {% extends 'base.html' %} <!-- base.html 상속 선언 // 상속 선언문은 닫아줄 필요 없음-->
     
     {% block body %} <!-- 구멍에 넣을 부분(contents 넣으면 됨) -->
     <h1>DTL(Django Template Language) 관련 문법</h1>
     <ul>
       <li>for</li>
       <li>if</li>
       <li>helper/filter</li>
       <li></li>
     </ul>
     
     {% endblock %} <!-- 구멍 닫기 -->
     ```

### Url

#### 1) 부하 url 만들기

* 기본 앱의 urls.py에서 부하 url 경로를 추가해준다

  ```python
  # urls.py
  from django.contrib import admin
  from django.urls import path, include # include 함수 추가해줘야함
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('num/', include('num.urls')), # num앱을 관리해주는 부하 url 만들기
  ]
  ```

#### 2) 부하 url settings

```python
from django.urls import path
from . import views # . 은 현재 폴더를 의미

urlpatterns = [
    path('', views.num), # ''는 현재 root 경로를 의미. 여기선 num
    path('push/', views.push),
    path('pull/', views.pull),
]
```

#### 3) Redirect

```python
# 기본 앱의 urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('', views.index, name='index'), # redirect하기 위해 별칭 'index'로 설정
]
```

```python
# views.py
from django.shortcuts import render, redirect

def create(request):
    return redirect('index') # 기본 앱의 urls.py에서 root경로 별칭 index로 해줌
```

---



# Tip

- VSCode에서 ctrl + p치고 찾고 싶은 파일명 대충 입력하면 쉽게 찾을 수 있다