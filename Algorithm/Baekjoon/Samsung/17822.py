from collections import deque

N, M, T = map(int, input().split())

info = [deque(map(int, input().split())) for _ in range(N)]
info = [[0] * M] + info

vars = [list(map(int, input().split())) for _ in range(T)]


def rotate(x, d, k):
    for idx in range(x, N + 1, x):
        if d == 0:
            info[idx].rotate(k)
        else:
            info[idx].rotate(-k)


def replace():
    lst = sum(info, deque())
    cal_lst = [x for x in lst if x != 0]
    if len(cal_lst) == 0:
        return
    mean = sum(cal_lst) / len(cal_lst)
    for i in range(1, N + 1):
        for j in range(M):
            if info[i][j] > mean and info[i][j] != 0:
                info[i][j] -= 1
            elif info[i][j] < mean and info[i][j] != 0:
                info[i][j] += 1


def find_adj(info):
    global flag
    tmp = [deque([x for x in y]) for y in info]
    # 원판 내
    for idx in range(1, N + 1):
        for j in range(M - 1):
            if info[idx][j] == 0:
                continue
            if info[idx][j] == info[idx][j + 1]:
                tmp[idx][j], tmp[idx][j + 1] = 0, 0
                flag = True
        if info[idx][0] == 0:
            continue
        if info[idx][-1] == info[idx][0]:
            tmp[idx][-1], tmp[idx][0] = 0, 0
            flag = True
    # 원판끼리
    for idx in range(M):
        for j in range(1, N):
            if info[j][idx] == 0:
                continue
            if info[j][idx] == info[j + 1][idx]:
                tmp[j][idx], tmp[j + 1][idx] = 0, 0
                flag = True

    return tmp


for var in vars:
    # 1. rotate
    rotate(*var)

    # 2. find adj
    flag = False
    info = find_adj(info)

    if not flag:
        replace()

res = sum(sum(info, deque()))
print(res)
