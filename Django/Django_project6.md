# Gravatar



# API

* API 폴더 참고

## Install

* `pip install djangorestframework`

* settings.py의 INSTALLED_APPS 변수에 'rest_framework' 추가
* music app 생성
* installed_apps 변수에 추가할 때 'musics.apps.MusicsConfig 도 가능
  * 원래는 이건데 장고가 똑똑해서 musics로 축약해서 해도 알아먹어서 이렇게 씀
  * legacy code에서는 위와 같이 apps안에 들어있는걸로 하는 경우도 있음

### restframework

* [restframework 참고](https://www.django-rest-framework.org/)

## DataSave

* `python manage.py dumpdata articles > dummy.json --indent 2`
  * dummy란 이름의 json 파일형식의 파일 생성

## DataLoad

### Fixtures

* app에 fixtures 폴더 생성
* app 이름으로 fixtures 안에 하위 폴더 생성
* fixtures/app/ 안에 dumpdata 넣음
* `python manage.py loaddata musics/dummy.json`

## 진행

* app에 serializers.py 생성

```python
from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id','title','artist_id',)
```

* views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    # return render() -> .html 페이지를 응답으로 보내주기
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    serializer = MusicSerializer(music)
    return Response(serializer.data)
```

```python
from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id','title','artist_id',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MusicDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)
```

```python
from django.shortcuts import render, get_object_or_404
from .models import Music, Artist
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    # return render() -> .html 페이지를 응답으로 보내주기
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'musics': artists,
    }
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)
```



## drf-yasg

* `pip install drf-yasg`
* settings.py의 INSTALLED_APPS 변수에 'drf_yasg' 추가

[참고](https://github.com/axnsan12/drf-yasg)

* urls.py

```python
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
```

```python
schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
    )
)

app_name = "musics"

urlpatterns = [
    path('musics/', views.music_list, name="music_list"),
    path('musics/<int:music_pk>', views.music_detail, name="music_detail"),
    path('docs/', schema_view.with_ui('redoc'), name="api_docs"),
    path('swagger/', schema_view.with_ui('swagger'), name="api_swagger"),
]
```



# Restful API

## Music : Comment = 1 : N

```
# music REST API
C			POST	/musics/
R(list)		GET		/musics/
R(detail)	GET		/musics/:pk
U			PUT		/musics/:pk
D			DELETE	/musics/:pk
```

```
# comment REST API
C			POST	/musics/:pk/comments
R(list)		GET		/musics/:pk/comments
R(detail)	GET		/musics/:pk/comments/:pk
U			PUT		/musics/:pk/comments/:pk
D			DELETE	/musics/:pk/comments/:pk
```



## Django axios 사용법(좋아요 기능과 관련)

#### CSRF Token

Django 에서 csrftoken을 생성해서 클라이언트에 보내주고, 클라이언트는 이를 쿠키에 저장하고, vue.js에서는 이 쿠키를 찾아서 요청헤더에 쿠키 값을 넣어서 보내줘야 한다. Django 에서와 Vue.js에서의 csrf 헤더와 토큰 이름을 맞춰줘야 한다.

```js
// POST 방법으로 보낼 때 해줘야하는 작업

// 사용할 axios 마다 지정해줄 수도 있고,
axios.post('/api/todo/create/', postData, {xsrfCookieName: 'csrftoken', xsrfHeaderName: 'X-CSRFToken'})
// 전역변수로 설정해줘서 사용도 가능
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.post(`/articles/${articleId}/like/`) 
```

CSRF Token은 Django에서 생성을 하는데 {% csrf_token %} 으로 생성한다.

Django 에서 처음부터 csrf token이 만들어져 있지 않다면 (CSRF cookie not set) 이라는 오류가 발생한다.

이러한 문제를 해결하기 위해서 Django 에서는 데코레이터를 제공하고 있다.