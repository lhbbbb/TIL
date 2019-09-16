T = int(input())


def isWall(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False


def DFS(i, j):
    direction = 0
    visited[i][j] = True
    lst[i][j] = 0
    x, y = j, i
    for _ in range(len(dx)):
        x = j + dx[direction]
        y = i + dy[direction]
        if isWall(x, y):
            if not visited[y][x] and lst[y][x] != 0:
                DFS(y, x)
            direction += 1


# 8면 탐색: 위쪽 방향, 좌우, 아래쪽 방향
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for idx in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0:
                DFS(i, j)
                cnt += 1

    print('#{} {}'.format(idx, cnt))
