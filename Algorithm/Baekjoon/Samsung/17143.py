R, C, M = map(int, input().split())

shark = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
shark[0] = [0] * (C + 1)
for i in range(R + 1):
    shark[i][0] = 0

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]


def move(y, x, dist, direction, size):
    i = 0
    flag = True
    next_y, next_x = y, x
    while i < dist:
        if flag:
            next_y += dy[direction]
            next_x += dx[direction]
        else:
            next_y -= dy[direction]
            next_x -= dx[direction]
        if next_y < 1 or next_x < 1 or next_y >= R + 1 or next_x >= C + 1:
            if flag:
                next_y -= dy[direction]
                next_x -= dx[direction]
            else:
                next_y += dy[direction]
                next_x += dx[direction]
            flag = not flag
            continue
        i += 1

    # 방향 정보 갱신
    if not flag:
        if direction == 1:
            shark[y][x][0][1] = 2
        elif direction == 2:
            shark[y][x][0][1] = 1
        elif direction == 3:
            shark[y][x][0][1] = 4
        elif direction == 4:
            shark[y][x][0][1] = 3

    shark[next_y][next_x].append(shark[y][x].pop(0))


for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[r][c] += [[s, d, z]]

total_size = 0
for i in range(1, C + 1):
    # 상어 잡기
    for j in range(1, R + 1):
        if shark[j][i]:
            total_size += shark[j][i].pop()[2]
            break

    # 상어 이동
    points = []
    for j in range(1, R + 1):
        for k in range(1, C + 1):
            if shark[j][k]:
                points.append((j, k))

    for j, k in points:
        move(j, k, shark[j][k][0][0], shark[j][k][0][1], shark[j][k][0][2])

    # 상어 잡아먹기
    for j in range(1, R + 1):
        for k in range(1, C + 1):
            if len(shark[j][k]) > 1:
                shark[j][k] = [max(shark[j][k], key=lambda x: x[2])]

print(total_size)
