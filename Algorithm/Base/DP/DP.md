# DP(Dynamic Programming)

## 개요

지역적 최적해를 사용하여 규칙성(점화식)을 발견하여 전역적 최적해를 찾는 기법이다.

## Memoization

1. 문제를 부분 문제로 분할
2. 부분 문제로 나누면 가장 작은 부분 문제부터 해를 구함
3. 결과 테이블에 저장, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함

* 반복되는 부분을 적절한 자료구조(stack, list)에 저장하여

* 계산을 하지 않고 저장한 자료구조에 index로 접근하는 방식으로 사용

```python
# 피보나치
memo = [0,1]

def pivo(n):
    if n < 2:
        return 1
   	else:
        memo.append(pivo(n-1)+pivo(n-2))
    return memo[n]
```

## DP 사용 최적화 문제를 해결하는 알고리즘 절차

1. 문제의 입력에 대해서 최적의 해답을 주는 재귀적 속성을 설정
2. 상향적으로 최적의 해답을 계산
3. 상향적으로 최적의 해답을 구축

* 주어진 문제에 대해 최적의 원칙이 적용될 수 있어야 DP로 해결할 수 있다

* 어떤 문제의 사례에 대한 최적 해가 그 사례를 분할한 부분사례에 대한 최적 해를 항상 포함하고 있으면, 그 문제는 최적의 원칙(The Principle of Optimality)이 적용된다

  **[출처]** [BOJ 11049 행렬곱셈순서 (DP 최소 연쇄행렬곱셈)](https://blog.naver.com/phj8498/221340992241)|**작성자** [흐이준](https://blog.naver.com/phj8498)

### 예제

#### 행렬 곱셈 순서

[11049](https://www.acmicpc.net/problem/11049), [등굣길](https://programmers.co.kr/learn/courses/30/lessons/42898), [거스름돈](https://programmers.co.kr/learn/courses/30/lessons/12907#)

