R, C, T = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def diffuse(i, j):
    diff_size = A[i][j] // 5
    cnt = 0
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= y < R and 0 <= x < C and A[y][x] != -1:
            status[y][x] += diff_size
            cnt += 1
    A[i][j] -= (diff_size * cnt)


for t in range(T):
    # 1. 확산
    status = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                diffuse(i, j)

    A = [[A[i][j] + status[i][j] for j in range(C)] for i in range(R)]

    # 2. 공기청정기 작동
    flag = False
    fresher = []
    for i in range(R):
        for j in range(C):
            if A[i][j] == -1:
                fresher = [(i, j), (i + 1, j)]
                flag = True
                break
        if flag:
            break

    # 위쪽 방향
    y, x = fresher[0]
    ## 아래
    for i in range(y - 1, -1, -1):
        A[i + 1][x] = A[i][x]
    A[y][x] = -1
    ## 왼쪽
    for i in range(1, C):
        A[0][i - 1] = A[0][i]
    ## 위쪽
    for i in range(y):
        A[i][C - 1] = A[i + 1][C - 1]
    ## 오른쪽
    for i in range(C - 1, 1, -1):
        A[y][i] = A[y][i - 1]
    A[y][1] = 0

    # 아래 방향
    y, x = fresher[1]
    for i in range(y + 1, R):
        A[i - 1][x] = A[i][x]
    A[y][x] = -1
    for i in range(C - 1):
        A[R - 1][i] = A[R - 1][i + 1]
    for i in range(R - 1, y, -1):
        A[i][C - 1] = A[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        A[y][i] = A[y][i - 1]
    A[y][1] = 0

print(sum(sum(A, [])) + 2)
