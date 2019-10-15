# 표준 CRUD

## 2019.10.15

## Settings

### settings.py

```python
INSTALLED_APPS = [
    'django_extensions',
    'articles',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'recap', 'templates'),],
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

### urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

### 그 외

* templates 폴더 만들어서 base.html 만들기
* form 형태에 bootstrap 적용

> {% load bootstrap4 %}
> {% bootstrap_css %}
> {% bootstrap_javascript jquery='full' %}

```html
<!-- base.html -->
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
<!DOCTYPE html>
<html lang="kr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>
```

## Model

```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
	
    # 내림차순 정렬
    class Meta:
        ordering = ('-pk',)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'article_pk':self.pk})
```

### 모델 클래스 내 get_absolute_url 멤버함수

[출처](https://wayhome25.github.io/django/2017/05/05/django-url-reverse/)

> 특정 모델에 대한 Detail뷰를 작성할 경우, Detail뷰에 대한 URLConf설정을 하자마자,
> 필히 get_absolute_url설정을 해주세요. 코드가 보다 간결해집니다

- **목적: 코드 간결화**
- 어떠한 모델에 대해서 detail 뷰를 만들게 되면 get_absolute_url() 멤버 함수를 무조건 선언
- resolve_url(모델 인스턴스), redirect(모델 인스턴스) 를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출
- resolve_url() 함수는 가장 먼저 get_absolute_url 함수의 존재 여부를 체크하고, 존재하면 호출하며 그 리턴값으로 URL을 사용

## Form

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__' # 모든 모델의 모든 필드를 다 가져옴
        fields = ('title','content',)
        widgets = {
            # '필드(칼럼)': Form속성
            'title': forms.TextInput(attrs={
                'placeholder': '제목을 입력해주세요.',
                'class': 'form-control title-class',
                'id': 'title',
            })
        }
    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text="제목은 20자 이내로 써주세요.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-title',
                'placeholder': '제목을 입력해주세요',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요',
                'rows':5,
            }
        )
    )
```

* ModelForm 사용



## View

### import

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed
from django.http import Http404
from django.views.decorators.http import require_POST
```

### Create

```python

```



### Read

### Update

### Delete

