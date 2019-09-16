#import sys

#sys.stdin = open('sample_input.txt', 'r')


def isWall(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return False
    else:
        return True


def DFS(i, j):
    global flag
    visited[i][j] = True
    direction = 0
    for _ in range(4):
        x = j + dx[direction]
        y = i + dy[direction]
        if not isWall(x,y):
            if miro[y][x] == 0 and not visited[y][x]:
                DFS(y,x)
            elif miro[y][x] == 3:
                flag = True
                return 1
        else:
            x -= dx[direction]
            y -= dy[direction]
        direction += 1
        if flag:
            return 1

    return 0

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


T = int(input())

for idx in range(1, T + 1):
    N = int(input())

    miro = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                res = DFS(i, j)
                break

    print('#{} {}'.format(idx, res))
