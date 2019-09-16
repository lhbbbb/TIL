T = int(input())


def isWall(x, y):
    if x < K and x >= 0 and y < K and y >= 0:
        return True
    else:
        return False


def side(box_lst):
    total = 0
    x, y = 0, 0
    direction = 0
    while direction <= 3:
        x += dx[direction]
        y += dy[direction]
        if isWall(x, y):
            total += box_lst[y][x]
        else:
            x -= dx[direction]
            y -= dy[direction]
            direction += 1

    return total


# 우하상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for idx in range(1, T + 1):
    N, M, K = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            box = [[lst[a][b] for b in range(j, j + K)] for a in range(i, i + K)]
            box_sum = side(box)
            if max_val < box_sum:
                max_val = box_sum

    print('#{} {}'.format(idx, max_val))
