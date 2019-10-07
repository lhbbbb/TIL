board = [list(map(int, input().split())) for _ in range(10)]


def search_one():
    for i in range(10):
        for j in range(10):
            if board[i][j]:
                return i, j


def select_size(y, x, size):
    if y + size <= 10 and x + size <= 10:
        for i in range(y, y + size):
            for j in range(x, x + size):
                if not board[i][j]:
                    return 0
        return 1
    else:
        return 0


def visit(y, x, size, num):
    for i in range(y, y + size):
        for j in range(x, x + size):
            board[i][j] = num


def backtrack(cnt, paper_cnt):
    global min_val, flag
    if cnt == 100:
        if min_val > paper_cnt:
            min_val = paper_cnt
        flag = True
    else:
        if paper_cnt >= min_val:
            return
        y, x = search_one()
        for i in range(1, 6):
            if papers[i] == 0:
                continue
            if select_size(y, x, i):
                papers[i] -= 1
                visit(y, x, i, 0)
                backtrack(cnt + i * i, paper_cnt + 1)
                papers[i] += 1
                visit(y, x, i, 1)
    if flag:
        return 1
    else:
        return 0


zero_cnt = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 0:
            zero_cnt += 1

papers = [0, 5, 5, 5, 5, 5]
if zero_cnt == 100:
    print(0)
else:
    flag = False
    min_val = 1e8
    backtrack(zero_cnt, 0)

    if flag:
        print(min_val)
    else:
        print(-1)
