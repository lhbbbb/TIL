# DP

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

