# 정의

* 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조
* 여러 개의 값들 중 **최댓값이나 최솟값을 빠르게 찾아내도록** 만들어진 자료구조

# 특징

* 반정렬 상태를 유지 (정렬된 상태가 아니다!!)
  * 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도
  * 즉, **부모 노드의 값이 자식 노드의 값보다 항상 큰(작은) 이진 트리**를 말한다
* 중복된 값을 허용한다

# 종류

1. 최대 힙
   * 부모 노드의 값이 자식 노드의 값보다 크거나 같은 완전 이진 트리
2. 최소 힙
   * 부모 노드의 값이 자식 노드의 값보다 작거나 같은 완전 이진 트리

# 구현

* 힙을 저장하는 표준적인 자료구조는 배열
* 구현을 쉽게 하기 위해 배열의 첫번째 인덱스인 0은 사용하지 않는다
* 특정 위치의 노드 번호는 새로운 노드가 추가되어도 변하지 않는다

## 배열

### 삽입

```python
def heap(data):
    tree.append(data)
    i = len(tree) - 1
    while i != 1:
        cur = i
        parent = i // 2
        if tree[parent] > tree[cur]:
            tree[parent], tree[cur] = tree[cur], tree[parent]
        else:
            break
        i //= 2

    print(tree)
```

### 삭제

```python
def heap_pop():
    tree[1], tree[-1] = tree[-1], tree[1]
    i = 1
    while i < len(tree):
        cur = i
        child = i * 2
        if child + 1 >= len(tree):
            break
        if tree[cur] > tree[child]:
            if tree[child] < tree[child + 1]:
                tree[cur], tree[child] = tree[child], tree[cur]
            else:
                if tree[child + 1] < tree[cur]:
                    tree[cur], tree[child + 1] = tree[child + 1], tree[cur]
        i *= 2
    tree.pop()
    print(tree)
```

```python
tree = [0]
heap(5)
heap(6)
heap(4)
heap(3)
heap(8)
heap(10)
heap(8)
heap(1)

heap_pop()
heap_pop()
heap_pop()
heap_pop()
```

