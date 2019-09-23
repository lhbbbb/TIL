# Django Model

## 모델에서 데이터 정렬

* 메타(Meta): 특정한 것에 대한 데이터. ex) 사진이라고 하면 사진에 대한 정보
* pk 기준 내림차순 정렬

```python
class Meta:
    ordering = ['-pk']
```

## 외래키 설정

* `pip install django-extensions`: 외래키를 사용하기 위해 패키지 설치
* 1:N 관계 설정
* settings.py의 INSTALLED_APPS 변수에 'django_extensions' 추가
* models.ForeignKey(어떤 모델(테이블), on_delete=models.CASCADE)
  * on_delete 속성: 소속된 데이터가 없어졌을 때 어떻게 남아있는 데이터를 처리할 것인지 정하는 옵션
  * CASCADE는 참조되어 있는 모든 것들을 뜻한다. (DB에서의 CASCADE를 생각하면 된다)
* 어떠한 칼럼도 지정하지 않으면 기본적으로 pk column을 참조하게 된다

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # models.OneToOne() 1:1
    # models.ManyToMany() N:M
```

