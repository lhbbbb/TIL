# 2019.10.23

# instargram의 특징

* 마이페이지
* 팔로워하고 있는 사람들의 피드

* 팔로우 기능
  * User follow User
  * 자기 스스로 M:N의 관계를 갖는다



# DTL

* 파이썬이 아니다
* 따라서 파이썬의 문법을 따르지 않는다
* method 콜을 할 때 ()를 쓰지 않고 property처럼 name만 사용한다



# 좋아요 취소

* exists 사용

## .get()과 .filter

### .get

* 조건에 맞는 값이 없으면 error return

### .filter

* 조건에 맞는 값이 없으면 빈 쿼리셋 return

```python
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
    else:
        # request.user.like_articles.add(article)
        article.like_users.add(user)

    return redirect(article)
```

```html
  {% if user in article.like_users.all %}
  <a href="{% url 'articles:like' article.pk %}">좋아요 취소</a>
  {% else %}
  <a href="{% url 'articles:like' article.pk %}">좋아요</a>
  {% endif %}
```



# 캐싱

## with

* [참고](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#with)
* DTL
* article.like_users.all 을 할 때마다 DB에서 불러서 가져오기 때문에 많은 코스트가 발생
* 따라서 한번 불러놓고 그 값을 저장해놓고 사용

```html
  <p>좋아하는 사람들:
  {% with likers=article.like_users.all %}
    {% for person in article.like_users.all %}
      {{ person }}
    {% endfor %}
  </p>
    {% if user in likers %}
    <a href="{% url 'articles:like' article.pk %}">좋아요 취소</a>
    {% else %}
    <a href="{% url 'articles:like' article.pk %}">좋아요</a>
    {% endif %}
  {% endwith %}
```

## ORM lazyloading

* [참고](http://raccoonyy.github.io/using-django-querysets-effectively-translate/)
* django의 쿼리는 마지막까지 지연된다
  * 쿼리셋의 내장 캐시에 평가된 모델들이 저장되기 때문에 똑같은 쿼리를 날리면 캐시에 저장된 결과를 사용한다
  * 따라서 똑같은 쿼리를 여러번 날려도  DB에서 쿼리는 단 한번만 발생한다
* lazyloading 때문에 굳이 with를 사용할 필요는 없다. 기억만 해두자

# 프로필

* 숨겨져 있는 유저 정보를 가져올 수 있음

```python
from django.contrib.auth import get_user_model
```

```python
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

* project app

```python
# urls.py
from accounts import views as accounts_views

urlpatterns = [
    path('<username>/', accounts_views.profile, name="profile"),
]
```



# 팔로우

* models.py
* related_name property: 역참조 될 때 어떻게 불리겠다..?

```python
from django.contrib.auth.models import AbstractUser
```

```python
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
```

* forms.py

```python
from django.contrib.auth.forms import UserCreationForm
```

```python
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

* views.py

```python
def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    user = request.user
    
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)    

    return redirect('profile', person.username)
```

* profile.html

```html
{% with followers=person.followers.all %}
{% if user in followers %}
<a class="btn btn-outline-primary" href="{% url 'accounts:follow' person.pk %}">언팔로우</a>
{% else %}
<a class="btn btn-primary" href="{% url 'accounts:follow' person.pk %}">팔로우</a>
{% endif %}
<p>팔로워수 : {{ followers|length }}</p>
<p>팔로워들 : 
    {% for follower in followers %}
      {{ follower }}
    {% endfor %}
  {% endwith %}
</p>
```



## Q

```python
from itertools import chain
```

```python
followings = request.user.followings.all()
followings_and_me = chain(followings, [request.user])
```



# Hashtag

* manytomany fields 는 중계 모델을 생성하기 때문에 원본 모델은 건드리지 않음. 따라서 마이그레이션해도 에러가 생기지 않음
* models.py

```python
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    
class Article(models.Model):
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

* views.py
  * 있는 지 찾아보고 없으면 만들기

```python
            # hashtag
            for word in article.content.split():
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
```

* 해당 해시태그를 가진 모든 글들 보여주기

```python
def tags(request):
    tags = Hashtag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'articles/tags.html', context)

def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    articles = hashtag.article_set.all()
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)
```

