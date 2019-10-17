from collections import deque

R, C, M = map(int, input().split())

shark = [[deque() for _ in range(C + 1)] for _ in range(R + 1)]
shark[0] = [0] * (C + 1)
for i in range(R + 1):
    shark[i][0] = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[r][c].append([s, d, z])

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]


def find_dist(x, direction):
    if direction in [1, 2]:
        x %= ((R - 1) * 2)
    else:
        x %= ((C - 1) * 2)

    return x


def move(y, x, velocity, direction, size):
    i = 0
    flag = True
    next_y, next_x = y, x
    dist = find_dist(velocity, direction)
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

    if shark[next_y][next_x]:
        eat_candi.append((next_y, next_x))
    shark[next_y][next_x].append(shark[y][x].popleft())


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

    eat_candi = []
    for j, k in points:
        move(j, k, shark[j][k][0][0], shark[j][k][0][1], shark[j][k][0][2])

    # 상어 잡아먹기
    for j, k in eat_candi:
        shark[j][k] = deque([max(shark[j][k], key=lambda x: x[2])])

print(total_size)
