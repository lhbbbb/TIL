# Graph

## Dictionary로 구현

* 중복되는 값을 set 자료형을 이용해서 제거

```python
# input 형태: 1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
graph = {}
## 양방향 그래프
for i in range(0, N, 2):
   	start, end = lst[i], lst[i + 1]
    if not graph.get(start):
        graph[start] = set()
    if not graph.get(end):
        graph[end] = set()
    graph[start].update([end])
    graph[end].update([start])

## 단방향 그래프
for i in range(0, N, 2):
    start, end = lst[i], lst[i+1]
    if not graph.get(start):
        graph[start] = []
    graph[start] += [end]
```

## Matrix로 구현

* 인접 행렬로 그래프 구현시의 단점
  * 입력값으로 주어지는 노드가 N개 보다 적을 시 불필요한 메모리를 낭비
  *  BFS나 DFS 검색시 불필요한 작업으로 인해 실행 시간이 느려지게 된다

```python
adj_matrix = [[0] * (N+1) for _ in range(N+1)]
# 양방향 그래프
for i in range(0, N, 2):
	start, end = lst[i], lst[i + 1]
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

# 단방향 그래프
for i in range(0, N, 2):
	start, end = lst[i], lst[i + 1]
    adj_matrix[start][end] = 1
```



## Linked List로 구현

