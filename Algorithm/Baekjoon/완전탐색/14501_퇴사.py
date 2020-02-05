N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
info = [[0, 0]] + info
check = [0] * (N + 1)


def backtracking(k, total, check):
    global max_val
    if k > N:
        if max_val < total:
            max_val = total
            # print(check, max_val)
    else:
        tmp = check[::]
        tmp[k] = 0
        backtracking(k + 1, total, tmp)
        days = info[k][0]
        revenue = info[k][1]
        if k + days <= N + 1:
            tmp[k] = 1
            backtracking(k + days, total + revenue, tmp)


max_val = 0
backtracking(1, 0, check)

print(max_val)
