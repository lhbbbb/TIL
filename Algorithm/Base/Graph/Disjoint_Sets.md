# 상호배타 집합(Disjoint Sets)

* 최소신장트리(MST) 알고리즘 중 크루스칼 알고리즘에 사용되는 자료구조
* 교집합이 없는 집합
* 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분
  * 대표자라고 칭함
* 상호배타 집합 표현 방법
  * 연결 리스트
  * 트리

```python
def makeset(x):
    p[x] = x


def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def union(x, y):
    p[findset(y)] = findset(x) # 자식의 부모를 부모의 부모로 업데이트


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    info = list(map(int, input().split()))

    p = [0] * (N + 1)
    for i in range(1, N + 1):
        makeset(i)

    for i in range(0, len(info), 2):
        union(info[i], info[i + 1])

    cnt = 0
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1
    print("#{} {}".format(tc, cnt))
```

