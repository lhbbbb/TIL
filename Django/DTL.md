# DTL

Django Template Language 문법

## 1. 데이터 넘겨받기

```html
<h2>데이터를 넘겨 받는 법</h2>
  <p>{{data}}{{name}}</p>
  {% for ele in data %}
    <p>{{ ele }}</p>
  {% endfor %}
```

## 2. for문

```html
<h2>데이터가 없을 때,</h2>
  {% for movie in empty_data %}
    <!-- forloop.counter를 쓰면 enumerate처럼 아이템에 idx를 같이 줄 수 있다 -->
    <p>{{ forloop.counter }}: {{ movie }}</p> 
  {% empty %}
    <p>영화 데이터가 없숩네다</p>
  {% endfor %}
```

## 3. 이중 for문

```html
<h2>2중 for문</h2>
  {% for array in matrix %}
    {% for num in array %}
      <p>{{ num }}</p>
    {% endfor %}
  {% endfor %}
```

## 4. 다양한 helper / filter

```html
<h2>다양한 helper / filter</h2>
  <h3>helper</h3>
  <!-- fake data 넣어주기 -->
  <p>{% lorem 3 p random %}</p> 
  <h3>filter</h3>
  {% for movie in empty_data %}
    <!-- 데이터는 그대로인데 컨텐츠의 길이를 줄이고 싶을때 -->
    <p>{{ movie|truncatechars:5 }}</p>
  {% endfor %}
```

## 5. int: 사칙연산 수행

number + 10

```html
<h4>int</h4>
  {{number|add:10}}
```

## 6. date time

```html
<!-- 게시판에서 자주 사용 -->
  <h4>datetime</h4>
  {% now "Y년 m월 d일 h시 i분 A" %}
```

* using database

```html
<!-- value property from database for input tag in django -->
<input type="date" name="open_date" value="{{ movie.open_date|date:'Y-m-d' }}">
```

```html
# django models.py
class Movie(models.Model):
    open_date = models.DateField()
```

