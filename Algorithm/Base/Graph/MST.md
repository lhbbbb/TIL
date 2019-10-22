# Minimum Spanning Tree(MST)

## Spanning Tree

* 최소 간선(n-1개)으로 그래프 내의 모든 정점을 연결하는 트리
* 하나의 그래프에서 스패닝 트리는 여러개가 존재할 수 있다

![spanning tree](assets\spanning_trees.jpg)

* 최소 신장 트리



## 프림

### 과정

1. 임의 정점을 하나 선택 시작
2. 선택한 정점과 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점 선택
3. 모든 정점 선택될 때까지 1,2 반복

## 크루스칼

### 과정

1. 간선 정렬
2. 정렬된 간선을 돌면서 각 간선에 속한 노드들이 사이클을 형성하는지 확인(Disjoint Set 알고리즘 사용)
   1. 각 간선에 속한 노드들의 부모노드가 같은지 확인(FindSet)
   2. 같으면 사이클 형성된것이므로 pass
   3. 같지 않으면 UnionSet을 사용해서 부모 노드를 가리키게 함

```python
def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def unionset(x, y):
    p[findset(y)] = findset(x)


for tc in range(1, T + 1):
    V, E = map(int, input().split())

    info = []
    for _ in range(E):
        info.append(list(map(int, input().split())))

    # sort edges by cost
    info.sort(key=lambda x: x[2])

    # find mst cost
    p = [x for x in range(V + 1)]
    cost = 0
    for ele in info:
        if findset(ele[0]) != findset(ele[1]):
            unionset(ele[0], ele[1])
            # print(p)
            cost += ele[2]

    print("#{} {}".format(tc, cost))
```

### 단점

* 시간복잡도가 간선을 정렬하는 시간에 영향을 받기 때문에 간선 수가 많으면 비효율적