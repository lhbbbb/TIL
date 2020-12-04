import sys

sys.stdin = open('input.txt', 'r')

N, M, k = map(int, input().split())

shark_board = [0] * N
scent_board = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move(y, x):
    global res
    cnt = 0
    for k in range(4):
        xx, yy = x + dx[k], y + dy[k]
        if 0 <= xx < N and 0 <= yy < N:
            if not scent_board[yy][xx]:
                cnt += 1

    # 아무 냄새 없는 칸 (우선순위)
    if cnt >= 2:
        arrows = shark_info[tmp[y][x][0]][tmp[y][x][1]]
        for arrow in arrows:
            xx, yy = x + dx[arrow - 1], y + dy[arrow - 1]
            if 0 <= xx < N and 0 <= yy < N:
                if not scent_board[yy][xx]:
                    if tmp[yy][xx]:
                        res -= 1
                        if tmp[yy][xx][0] > tmp[y][x][0]:
                            tmp[yy][xx] = [tmp[y][x][0], arrow]
                        tmp[y][x] = 0
                        break
                    else:
                        tmp[yy][xx] = [tmp[y][x][0], arrow]
                        tmp[y][x] = 0
                        break
    # 아무 냄새 없는 칸 (바로)
    elif cnt == 1:
        for k in range(4):
            xx, yy = x + dx[k], y + dy[k]
            if 0 <= xx < N and 0 <= yy < N:
                if not scent_board[yy][xx]:
                    if tmp[yy][xx]:
                        res -= 1
                        if tmp[yy][xx][0] > tmp[y][x][0]:
                            tmp[yy][xx] = [tmp[y][x][0], k + 1]
                        tmp[y][x] = 0
                        break
                    else:
                        tmp[yy][xx] = [tmp[y][x][0], k + 1]
                        tmp[y][x] = 0
                        break
    # 냄새 있는 칸
    else:
        arrows = shark_info[tmp[y][x][0]][tmp[y][x][1]]
        for arrow in arrows:
            xx, yy = x + dx[arrow - 1], y + dy[arrow - 1]
            if 0 <= xx < N and 0 <= yy < N:
                if scent_board[yy][xx] and scent_board[yy][xx][0] == tmp[y][x][0]:
                    tmp[yy][xx] = [tmp[y][x][0], arrow]
                    tmp[y][x] = 0
                    break


for i in range(N):
    shark_board[i] = list(map(int, input().split()))

info = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if shark_board[i][j]:
            shark_board[i][j] = [shark_board[i][j], info[shark_board[i][j] - 1]]

shark_info = {}
for i in range(1, M + 1):
    shark_info[i] = {}

# 1: 위 2: 아래 3: 왼 4: 오
for i in range(1, M + 1):
    for j in range(1, 5):
        lst = list(map(int, input().split()))
        shark_info[i][j] = lst

res = M
time = 0
while time <= 1000:
    for i in range(N):
        for j in range(N):
            if shark_board[i][j]:
                scent_board[i][j] = [shark_board[i][j][0], k]

    tmp = [ele[:] for ele in shark_board]
    for i in range(N):
        for j in range(N):
            if shark_board[i][j]:
                move(i, j)

    shark_board = [ele[:] for ele in tmp]

    for i in range(N):
        for j in range(N):
            if scent_board[i][j]:
                scent_board[i][j][1] -= 1
                if scent_board[i][j][1] == 0:
                    scent_board[i][j] = 0

    time += 1

    if res == 1:
        break

if time <= 1000:
    print(time)
else:
    print(-1)
