# DFS

* 그래프 탐색 방법 중 깊이 우선 탐색 방법

## 구현

### 그래프

그래프 종류 참조:  [Graph](./Graph.md)

```python
visited = [0] * (노드개수+1) # 1부터 시작하는 인덱스 맞춰주기 위해 0을 추가하여 생성
graph = {
    1: [2,3],
    2: [4,5],
    3: [6,9]
} # 단방향 그래프
```

### 반복문

1. 시작 노드를 스택에 넣는다
2. 스택에 노드가 없을 때까지 다음의 과정 반복
   1. 스택에서 가장 위에 있는(가장 마지막에 추가한) 노드를 꺼낸다
   2. 현재 노드의 자식 노드들을 순회한다
   3. 해당 노드가 방문했던 노드인지 확인한다
   4. 방문하지 않은 노드들을 스택에 추가한다
   5. 방문 리스트에 노드 정보를 추가한다

```python
stack = [start]
visited[node] = True
while stack:
    node = stack.pop()
    for next_node in graph[node]:
        if not visited[next_node]:
            stack.append(next_node)
            visited[next_node] = True
```

### 재귀

1. 시작 노드를 방문했다고 표시한다
2. 현재 노드의 자식 노드를 순회한다
3. 해당 노드가 방문했던 노드인지 확인한다
4. 방문하지 않는 노드를 시작노드로 하여 1~3을 반복한다

```python
DFS(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            DFS(next_node)
```