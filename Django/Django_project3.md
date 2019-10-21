http의 단점

stateless 

* 로그인의 본질
* cookie
  * 서버가 유저에게 보내는 과자부스러기
* session
* cache
* 

http가 stateless하기 때문에 cookie를 사용함



cookie만으로 authentication하면 너무 위험함

사용자의 쿠키정보를 ctrl c,v하면 다른 곳에서 그 사용자인것처럼 행동가능

광고 => 쿠키로 정보를 알아와서 해당 유저에게 광고 보여줌



쿠키 단점 보완

* IP, MAC, Cookie 정보가 다 일치해야만 해당 유저로 인식하게 바뀜



# 로그인 기능 만들기

1. `python manage.py startapp accounts`: app_name에 accounts 무조건 써야함
2. settings.py 에서 app 등록
3. urls.py에서 include로 경로 추가
4. views.py에서 django에서 제공하는 함수 사용



## UserCreationForm(회원가입)

* User에 대한 CRUD
* 회원가입

```python
from django.contrib.auth.forms import UserCreationForm
```

```python
# Create your views here.
def signup(request):
    # 만약 로그인 되어있으면, articles/ 로 리다이렉트
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == "POST":
        # 실제 DB에 유저 정보 저장
        form = UserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```html
<!-- signup.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block body %}
<h1>회원가입</h1>

<form method="POST">
  {% csrf_token %}
  {% bootstrap_form form %}
  <!-- <button type="submit" class="btn btn-primary">제출</button> -->
  {% buttons submit="회원가입" %}{% endbuttons %} <!-- bootstrap form으로 만드는 버튼 -->
</form>

{% endblock %}
```

## AuthenticationForm(로그인)

### accounts

* Session에 대한 CRUD

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
```

* 로그인

```python
def login(request):
    # 만약 로그인 되어있으면, articles/ 로 리다이렉트
    if request.user.is_authenticated:
        return redirect('articles:index')
        
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 시킨다.
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

* 로그아웃

```python
def logout(request):
    # 세션을 지우기
    auth_logout(request)
    return redirect('articles:index')
```

* 회원탈퇴

```python
@require_POST
def delete(request):
    # DB에서 user를 삭제한다.
    request.user.delete()
    return redirect('accounts:signup')
```

### articles

* 로그인 세션 유지
  * login_required의 데코레이터의 기본값이 accounts의 login 함수로 설정되어있음
  * If the user isn’t logged in, redirect to [`settings.LOGIN_URL`](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-LOGIN_URL), passing the current absolute path in the query string. Example: `/accounts/login/?next=/polls/3/`.
  * LOGIN_URL: Default: `'/accounts/login/'`

```python
from django.contrib.auth.decorators import login_required
```

```python
# create
@login_required
def create(request):
    if request.method == 'POST':    
        form = ArticleForm(request.POST)
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            article = form.save()
            return redirect(article)
        else:
            return redirect('articles:create')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
```

* 나머지 update, delete, create_comment 마찬가지로 @login_required 붙여주면 됨

# 기술면접

* cookie와 session의 관계에 대해서 설명해보시오