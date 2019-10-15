# Django

## 2019.10.15

`pip install ipython`

```python
from IPython import embed
```

embed: 특정 폼이 어떻게 들어가있는지 확인

* 터미널 창에서 shell_plus로 폼의 정보 확인 가능
* 디버깅할 때 사용하면 데이터의 유입과 흐름을 파악할 수 있으므로 편리하다



settings.py 에서 'django_extensions' 추가

`python manage.py shell_plus`



## Form

### widget 사용

```python
from django import forms

class ArticleForm(forms.Form):
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



## 404에러 띄우기

```python
def detail(request, article_pk):
    # get_object_or_404(Article, pk=article_pk)
    # get_object_or_404 직접 작성
    try:
        Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404('해당하는 id의 글이 존재하지 않습니다')
    article = Article.objects.get(pk=article_pk)
    
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)
```



## 405에러

* method 에러



## ModelForm

```python
# forms.py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' # 모든 모델의 모든 필드를 다 가져옴
```



```python
# CREATE
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)    
    else:
        form = ArticleForm(request.POST)
        embed()
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            article = form.save() # ModelForm을 사용했을 시
            return redirect(article)
        else:
            return redirect('articles:create')
```



```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # 실제 DB의 데이터를 수정
        form = ArticleForm(request.POST, instance=article) # ModelForm update
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            form.save()
            return redirect(article)
    # 편집 화면
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```



### Customizing

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content',) # 명시적으로 지정
        # exclude = ('title',) ## 특정 칼럼 폼에서 제외시키기
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



## View decorator django

```python
from django.views.decorators.http import require_POST
@require_POST # POST 방식으로만 작동함
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article) # get_absolute_url => detail page
```

