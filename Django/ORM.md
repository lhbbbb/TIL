# Django ORM

## Database

- SqlLite
  - 경량화 DB, 핸드폰에서 주로 사용함

### SQL

RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

### ORM -- 면접 질문에 자주 나옴

- Object-Relation Mapping
- 데이터베이스와 파이썬과의 통역을 해주는 하나의 프로그램
- 파이썬 코드를 최적화된 sql 구문으로 만들어줘서 속도가 빠름

#### DjangoORM

------



## 봐야할 파일

- app의 models.py
- 기본 app의 settings.py의 DATABASES 변수와 연관되어 있음

## 사용방법

### Django

#### migration

- app의 models.py 에서 클래스 정의(DB의 table 정의라고 생각하면 된다)

```python
# articles app(내가 만든 app)
from django.db import models

# Create your models here.
class Article(models.Model):
    # column 설정
    title = models.TextField() 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### git bash

1. `python manage.py makemigrations`
2. `python manage.py migrate`

#### column 추가하기

1. models.py에서 필드 추가해주고

   ```python
   # Create your models here.
   class Article(models.Model):
       # column 설정
       title = models.TextField() 
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       image_url = models.TextField()
   ```

2. git bash에서 `python manage.py makemigrations`

3. 다음 화면 뜨면

![1566192812162](assets\orm_migrate.png)

​	1번 // 필드 추가하고 빈값은 널값으로 채우겠다

​	`''` 입력

### VSCode

- extension에서 sqlite install
- f1 sqlite => open database

### 대화식 python shell

Django에서 사용 가능한 모듈 및 메서드를 python shell에서 사용 가능

git bash 창에서 커맨드 입력

1. `python manage.py shell` 입력
2. `from articles.models import Article`
3. `Article.objects.all()`
4. `article = Article(title="",content="")` // 키워드 인자로
5. `article.save()` // DB에 저장

#### shell 환경에서 해보기

```python
INSTALLED_APPS = INSTALLED_APPS + [
'django_extensions',
]
```

* `python manage.py shell_plus`도 가능

##### 기타

대화식 python shell에서 command line으로 한 것을 django에서 scripts 형식으로 사용할 수 있다

```python
# 내가 만든 앱의 views.py
from .models import Article
articles = Article(title=headline,content=text,image_url=img_url)
articles.save()
```

- DB에서 불러오기

  ```python
  articles = Article.objects.all() # Article table(클래스)에 있는 모든 레코드(객체)를 가져온다
  ```

------

* [django DB 삭제하기](https://wikidocs.net/9926)

## Tip

- scrimba: 영상에서 바로 코드 칠 수 있음 신기신기. 나중에 구현 가능?
- ORM에 대해서 알자. 면접 질문으로 자주나옴