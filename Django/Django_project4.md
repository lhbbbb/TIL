# Cookie 만들기

```python
res.set_cookie(key, value)
```



# Middleware

* 중간에 껴서 대신 해주는 것

* Django ORM: DB에 대한 middleware
* DTL: Template에 대한 middleware
* 

`request.session._session`

sess

캐시는 상대적인 개념

캐싱: 원래있던 데이터 혹은 저장소가 너무 시간적 비용이 많이 들어서 조그만 곳에 가까운 은닉처 혹은 보관소를 만들어 보관하는 것



# 방문자 수 늘리기

```python
def index(request):
    # embed()
    visits_num = request.session.get('visits', 0)
    request.session['visits'] = visits_num + 1
    request.session.modified = True
    embed()
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'visits': visits_num,
    }
    return render(request, 'articles/index.html', context)
```

```python
In [1]: request.session._session
Out[1]:
{'_auth_user_id': '2',
 '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
 '_auth_user_hash': '6c61762722b5cdcabbb4e86fbe7732d616bad16e',
 'visits': 2}
```



# Update

```python
from django.contrib.auth.forms import UserChangeForm
```

```python
@login_required
def update(request):
    if request.method=="POST":
        #실제 DB에 적용
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
```



## Customizing

* forms.py

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
```

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','first_name','last_name','username',)
```



# PasswordChangeForm

```python
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
```

```python
def change_password(request):
    if request.method == "POST":
        # 실제 비번 변경
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # session auth hash가 변경
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌(form)
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
```



# 템플릿 중복

```html
<!-- auth_form.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}
{% if request.resolver_match.url_name == 'signup' %}
  <h1>회원가입</h1>
{% elif request.resolver_match.url_name == 'login' %}
  <h1>로그인</h1>
{% elif request.resolver_match.url_name == 'update' %}
  <h1>회원정보 수정</h1>
{% else %}
  <h1>비밀번호 수정</h1>
{% endif %}

<form method="POST">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons submit="비밀번호 수정" %}{% endbuttons %}
</form>

{% endblock %}
```



# 유저 1:N 관계 설정

* models.py

```python
from django.conf import settings
```

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

settings.AUTH_USER_MODEL 간접 레퍼런스: 변수명이기 때문에 나중에 커스터마이징 할 때 편함

auth.User 를 사용하게 되면 커스터마이징 불편



# 좋아요 기능

> M:N
>
> - 수강신청
> - 예약(진료)
> - 좋아요 or follow

* M:N 관계는 두 개의 테이블 만으로 표현할 수 없다
* 중간에 매개체 역할을 하는 테이블을 하나 더 둔다(join table)
* 동사적인 느낌이 크다
* 보통 목적어에 다는 느낌

### models.py

```python
class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles',blank=True)
```

* shell_plus

```powershell
In [18]: a.like_articles.add(Article.objects.get(pk=2))

In [19]: a.like_articles.all()
Out[19]: <QuerySet [<Article: fsdfsdf>]>

In [20]: a.like_articles.remove(article)

In [21]: a.like_articles.all()
Out[21]: <QuerySet []>
```

```python
def like(request, article_pk):
    # article_pk로 넘어온 글에 현재 접속중인 유저를 추가한다.
    article = get_object_or_404(Article, pk=article_pk)
    # request.user.like_articles.add(article)
    article.like_users.add(request.user)
    return redirect(article)
```

