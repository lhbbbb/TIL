import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def backtrack(k, total):
    global min_val
    if k >= len(plan):
        if min_val > total:
            min_val = total
    else:
        if min_val < total:
            return
        else:
            for i in range(4):
                if i == 0:
                    new_total = total + plan[k] * rate[i]
                    backtrack(k + 1, new_total)
                elif i == 1:
                    new_total = total + rate[i]
                    backtrack(k + 1, new_total)
                elif i == 2:
                    new_total = total + rate[i]
                    backtrack(k + 3, new_total)
                else:
                    new_total = total + rate[i]
                    backtrack(k + 12, new_total)


for tc in range(1, T + 1):
    rate = list(map(int, input().split()))

    plan = list(map(int, input().split()))

    min_val = 1e8

    for i in range(len(plan)):
        if plan[i] != 0:
            backtrack(i, 0)
            break

    print('#{} {}'.format(tc, min_val))
