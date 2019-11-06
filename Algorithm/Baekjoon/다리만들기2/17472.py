N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def union(x, y):
    p[findset(y)] = findset(x)


def numbering(i, j, num):
    global points
    queue = [(i, j)]
    front, rear = -1, 0
    info[i][j] = num
    visited[i][j] = 1
    while front != rear:
        front += 1
        y, x = queue[front]
        for k in range(4):
            yy = y + dy[k]
            xx = x + dx[k]
            if 0 <= yy < N and 0 <= xx < M:
                if info[yy][xx] and not visited[yy][xx]:
                    visited[yy][xx] = 1
                    info[yy][xx] = num
                    queue.append((yy, xx))
                    rear += 1
    points += queue


visited = [[0] * M for _ in range(N)]
number = 1
points = []
for i in range(N):
    for j in range(M):
        if info[i][j] and not visited[i][j]:
            numbering(i, j, number)
            number += 1
p = [x for x in range(number)]
graph = {}

for point in points:
    init = info[point[0]][point[1]]
    for k in range(4):
        y, x = point
        cnt = 0
        while True:
            y += dy[k]
            x += dx[k]
            if 0 <= y < N and 0 <= x < M:
                if info[y][x] == init:
                    break
                if info[y][x] == 0:
                    cnt += 1
                else:
                    if cnt < 2:
                        break
                    if not graph.get((init, info[y][x])):
                        graph[(init, info[y][x])] = cnt
                    if graph[(init, info[y][x])] > cnt:
                        graph[(init, info[y][x])] = cnt
                    break
            else:
                break
# Kruskal
## sort edges by cost
sorted_graph = sorted(graph, key=lambda key: graph[key])
cost = 0
## check if creating cycle
for parent, child in sorted_graph:
    if findset(parent) != findset(child):
        union(parent, child)
        cost += graph[(parent, child)]

## check all island connected
set_cnt = 0
for i in range(1, number):
    if i == p[i]:
        set_cnt += 1

if set_cnt != 1:
    print(-1)
else:
    print(cost)
