# Python Class

## 클래스

### 멤버변수

* `__변수명`: 프라이빗 필드 지정

```python
class Person:
    self.__name = name # 프라이빗 필드 생성 // __ 키워드를 앞에 써주면 프라이빗으로 설정
```



### property

* c++이나 java처럼 클래스에서 private, protected 키워드의 역할을 파이썬에서는 `_, __`로 대신한다.

* 그리고 getter나 setter 메서드를 `@property`와 `@변수명setter`로 대신하게 된다.

* 다만 파이썬에서는 저렇게 키워드 설정을 했다고 해도 클래스 외부에서 절대로 접근할 수 없어지는게 아니다. 즉, 강제되는 사항이 아니고 필요하다면 사용하는 기능이다. 외부에서 `_, __`로 접근하면 여전히 사용가능하다. 

```python
class Student:
    def __init__(self, korean, english, math):
        self.__korean = korean # private으로 변수 설정. 외부에서 instance.korean으로 접근 불가
        self.__english = english
        self.__math = math

    @property # getter와 같은 기능
    def korean(self):
        return self.__korean

    @property
    def english(self):
        return self.__english

    @property
    def math(self):
        return self.__math

    @korean.setter # setter와 같은 기능 => 외부에서 instance.korean으로 접근 가능해짐
    def korean(self, korean):
        self.__korean = korean

    def sum(self):
        return print('국어, 영어, 수학의 총점: {}'.format(sum([self.english, self.korean, self.math])))


numbers = map(int, input().split(','))
stu1 = Student(*numbers)

stu1.sum()

```



