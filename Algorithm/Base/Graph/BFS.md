# BFS

* 그래프 탐색 기법 중 너비 우선 탐색

## 구현

1. 시작 노드를 큐에서 꺼낸다
2. 현재 노드의 자식 노드들을 순회한다
3. 자식 노드들이 방문했던 노드인지 확인한다
4. 방문하지 않은 노드면 큐에 추가한다
5. 방문 목록에 노드를 추가한다

```python
BFS(start):
    queue = [start]
    while queue:
       	node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
```



## 미로 거리 찾기 문제

### Depth 구하기

```python
import sys

sys.stdin = open('sample_input.txt', 'r')


def BFS(i, j):
    y, x = i, j
    visited[y][x] = 1
    node = (y, x)
    queue = [node]
    while queue:
        start_y, start_x = queue.pop(0)
        for k in range(4):
            x = start_x + dx[k]
            y = start_y + dy[k]
            if x >= 0 and x < N and y >= 0 and y < N:
                if not visited[y][x] and lst[y][x] != 1:
                    if lst[y][x] == 3:
                        return visited[start_y][start_x] - 1
                    visited[y][x] = visited[start_y][start_x] + 1 # depth 구하는 부분
                    queue.append((y, x))
    return 0


T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                res = BFS(i, j)
                break

    print('#{} {}'.format(tc, res))
```

### pop을 사용하지 않고 queue를 구현하여 depth 구하기

```python
def BFS(start):
    global depth
    node = (start, 1)
    queue = [node]
    visited[node[0]] = True
    front, rear = -1, 0
    while front != rear: # 맨앞 포인터가 맨 뒤 포인터와 같아지면 모두 꺼낸 것으로 보고 종료
        front += 1
        node = queue[front]
        if graph.get(node[0]):
            for end_node in graph[node[0]]:
                if not visited[end_node]:
                    visited[end_node] = True
                    depth = node[1] + 1
                    queue.append((end_node, depth))
                    rear += 1
    return queue
```

## Card Shuffle 문제

```python
def BFS():
    front, rear = -1, 0
    while front != rear:
        front += 1
        node = queue[front]
        if node[1] > 5:
            return queue
        for x in range(N // 2 + 1):
            index = N // 2 - x
            for _ in range(x):
                node[0][index], node[0][index + 1] = node[0][index + 1], node[0][index]
                index += 2
            if node[0] == sorted(lst) or node[0] == sorted(lst, reverse=True):
                return node
            queue.append((node[0][::], node[1] + 1))
            rear += 1
        for x in range(N - 1 - N // 2, 0, -1):
            index = N // 2 - x
            for _ in range(x):
                node[0][index], node[0][index + 1] = node[0][index + 1], node[0][index]
                index += 2
            if node[0] == sorted(lst) or node[0] == sorted(lst, reverse=True):
                return node
            queue.append((node[0][::], node[1] + 1))
            rear += 1


N = 4
lst = [4, 2, 1, 3]

depth = 0
queue = [(lst, depth)]
print(BFS())
```

