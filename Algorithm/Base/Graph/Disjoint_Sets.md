# 상호배타 집합(Disjoint Sets)

* 교집합이 없는 집합
* 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분
  * 대표자라고 칭함
* 상호배타 집합 표현 방법
  * 연결 리스트
  * 트리
  * 리스트

```python
# 리스트를 이용한 표현
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

## 트리로 표현 시 대표적 문제점

- 문제에서 주는 그래프의 순서에 따라 집합을 union 하는 과정에서 편향된 트리 구조가 생성될 수 있다.

모든 원소들이 루트를 부모로 가리키도록 하는 방법으로 해결가능하다.

## 연산의 효율을 높이는 방법

### 1. rank를 이용한 union

- 각 노드는 자신을 루트로 하는 subtree의 높이를 rank라는 이름으로 저장
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙임

### 2. path compression

- find-set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 부모 정보를 변경

### 3. 구현

```python
# makeset(x): 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
## p[x]: 루트 x의 부모 저장
## rank[x]: 루트 노드가 x인 트리의 랭크 값 저장
def makeset(x):
    p[x] = x # 자기 자신
    rank[x] = 0

# findset(x): x를 포함하는 집합을 찾는 연산
def findset(x):
    if x != p[x]: # x가 루트가 아닌 경우
        p[x] = findset(p[x]) # path compression
    return p[x]

# union(x, y): x와 y를 포함하는 두 집합을 통합하는 연산
def union(x,y):
    link(findset(x), findset(y))

# rank를 이용한 union
def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1
```

## 활용

구현이 간단하고 동작 속도가 빨라 그래프 영역에서 많이 사용되고 다른 알고리즘의 일부로 활용된다.

- 그래프 연결성 확인
- 최소신장트리(MST) 알고리즘 중 크루스칼 알고리즘에 사용되는 자료구조

또는 각 집합에 속한 원소의 수를 관리할 때 사용되기도 한다.

- 가장 큰 집합 추적
- 집합의 노드 개수가 몇 개 이상이 되는 시점 찾기