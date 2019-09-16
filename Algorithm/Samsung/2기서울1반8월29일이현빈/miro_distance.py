#import sys

#sys.stdin = open('sample_input.txt', 'r')


def BFS(i, j):
    y, x = i, j
    visited[y][x] = 1
    node = (y, x)
    queue = [node]
    node_cnt = 1
    depth = 0
    while queue:
        a, b = queue.pop(0)
        for k in range(4):
            x = b + dx[k]
            y = a + dy[k]
            if x >= 0 and x < N and y >= 0 and y < N:
                if not visited[y][x] and lst[y][x] != 1:
                    if lst[y][x] == 3:
                        return visited[a][b] - 1
                    visited[y][x] = visited[a][b] + 1
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
