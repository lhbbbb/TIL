import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def backtrack(k, cnt, energy):
    global min_val
    if k + 1 >= N:
        if min_val > cnt:
            min_val = cnt
    else:
        cnt += 1
        if min_val > cnt:
            if k + 1 + charge[k] >= N:
                if min_val > cnt:
                    min_val = cnt
                return
            for i in range(1, charge[k] + 1):
                backtrack(k + i, cnt, energy + charge[k])


for tc in range(1, T + 1):
    info = list(map(int, input().split()))
    N = info[0]
    charge = info[1:]
    min_val = 1000000
    backtrack(0, 0, 0)

    print('#{} {}'.format(tc, min_val - 1))
