import sys

sys.stdin = open('input.txt', 'r')

N = int(input())


# t=1 => 1*1, t=2 => 1*2, t=3 => 2*1
# x=row, y=col


def apply_board(lst):
    for i in range(4):
        for j in range(4):
            lst[i][j] = moving_board[i][j]


def rotate(lst):
    lst = lst[::-1]
    moving_board = [list(x) for x in zip(*lst)]
    return moving_board


def is_wall(x, y):
    if 0 <= x < 10 and 0 <= y < 4:
        return False
    else:
        return True


def find_point(lst):
    for i in range(4):
        for j in range(4):
            if lst[i][j]:
                x, y = i, j
                return x, y


def move(t, lst):
    x, y = find_point(lst)

    if t == 1:
        while True:
            x += 1
            if is_wall(x, y):
                break
            if lst[x][y]:
                break
            lst[x][y], lst[x - 1][y] = lst[x - 1][y], lst[x][y]
    elif t == 2:
        while True:
            x += 1
            if is_wall(x, y):
                break
            if lst[x][y] or lst[x][y + 1]:
                break
            lst[x][y], lst[x - 1][y] = lst[x - 1][y], lst[x][y]
            lst[x][y + 1], lst[x - 1][y + 1] = lst[x - 1][y + 1], lst[x][y + 1]
    else:
        x += 1
        while True:
            x += 1

            if is_wall(x, y):
                break
            if lst[x][y]:
                break
            lst[x][y], lst[x - 1][y] = lst[x - 1][y], lst[x][y]
            lst[x - 1][y], lst[x - 2][y] = lst[x - 2][y], lst[x - 1][y]


def check_score(lst):
    global score

    while True:
        for i in range(9, 5, -1):
            flag = True
            for j in range(4):
                if not lst[i][j]:
                    flag = False
                    break
            if flag:
                lst[i] = [0, 0, 0, 0]
                score += 1
                for k in range(i, 5, -1):
                    lst[k], lst[k - 1] = lst[k - 1], lst[k]
                break

        if i == 6:
            break


def check_delete(lst):
    cnt = 0
    for i in range(4, 6):
        for j in range(4):
            if lst[i][j]:
                cnt += 1
                break

    if cnt:
        for k in range(1, cnt + 1):
            lst[-k] = [0, 0, 0, 0]

        for i in range(9 - cnt, 3, -1):
            lst[i + cnt], lst[i] = lst[i], lst[i + cnt]


board = [[0] * 4 for _ in range(10)]
Tboard = [[0] * 4 for _ in range(10)]
score = 0
# 1
for _ in range(N):
    t, x, y = map(int, input().split())
    moving_board = [[0] * 4 for _ in range(4)]
    if t == 1:
        moving_board[x][y] = 1
    elif t == 2:
        moving_board[x][y] = 1
        moving_board[x][y + 1] = 1
    else:
        moving_board[x][y] = 1
        moving_board[x + 1][y] = 1
    # 2
    apply_board(board)
    move(t, board)

    # 3
    moving_board = rotate(moving_board)
    apply_board(Tboard)
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
    move(t, Tboard)

    # 4
    check_score(board)
    check_score(Tboard)

    # 5
    check_delete(board)
    check_delete(Tboard)

res = 0
for i in range(6, 10):
    for j in range(4):
        if board[i][j]:
            res += 1

        if Tboard[i][j]:
            res += 1

print(score)
print(res)