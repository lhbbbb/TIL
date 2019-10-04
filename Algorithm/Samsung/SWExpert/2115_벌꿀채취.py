import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def profit(k, total, cost):
    global revenue
    if k == len(ele):
        if total > revenue:
            revenue = total
    else:
        new_cost = cost - ele[k]
        if new_cost >= 0:
            new_total = total + ele[k] ** 2
            profit(k + 1, new_total, new_cost)
        profit(k + 1, total, cost)


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N):
        for j in range(N):
            task1 = info[i][j:j + M]
            for k in range(i, N):
                for l in range(N):
                    if k == i:
                        if l < j + M:
                            continue
                    max_length = l + M
                    if max_length <= N:
                        case = []
                        task2 = info[k][l:max_length]
                        case += [task1] + [task2]
                        val = 0
                        for ele in case:
                            revenue = 0
                            profit(0, 0, C)
                            val += revenue
                        if max_val < val:
                            max_val = val


    print('#{} {}'.format(tc, max_val))
