# Django

## 2019.10.14

RECAP 프로젝트

```django
# 번역 해주는 애들(internationalization)
USE_I18N = True
# localization
USE_L10N = True

USE_TZ = True
```



### Test.py

* 구현해낼 기능이나 만들어야할 모델을 미리 짬
* test code를 먼저짜고 개발은 후에
* 기술부채를 해결하기 위해(app이 커지고 복잡해지면 생기는 문제를 기술 부채라고 한다)



### admin.py

```django
from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at')
    list_display_links = ('title',)

admin.site.register(Article, ArticleAdmin)
```



* restful 형식

* graphql 형식

* get_absolute_url 정리



## django Form

[참고블로그](https://wayhome25.github.io/django/2017/05/06/django-form/)

### Bootstrap Form

* `pip install django-bootstrap4`

* settings.py의 installed_apps에 bootstrap4 추가

#### base.html

* 최상단에 다음 코드 입력

```html
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
```

#### create.html

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
```

