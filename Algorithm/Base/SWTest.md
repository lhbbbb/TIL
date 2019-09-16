# SWTest

## AD

### 다리 최소 비용

#### target

* 다리를 짓는데 드는 최소 비용 구하기

#### How to

1. BFS 돌려서 섬 번호 매기고 좌표 저장
2. 1에서 저장한 좌표에서 시작하여 상하좌우 탐색해서 0이면 그 방향으로 0이 아닌 값 만날때까지 DFS. 0의 개수를 count하여 다리를 짓는데 필요한 코스트를 구함
3. 구한 다리 코스트로 그래프 정보를 나타내는 가중치 인접행렬 만들기
4. 가능한 인접 행렬의 조합 만들기
5. 각 인접 행렬마다 그래프 연결 관계 확인. 
   1. 각 노드를 한번은 순회해야함 => 노드들이 다 연결되어 있어야함
   2. 그렇지 않으면 섬 전체가 연결이 되지 않은 것이므로 -1 return
6. 그래프를 탐색하면서 가중치를 합산하여 다리 짓는 코스트 구함
7. 각 인접행렬당 드는 코스트를 비교하여 최소 코스트를 구함

```python
import sys

sys.stdin = open('bridge.txt', 'r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def perm_r(k):
    if k == R:
        graphs.append(t[::])
    else:
        for i in range(num):
            if visited[i]:
                continue
            t[k] = info[i]
            visited[i] = True
            perm_r(k + 1)
            visited[i] = False


def BFS(i, j, num):
    visited[i][j] = True
    lst[i][j] = num
    queue = [(i, j)]
    front, rear = -1, 0
    while front != rear:
        front += 1
        y, x = queue[front]
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                if not visited[next_y][next_x] and lst[next_y][next_x] != 0:
                    visited[next_y][next_x] = True
                    lst[next_y][next_x] = num
                    queue += [(next_y, next_x)]
                    rear += 1


def search(i, j, k, origin):
    cnt = 1
    y, x = i, j
    next_y = y + dy[k]
    next_x = x + dx[k]
    flag = False
    if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
        while lst[next_y][next_x] == 0:
            cnt += 1
            next_y += dy[k]
            next_x += dx[k]
            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:
                flag = True
                break
    else:
        flag = True
    if flag:
        return 0
    else:
        origin_y, origin_x = origin
        adj_matrix[lst[origin_y][origin_x]][lst[next_y][next_x]] = cnt


def connect(start):
    visited[start] = True
    queue = [start]
    front, rear = -1, 0
    while front != rear:
        front += 1
        node = queue[front]
        for next_node in range(1, num + 1):
            if not visited[next_node] and adj_matrix[node][next_node]:
                visited[next_node] = True
                queue += [next_node]
                rear += 1
    for i in range(1, num + 1):
        if visited[i] != True:
            return 1
    return 0


# 1. 섬 번호 매기기
num = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][j] != 0 and not visited[i][j]:
            num += 1
            BFS(i, j, num)
# 2. 섬 인접 행렬 만들기
visited = [[0] * N for _ in range(N)]
adj_matrix = [[0] * (num + 1) for _ in range(num + 1)]
for i in range(N):
    for j in range(N):
        if lst[i][j] != 0 and not visited[i][j]:
            visited[i][j] = True
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if y >= 0 and y < N and x >= 0 and x < N and lst[y][x] == 0:
                    search(y, x, k, (i, j))

# 3. 가능한 그래프 조합 만들기 # todo: nC2(양 옆) * (n-2)P2를 사용하면 반으로 줄일 수 있음(중복되는 거 피할 수 있음)
R = num
t = [0] * num
visited = [0] * num
info = [x for x in range(1, num + 1)]
graphs = []
perm_r(0)
# 4. 섬 전체가 연결되는지 확인
visited = [0] * (num + 1)
min_val = 100000
if connect(info[0]):
    print(-1)
else:
    # 5. 그래프 연결 가능 여부 확인하면서 코스트 최소값 구하기
    for graph in graphs:
        cost = 0
        flag = True
        for i in range(num - 1):
            if not adj_matrix[graph[i]][graph[i + 1]]:
                flag = False
                break
            cost += adj_matrix[graph[i]][graph[i + 1]]
        if flag:
            if min_val > cost:
                min_val = cost
    print(min_val)
```

