N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(i, j, size):
    queue = [(i, j, 0)]
    visited[i][j] = True
    cnt = 0
    criteria = -1
    candi = []
    flag = False
    while queue:
        y, x, cnt = queue.pop(0)
        if cnt == criteria:
            flag = True
            break
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
                if info[next_y][next_x] <= size:
                    if not visited[next_y][next_x]:
                        if info[next_y][next_x] != 0 and info[next_y][next_x] < size:
                            criteria = cnt + 1
                            candi.append((next_y, next_x, cnt + 1))
                        queue.append((next_y, next_x, cnt + 1))
                        visited[next_y][next_x] = True
    if flag:
        point = (1e8, 1e8)
        for ele in candi:
            if ele[2] == cnt:
                if point[0] > ele[0]:
                    point = ele
                elif point[0] == ele[0]:
                    if point[1] > ele[1]:
                        point = ele
        info[point[0]][point[1]] = 0
        return point
    else:
        return 0


# 시작 위치
for i in range(N):
    for j in range(N):
        if info[i][j] == 9:
            move_y, move_x = i, j
            info[i][j] = 0
            break

# 도움 요청
fish_size = 2
eat = 0
help_time = 0
while True:
    if eat == fish_size:
        eat = 0
        fish_size += 1

    visited = [[0] * N for _ in range(N)]
    res = BFS(move_y, move_x, fish_size)

    if res:
        move_y, move_x, move_cnt = res
        eat += 1
        help_time += move_cnt
    else:
        break

print(help_time)
