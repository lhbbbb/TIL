# Python Basic inner function

## packing, unpacking

* 참고 url: https://wikidocs.net/22801

### * operator

### ** operator

---



## enumerate() function

* 인덱스와 값을 tuple 형태로 반환해주는 함수

### how to use

* enumerate(*iterable*, *start*=0)
  * *iterable* must be a sequence
    * kinds of sequence: list, tuple, range, string
  * *start* means index start number

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
for index, value in enumerate(seasons):
    print(index, value)
'''
0 Spring
1 Summer
2 Fall
3 Winter
'''
```

---



## eval() function

* possible to use *expression*

### how to use

* eval(*expression*)

```python
x = 1
exp = "x+5"
print(eval(exp)) # return 1+5 => 6
```

---



## map function

* Return an iterator that applies *function* to every item of *iterable*, yielding the results

### how to use

* map(*function*, *iterable*, ...)

```python
mapping = map(lambda x: 4, (1,2,3,4)) # all elements have values 4
print(list(mapping))
# [4, 4, 4, 4]
```



---



## filter function

* Construct an iterator from those elements of *iterable* for which *function* returns true

### how to use

* filter(*function*,*iterable*)
  * *iterable* may be either a sequence, a container which supports iteration, or an iterator
  * *iterables*
    * https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835c

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtering = filter(lambda x: x % 2 == 0, lst)
print(list(filtering))
# [2, 4, 6, 8, 10]
```



## Format function

* convert number to bin, oct, hex...

### how to use

```python
>>> format(42, 'b')
'101010'
>>> format(42, 'o')
'52'
>>> format(42, 'x')
'2a'
>>> format(42, 'X')
'2A'
>>> format(42, 'd')
'42'
```