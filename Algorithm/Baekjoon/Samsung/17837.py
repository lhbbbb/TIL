N, K = map(int, input().split())

info = [[0] + list(map(int, input().split())) for _ in range(N)]
info = [[0] * (N + 1)] + info
horses = [list(map(int, input().split())) for _ in range(K)]
status = [[0] + [[] for _ in range(N)] for _ in range(N)]
status = [[0] * (N + 1)] + status

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]


def is_wall(y, x):
    if 1 <= y < N + 1 and 1 <= x < N + 1:
        return True
    else:
        return False


def select_horse(num, y, x):
    tmp = []
    for idx, ele in enumerate(status[y][x]):
        if ele == num:
            tmp = status[y][x][idx:]
            status[y][x] = status[y][x][:idx]

    return tmp


def change_arrow(x):
    if x == 1:
        return 2
    elif x == 2:
        return 1
    elif x == 3:
        return 4
    else:
        return 3


def move(num, y, x, arrow):
    tmp = select_horse(num, y, x)
    yy = y + dy[arrow]
    xx = x + dx[arrow]
    if is_wall(yy, xx):
        # 0: white, 1: red, 2: blue
        if info[yy][xx] == 0:
            status[yy][xx] += tmp
            for ele in tmp:
                horses[ele - 1][0] = yy
                horses[ele - 1][1] = xx
            if len(status[yy][xx]) >= 4:
                return True
        elif info[yy][xx] == 1:
            tmp.reverse()
            status[yy][xx] += tmp
            for ele in tmp:
                horses[ele - 1][0] = yy
                horses[ele - 1][1] = xx
            if len(status[yy][xx]) >= 4:
                return True
        else:
            status[y][x] += tmp

    # blue
    else:
        status[y][x] += tmp


def turn(num, y, x, arrow):
    yy = y + dy[arrow]
    xx = x + dx[arrow]

    if is_wall(yy, xx):
        # 0: white, 1: red, 2: blue
        if info[yy][xx] == 2:
            c_arrow = change_arrow(arrow)
        else:
            c_arrow = arrow
        horses[num - 1][2] = c_arrow
        if move(num, y, x, c_arrow):
            return True
    # blue
    else:
        c_arrow = change_arrow(arrow)
        horses[num - 1][2] = c_arrow
        if move(num, y, x, c_arrow):
            return True


# 1. init setting
horse_num = 1
for horse in horses:
    y, x, arrow = horse
    status[y][x].append(horse_num)
    horse_num += 1

cnt = 0
while True:
    # 2. turn
    for horse_num, horse in enumerate(horses):
        flag = turn(horse_num + 1, *horse)
        if flag:
            break
    cnt += 1
    if flag:
        print(cnt)
        break
    if cnt > 1000:
        print(-1)
        break
